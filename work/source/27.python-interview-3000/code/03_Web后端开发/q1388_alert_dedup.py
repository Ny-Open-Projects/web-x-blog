"""告警去重:静默窗口与恢复闭环(纯标准库)。"""


class AlertManager:
    def __init__(self):
        self.state = {}

    def fire(self, key, now, silence=1800):
        st = self.state.setdefault(key, {"count": 0, "last_sent": -10 ** 9, "open": False})
        st["count"] += 1
        if not st["open"]:
            st["open"] = True
            st["last_sent"] = now
            return "notify"
        if now - st["last_sent"] >= silence:
            st["last_sent"] = now
            return f"notify-again x{st['count']}"
        return f"suppress count={st['count']}"

    def resolve(self, key):
        st = self.state.get(key)
        if st and st["open"]:
            st["open"] = False
            return f"resolved total={st['count']}"
        return None


am = AlertManager()
print("t=0    ", am.fire("5xx-spike", 0))
print("t=60   ", am.fire("5xx-spike", 60))       # 静默期内只计数
print("t=2000 ", am.fire("5xx-spike", 2000))     # 超静默期升级提醒
print("t=2100 ", am.fire("5xx-spike", 2100))
print("恢复   ", am.resolve("5xx-spike"))
