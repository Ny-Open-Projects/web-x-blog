---
title: [Q389] argparse 命令行与输入校验
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q389 · argparse 命令行与输入校验

> 难度:★★☆ | 标签:argparse, CLI, 输入校验

**问**:写一个规范的命令行工具需要哪些要素?如何校验参数?

**答**:argparse 四要素:①位置参数与可选参数(`--verbose`, `type=`);②`choices`/`type` 做第一道校验;③自定义 `type` 函数做语义校验(如端口范围、路径存在),抛 `argparse.ArgumentTypeError`;④子命令 `add_subparsers` 组织多命令工具。校验原则:边界处 fail-fast,错误信息指明正确用法;交互式输入用 `input()` + 循环重试,并在转换处捕获 ValueError。注意非交互环境(stdin 关闭/管道喂空)`input()` 会抛 EOFError——自动化跑 demo 时应先检测 stdin 是否可用,不可用直接取默认值,别让交互逻辑把脚本挂死。

```python
# file: code/02_并发与网络工程/q389_argparse.py
"""argparse 命令行工具骨架 + 自定义校验 + 交互输入校验。"""
import argparse
import pathlib
import sys


def port_type(value: str) -> int:
    port = int(value)
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError(f"端口 {port} 不在 1-65535 范围")
    return port


def build_parser():
    p = argparse.ArgumentParser(prog="deploy", description="部署工具示例")
    p.add_argument("target", help="部署目标目录")
    p.add_argument("--port", type=port_type, default=8000)
    p.add_argument("--env", choices=["dev", "staging", "prod"], default="dev")
    sub = p.add_subparsers(dest="action")
    sub.add_parser("plan", help="只做 dry-run")
    sub.add_parser("apply", help="真正执行")
    return p


def ask_int(prompt, lo, hi, default=None):
    """交互输入校验:非法输入循环重试。

    非交互环境(stdin 关闭, 如 CI/演示脚本)input() 会抛 EOFError,
    此时直接回退默认值, 不让交互把脚本挂死。
    """
    while True:
        try:
            raw = input(f"{prompt} [{lo}-{hi}]{' 默认 ' + str(default) if default else ''}: ").strip()
        except EOFError:
            print(f"(检测到无交互输入, 使用默认值 {default})")
            return default
        if not raw and default is not None:
            return default
        try:
            v = int(raw)
            if lo <= v <= hi:
                return v
        except ValueError:
            pass
        print("输入无效, 请重试")


if __name__ == "__main__":
    argv = sys.argv[1:] or ["./app", "--port", "9443", "--env", "prod", "apply"]
    args = build_parser().parse_args(argv)  # 实际使用时让命令行传入
    target = pathlib.Path(args.target)
    print(f"action={args.action} target={target} port={args.port} env={args.env}")
    if sys.stdin and sys.stdin.isatty():
        replicas = ask_int("请输入副本数", 1, 10, default=3)
    else:
        replicas = 3
        print("(非交互环境, 副本数取默认值 3)")
    print("副本数 =", replicas)
```

**追问**:
- click/typer 和 argparse 怎么选?argparse 零依赖适合内置工具;click/typer 装饰器风格更省代码,适合多命令大型 CLI。
- `parse_args` 失败时退出码是多少?打印 usage 并以 2 退出,脚本可以据此区分"参数错误"和其他失败。
