"""依赖就绪判断与超时熔断:调度器视角的 DAG 执行模拟"""

import datetime as dt

TASKS = {
    # name: 依赖任务列表
    "ods_sync":   [],
    "dim_user":   [],
    "dwd_clean":  ["ods_sync"],
    "ads_funnel": ["dwd_clean", "dim_user"],
    "ads_report": ["ads_funnel"],
}

STUCK = {"dim_user"}              # 模拟一个上游迟迟不成功
DEADLINE = dt.time(4, 0)
NOW = dt.time(4, 30)


def next_runnable(done, failed):
    out = []
    for name, deps in TASKS.items():
        if name in done or name in failed:
            continue
        if all(d in done for d in deps):
            out.append(name)
    return sorted(out)


def schedule(deadline=DEADLINE, now=NOW):
    done, failed = [], set()
    for name in sorted(TASKS):
        deps = TASKS[name]
        if any(d in failed for d in deps):
            failed.add(name)      # 依赖失败级联熔断
    rounds = 0
    while rounds < 10:
        runnable = next_runnable(done, failed)
        if not runnable:
            break
        for name in runnable:
            if name in STUCK:
                failed.add(name)
                print(f"  任务 {name} 超时失败 -> 熔断")
            else:
                done.append(name)
                print(f"  任务 {name} 完成")
        rounds += 1
    if now > deadline:
        print(f"  已超过 deadline {deadline},剩余任务冻结并告警")
    return done, failed


if __name__ == "__main__":
    print("调度开始:")
    done, failed = schedule()
    print("\n完成:", done)
    print("失败/熔断:", sorted(failed))
    print("要点:就绪=依赖全部成功;熔断要输出明确的未跑清单,而不是让下游空跑")
