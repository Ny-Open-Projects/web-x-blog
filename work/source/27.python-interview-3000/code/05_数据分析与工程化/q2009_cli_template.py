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
