---
title: [Q1844] CyclicBarrier 概念与模拟:代数 generation 是复用的钥匙
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1844 · CyclicBarrier 概念与模拟:代数 generation 是复用的钥匙

> 难度:★★★ | 标签:Barrier, 同步, 分阶段并行

**问**:Barrier 和 Latch 都能让一组线程互相等,区别是什么?为什么 Barrier 可以反复用而 Latch 不行?

**答**:关键在 '代 generation':Barrier 每凑齐 parties 个到达者,就把当前代关闭、代数加一、放行全员,下一批人进入新一代;Latch 只有 '到零' 一个终态,没有代的概念。

- 每个等待者记住自己所属的代,被唤醒后发现代变了才通过,这个 '代校验' 让栅栏天然可复用;

- 最后到达者负责执行栅栏动作 barrier action 并翻代,动作完成前谁都不走,演示里动作日志每轮恰好一条;

- 演示三个线程跑两轮,到达序号 0..2 每轮各出现一次,代数从 0 涨到 2。

典型场景是多阶段流水线:每阶段所有 worker 完成后才统一进入下一阶段,比如并行模拟里 '所有体素更新完才交换边界'。

```python
# file: code/02_并发与网络工程/q1844_cyclic_barrier_gen.py
# -*- coding: utf-8 -*-
"""CyclicBarrier 概念与模拟: 用代数 generation 实现可复用栅栏。

- 核心是 "代": 每凑齐 parties 个到达者, 执行一次栅栏动作, 代数加一, 放行全员;
- 等待者记住自己所属的代, 被唤醒后发现代变了才通过, 因此栅栏天然可复用;
- 最后到达者负责跑栅栏动作并翻代, 这与 threading.Barrier 的行为一致。
"""
import threading
import time


class GenerationBarrier:
    def __init__(self, parties, action=None):
        self._parties = parties
        self._action = action
        self._cond = threading.Condition()
        self._arrived = 0
        self._generation = 0
        self.action_log = []

    def wait(self, timeout=5.0):
        """返回到达序号, 全员到齐时最后到达者执行 action 并翻代。"""
        with self._cond:
            g = self._generation
            self._arrived += 1
            idx = self._arrived
            if idx == self._parties:
                self._arrived = 0
                if self._action is not None:
                    self._action(g)
                self._generation = g + 1
                self._cond.notify_all()
                return 0
            deadline = time.monotonic() + timeout
            while self._generation == g:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("barrier 等待超时")
                self._cond.wait(remain)
            return idx


def main():
    rounds_seen = []
    barrier = GenerationBarrier(3, action=lambda g: rounds_seen.append(g))
    finished = []
    finish_lock = threading.Lock()

    def worker(name):
        for r in range(2):                    # 两轮, 验证复用
            idx = barrier.wait()
            with finish_lock:
                finished.append((name, r, idx))

    ts = [threading.Thread(target=worker, args=("w%d" % i,)) for i in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=5.0)
        assert not t.is_alive(), "两轮栅栏都应通过, 不应卡死"

    print("栅栏动作执行记录(每轮一次):", rounds_seen)
    print("线程完成情况:", sorted(finished))
    assert rounds_seen == [0, 1], "栅栏动作每轮恰好执行一次, 代数 0 与 1"
    assert len(finished) == 6, "3 个线程 x 2 轮 = 6 次通过"
    per_round = {}
    for name, r, idx in finished:
        per_round.setdefault(r, []).append(idx)
    for r, idxs in per_round.items():
        assert sorted(idxs) == [0, 1, 2], "每轮到达序号 0..2 恰好各一次"
    print("结论: 代数是栅栏复用的钥匙, 动作由最后到达者代跑")


if __name__ == "__main__":
    main()
```

**追问**:1) 最后到达者跑动作时,其他人在什么状态?——都挂在当前代的条件变量上;动作耗时会长尾拖住全员,所以动作要短,或者把动作交给独立的下一阶段任务。2) 代校验为什么能防「上一代的唤醒误伤下一代」?——等待者唤醒后检查「当前代数是否还等于自己所属代」,不等说明自己等的代已经关闭,直接通过;没有代校验,复用栅栏会把新一批等待者错误放行——「代」就是把一次性 Latch 的正确性扩展到可复用的关键。3) 栅栏动作的耗时约束怎么落地?——动作在最后到达者上下文里跑,全员被它拖住;动作要短(打日志/翻转开关),重的协调工作交给动作里 spawn 的异步任务;或规定动作超时也标记 broken。4) 生产陷阱?——动作抛异常没转 broken(整组永久卡死,见 Q1845);parties 数与实际线程数不符(有人到不了,全员等待);复用栅栏不区分代(混杂两批任务);把重 IO 放进动作(全员长尾)。


---
