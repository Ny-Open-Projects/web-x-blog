"""Q2858 供应商配额的分桶计费:档位桶 应急桶与借据台账。

不同模型档位的价格和配额差一个量级,混在一个池子里算账必然互相
挤占。按档位分桶计费,主桶耗尽可借应急桶,借了多少留借据,应急桶
再耗尽就记超支——账目每一笔都对得上。
"""


class BucketBilling:
    def __init__(self, caps, emergency_cap):
        self.caps = dict(caps)
        self.used = {k: 0 for k in caps}
        self.emergency_cap = emergency_cap
        self.emergency_used = 0
        self.ious = []
        self.overages = []

    def record(self, tenant, tier, tokens):
        cap = self.caps[tier]
        need = self.used[tier] + tokens
        if need <= cap:
            self.used[tier] = need
            return "in_bucket"
        borrow = min(need - cap, self.emergency_cap - self.emergency_used)
        self.emergency_used += borrow
        spill = need - cap - borrow
        if borrow > 0:
            self.ious.append({"tenant": tenant, "tier": tier,
                              "borrow": borrow})
        if spill > 0:
            self.overages.append({"tenant": tenant, "tier": tier,
                                  "spill": spill})
        self.used[tier] = cap
        return "borrowed" if spill == 0 else "overage"


def main():
    bill = BucketBilling(caps={"lite": 5000, "pro": 10000},
                         emergency_cap=3000)
    assert bill.record("t1", "pro", 8000) == "in_bucket"
    r1 = bill.record("t1", "pro", 4000)   # 主桶差 2000,借应急
    assert r1 == "borrowed", r1
    assert bill.ious == [{"tenant": "t1", "tier": "pro", "borrow": 2000}]
    assert bill.used["pro"] == 10000 and bill.emergency_used == 2000
    r2 = bill.record("t1", "pro", 2000)   # 再借 1000,应急只剩 1000,溢出 1000
    assert r2 == "overage", r2
    assert bill.overages == [{"tenant": "t1", "tier": "pro", "spill": 1000}]
    # lite 桶不受 pro 桶挤占影响
    assert bill.record("t2", "lite", 1000) == "in_bucket"
    assert bill.used["lite"] == 1000
    print("主桶用量:", bill.used)
    print("应急桶:", bill.emergency_used, "借据:", bill.ious)
    print("超支记录:", bill.overages)


if __name__ == "__main__":
    main()
