import heapq
import random


def simulate(lam: float, service_s: float, workers: int,
             horizon_s: float = 5.0, seed: int = 1343) -> dict:
    """泊松到达 + 指数定长服务的离散事件模拟。"""
    rnd = random.Random(seed)
    arrivals = []
    t = 0.0
    while True:
        t += rnd.expovariate(lam)
        if t >= horizon_s:
            break
        arrivals.append(t)

    free = [0.0] * workers
    heapq.heapify(free)
    total_time = waits = 0.0
    for at in arrivals:
        w = heapq.heappop(free)
        start = max(at, w)
        waits += start - at
        end = start + service_s
        total_time += end - at
        heapq.heappush(free, end)

    n = len(arrivals)
    return {"n": n,
            "L": total_time / horizon_s,          # 平均在途数
            "W": total_time / n,                  # 平均停留时间
            "wait_ratio": waits / total_time}


def main() -> None:
    lam, service = 100.0, 0.01
    print(f"λ={lam:.0f}/s, W_service={service*1000:.0f}ms -> 理论稳态 L=λ×W={lam*service:.1f}")

    r1 = simulate(lam, service, workers=8)
    print(f"worker=8 (≈8L): L实测={r1['L']:.2f}, 排队占比 {r1['wait_ratio']:.0%}")
    assert 0.7 <= r1["L"] <= 1.3 and r1["wait_ratio"] < 0.1

    r2 = simulate(lam, service, workers=2)
    print(f"worker=2 (2L):  L实测={r2['L']:.2f}, 排队占比 {r2['wait_ratio']:.0%}")
    assert r2["wait_ratio"] < 0.3

    r3 = simulate(lam, service, workers=1)
    print(f"worker=1 (<L):  L实测={r3['L']:.2f}, 排队占比 {r3['wait_ratio']:.0%}")
    assert r3["wait_ratio"] > 0.5, "worker 低于 λW 时应出现明显排队"
    print("容量公式: workers >= ceil(λ×W) 再乘安全系数 2-3, 队列上限 = 可容忍延迟 - λ×W")


if __name__ == "__main__":
    main()
