---
title: [Q1336] 熔断恢复探测:half-open 的试金石策略
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1336 · 熔断恢复探测:half-open 的试金石策略

> 难度:★★★★ | 标签:熔断器, half-open, 恢复探测

**问**:熔断器打开后,怎么知道依赖"真的恢复了"?恢复探测失败又该怎么退?

**答**:恢复探测是熔断器里最容易做错的部分。冷却时间到点不能直接回到 CLOSED,而要进 HALF_OPEN:只放行少量"试金石"请求去探路,其余请求继续被拒——防止依赖刚恢复又被流量打趴。试金石的判定规则:连续 N 个探测全部成功才回到 CLOSED(单次成功可能是运气);任何一个探测失败,立刻重开熔断,且冷却时间翻倍(指数退到上限),避免对"时好时坏"的依赖反复试探。进 CLOSED 后建议再给一段"观察期"逐步放量,而不是瞬间恢复 100% 流量。下面的演示完整走一遍 OPEN → 冷却 → HALF_OPEN 探测 → 成功闭合,以及探测失败翻倍冷却两条路径。

```python
# file: code/02_并发与网络工程/q1336_breaker_recovery_probe.py
import threading
import time


class CircuitBreaker:
    CLOSED, OPEN, HALF_OPEN = "CLOSED", "OPEN", "HALF_OPEN"

    def __init__(self, fail_threshold: int = 3, cooldown: float = 0.2,
                 probes_needed: int = 2, max_cooldown: float = 1.0) -> None:
        self._lock = threading.Lock()
        self._state = self.CLOSED
        self._fails = 0
        self._open_until = 0.0
        self._cooldown = cooldown
        self._probes_ok = 0
        self._probes_needed = probes_needed
        self._max_cooldown = max_cooldown
        self.log = []

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()
            if self._state == self.CLOSED:
                return True
            if self._state == self.OPEN and now >= self._open_until:
                self._state = self.HALF_OPEN      # 冷却结束: 进探测态
                self._probes_ok = 0
                self.log.append("OPEN -> HALF_OPEN 放行试金石")
                return True
            return False                          # OPEN 冷却期或 HALF_OPEN 探测期

    def record(self, ok: bool) -> None:
        with self._lock:
            if self._state == self.CLOSED:
                if ok:
                    self._fails = 0
                else:
                    self._fails += 1
                    if self._fails >= 3:
                        self._state = self.OPEN
                        self._open_until = time.monotonic() + self._cooldown
                        self.log.append(f"CLOSED -> OPEN 冷却 {self._cooldown:.2f}s")
            elif self._state == self.HALF_OPEN:
                if ok:
                    self._probes_ok += 1
                    if self._probes_ok >= self._probes_needed:
                        self._state = self.CLOSED
                        self._fails = 0
                        self._cooldown = 0.2       # 恢复初始冷却
                        self.log.append("HALF_OPEN -> CLOSED 探测连续成功")
                else:
                    self._cooldown = min(self._cooldown * 2, self._max_cooldown)
                    self._state = self.OPEN
                    self._open_until = time.monotonic() + self._cooldown
                    self.log.append(f"探测失败 -> 重开 OPEN 冷却翻倍为 {self._cooldown:.2f}s")

    @property
    def state(self) -> str:
        return self._state


def main() -> None:
    brk = CircuitBreaker(cooldown=0.2)

    for i in range(3):
        brk.record(False)                  # 依赖连续失败
    print("状态机:", brk.log[-1])
    assert brk.state == "OPEN"
    assert not brk.allow(), "冷却期内请求应被拒"

    time.sleep(0.25)
    assert brk.allow(), "冷却结束应放行试金石"
    brk.record(True)
    assert brk.state == "HALF_OPEN"
    assert not brk.allow(), "探测期内其余请求继续被拒"
    brk.record(True)                       # 第二块试金石成功
    print("状态机轨迹:")
    for line in brk.log:
        print(" ", line)
    assert brk.state == "CLOSED"
    print("恢复探测: 连续试金石成功 -> 闭合, 冷却复位")

    # 探测失败路径: 冷却翻倍
    brk2 = CircuitBreaker(cooldown=0.1, probes_needed=1)
    for _ in range(3):
        brk2.record(False)
    time.sleep(0.15)
    brk2.allow()
    brk2.record(False)                     # 试金石失败
    assert brk2.state == "OPEN"
    print("失败路径:", brk2.log[-1])
    assert "翻倍" in brk2.log[-1]


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么不只放一个探测请求、成功就闭合?——单次成功无法区分"恢复"与"抖动";连续 N 次探测成功配合闭合后的观察期,才能把恢复流量的斜率压平。2) 探测失败的退避为什么翻倍?——时好时坏的依赖(半死状态)最怕规律性探测;翻倍冷却让探测频率指数下降,给依赖真正的喘息;上限封顶防止探测周期变成小时级,恢复检测形同虚设。3) 闭合后的观察期怎么实现?——逐步放量(10%→50%→100%)或按错误率自适应;观察期指标单列,失败立刻回 OPEN;这与灰度分流(Q1340)共享同一思想:恢复也要灰度,瞬间 100% 等于赌依赖已满血。4) 生产陷阱?——HALF_OPEN 期间所有请求照常放行(失去保护意义);单次探测成功就闭合(运气闭合,见原问);探测请求与真实流量走不同代码路径(探测绿了真实流量照样挂);熔断状态机与降级链(Q1342)没有联动,OPEN 期间还在等主服务超时。

---
