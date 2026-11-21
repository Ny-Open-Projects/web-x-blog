"""租户配额的预留-结算模型: 先占座, 跑完按实结算"""


class QuotaLedger:
    def __init__(self, tenant, monthly_quota):
        self.tenant = tenant
        self.quota = monthly_quota
        self.reserved = 0
        self.used = 0
        self.holds = {}   # job_id -> 预留量

    def available(self):
        return self.quota - self.reserved - self.used

    def reserve(self, job_id, units):
        if job_id in self.holds:
            return False, f"{job_id} 已有预留, 不可重复占座"
        if units > self.available():
            return False, f"预留 {units} 超出剩余配额 {self.available()}, 拒绝"
        self.reserved += units
        self.holds[job_id] = units
        return True, f"预留成功, 剩余 {self.available()}"

    def settle(self, job_id, actual):
        if job_id not in self.holds:
            return False, f"{job_id} 无预留记录"
        hold = self.holds.pop(job_id)
        self.reserved -= hold
        self.used += actual
        over = actual - hold
        note = f"实际 {actual} 超预留 {over}, 计入已用" if over > 0 else f"实际 {actual}, 释放 {hold - actual}"
        return True, f"结算完成, 剩余 {self.available()} ({note})"


if __name__ == "__main__":
    led = QuotaLedger("tenant_a", 100)
    seq = [
        ("reserve", "j1", 60), ("reserve", "j2", 50), ("settle", "j1", 40),
        ("reserve", "j2", 50), ("settle", "j2", 45), ("reserve", "j3", 20),
    ]
    for op, job, units in seq:
        fn = led.reserve if op == "reserve" else led.settle
        ok, why = fn(job, units)
        print(f"{op:<8} {job} {units:>3}: {'OK ' if ok else 'REJ'} {why}")
    assert led.available() == 15, "最终剩余应为 15"
    assert led.used == 85 and led.reserved == 0, "已用 85, 无挂起预留"
    print("要点: 预留防超卖, 结算按实回收, 挂起预留必须可观测, 否则漏结算就是配额黑洞")
