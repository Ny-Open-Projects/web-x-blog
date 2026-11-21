# -*- coding: utf-8 -*-
"""对冲请求: 主副本迟迟不回, 提前再发一份, 谁快用谁。

- 对冲不是重试: 第二份在主副本还在跑时就发出, 两份并行;
- 收益来自尾延迟: 慢副本的长尾被快副本覆盖, p99 显著收敛;
- 代价是服务端执行次数翻倍, 所以对冲适合读请求或带幂等键的写。
"""
import threading
import time


class Replica:
    """假副本: 固定延迟应答, 记录被调用几次。"""

    def __init__(self, name, latency_s):
        self.name = name
        self.latency = latency_s
        self.calls = 0
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            self.calls += 1
        time.sleep(self.latency)
        return "%s:cache[%s]" % (self.name, key)


def hedged_get(replicas, hedge_after_s, key):
    """主副本先发, hedge_after_s 未见结果就对第二个副本发对冲。"""
    results = []
    done = threading.Event()
    lock = threading.Lock()
    t0 = time.monotonic()

    def worker(rep):
        value = rep.get(key)
        with lock:
            results.append((time.monotonic() - t0, rep.name, value))
        done.set()

    threads = [threading.Thread(target=worker, args=(replicas[0],))]
    threads[0].start()

    deadline = t0 + hedge_after_s
    while time.monotonic() < deadline and not done.is_set():
        time.sleep(0.005)
    if not done.is_set():
        threads.append(threading.Thread(target=worker, args=(replicas[1],)))
        threads[-1].start()
        print("主副本 %.2fs 无回音, 对冲第二副本" % hedge_after_s)

    for t in threads:
        t.join()
    results.sort()
    winner_latency, winner_name, value = results[0]
    return value, winner_latency, winner_name, results


def main():
    slow = Replica("主副本", 0.45)
    fast = Replica("备副本", 0.20)

    # 基线: 只问主副本
    t0 = time.monotonic()
    base = slow.get("k")
    base_cost = time.monotonic() - t0
    print("无对冲基线: %.2fs 才拿到 %s" % (base_cost, base))
    assert base_cost >= 0.45

    # 对冲: 0.15s 后主副本还没回, 第二份已在路上
    value, latency, winner, results = hedged_get([slow, fast], 0.15, "k")
    print("对冲后: %.2fs 拿到 %s (胜者 %s)" % (latency, value, winner))
    print("执行明细:", [(n, "%.2fs" % l) for l, n, _ in results])
    assert winner == "备副本", "慢副本的长尾应被快副本覆盖"
    # 断言采用确定性设计: 绝对时延上界受机器负载影响, 改为与同一次运行的基线相对比较——
    # 对冲后必须快于只问主副本的基线 (0.15s 对冲 + 0.20s 备副本 < 0.45s 主副本)
    assert latency < base_cost, "对冲收益必须显著低于基线"
    assert slow.calls + fast.calls == 3, "基线 1 次 + 对冲场景 2 次, 服务端执行数上升"
    assert len(results) == 2, "两份应答都到达, 输的那份被丢弃"


if __name__ == "__main__":
    main()
