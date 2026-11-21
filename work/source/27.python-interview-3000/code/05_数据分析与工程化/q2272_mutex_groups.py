"""互斥组: 同表写入任务串行化与锁申请"""

from collections import namedtuple

Task = namedtuple("Task", "name locks dur")
TASKS = [
    Task("dwd_orders_build", ["orders", "user"], 30),
    Task("dws_orders_agg", ["orders"], 20),
    Task("dws_user_agg", ["user"], 15),
    Task("ads_both", ["orders", "user"], 10),
]


def schedule(tasks):
    """全部锁可用才启动, 等价于按互斥组串行; 返回时间线"""
    busy_until, timeline = {}, []
    for task in tasks:
        start = max([busy_until.get(r, 0) for r in sorted(task.locks)] + [0])
        end = start + task.dur
        for r in task.locks:
            busy_until[r] = end
        timeline.append((task.name, task.locks, start, end))
    return timeline


if __name__ == "__main__":
    timeline = schedule(TASKS)
    print(f"{'任务':<18}{'锁':<16}{'起':>4}{'止':>4}")
    for name, locks, s, e in timeline:
        print(f"{name:<18}{','.join(locks):<16}{s:>4}{e:>4}")
    makespan = max(e for _, _, _, e in timeline)
    print(f"总工期 {makespan} 分钟, 无互斥理论下限 {max(t.dur for t in TASKS)}; 差值是一致性代价")
    print("要点: 锁粒度到表; 多锁按固定顺序申请防死锁; 等锁带超时告警; 互斥声明走配置评审")
