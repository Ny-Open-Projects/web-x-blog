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
