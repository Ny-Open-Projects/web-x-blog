---
title: [Q1343] 容量估算:Little's Law 定线程池大小
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1343 · 容量估算:Little's Law 定线程池大小

> 难度:★★★☆ | 标签:Little's Law, 容量规划, 线程池

**问**:QPS 100、平均耗时 10ms,线程池开多大?拍脑袋 100 行吗?公式是什么?

**答**:Little's Law:L = λ × W——系统内平均在途请求数 = 到达率 × 平均停留时间。λ=100/s、W=0.01s,稳态在途数 L=1,理论上 1 个 worker 就能扛,留余量 2-4 倍即可;开 100 个线程纯属浪费,还会带来调度与上下文切换成本。但公式只对"无排队"成立:worker 数小于 L 时队列开始堆积,停留时间从"服务时间"膨胀成"排队+服务",在途数随之爆炸——所以容量估算必须回答两个问题:稳态需要几个 worker(λ×W),以及突发能容忍多深的队列。下面的模拟用离散事件验证:worker 充足时实测 L 贴近公式;worker 不足时 L 远超公式,呈排队膨胀。

```python
# file: code/02_并发与网络工程/q1343_littles_law_capacity.py
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
```

**追问**:1) 为什么"平均耗时"要用停留时间 W 而不是服务时间?——Little's Law 里的 W 是请求从进入到离开的全程时间;用服务时间代入会系统性低估容量,尤其是有排队时,低估可能差一个数量级。2) 公式失效的两个方向?——worker<L 时排队膨胀(W 从服务时间变成排队+服务,L 随之爆炸,正反馈过载);worker 远大于 L 时资源浪费+调度开销;容量估算要同时回答「稳态 worker 数」与「突发队列深度」两个问题——只算一个都不完整。3) 突发队列深度怎么定?——按「突发时长×(到达率-服务能力)」估最大积压,队列上限设在该值与内存账之间;配合削峰(Q1334)决定超出的怎么拒;还要核对线程栈内存账(每线程 8MB 虚拟内存,100 线程就是 800MB)。4) 生产陷阱?——用 P50 耗时算 W(尾延迟时代 W 被 P99 主导,容量被低估数倍);线程池大小忽略 IO 等待(阻塞 IO 下 worker 时间大头在等 IO,公式要按「并发在途」而不是「CPU 密集」算,Q655 的线程模型);队列无界,Little's Law 完全失效(无限队列吸收一切,延迟无限涨);拍脑袋 100 线程(见原问)。

---
