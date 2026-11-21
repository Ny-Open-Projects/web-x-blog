---
title: [Q2593] 多租户 fair-share 调度:按权重分蛋糕闲者让位
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2593 · 多租户 fair-share 调度:按权重分蛋糕闲者让位

> 难度:★★★★ | 标签:LLM 运维, 调度, 多租户

**问**:三个租户共享一池推理容量,怎么保证谁都吃不亏、闲的不浪费?

**答**:加权令牌轮转是 fair-share 的最小实现:每轮按权重给租户发令牌,有需求才消费,余量自然流转。三个性质要在实现里逐个验证:吃得饱——总供给大于等于总需求时人人满足;争抢收敛——需求远超供给时,份额收敛到权重比,本例 2 比 1 的权重分出 60 比 30;闲置让位——零需求的租户令牌被活跃方白拿,这是 fair-share 区别于硬限流的特征,硬限流下闲置就是浪费。它保证长期公平而不是瞬时公平,短窗口内租户可能拿到偏离权重的份额,这是特性不是缺陷,突发因此成为可能。要补的工程件是观测:每租户的应得份额与实得份额分开统计,偏差即不公指标,进容量周报。

```python
# file: code/06_Agent与LLM及系统设计/q2593_fair_share.py
"""Q2593 多租户 fair-share 调度:按权重分蛋糕,闲者让位。

加权令牌轮转:每轮给租户发 w 个令牌,有需求才消费,余量
自然流转;争抢时份额收敛到权重比,空闲租户的份额被活跃方
白拿,这是 fair-share 区别于硬限流的特征。
"""


def schedule(weights, demand, rounds):
    tokens = {t: 0 for t in weights}
    served = {t: 0 for t in weights}
    for _ in range(rounds):
        for t, w in weights.items():
            tokens[t] += w
        for t in weights:
            if demand[t] > served[t]:
                use = min(tokens[t], demand[t] - served[t])
                tokens[t] -= use
                served[t] += use
    return served


def main():
    r = schedule({"A": 2, "B": 1}, {"A": 40, "B": 20}, 40)   # 供给 120 = 需求
    assert r == {"A": 40, "B": 20}, r
    r2 = schedule({"A": 2, "B": 1}, {"A": 100, "B": 100}, 30)  # 供给 90 全争抢
    assert r2 == {"A": 60, "B": 30}, r2
    r3 = schedule({"A": 2, "B": 1}, {"A": 100, "B": 0}, 10)
    assert r3 == {"A": 20, "B": 0}, r3
    print("吃得饱:", r, "需求全满足")
    print("争抢:", r2, "A:B = 2:1 收敛到权重比")
    print("B 闲置:", r3, "A 白拿 B 的份额")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:权重怎么定?答:按 SLA 等级与付费档位定,再按不公指标回校,权重是治理决策不是技术参数。
- 追问二:有租户恶意憋大招怎么办?答:令牌封顶加突发审计,长期闲置突然爆量的行为触发人工审查。
