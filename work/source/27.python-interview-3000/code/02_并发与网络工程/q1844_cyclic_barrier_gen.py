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
