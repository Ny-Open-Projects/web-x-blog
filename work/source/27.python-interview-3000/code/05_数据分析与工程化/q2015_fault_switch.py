"""故障注入开关:默认关闭,显式 arm 才生效,带自动过期防遗忘"""

import time


class FaultSwitch:
    def __init__(self, name):
        self.name = name
        self.armed_until = 0.0
        self.triggered = 0

    def arm(self, seconds=60):
        self.armed_until = time.time() + seconds
        print(f"[fault] {self.name} 已激活 {seconds}s")

    def disarm(self):
        self.armed_until = 0.0

    @property
    def active(self):
        return time.time() < self.armed_until

    def check(self, error_factory):
        """调用点模板: 常驻代码路径,未 arm 时零开销直通"""
        if self.active:
            self.triggered += 1
            raise error_factory()
        return False


TIMEOUT_FAULT = FaultSwitch("downstream_timeout")


def call_downstream(latency):
    TIMEOUT_FAULT.check(lambda: TimeoutError(f"注入故障: 下游 {latency}ms 超时"))
    return f"ok({latency}ms)"


if __name__ == "__main__":
    print(call_downstream(20))
    TIMEOUT_FAULT.arm(seconds=1)
    try:
        call_downstream(35)
    except TimeoutError as e:
        print("注入命中并被上游捕获:", e)
    time.sleep(1.1)
    print("过期自动失效:", call_downstream(25))
    TIMEOUT_FAULT.disarm()
    print(f"注入次数 {TIMEOUT_FAULT.triggered}, 开关 active={TIMEOUT_FAULT.active}")
    print("要点:故障点常驻代码但默认关闭;arm 必须显式且自动过期,防止演练开关忘关变成真事故;注入的异常类型与真实故障一致,上游才练得到")
