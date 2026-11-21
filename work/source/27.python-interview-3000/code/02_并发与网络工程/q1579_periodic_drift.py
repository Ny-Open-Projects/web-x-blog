"""周期任务的漂移账: sleep 链 vs 绝对时刻调度。

threading.Timer 链和 sleep(period) 都是"上一次结束后再等一个周期",
任务自身耗时累计进周期 -> 漂移线性增长。正确姿势: 记住绝对时刻表
next = start + n * period, 睡到点为止, 任务耗时被吸收而非叠加。
"""
import time

PERIOD = 0.2
JOB_COST = 0.05
ROUNDS = 6


def job():
    time.sleep(JOB_COST)        # 模拟每轮任务自身的耗时


def naive_schedule():
    stamps = []
    for _ in range(ROUNDS):
        job()
        stamps.append(time.monotonic())
        time.sleep(PERIOD)      # 错误: 周期被 JOB_COST 拉长
    return stamps


def absolute_schedule():
    stamps = []
    start = time.monotonic()
    for n in range(1, ROUNDS + 1):
        target = start + n * PERIOD
        delta = target - time.monotonic()
        if delta > 0:
            time.sleep(delta)
        stamps.append(time.monotonic())
        job()                   # 任务耗时占用下一个周期的富余
    return stamps


def drift(stamps, period):
    return max(abs((t - stamps[0]) - i * period)
               for i, t in enumerate(stamps))


def main():
    naive = naive_schedule()
    absolute = absolute_schedule()
    d1 = drift(naive, PERIOD)
    d2 = drift(absolute, PERIOD)
    print("sleep 链 各轮触发时刻:", [round(t - naive[0], 3) for t in naive])
    print("绝对时刻 各轮触发时刻:", [round(t - absolute[0], 3) for t in absolute])
    print("sleep 链最大漂移: %.3fs | 绝对时刻最大漂移: %.3fs" % (d1, d2))
    assert d1 > d2 + 0.1, "sleep 链的漂移应显著大于绝对时刻调度"
    assert d2 < 0.1, "绝对时刻调度应几乎无漂移"
    print("结论: 周期调度的锚必须是绝对时刻, 而不是'上一轮结束'")


if __name__ == "__main__":
    main()
