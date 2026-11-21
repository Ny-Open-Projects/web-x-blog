---
title: [Q2629] argparse 子命令与互斥组:CLI 的树形结构
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2629 · argparse 子命令与互斥组:CLI 的树形结构

> 难度:★★★☆☆ | 标签:argparse, 子命令, CLI 设计

**问**:`git style` 的子命令 CLI 用 argparse 怎么搭?互斥选项怎么做?

**答**:子命令用 `add_subparsers`:每个子命令是一个独立 parser,共享顶层 `-h`;给 `dest="cmd"` 并设 `required=True`(3.7+)保证裸调用时报错;惯用法是 `set_defaults(func=handler)` 把处理函数挂进命名空间,主逻辑按 `args.func(args)` 分发,避免 if-elif 链。互斥组用 `add_mutually_exclusive_group`,组内选项同给会报错退出;`required=True` 的互斥组表示必选其一。这套结构是 pip、docker 同款,扩展时只需注册新 subparser,不动主流程。

```python
# file: code/01_语言核心与底层/q2629_argparse_subcommands.py
"""argparse 子命令 + 互斥组 + set_defaults 分发。"""
import argparse


def cmd_train(args):
    print(f"train epochs={args.epochs}")


def cmd_sync(args):
    mode = "force" if args.force else "dry-run" if args.dry_run else "normal"
    print(f"sync mode={mode}")


def build():
    parser = argparse.ArgumentParser(prog="tool")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_train = sub.add_parser("train", help="训练")
    p_train.add_argument("--epochs", type=int, default=10)
    p_train.set_defaults(func=cmd_train)

    p_sync = sub.add_parser("sync", help="同步")
    group = p_sync.add_mutually_exclusive_group()
    group.add_argument("--force", action="store_true")
    group.add_argument("--dry-run", action="store_true")
    p_sync.set_defaults(func=cmd_sync)
    return parser


if __name__ == "__main__":
    build().parse_args(["train", "--epochs", "3"]).func
    build().parse_args(["sync", "--dry-run"]).func

    try:
        build().parse_args(["sync", "--force", "--dry-run"])
    except SystemExit:
        print("互斥冲突 -> SystemExit(2)")
```

**追问**:1) 子命令还想再挂子命令可以吗?——可以,subparser 上继续 add_subparsers 即可形成任意深度树,`dest` 各层不同就不会互相覆盖。2) 子命令的机制要点?——add_subparsers(dest="command", required=True) 拿到下发命令;sub.set_defaults(func=handler) 让 args.func(args) 统一分发;嵌套树逐层挂 dest。3) 互斥组与默认值?——add_mutually_exclusive_group 防冲突组合;required 可选;默认值与 dest 命名冲突是高频坑。4) 生产陷阱?——顶层 dest 重名覆盖嵌套命令;required=False 时漏命令静默;嵌套 help 文本与版本号;子命令参数在父级拿不到。
