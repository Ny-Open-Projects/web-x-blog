---
title: [Q1100] dry-run 与破坏性操作确认
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1100 · dry-run 与破坏性操作确认

> 难度:★★★☆ | 标签:CLI, 安全

**问**:一个会删数据、重启服务的运维 CLI,怎么设计才能让人放心敲回车?

**答**:三层防护:dry-run(默认只打印执行计划,每个动作一行,标明影响面)、显式确认(危险命令要求 `--yes` 或交互确认,交互里复读将被删除的对象)、最小爆炸半径(--limit 限制批量规模,分批执行)。实现关键是"计划与执行分离":先构建动作列表,审查后统一执行,这样 dry-run 与真实执行走同一条代码路径,不会出现"预览的和干的不一样"。

```python
# file: code/05_数据分析与工程化/q1100_dry_run.py
import sys

PLAN = ["mkdir /srv/app", "write config", "restart service"]

def confirm(prompt):
    if "--yes" in sys.argv:
        return True
    try:
        return input(prompt + " [y/N] ").strip().lower() == "y"
    except EOFError:
        print("非交互环境:请显式传 --yes 确认")
        return False

def main(argv):
    dry = "--dry-run" in argv
    print("执行计划:")
    for step in PLAN:
        print("  -", step)
    if dry:
        print("dry-run:未做任何修改")
        return 0
    if not confirm("确认执行以上动作?"):
        print("已取消")
        return 0
    print("已执行(演示)")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

**追问**:
- 追问 1:dry-run 怎么保证与真实执行一致?—— 共用"构建计划"函数,dry-run 渲染计划,真实执行同一计划,禁止两条分支各自拼逻辑。
- 追问 2:脚本调用时怎么跳过交互?—— `--yes` 显式声明,但保留 dry-run 供 CI 预检,危险等级越高越倾向人工。
