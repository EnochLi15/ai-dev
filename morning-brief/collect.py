#!/usr/bin/env python3
"""AI 晨报采集层（morning-brief/collect.py）

按方案（README.md）抓取全部已验证信源，产出：
  morning-brief/run/<date>/collected.md   —— 分源素材清单（供筛选/撰写）
  morning-brief/run/<date>/raw/*.json|txt —— 原始快照（供回源核对，防幻觉）
GitHub 趋势榜自动按 trending-ledger.json 去重（已报项目不再出现）。

用法：python3 collect.py [--date 2026-11-03]
说明：run/ 目录为工作快照，不入库；每个信源独立容错，单个失败不影响其余。
"""
import json, re, html, subprocess, sys, datetime, pathlib, urllib.request, concurrent.futures

args = sys.argv[1:]
DATE = args[args.index('--date') + 1] if '--date' in args else datetime.date.today().isoformat()
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / 'run' / DATE
RAW = OUT / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

def curl(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', 'ignore')

def text(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()

SECTIONS = []  # (source_name, ok, [lines])
def note(name, lines, ok=True):
    SECTIONS.append((name, ok, lines))

# ---------- 1. Hacker News top60（AI 关键词过滤） ----------
KW = re.compile(r'\b(ai|agent|llm|gpt|claude|openai|anthropic|gemini|copilot|cursor|llama|deepseek|qwen|mistral|mcp|rag|model|codex|prompt|inference|robot|coding)\b', re.I)
try:
    ids = json.loads(curl('https://hacker-news.firebaseio.com/v0/topstories.json'))[:60]
    def hn_item(i):
        try:
            return json.loads(curl(f'https://hacker-news.firebaseio.com/v0/item/{i}.json', 8))
        except Exception:
            return None
    with concurrent.futures.ThreadPoolExecutor(12) as ex:
        items = [d for d in ex.map(hn_item, ids) if isinstance(d, dict)]
    (RAW / 'hn-items.json').write_text(json.dumps(items, ensure_ascii=False, indent=1))
    rows = [d for d in items if d.get('title') and KW.search(d['title'])]
    rows.sort(key=lambda d: -d.get('score', 0))
    lines = []
    for d in rows[:25]:
        u = d.get('url') or ('https://news.ycombinator.com/item?id=' + str(d.get('id')))
        lines.append('{}pts {}c | {} | {}'.format(d.get('score', 0), d.get('descendants', 0), d.get('title'), u))
    note('Hacker News top60（AI 过滤）', lines)
except Exception as e:
    note(f'Hacker News（失败：{e}）', [], ok=False)

# ---------- 2. GitHub 趋势榜（周榜代理 + 台账去重 + topic 检索） ----------
def gh(endpoint):
    r = subprocess.run(['gh', 'api', endpoint], capture_output=True, text=True, timeout=60)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else {}

try:
    shown = set()
    ledger_path = ROOT / 'trending-ledger.json'
    if ledger_path.exists():
        led = json.loads(ledger_path.read_text())
        shown = {x['repo'] for x in led.get('shown', [])}
    week_ago = (datetime.date.fromisoformat(DATE) - datetime.timedelta(days=7)).isoformat()
    lines = []
    for label, q in [
        ('近7天新建+stars>150', f'created:>{week_ago} stars:>150'),
        ('topic:ai-agents 近2周+stars>80', f'topic:ai-agents created:>{(datetime.date.fromisoformat(DATE)-datetime.timedelta(days=14)).isoformat()} stars:>80'),
        ('topic:llm 近2周+stars>150', f'topic:llm created:>{(datetime.date.fromisoformat(DATE)-datetime.timedelta(days=14)).isoformat()} stars:>150'),
    ]:
        res = gh('search/repositories?q=' + urllib.request.quote(q, safe='') + '&sort=stars&order=desc&per_page=15')
        for it in res.get('items', []):
            mark = '（已报过，仅回访判断）' if it['full_name'] in shown else ''
            lines.append(f"⭐{it['stargazers_count']} born:{it['created_at'][:10]} [{label}] {it['full_name']}{mark} — {text(it.get('description') or '')[:90]}")
    (RAW / 'github-trending.json').write_text(json.dumps({'query_date': DATE, 'shown_before': sorted(shown)}, ensure_ascii=False, indent=1))
    note('GitHub 趋势榜（周榜代理，已按台账去重标记）', lines[:30])
except Exception as e:
    note(f'GitHub 趋势榜（失败：{e}）', [], ok=False)

# ---------- 3. 官方一手信源 ----------
try:
    s = curl('https://www.anthropic.com/news')
    (RAW / 'anthropic-news.html').write_text(s)
    datepat = re.compile(r'(?:Nov|Oct|Sep|Dec|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug)\w*\s+\d{1,2},?\s+20\d\d')
    seen, seen_url, lines = set(), set(), []
    for m in re.finditer(r'<a[^>]+href="(/news/[^"]+)"[^>]*>(.*?)</a>', s, re.S):
        t = text(m.group(2))
        if len(t) > 12 and t not in seen and m.group(1) not in seen_url:
            seen.add(t); seen_url.add(m.group(1))
            dm = datepat.search(s, m.start())
            lines.append(f"{dm.group(0) if dm else '?':>14} | https://www.anthropic.com{m.group(1)} | {t[:100]}")
    note('Anthropic Newsroom', lines[:15])
except Exception as e:
    note(f'Anthropic（失败：{e}）', [], ok=False)

for name, url, pat, raw_name in [
    ('Cursor changelog', 'https://cursor.com/changelog', r'<h[23][^>]*>(.*?)</h[23]>', 'cursor-changelog.html'),
    ('GitHub Blog changelog', 'https://github.blog/changelog/', r'>([^<>]{18,110})<', 'github-changelog.html'),
]:
    try:
        s = curl(url)
        (RAW / raw_name).write_text(s)
        heads = []
        for x in re.findall(pat, s, re.S):
            h = text(x).lstrip('# ')
            if len(h) > 12 and h not in heads:
                heads.append(h)
        heads = heads[:22]
        note(name, [f'- {h[:100]}' for h in heads])
    except Exception as e:
        note(f'{name}（失败：{e}）', [], ok=False)

try:
    s = curl('https://blog.google/technology/ai/rss/')
    (RAW / 'google-ai.xml').write_text(s)
    lines = []
    for it in re.findall(r'<item>(.*?)</item>', s, re.S):
        t = re.search(r'<title>(?:<!\[CDATA\[)?([^<\]]+)', it)
        d = re.search(r'<pubDate>([^<]+)</pubDate>', it)
        l = re.search(r'<link>([^<]+)</link>', it)
        if t and l:
            lines.append(f"{d.group(1)[:16] if d else '?'} | {text(t.group(1))[:100]} | {l.group(1)}")
    note('Google AI 官方博客 RSS', lines[:12])
except Exception as e:
    note(f'Google AI RSS（失败：{e}）', [], ok=False)

# ---------- 4. 中文媒体 ----------
try:
    s = curl('https://www.qbitai.com/')
    (RAW / 'qbitai.html').write_text(s)
    seen, lines = set(), []
    for m in re.finditer(r'<a[^>]+href="(https://www\.qbitai\.com/2026/\d+/[^"]+)"[^>]*>(.*?)</a>', s, re.S):
        t = text(m.group(2))
        if len(t) > 10 and t not in seen:
            seen.add(t)
            lines.append(f"{m.group(1)} | {t[:80]}")
    note('量子位', lines[:15])
except Exception as e:
    note(f'量子位（失败：{e}）', [], ok=False)

# ---------- 5. 精选博客 ----------
try:
    s = curl('https://simonwillison.net/atom/everything/')
    (RAW / 'simonwillison.xml').write_text(s)
    lines = []
    for it in re.findall(r'<entry>(.*?)</entry>', s, re.S)[:10]:
        t = re.search(r'<title>(?:<!\[CDATA\[)?([^<\]]+)', it)
        d = re.search(r'<published>([^<]+)</published>', it)
        l = re.search(r'<link[^>]+href="([^"]+)"', it)
        if t:
            lines.append(f"{d.group(1)[:16] if d else '?'} | {text(t.group(1))[:90]} | {l.group(1) if l else ''}")
    note('Simon Willison（LLM 一手实测）', lines)
except Exception as e:
    note(f'Simon Willison（失败：{e}）', [], ok=False)

# ---------- 汇总输出 ----------
fail = [n for n, ok, _ in SECTIONS if not ok]
with open(OUT / 'collected.md', 'w', encoding='utf-8') as f:
    f.write(f"# 采集素材 · {DATE}\n\n> 采集时间：{datetime.datetime.now().isoformat(timespec='seconds')}\n> 失败信源：{fail or '无'}\n\n")
    for name, ok, lines in SECTIONS:
        f.write(f"\n## {name}{' ⚠️失败' if not ok else ''}\n\n")
        f.write('\n'.join(lines) if lines else '（无内容）')
        f.write('\n')
print(f"OK -> {OUT / 'collected.md'}  失败信源: {fail or '无'}")
