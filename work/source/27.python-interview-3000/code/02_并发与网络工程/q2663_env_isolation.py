# -*- coding: utf-8 -*-
"""子进程的环境变量隔离: env 参数与 PATH 的陷阱。

- 默认 env=None: 完整继承父进程环境, 凭证等敏感变量也一起带过去;
- 显式传 env: 子进程只看到白名单变量, 这是最小暴露面;
- PATH 也属于环境: 子进程的 PATH 决定裸名可执行文件的查找范围。
"""
import os
import subprocess
import sys

PROBE = (
    "import os, shutil; "
    "print('env_keys=%d' % len(os.environ)); "
    "print('has_secret=%s' % ('API_TOKEN' in os.environ)); "
    "print('which_python3=%s' % (shutil.which('python3') or 'NOT-FOUND'))"
)


def run(env):
    r = subprocess.run([sys.executable, "-c", PROBE],
                       capture_output=True, text=True, env=env, timeout=10)
    return r.stdout.strip().splitlines()


if __name__ == "__main__":
    os.environ["API_TOKEN"] = "should-not-leak"

    print("== 默认继承父进程环境 ==")
    for line in run(None):
        print("  ", line)

    print("== 白名单环境(仅 MINIMAL 与受控 PATH) ==")
    clean = {"MINIMAL": "1", "PATH": "/usr/bin:/bin"}
    for line in run(clean):
        print("  ", line)

    print("== 子进程 PATH 指向空目录时, 裸名查找会怎样 ==")
    try:
        subprocess.run(["python3", "-c", "print(1)"],
                       capture_output=True, env={"PATH": "/nonexistent"},
                       timeout=10)
        print("  竟然成功了")
    except FileNotFoundError as e:
        print("  FileNotFoundError:", e)

    print("== 结论: 凭证要靠白名单 env 挡住, 别依赖子进程自觉 ==")
