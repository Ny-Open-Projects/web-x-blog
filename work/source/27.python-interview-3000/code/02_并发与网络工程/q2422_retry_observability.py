# -*- coding: utf-8 -*-
"""重试的可观测性: 每一次尝试都要留下身位, 事后才对得上账。

- 尝试日志四要素: 第几次、结果、单次耗时、休眠多久, 缺一无法排障;
- 汇总层给两个数: 总尝试次数与总耗时, SLO 报表直接取用;
- 尝试号让服务端日志能按 attempt 分桶, 重复扣款这类事故一查便知。
"""
import time


class AttemptLog:
    def __init__(self):
        self.entries = []

    def record(self, n, outcome, elapsed_s, sleep_s):
        self.entries.append({"n": n, "outcome": outcome,
                             "elapsed_s": round(elapsed_s, 4),
                             "sleep_s": round(sleep_s, 4)})

    def summary(self):
        fails = [e for e in self.entries if e["outcome"] == "fail"]
        return {
            "attempts": len(self.entries),
            "failures": len(fails),
            "total_s": round(sum(e["elapsed_s"] + e["sleep_s"]
                                 for e in self.entries), 4),
        }


def call_once(cost_s, ok):
    t0 = time.monotonic()
    time.sleep(cost_s)
    return "ok" if ok else "fail", time.monotonic() - t0


def retry_with_observability(attempt_costs, attempt_oks, backoff=0.05):
    """attempt_costs/attempt_oks 是剧本, 逐次回放并记账。"""
    log = AttemptLog()
    for n, (cost, ok) in enumerate(zip(attempt_costs, attempt_oks), start=1):
        outcome, elapsed = call_once(cost, ok)
        sleep = 0.0 if ok else backoff * (2 ** (n - 1))
        if not ok:
            time.sleep(sleep)                # 指数退避, 也记进账本
        log.record(n, outcome, elapsed, sleep)
        if ok:
            break
    return log


def main():
    # 场景一: 两次失败后第三次成功
    log = retry_with_observability([0.02, 0.02, 0.02], [False, False, True])
    for e in log.entries:
        print("  尝试 %(n)d: %(outcome)s 单次 %(elapsed_s)ss 休眠 %(sleep_s)ss" % e)
    s = log.summary()
    print("汇总:", s)
    assert s["attempts"] == 3 and s["failures"] == 2
    assert log.entries[1]["sleep_s"] == 0.1, "退避序列应按指数增长"

    # 场景二: 预算耗尽, 全军覆没
    log2 = retry_with_observability([0.01] * 3, [False] * 3, backoff=0.02)
    s2 = log2.summary()
    print("耗尽场景汇总:", s2)
    assert s2["attempts"] == 3 and s2["failures"] == 3, "耗尽也要完整记账"
    assert all(e["outcome"] == "fail" for e in log2.entries)
    print("结论: 重试不可观测, 等于花钱买未知数")


if __name__ == "__main__":
    main()
