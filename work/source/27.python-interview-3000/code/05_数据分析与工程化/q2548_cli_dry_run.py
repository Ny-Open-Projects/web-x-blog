"""CLI 的 --dry-run 预演: 只出计划 零副作用"""

import csv
import json
import os
import tempfile

ROWS = [{"id": 1, "user": "u1", "amt": 100.0},
        {"id": 2, "user": "u2", "amt": 250.0},
        {"id": 3, "user": "u3", "amt": 80.0}]


def make_plan(rows, target_dir):
    path = os.path.join(target_dir, "orders_export.csv")
    return {"target": path, "rows": len(rows), "bytes_estimate": len(json.dumps(rows))}


def export(rows, target_dir, dry_run=False):
    plan = make_plan(rows, target_dir)
    if dry_run:
        return plan, False
    with open(plan["target"], "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return plan, True


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        plan, wrote = export(ROWS, tmp, dry_run=True)
        print(f"dry-run 计划: 将写 {plan['rows']} 行到 {os.path.basename(plan['target'])}, 实际写入={wrote}")
        assert not wrote and os.listdir(tmp) == [], "dry-run 不得留下任何文件"
        print("预演后目录仍为空, 副作用为零, 可安全接进审批流")
        plan, wrote = export(ROWS, tmp, dry_run=False)
        with open(plan["target"], encoding="utf-8") as f:
            n = sum(1 for _ in f) - 1
        print(f"正式执行: 写入 {n} 行, 与计划一致={n == plan['rows']}")
        assert wrote and n == plan["rows"]
    print("要点: dry-run 与正式执行共用同一份 plan 生成逻辑, 计划与结果天然对得上, 不容两套代码漂移")
