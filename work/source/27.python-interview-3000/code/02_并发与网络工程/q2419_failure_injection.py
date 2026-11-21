# -*- coding: utf-8 -*-
"""失败注入的确定性开关: 同一颗种子同一份剧本, 关掉就风平浪静。

- 注入剧本由种子推导: 第几次调用失败、失败成什么, 跨次运行完全一致;
- 环境开关 CHAOS=off 是总闸, 生产排障时一键还原成干净世界;
- 确定性是回归测试的前提: 修好了就是修好了, 不靠抽签。
"""
import os
import random


class ChaosDisabled(Exception):
    pass


class FailureInjector:
    """按种子生成确定性剧本: attempt 序号 -> 是否失败。"""

    def __init__(self, seed, fail_attempts, total_calls=5, enabled=None):
        if enabled is None:
            enabled = os.environ.get("CHAOS", "on") != "off"
        self.enabled = enabled
        rng = random.Random(seed)
        pool = list(range(1, total_calls + 1))
        rng.shuffle(pool)
        self.plan = set(pool[:fail_attempts])    # 失败的调用序号
        self.schedule = [(i, i in self.plan) for i in range(1, total_calls + 1)]

    def check(self, attempt):
        """返回注入的异常或 None; 总闸关闭时天下太平。"""
        if not self.enabled:
            return None
        if attempt in self.plan:
            return TimeoutError("注入: 第 %d 次调用超时" % attempt)
        return None


def call_with_retry(injector, max_attempts=5):
    attempts = []
    for n in range(1, max_attempts + 1):
        exc = injector.check(n)
        attempts.append((n, exc is None))
        if exc is None:
            return "成功", attempts
        print("  尝试 %d 失败: %s" % (n, exc))
    raise RuntimeError("预算耗尽")


def main():
    # 同一种子, 两次独立运行, 剧本逐位一致
    a = FailureInjector(seed=42, fail_attempts=2).schedule
    b = FailureInjector(seed=42, fail_attempts=2).schedule
    c = FailureInjector(seed=43, fail_attempts=2).schedule
    print("种子 42 剧本 A:", a)
    print("种子 42 剧本 B:", b)
    print("种子 43 剧本 C:", c)
    assert a == b, "同种子必须可复现"
    assert a != c, "不同种子应产生不同剧本"

    # 注入开启: 剧本前两次失败, 第三次成功
    print("CHAOS=on 重放, 剧本:", sorted(FailureInjector(5, 2).plan))
    inj = FailureInjector(seed=5, fail_attempts=2)
    result, log = call_with_retry(inj)
    print("  结局:", result, "尝试记录:", log)
    expected = [not fail for _, fail in inj.schedule[:len(log)]]
    assert result == "成功" and [x[1] for x in log] == expected, \
        "尝试结局必须与剧本逐位一致"
    assert len(log) == 3 and log[-1][1], "两次注入失败后第三次应成功"

    # 总闸关闭: 同一剧本但注入失效
    print("CHAOS=off 重放:")
    result, log = call_with_retry(FailureInjector(seed=42, fail_attempts=2,
                                                  enabled=False))
    print("  结局:", result, "尝试记录:", log)
    assert log == [(1, True)], "总闸一关, 第一次就该直接成功"


if __name__ == "__main__":
    main()
