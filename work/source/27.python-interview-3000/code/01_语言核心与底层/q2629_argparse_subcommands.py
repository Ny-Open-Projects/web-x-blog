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
