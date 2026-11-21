import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sync", description="数据同步工具")
    p.add_argument("source")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--dry-run", action="store_true")
    return p


def run_sync(source: str, limit: int, dry_run: bool) -> str:
    mode = "dry-run" if dry_run else "sync"
    return f"{mode} {source} limit={limit}"


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    print(run_sync(args.source, args.limit, args.dry_run))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(["db1", "--limit", "5", "--dry-run"]))
