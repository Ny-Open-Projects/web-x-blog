import random


def backoff_exp(base: int, attempt: int, cap: int) -> float:
    return min(cap, base * (2 ** attempt))


def full_jitter(base: int, attempt: int, cap: int, rnd: random.Random) -> float:
    return rnd.uniform(0, backoff_exp(base, attempt, cap))


def equal_jitter(base: int, attempt: int, cap: int, rnd: random.Random) -> float:
    exp = backoff_exp(base, attempt, cap)
    return exp / 2 + rnd.uniform(0, exp / 2)


def decorrelated_jitter(base: int, prev: float, cap: int, rnd: random.Random) -> float:
    return min(cap, rnd.uniform(base, prev * 3))


def main() -> None:
    rnd = random.Random(1335)
    base, cap = 1, 8

    print("attempt | 裸指数 | full | equal | decorrelated")
    prev = base
    for a in range(5):
        d = decorrelated_jitter(base, prev, cap, rnd)
        prev = d
        print(f"  {a}     |  {backoff_exp(base, a, cap):.0f}   | {full_jitter(base, a, cap, rnd):4.2f} "
              f"| {equal_jitter(base, a, cap, rnd):4.2f} | {d:4.2f}")

    # 风暴模拟: 100 个客户端第 0 秒同时失败, 各自重试 3 次
    clients_no_jitter = [backoff_exp(base, 1, cap)] * 100   # 全员同一时刻重试
    ticks_no = {}
    for t in clients_no_jitter:
        ticks_no[round(t, 1)] = ticks_no.get(round(t, 1), 0) + 1
    peak_no = max(ticks_no.values())

    ticks_full = {}
    for _ in range(100):
        t = full_jitter(base, 1, cap, rnd)
        key = round(t / 0.25)               # 0.25s 一档
        ticks_full[key] = ticks_full.get(key, 0) + 1
    peak_full = max(ticks_full.values())

    print(f"无抖动: 重试时刻 {set(round(t, 1) for t in clients_no_jitter)}, "
          f"峰值并发 {peak_no}/tick")
    print(f"full jitter: 重试散布在 {len(ticks_full)} 个时间档, 峰值并发 {peak_full}/tick")
    assert peak_no == 100
    assert peak_full <= 60 and peak_no > peak_full * 1.5, "抖动必须显著削峰"
    print("结论: 退避决定节奏, 抖动决定不同步, 缺一不可")


if __name__ == "__main__":
    main()
