"""Q2864 重试预算:失败率联动重试闸门 防Retry风暴。

无预算的重试是雪崩放大器:下游一抖,重试流量能把基数放大三倍。
给重试设预算桶:每个完成的请求回填 1 个令牌,每次重试花 1 个,
预算耗尽后失败请求直接快速失败——用牺牲一小撮请求换整个系统的稳定。
"""


class RetryBudget:
    def __init__(self, window_requests=100, ratio=0.1):
        self.capacity = int(window_requests * ratio)
        self.tokens = float(self.capacity)

    def try_acquire_retry(self):
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False

    def on_request_done(self):
        """每完成一个客户端请求(不论成败)回填 1 令牌,不超容量。"""
        self.tokens = min(self.capacity, self.tokens + 1.0)


def simulate(requests, budget):
    """requests: 每项 (失败次数, 想重试的次数)。返回统计。"""
    allowed = denied = shed = 0
    for fails, wanted in requests:
        used = 0
        for _ in range(wanted):
            if budget.try_acquire_retry():
                used += 1
                allowed += 1
            else:
                denied += 1
                break
        if used < wanted and fails > used:
            shed += 1  # 想重试被拒,快速失败
        budget.on_request_done()
    return {"allowed": allowed, "denied": denied, "shed": shed}


def main():
    # 前 20 个普通请求各想重试 1 次,后 15 个困难请求想重试 2 次
    requests = [(1, 1)] * 20 + [(2, 2)] * 15
    budget = RetryBudget(window_requests=100, ratio=0.1)
    stats = simulate(requests, budget)
    # 普通请求净消耗 0(花1回填1);困难请求花2回填1,净 -1
    # 预算 10 个令牌:前 9 个困难请求重满 2 次,第 10 个起只重 1 次
    assert stats["allowed"] == 20 + 9 * 2 + 6, stats
    assert stats["denied"] == 6, stats
    assert stats["shed"] == 6, stats
    assert budget.tokens < 10.0, budget.tokens
    print("重试放行:", stats["allowed"], "被闸:", stats["denied"])
    print("快速失败请求:", stats["shed"], "(占 17%,换下游不被重试放大)")
    print("剩余预算:", budget.tokens)


if __name__ == "__main__":
    main()
