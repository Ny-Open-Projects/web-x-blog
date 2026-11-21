"""回滚演练脚本:dry-run 出计划、真演练记录耗时与健康验证"""

import datetime as dt
import time

DRILL_LOG = []


def step(name, fn=None, dry_run=False):
    print(f"  [计划] {name}") if dry_run else print(f"  [执行] {name}", end=" ")
    if dry_run:
        return
    start = time.perf_counter()
    if fn:
        fn()
    time.sleep(0.05)  # 模拟动作耗时
    DRILL_LOG.append((name, time.perf_counter() - start))
    print(f"完成 用时 {time.perf_counter() - start:.2f}s")


def rollback_drill(current="v2.3.1", target="v2.3.0", dry_run=False):
    print(f"回滚演练 {current} -> {target} dry_run={dry_run}")
    actions = [
        ("冻结新变更窗口", None),
        ("摘除金丝雀流量", None),
        ("切换镜像到上一版本", None),
        ("验证健康检查与冒烟", None),
        ("恢复流量并观察 10 分钟", None),
    ]
    for name, fn in actions:
        step(name, fn, dry_run)
    if not dry_run:
        total = sum(t for _, t in DRILL_LOG)
        print(f"演练总耗时 {total:.2f}s,记录进演练台账")
    print("要点:回滚演练的产出是'MTTR 实测值 + 剧本里缺的步骤',不是跑一遍就完了")


if __name__ == "__main__":
    rollback_drill(dry_run=True)
    print()
    rollback_drill(dry_run=False)
