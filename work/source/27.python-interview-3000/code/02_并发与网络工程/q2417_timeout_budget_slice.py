# -*- coding: utf-8 -*-
"""超时预算的传递与分片: 一笔预算切给各步, 再留一块给兜底。

- 总预算先分片: 连接、调用各拿固定比例, 再切一块预留给人机兜底;
- 每步的实际超时 = min(自己的片, 剩余 - 预留), 谁也不许吃掉别人的份额;
- 步骤超了自己片内就立即止损, 预算永远够最后一步把降级答案端出来。
"""
import time


class BudgetExceeded(Exception):
    pass


class Budget:
    """一笔带预留的总预算, 步骤凭片内额度开工。"""

    def __init__(self, total_s, reserve_ratio=0.25):
        self.t0 = time.monotonic()
        self.total = total_s
        self.reserve = total_s * reserve_ratio
        self.used = 0.0

    def slice_for(self, own_s):
        """本步可用 = min(声明额度, 剩余 - 预留)。"""
        remaining = self.total - (time.monotonic() - self.t0) - self.reserve
        return max(0.0, min(own_s, remaining))

    def run(self, name, work_s, quota_s, fn):
        allowed = self.slice_for(quota_s)
        t0 = time.monotonic()
        try:
            result = fn(allowed)
        finally:
            cost = time.monotonic() - t0
        self.used += cost
        print("%-6s 片内额度 %.2fs, 实际 %.2fs" % (name, allowed, cost))
        return result


def main():
    def connect(timeout):
        time.sleep(0.1)                      # 连接 0.1s, 顺利完成
        return "conn"

    def guarded_call(allowed):
        """对端需要 0.5s; 真实世界由 socket 超时在片内打断它。"""
        t0 = time.monotonic()
        time.sleep(min(0.5, allowed))
        if 0.5 > allowed:
            raise BudgetExceeded(
                "对端要 0.5s, 片内只有 %.2fs, 止损" % allowed)
        return "never"

    def fallback(timeout):
        time.sleep(0.05)                     # 兜底: 读本地缓存快照
        return "cached-snapshot"

    budget = Budget(total_s=0.6, reserve_ratio=0.3)
    conn = budget.run("连接", 0.1, 0.3, connect)
    assert conn == "conn"

    try:
        budget.run("调用", 0.2, 0.2, guarded_call)
        raise AssertionError("卡死的调用必须在片内被打断")
    except BudgetExceeded as e:
        print("调用   撞上片内止损:", e)

    answer = budget.run("兜底", 0.05, 0.1, fallback)
    spent = time.monotonic() - budget.t0
    print("最终答案:", answer, "| 总耗时 %.2fs / 预算 0.60s" % spent)
    assert answer == "cached-snapshot", "兜底步骤必须在预算内完成"
    assert spent < 0.75, "整条链路必须在预算附近收敛"


if __name__ == "__main__":
    main()
