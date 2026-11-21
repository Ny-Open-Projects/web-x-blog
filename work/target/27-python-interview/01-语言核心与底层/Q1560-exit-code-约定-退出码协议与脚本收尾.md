---
title: [Q1560] exit code 约定:退出码协议与脚本收尾
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1560 · exit code 约定:退出码协议与脚本收尾

> 难度:★★☆☆☆ | 标签:CLI, exit code, 脚本

**问**:CLI 脚本的退出码有哪些约定?sys.exit("msg") 会发生什么?怎么在 shell 里利用退出码?

**答**:退出码是 CLI 与外界的机器协议:0 成功、1 一般错误、2 用法错误(argparse 约定),os.EX_USAGE/EX_DATAERR/EX_NOINPUT 等 BSD sysexits 常量语义更细;128+N 表示被信号 N 杀死(shell 里 KeyboardInterrupt 常见 130)。sys.exit 的参数语义:None/0 → 0,int → 该码,str → 打到 stderr 并以 1 退出——「exit(str) 永远是失败」,别拿它输出成功信息。工程约定:main(argv) 返回 int,入口 sys.exit(main(sys.argv[1:])),错误路径可测试;钩子与 CI 以非 0 判失败;进程内测试用 subprocess 断言 returncode。argparse 的用法错误固定 SystemExit(2),自建 CLI 建议对齐。

```python
# file: code/01_语言核心与底层/q1560_exit_codes.py
import argparse
import contextlib
import io
import os
import subprocess
import sys

EX_USAGE = getattr(os, "EX_USAGE", 64)     # BSD sysexits,macOS 可用


def build_parser():
    parser = argparse.ArgumentParser(prog="scaler", add_help=False)
    parser.add_argument("--scale", type=float, default=1.0)
    parser.add_argument("value", type=float)
    return parser


def main(argv):
    try:
        args = build_parser().parse_args(argv)
    except SystemExit as err:
        return EX_USAGE if err.code == 2 else err.code
    if args.scale == 0:
        print("scale 不能为 0", file=sys.stderr)
        return 1
    print(args.value * args.scale)
    return 0


if __name__ == "__main__":
    for argv in (["3", "--scale", "2"], ["3", "--scale", "0"], ["--bogus", "3"]):
        noise = io.StringIO()
        with contextlib.redirect_stderr(noise):
            code = main(argv)
        print(argv, "-> exit", code)

    # 独立进程视角:shell 里看 $? 与 subprocess 的 returncode
    probes = ["sys.exit(3)", "sys.exit('boom')", "sys.exit(None)",
              "raise KeyboardInterrupt"]
    for body in probes:
        done = subprocess.run([sys.executable, "-c", "import sys\n" + body],
                              capture_output=True, text=True)
        note = done.stderr.strip().splitlines()[-1] if done.stderr.strip() else ""
        print("%-26s -> returncode %s %s" % (body, done.returncode, note[:40]))
```

**追问**:1) 退出码 130 从哪来?——128 + 信号编号(SIGINT=2)是 shell 的约定;subprocess 看到的 returncode 是 -2,同一个事实的两种表示。2) 退出码协议?——0 成功、非 0 失败、1 一般错误、2 用法错误;128+n 信号致死;sys.exit(int) 抛 SystemExit,字符串会打到 stderr 且码为 1。3) 收尾协议?——atexit/finally 做清理,stdout/stderr flush 后退出;os._exit 跳过清理只给 fork 子进程用;CI 判定只看码,所以失败必须非 0。4) 生产陷阱?——脚本吞异常后静默 exit 0,CI 全绿假象;把 traceback 直接甩给终端用户(应翻译成友好错误);crontab 只看码不看 stderr。
