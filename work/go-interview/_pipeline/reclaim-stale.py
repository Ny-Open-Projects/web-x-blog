#!/usr/bin/env python3
"""
回收「卡死」的 running 任务。

背景：state.json 不记录任务领取时间戳，无法直接判断某个 running 是否被
已死掉的会话占着不放。若不管，卡死的 2 个任务会让后续所有自动化会话都因
「running > 0 → 避让」而整夜空跑。

判定策略（保守，宁可不回收也不误伤）：
  以「最新卡片 mtime」与「最新 git commit 时间」作为活跃度代理指标，
  **两者都**超过阈值（默认 30 分钟）才判定为停滞并回收。
  只回收 running 状态的任务，其余状态不动。

回收用 `queue.py reset`（放回 pending，不计失败、不触发退避），
不用 `queue.py fail`（fail 会累加 consec_fail 并施加指数退避惩罚）。
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # work/go-interview
STATE = ROOT / "_pipeline" / "state.json"
TARGET = ROOT / "target"
QUEUE = ROOT / "_pipeline" / "queue.py"


def minutes_ago(ts):
    if ts is None:
        return float("inf")
    return (time.time() - ts) / 60.0


def newest_card_mtime():
    mds = list(TARGET.glob("*.md"))
    if not mds:
        return None
    return max(p.stat().st_mtime for p in mds)


def newest_commit_ts():
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%ct"],
            capture_output=True, text=True, timeout=30,
        )
        v = (out.stdout or "").strip()
        return float(v) if v else None
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description="回收卡死的 running 任务")
    ap.add_argument("--minutes", type=float, default=30.0,
                    help="停滞阈值（分钟），默认 30")
    ap.add_argument("--dry-run", action="store_true", help="只报告不执行")
    args = ap.parse_args()

    st = json.load(open(STATE, encoding="utf-8"))
    running = [t for t in st["tasks"].values() if t.get("status") == "running"]

    if not running:
        print("无 running 任务，无需回收。")
        return 0

    card_age = minutes_ago(newest_card_mtime())
    commit_age = minutes_ago(newest_commit_ts())
    print(f"running={len(running)} | 最新卡片 {card_age:.1f} 分钟前 | "
          f"最新提交 {commit_age:.1f} 分钟前 | 阈值 {args.minutes} 分钟")

    if card_age < args.minutes or commit_age < args.minutes:
        print("判定：仍有活跃产出，不回收（避免误伤正在工作的会话）。")
        return 0

    ids = [t["id"] for t in running]
    print(f"判定：已停滞超过阈值 → 回收 {ids}")

    if args.dry_run:
        print("（--dry-run，未实际执行）")
        return 0

    for tid in ids:
        subprocess.run(["python3", str(QUEUE), "reset", tid], check=False)
    print("已放回队列（reset，不计失败、不退避），可继续派单。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
