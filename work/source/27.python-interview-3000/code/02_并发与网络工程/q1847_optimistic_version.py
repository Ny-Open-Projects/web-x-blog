# -*- coding: utf-8 -*-
"""CAS 循环乐观锁: 版本号提交保证复合状态的一致性。

- 复合状态(两个账户余额)的读改写跨多个字段, 单项原子性救不了;
- 每次修改基于快照准备变更, 提交时校验版本号, 版本变了说明有人抢先, 重试;
- 对照组: 无版本校验的 "读了就写" 在高频交错下会丢失更新, 总额漂移。
"""
import sys
import threading
import random

sys.setswitchinterval(1e-6)

ROUNDS = 600
THREADS = 4


class VersionedState:
    def __init__(self, init):
        self._lock = threading.Lock()
        self._state = dict(init)
        self._ver = 0
        self.commits = 0
        self.retries = 0

    def snapshot(self):
        with self._lock:
            return self._ver, dict(self._state)

    def commit(self, expected_ver, mutator):
        with self._lock:
            if self._ver != expected_ver:
                self.retries += 1
                return False                # 版本已变, 有人抢先, 拒绝提交
            mutator(self._state)
            self._ver += 1
            self.commits += 1
            return True


def transfer_worker(state, naive_state, seed):
    rng = random.Random(seed)
    for _ in range(ROUNDS):
        # 乐观版: 基于快照准备变更, 版本不符就重试
        while True:
            ver, snap = state.snapshot()
            direction = rng.random() < 0.5

            def mut(st, direction=direction):
                if direction:
                    st["a"] -= 1
                    st["b"] += 1
                else:
                    st["a"] += 1
                    st["b"] -= 1

            if state.commit(ver, mut):
                break
        # 朴素版: 读了就写, 不校验版本
        ver2, snap2 = naive_state.snapshot()
        direction = rng.random() < 0.5

        def mut2(st, direction=direction):
            if direction:
                st["a"] -= 1
                st["b"] += 1
            else:
                st["a"] += 1
                st["b"] -= 1

        mut2(naive_state._state)            # 裸写, 无提交校验


def main():
    state = VersionedState({"a": 100, "b": 100})
    naive_state = VersionedState({"a": 100, "b": 100})
    ts = [threading.Thread(target=transfer_worker, args=(state, naive_state, i))
          for i in range(THREADS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

    ver, snap = state.snapshot()
    nver, nsnap = naive_state.snapshot()
    print("乐观版: 版本=%d 提交=%d 冲突重试=%d 状态=%s 总额=%d"
          % (ver, state.commits, state.retries, snap, snap["a"] + snap["b"]))
    print("朴素版: 状态=%s 总额=%d (应保持 200)" % (nsnap, nsnap["a"] + nsnap["b"]))
    assert snap["a"] + snap["b"] == 200, "乐观版总额必须守恒"
    assert state.retries > 0, "高频交错下必然发生版本冲突重试"
    print("结论: 版本号是复合状态的 CAS, 提交那一刻见真章")


if __name__ == "__main__":
    main()
