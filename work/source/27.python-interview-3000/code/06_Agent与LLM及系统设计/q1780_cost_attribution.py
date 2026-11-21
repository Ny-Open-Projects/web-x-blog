"""成本归因到租户:每次调用记 token 流水,聚合成账单并校验分账总额守恒。"""

PRICE_IN = 0.002                                # 每千 token 输入价
PRICE_OUT = 0.006                               # 每千 token 输出价

KNOWN_TENANTS = {"tenant-a", "tenant-b", "tenant-c"}


class CostLedger:
    def __init__(self):
        self.rows = []

    def record(self, tenant, tokens_in, tokens_out):
        assert tenant in KNOWN_TENANTS, "未登记租户不允许记账,拒绝进公共池"
        cost = tokens_in / 1000.0 * PRICE_IN + tokens_out / 1000.0 * PRICE_OUT
        self.rows.append({"tenant": tenant, "tin": tokens_in, "tout": tokens_out,
                          "cost": round(cost, 6)})
        return cost

    def bill(self, tenant):
        rows = [r for r in self.rows if r["tenant"] == tenant]
        return {"calls": len(rows),
                "tokens": sum(r["tin"] + r["tout"] for r in rows),
                "cost": round(sum(r["cost"] for r in rows), 6)}

    def audit(self):
        """审计:分账之和必须等于总账,防止归因丢失。"""
        total = round(sum(r["cost"] for r in self.rows), 6)
        parts = round(sum(self.bill(t)["cost"] for t in KNOWN_TENANTS), 6)
        return {"total": total, "parts": parts, "balanced": total == parts}


if __name__ == "__main__":
    led = CostLedger()
    led.record("tenant-a", 1000, 500)            # 0.005
    led.record("tenant-a", 2000, 1000)           # 0.010
    led.record("tenant-b", 500, 1500)            # 0.010
    bill_a = led.bill("tenant-a")
    assert bill_a == {"calls": 2, "tokens": 4500, "cost": 0.015}
    assert led.bill("tenant-b")["cost"] == 0.01
    audit = led.audit()
    assert audit["balanced"] is True and audit["total"] == 0.025, "分账守恒"

    rejected = False
    try:
        led.record("tenant-x", 100, 100)
    except AssertionError:
        rejected = True
    assert rejected, "未登记租户记账必须被拒"
    print("成本归因通过:按租户流水记账 可聚合 总额守恒,未登记租户被拒")
