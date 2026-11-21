"""分区级重跑台账: 只重算失败的分区, 成功分区原样复用"""

PARTITIONS = ["2026-11-01", "2026-11-02", "2026-11-03", "2026-11-04", "2026-11-05"]


def plan_rerun(ledger, partitions):
    """幂等重跑规划器: 只挑失败与缺失的分区, 结果与调用次数无关"""
    todo = [p for p in partitions if ledger.get(p) != "success"]
    return todo


def run_partition(ledger, part, outcome):
    ledger[part] = outcome


if __name__ == "__main__":
    ledger = {"2026-11-01": "success", "2026-11-02": "fail",
              "2026-11-04": "fail"}  # 11-03 与 11-05 从未跑过
    todo1 = plan_rerun(ledger, PARTITIONS)
    print(f"首次规划重跑: {todo1}")
    assert todo1 == ["2026-11-02", "2026-11-03", "2026-11-04", "2026-11-05"]
    # 执行: 两个失败分区修复, 11-03 成功, 11-05 仍然失败
    for p, outcome in [("2026-11-02", "success"), ("2026-11-03", "success"),
                       ("2026-11-04", "success"), ("2026-11-05", "fail")]:
        run_partition(ledger, p, outcome)
    todo2 = plan_rerun(ledger, PARTITIONS)
    print(f"二轮规划重跑: {todo2}")
    assert todo2 == ["2026-11-05"], "只有仍失败的分区需要重跑"
    # 幂等性: 规划器重复调用结果不变
    assert plan_rerun(ledger, PARTITIONS) == plan_rerun(ledger, PARTITIONS)
    run_partition(ledger, "2026-11-05", "success")
    todo3 = plan_rerun(ledger, PARTITIONS)
    print(f"全绿后规划重跑: {todo3}")
    assert todo3 == [], "全部成功后规划应为空, 重复规划也不产生任何动作"
    print("要点: 分区台账把'重跑什么'变成纯函数查询, 幂等性由状态而非纪律保证, 补数不再靠人肉记清单")
