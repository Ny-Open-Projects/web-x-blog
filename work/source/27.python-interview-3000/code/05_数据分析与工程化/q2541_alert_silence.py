"""断流告警的静默期: 同因重复只计数, 超期重提醒, 恢复即清零"""

SILENCE = 30       # 静默期分钟


class AlertManager:
    def __init__(self):
        self.active = {}      # key -> last_notify 时刻
        self.notified = 0
        self.suppressed = 0

    def fire(self, source, kind, now):
        key = (source, kind)
        if key in self.active:
            if now - self.active[key] < SILENCE:
                self.suppressed += 1
                return "suppressed"
            self.active[key] = now
            self.notified += 1
            return "reminded"
        self.active[key] = now
        self.notified += 1
        return "notified"

    def recover(self, source, kind, now):
        self.active.pop((source, kind), None)
        return f"已恢复@{now}"


if __name__ == "__main__":
    m = AlertManager()
    print(f"10:00 首报: {m.fire('orders_db', 'no_data', 0)}")
    print(f"10:10 重复: {m.fire('orders_db', 'no_data', 10)} (静默期内只计数)")
    print(f"10:40 再响: {m.fire('orders_db', 'no_data', 40)} (超静默期重提醒)")
    print(f"10:50 恢复: {m.recover('orders_db', 'no_data', 50)}")
    print(f"11:00 再断: {m.fire('orders_db', 'no_data', 60)} (恢复后是新事件)")
    assert (m.notified, m.suppressed) == (3, 1)
    print(f"统计: 实际通知 {m.notified} 次, 静默压制 {m.suppressed} 次")
    print("要点: 静默键 = 源+类型, 通知不消失只是降噪, 恢复事件必须清静默否则复发被吞")
