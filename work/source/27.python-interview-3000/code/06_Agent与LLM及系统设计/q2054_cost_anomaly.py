"""成本异常告警:小时成本序列的突刺与漂移两类检测,告警带冷却去重。"""
from statistics import median


class CostWatcher:
    def __init__(self, spike_mult=3.0, drift_ratio=0.3, cooldown=2):
        self.series = []             # (hour, cost)
        self.spike_mult = spike_mult
        self.drift_ratio = drift_ratio
        self.cooldown = cooldown
        self.last_alert_hour = None

    def _cooled(self, hour):
        return self.last_alert_hour is None or hour - self.last_alert_hour >= self.cooldown

    def push(self, hour, cost):
        self.series.append((hour, cost))
        alerts = []
        costs = [c for _, c in self.series]
        # 突刺:当前值高于前几小时中位数的 spike_mult 倍
        if len(costs) >= 4:
            base = median(costs[:-1][-6:])
            if base > 0 and cost > base * self.spike_mult and self._cooled(hour):
                alerts.append("突刺:%d 高于基线 %.0f 的 %.1f 倍" % (cost, base, self.spike_mult))
        # 漂移:最近 3 小时均值比之前 3 小时均值高 drift_ratio
        if len(costs) >= 6:
            recent, prev = costs[-3:], costs[-6:-3]
            mr, mp = sum(recent) / 3.0, sum(prev) / 3.0
            if mp > 0 and mr > mp * (1 + self.drift_ratio) and self._cooled(hour):
                alerts.append("漂移:近 3 小时均值 %.0f 比之前 %.0f 上升超 %.0f%%"
                              % (mr, mp, self.drift_ratio * 100))
        if alerts:
            self.last_alert_hour = hour
        return alerts


if __name__ == "__main__":
    w = CostWatcher()
    for h, c in [(1, 100), (2, 110), (3, 95), (4, 105)]:
        assert w.push(h, c) == [], "正常波动不告警"

    a1 = w.push(5, 500)                      # 基线约 102,500 是 4.9 倍
    assert len(a1) == 1 and "突刺" in a1[0], a1

    a2 = w.push(6, 480)                      # 冷却期内,同类突刺不再重复告警
    assert a2 == [], "冷却期必须压制重复告警"

    a3 = w.push(8, 200)                      # 冷却已过:5+2=7,8 可再报;此时也构成漂移
    assert a3 and ("漂移" in a3[0] or "突刺" in a3[0]), a3

    # 纯漂移场景:缓慢爬升不触发突刺,但均值抬升 30% 以上
    w2 = CostWatcher()
    for h, c in [(1, 100), (2, 100), (3, 100), (4, 140), (5, 145), (6, 150)]:
        alerts = w2.push(h, c)
    assert alerts and "漂移" in alerts[0], alerts
    print("成本告警通过:突刺与漂移两类都命中,冷却压制重复,缓慢爬升漏不掉")
