#!/usr/bin/env python3
"""hello_world.py 的单元测试。

运行:python3 test_hello_world.py -v
"""

import io
import subprocess
import sys
import contextlib
import unittest

from hello_world import greeting, main


class TestGreeting(unittest.TestCase):
    def test_greeting_text(self):
        """默认问候语固定为 Hello, World!"""
        self.assertEqual(greeting(), "Hello, World!")

    def test_main_prints_greeting(self):
        """main() 向标准输出打印问候语并返回 0"""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exit_code = main()
        self.assertEqual(exit_code, 0)
        self.assertEqual(buf.getvalue(), "Hello, World!\n")


class TestScript(unittest.TestCase):
    def test_script_runs_standalone(self):
        """脚本可直接运行,输出 Hello, World! 且退出码为 0"""
        proc = subprocess.run(
            [sys.executable, "hello_world.py"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout, "Hello, World!\n")


if __name__ == "__main__":
    unittest.main()
