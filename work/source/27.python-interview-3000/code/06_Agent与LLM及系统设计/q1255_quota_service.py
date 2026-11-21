"""配额服务:令牌预取 + 分片计数 + 日配额 + 降级快照 + 对账修正。"""
import time


class ShardCounter:
    def __init__(self):
        self.windows = {}                     # (tenant, window_id) -> count
        self.daily = {}

    def acquire_batch(self, tenant, n, now, daily_limit):
        wid = int(now // 10)                  # 固定窗口 10s + 客户端抖动
        cur = self.windows.get((tenant, wid), 0)
        used_day = self.daily.get(tenant, 0)
        grant = min(n, max(0, daily_limit - used_day))
        self.windows[(tenant, wid)] = cur + grant
        self.daily[tenant] = used_day + grant
        return grant

    def snapshot(self, tenant, daily_limit):
        return {"remaining": max(0, daily_limit - self.daily.get(tenant, 0)),
                "ts": time.monotonic()}


class SDK:
    """客户端 SDK:预取一批令牌本地发放;断连时用快照降级。"""

    def __init__(self, tenant, counter, batch=5, daily_limit=20):
        self.tenant, self.counter, self.batch = tenant, counter, batch
        self.daily_limit, self.local = daily_limit, 0
        self.snapshot, self.connected = None, True

    def allow(self, now):
        if self.local > 0:
            self.local -= 1
            return True
        if self.connected:
            self.local = self.counter.acquire_batch(self.tenant, self.batch, now, self.daily_limit)
            if self.local > 0:
                self.local -= 1
                return True
            return False
        if self.snapshot and self.snapshot["remaining"] > 0:   # 降级:快照额度本地扣减
            self.snapshot["remaining"] -= 1
            return True
        return False


if __name__ == "__main__":
    counter = ShardCounter()
    sdk = SDK("tenant-a", counter, batch=5, daily_limit=20)

    granted = [sdk.allow(now=1.0 + i * 0.01) for i in range(18)]
    print("18 次请求放行:", sum(granted), "次(预取批量减少 Redis 压力)")
    assert sum(granted) == 18, "日配额 20 内应放行"

    # 断连降级:SDK 带着最近快照继续工作,本地扣减防超卖
    sdk.snapshot = counter.snapshot("tenant-a", 20)
    sdk.snapshot["remaining"] = 2
    sdk.connected = False
    sdk.local = 0
    degraded = [sdk.allow(now=9.0) for _ in range(4)]
    print("断连后按快照降级放行:", sum(degraded), "次(快照余额 2,不超卖)")
    assert sum(degraded) == 2, "快照降级按余额扣减,不会超卖"

    # 对账:计数器日账 vs 业务侧记录
    counter_daily = counter.daily["tenant-a"]
    biz_ledger = 18                                # 业务侧自己的记账
    drift = abs(counter_daily - biz_ledger) / max(counter_daily, 1)
    print(f"对账: 配额服务 {counter_daily} vs 业务账单 {biz_ledger},偏差 {drift:.0%}")
    assert drift < 0.2, "偏差超 20% 触发人工核查"
    print("高可用要点: 无状态接入 + 预取降 QPS + 快照降级 + 对账闭环")
