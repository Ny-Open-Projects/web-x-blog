---
title: [Q2009] 脚本入口统一 argparse 模板:公共参数与子命令
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2009 · 脚本入口统一 argparse 模板:公共参数与子命令

> 难度:★★☆ | 标签:argparse, CLI

**问**:组里十几个运维脚本各有各的参数风格,你怎么把它们统一起来?

**答**:统一入口模板一次投入长期受益:公共参数(--dry-run、--log-level、--config)在公共 parser 定义一次,经 parents 注入每个子命令,新增子命令自动继承;业务参数挂在子命令上。实测 datatool 的 export 与 backfill 共享同一套公共参数。--dry-run 是破坏性操作的标配,先打印将执行的动作;--log-level 统一三档;--config 让环境切换不靠改代码。顺手统一退出码约定:0 成功、2 用法错误、1 业务失败,让 cron 和 CI 能按退出码分支。新脚本从模板复制起步,评审时加参数风格一致性检查——一致性比"哪种风格更好"重要。

```python
# file: code/05_数据分析与工程化/q2009_cli_template.py
"""脚本入口统一模板:公共参数一次定义,经 parents 注入所有子命令"""

import argparse


def common_args():
    """公共参数只在这里定义一次,新子命令 parents 接上即可继承"""
    c = argparse.ArgumentParser(add_help=False)
    c.add_argument("--dry-run", action="store_true", help="只打印不执行")
    c.add_argument("--log-level", default="INFO",
                   choices=["DEBUG", "INFO", "WARNING"])
    c.add_argument("--config", default="prod", help="环境配置名")
    return c


def build_parser():
    common = common_args()
    p = argparse.ArgumentParser(prog="datatool",
                                description="统一脚本入口模板,公共参数放子命令之后")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_export = sub.add_parser("export", parents=[common], help="导出报表")
    p_export.add_argument("--date", required=True)
    p_export.add_argument("--fmt", default="csv", choices=["csv", "xlsx"])

    p_backfill = sub.add_parser("backfill", parents=[common],
                                help="回填历史分区")
    p_backfill.add_argument("--start", required=True)
    p_backfill.add_argument("--end", required=True)
    return p


def run(args):
    if args.cmd == "export":
        print(f"export date={args.date} fmt={args.fmt}")
    else:
        print(f"backfill {args.start} -> {args.end}")
    print(f"config={args.config} log_level={args.log_level}")
    if args.dry_run:
        print("dry-run: 以上动作未真正执行")


if __name__ == "__main__":
    parser = build_parser()
    for argv in (["export", "--date", "2026-11-04", "--fmt", "xlsx",
                  "--dry-run", "--log-level", "DEBUG"],
                 ["backfill", "--start", "2026-11-01", "--end", "2026-11-03"]):
        print("$ datatool", " ".join(argv))
        run(parser.parse_args(argv))
        print()
    print("要点:--dry-run/--log-level/--config 只定义一次,经 parents 注入每个子命令,新脚本先抄模板;子命令让一个入口长成工具箱,而不是复制十个各写各的脚本")
```

**追问**:
- 追问 1:为什么不用 click 或 typer?—— 模板思想不变;argparse 标准库零依赖,内部小工具优先,对外发布再换现代框架。
- 追问 2:公共参数放子命令前还是后?—— 模板里放子命令后随子命令注入,usage 写清楚;全组一致比哪种更好更重要。
