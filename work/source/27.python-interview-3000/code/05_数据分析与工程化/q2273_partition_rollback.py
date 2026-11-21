"""分区级回滚: 误写分区检测, 快照覆盖与审计"""

import hashlib
import json
from datetime import date

PART_ROWS = {
    date(2026, 3, 6): 1_020_000,
    date(2026, 3, 7): 1_015_000,
    date(2026, 3, 8): 12_000,      # 上游脏数据污染当天分区
    date(2026, 3, 9): 1_018_000,
}
BASELINE = 1_017_000
TOL = 0.3
SNAPSHOT = {   # 模拟快照服务返回: 内容与校验和
    "rows": 1_018_000,
    "blob": "snapshot_d7_parquet",
    "checksum": hashlib.md5(b"snapshot_d7_parquet").hexdigest(),
}


def detect_bad():
    return sorted(d for d, n in PART_ROWS.items() if abs(n - BASELINE) / BASELINE > TOL)


def repair_plan(upstream_fixed):
    steps = ["冻结下游对该分区的读取"]
    if upstream_fixed:
        steps.append("上游已修复 -> 重跑当天管道生成新分区")
    else:
        steps.append(f"上游未修 -> 用快照整体覆盖, 校验和 {SNAPSHOT['checksum'][:8]}")
        steps.append(f"覆盖后复核行数 {SNAPSHOT['rows']} 并打 degraded 标注")
    steps.append("写审计记录供追溯")
    return steps


if __name__ == "__main__":
    bad = detect_bad()
    print(f"异常分区: {[str(d) for d in bad]} (偏离基线超 {TOL:.0%})")
    for d in bad:
        for s in repair_plan(upstream_fixed=False):
            print(f"  {d}: {s}")
    audit = {"partition": str(bad[0]) if bad else None, "action": "restore_from_snapshot",
             "checksum": SNAPSHOT["checksum"][:8], "rows": SNAPSHOT["rows"]}
    print("审计:", json.dumps(audit, ensure_ascii=False))
    print("要点: 修复粒度到分区; 快照先验校验和再覆盖; 一切覆盖动作写审计可追溯")
