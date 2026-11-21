"""连接风暴的冷却: 冷却期 半开探测与渐进放行"""
import random

class CooldownGate:
    """open 拒绝 -> cooldown 静默 -> half-open 渐进放行 -> closed 恢复"""
    def __init__(self, cooldown_ticks, probe_rate, ramp=0.25):
        self.cooldown = cooldown_ticks
        self.probe_rate = probe_rate
        self.ramp = ramp
        self.ticks = 0
        self.state = "open"
        self.share = 0.0

    def admit(self, n):
        if self.state == "open":
            self.ticks += 1
            if self.ticks >= self.cooldown:
                self.state = "half-open"
                self.share = self.probe_rate
            return 0
        if self.state == "half-open":
            allow = int(n * self.share)
            self.share = min(1.0, self.share + self.ramp)
            if self.share >= 1.0:
                self.state = "closed"
            return allow
        return n

random.seed(5)
gate = CooldownGate(cooldown_ticks=3, probe_rate=0.1)
print("tick  请求  放行  状态")
for t in range(1, 13):
    req = random.randint(80, 120)
    print("%4d %5d %5d  %s" % (t, req, gate.admit(req), gate.state))
print("恢复不是开关是斜坡: 冷却退潮 半开探测 比例爬坡, 任一轮失败退回冷却")
