#!/usr/bin/env python3
"""Hello, World! —— 经典入门程序。

运行:python3 hello_world.py
"""


def greeting():
    """返回问候语文本。"""
    return "Hello, World!"


def main():
    print(greeting())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
