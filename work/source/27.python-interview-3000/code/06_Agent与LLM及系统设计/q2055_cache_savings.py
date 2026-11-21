"""缓存命中的收益核算:命中省下的输入 token 与费用记账,输出命中率与节省比。"""


class CacheLedger:
    def __init__(self, price_per_1k):
        self.price = price_per_1k
        self.hits = 0
        self.misses = 0
        self.saved_tokens = 0
        self.gross_tokens = 0       # 若完全无缓存本应支付的输入 token

    def record(self, prompt_tokens, hit):
        self.gross_tokens += prompt_tokens
        if hit:
            self.hits += 1
            self.saved_tokens += prompt_tokens
        else:
            self.misses += 1

    def report(self):
        total = self.hits + self.misses
        rate = self.hits / float(total) if total else 0.0
        saved_cost = self.saved_tokens / 1000.0 * self.price
        actual_cost = (self.gross_tokens - self.saved_tokens) / 1000.0 * self.price
        denom = saved_cost + actual_cost
        return {"requests": total, "hit_rate": round(rate, 3),
                "saved_tokens": self.saved_tokens,
                "gross_tokens": self.gross_tokens,
                "saved_cost": round(saved_cost, 4),
                "actual_cost": round(actual_cost, 4),
                "savings_ratio": round(saved_cost / denom, 3) if denom else 0.0}


if __name__ == "__main__":
    led = CacheLedger(price_per_1k=0.002)
    # 10 次请求:7 次命中(每次 800 token),3 次未命中(每次 1000 token)
    for _ in range(7):
        led.record(800, hit=True)
    for _ in range(3):
        led.record(1000, hit=False)
    r = led.report()
    assert r["requests"] == 10 and r["hit_rate"] == 0.7
    assert r["saved_tokens"] == 5600
    assert r["gross_tokens"] == 7 * 800 + 3 * 1000 == 8600
    assert r["saved_cost"] == 0.0112, r["saved_cost"]
    assert r["actual_cost"] == 0.006, r["actual_cost"]
    assert r["savings_ratio"] == 0.651, "节省比按费用口径 5.6 除以 8.6"
    assert r["saved_cost"] > r["actual_cost"], "高命中下省的比花的多"

    empty = CacheLedger(price_per_1k=0.002)
    assert empty.report() == {"requests": 0, "hit_rate": 0.0, "saved_tokens": 0,
                              "gross_tokens": 0, "saved_cost": 0,
                              "actual_cost": 0, "savings_ratio": 0}
    print("收益核算通过:7 成命中省 5600 token 合 0.0112 元,节省比 0.651 账目闭合")
