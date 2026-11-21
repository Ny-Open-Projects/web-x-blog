"""熔断器: 失败率统计 -> open -> 半开探测 -> 恢复"""
import time

class CircuitBreaker:
    def __init__(self, fail_threshold=3, window=5.0, cooldown=2.0):
        self.fail_threshold, self.window, self.cooldown = fail_threshold, window, cooldown
        self.state = "closed"
        self.failures, self.opened_at = [], 0.0

    def allow(self):
        if self.state == "open":
            if time.monotonic() - self.opened_at > self.cooldown:
                self.state = "half-open"           # 半开: 放一个探测请求
                return True
            return False
        return True

    def record(self, ok):
        now = time.monotonic()
        if ok:
            if self.state == "half-open":
                self.state = "closed"              # 探测成功恢复
            self.failures = [t for t in self.failures if now - t < self.window]
        else:
            self.failures.append(now)
            if self.state == "half-open" or len(self.failures) >= self.fail_threshold:
                self.state, self.opened_at = "open", now

if __name__ == "__main__":
    cb = CircuitBreaker()
    for i in range(4):                             # 连续失败 3 次触发熔断
        if cb.allow():
            cb.record(False)
            print(f"请求{i}: 调用失败")
        else:
            print(f"请求{i}: 熔断中, 快速失败走降级")
    print("状态:", cb.state)
    time.sleep(2.1)
    print("冷却后半开探测:", cb.allow(), cb.record(True) or cb.state, "已恢复")
