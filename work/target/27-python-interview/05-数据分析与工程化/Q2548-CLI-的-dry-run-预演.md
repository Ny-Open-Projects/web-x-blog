---
title: [Q2548] CLI 的 --dry-run 预演
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2548 · CLI 的 --dry-run 预演

> 难度:★☆☆☆ | 标签:CLI, dry-run

**问**:一个会写文件、会调接口的工具,怎么让用户敢直接跑?

**答**:给所有有副作用的命令配 --dry-run:预演时执行与正式运行完全相同的计划生成逻辑,输出"将写哪个文件、多少行、估多大",但不落一笔副作用。实测 dry-run 后目标目录 os.listdir 为空,零副作用得到断言级验证;正式执行写入 3 行,与计划声明的行数严格一致——因为计划与执行共用同一份 plan 生成代码,不存在两套逻辑漂移的空间。dry-run 的价值是把"你确定吗"从口头确认变成机器验证:预演输出可以贴进审批单、可以接进自动审核,审批通过再去掉 dry-run 执行。写文件的、发请求的、改配置的命令都该有它,这是 CLI 的安全带。预演还能顺带暴露路径权限、目标冲突这类环境问题,提前到执行前失败。

```python
# file: code/05_数据分析与工程化/q2548_cli_dry_run.py
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
```

**追问**:
- 追问 1:dry-run 能覆盖外部副作用吗?—— 对写类接口传 execute=false 让下游也预演,或预演时改调影子环境;只预演本地、外部照发是最常见的假安全。
- 追问 2:预演和事务回滚什么关系?—— 互补:事务保证"失败即无痕",dry-run 保证"执行前人已看过计划",一个管失败一个管决策。
