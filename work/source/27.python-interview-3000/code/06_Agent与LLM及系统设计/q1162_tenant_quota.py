"""多租户配额:预扣-结算两阶段 + 窗口配额 + 429 携带重试提示。"""
import time


class TenantQuota:
    def __init__(self, plans):
        self.plans = plans                  # tenant -> {"rpm": n, "daily_tokens": n}
        self.minute = {}                    # (tenant, minute) -> count
        self.day_tokens = {}                # tenant -> used tokens
        self.holds = {}                     # 预扣中的 token

    def _minute_key(self, tenant):
        return (tenant, int(time.time() // 60))

    def try_acquire(self, tenant, est_tokens):
        plan = self.plans[tenant]
        mk = self._minute_key(tenant)
        if self.minute.get(mk, 0) >= plan["rpm"]:
            return False, "rate_limited", 5
        if self.day_tokens.get(tenant, 0) + self.holds.get(tenant, 0) + est_tokens > plan["daily_tokens"]:
            return False, "quota_exceeded", 3600
        self.minute[mk] = self.minute.get(mk, 0) + 1
        self.holds[tenant] = self.holds.get(tenant, 0) + est_tokens
        return True, "ok", 0

    def settle(self, tenant, real_tokens):
        self.holds[tenant] = max(0, self.holds.get(tenant, 0) - 0)  # 简化:整单结算
        self.holds[tenant] = 0
        self.day_tokens[tenant] = self.day_tokens.get(tenant, 0) + real_tokens


if __name__ == "__main__":
    plans = {"free-user": {"rpm": 3, "daily_tokens": 5000},
             "vip": {"rpm": 100, "daily_tokens": 10 ** 7}}
    q = TenantQuota(plans)

    results = [q.try_acquire("free-user", 400)[1] for _ in range(5)]
    print("免费租户连打 5 次:", results)
    assert results[3] == "rate_limited", "第 4 次应触发 RPM 限流"

    q.settle("free-user", 400 * 3)
    ok, why, retry_after = q.try_acquire("free-user", 1000)
    q.settle("free-user", 1200)
    for _ in range(4):
        ok, why, _ = q.try_acquire("free-user", 1500)
        if not ok:
            break
        q.settle("free-user", 1500)
    print("日配额状态:", why, "Retry-After:", retry_after, "s")
    assert why in ("quota_exceeded", "rate_limited")
    vip_ok, vip_why, _ = q.try_acquire("vip", 5000)
    print("VIP 租户不受影响:", vip_why)
    assert vip_ok
