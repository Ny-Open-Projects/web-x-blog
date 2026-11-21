"""作业队列的老化防饿: 等待时间兑换优先级, 低优作业也能出头"""
import random

AGING_INTERVAL = 10   # 每等待 10 拍
BOOST = 1             # 有效优先级 +1
HORIZON = 50


def effective(base, waited):
    return base + waited // AGING_INTERVAL * BOOST


def simulate(aging=True):
    queue, done, schedule_log = [], [], []
    arrivals = {t: [] for t in range(HORIZON)}
    for t in range(HORIZON):                  # 高优作业流: 每拍来一个, 到达率等于服务率
        arrivals[t].append((5, f"adhoc_{t}"))
    arrivals[0].append((1, "nightly_backfill"))  # 永远的低优, 与高优同拍进场
    for t in range(HORIZON):
        for base, name in arrivals[t]:
            queue.append([base, t, name])
        if not queue:
            continue
        if aging:
            pick = max(queue, key=lambda j: (effective(j[0], t - j[1]), -j[1]))
        else:
            pick = max(queue, key=lambda j: (j[0], -j[1]))
        queue.remove(pick)
        done.append((t, pick[2]))
        schedule_log.append(f"tick {t}: {pick[2]} (base {pick[0]}, 等了 {t - pick[1]} 拍)")
    return done, schedule_log


if __name__ == "__main__":
    done_a, log_a = simulate(aging=True)
    done_n, _ = simulate(aging=False)
    night_a = next((t for t, n in done_a if n == "nightly_backfill"), None)
    night_n = next((t for t, n in done_n if n == "nightly_backfill"), None)
    print("老化开启后的关键调度:")
    for line in log_a[-3:]:
        print(f"  {line}")
    print(f"nightly_backfill 在第 {night_a} 拍被执行")
    print(f"关闭老化的对照: nightly_backfill 执行时刻 {night_n} (None 表示饿死)")
    assert night_a is not None and night_a <= 45, "老化应让低优作业在时限内出头"
    assert night_n is None, "无老化时持续高优流会把低优作业饿死"
    waits = [t - 0 for t, n in done_a if n == "nightly_backfill"]
    assert waits and waits[0] <= 45
    print("要点: 老化把等待时间兑换成优先级, 队列公平从'运气'变成'参数', AGING_INTERVAL 和 BOOST 就是公平价格")
