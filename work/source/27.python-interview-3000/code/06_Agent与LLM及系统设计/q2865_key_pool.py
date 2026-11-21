"""Q2865 密钥池轮换:多 key 分摊限流与冷却调度。

单一 API key 撞上限流,服务就停摆;多把 key 轮着用可以把限流额度
翻倍。轮换策略:优先用剩余额度最多的 key,耗尽的进入冷却,整窗
重置后回归池子;全池耗尽要显式报错,而不是拿着 429 硬敲。
"""


class KeyPool:
    def __init__(self, limits):
        self.limits = dict(limits)          # key -> 窗口内额度
        self.used = {k: 0 for k in limits}
        self.window_end = 0
        self.order = list(limits)           # 固定顺序用于同分裁决

    def acquire(self, now):
        if now >= self.window_end and self.window_end > 0:
            self.used = {k: 0 for k in self.limits}
            self.window_end = 0
        best, best_left = None, -1
        for k in self.order:
            left = self.limits[k] - self.used[k]
            if left > best_left:
                best, best_left = k, left
        if best_left <= 0:
            self.window_end = self.window_end or (now + 60)
            return None
        self.used[best] += 1
        return best


def main():
    pool = KeyPool({"k1": 2, "k2": 2, "k3": 2})
    seq = [pool.acquire(now=0) for _ in range(7)]
    # 前三把各用一次,接着各自第二次,第七次全池耗尽
    assert seq[:3] == ["k1", "k2", "k3"], seq
    assert seq[3:6] == ["k1", "k2", "k3"], seq
    assert seq[6] is None, seq
    # 窗口未重置继续取:仍然拿不到
    assert pool.acquire(now=30) is None
    # 窗口翻篇:池子满血复活
    assert pool.acquire(now=61) == "k1", pool.used
    print("轮换序列:", seq[:6], "第7次:", seq[6])
    print("窗口重置后恢复:", pool.used)


if __name__ == "__main__":
    main()
