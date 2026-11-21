# -*- coding: utf-8 -*-
"""线程安全的通用对象池: Condition 实现 borrow/give_back 的完整语义。

- 池空且未达上限时现场创建; 已达上限则等待归还, 带超时快速失败;
- 借出集合登记 id 防止重复归还或归还外来对象, 这是池不变量的关键;
- high_water 记录同时在用的峰值, 用来回答 "池开多大才够"。
"""
import threading
import time


class ObjectPool:
    def __init__(self, factory, size):
        self._factory = factory
        self._size = size
        self._cond = threading.Condition()
        self._idle = []
        self._created = 0
        self._in_use = 0
        self._borrowed_ids = set()
        self.high_water = 0

    def borrow(self, timeout=2.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while True:
                if self._idle:
                    obj = self._idle.pop()
                    break
                if self._created < self._size:
                    self._created += 1
                    obj = self._factory()
                    break
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("对象池已耗尽且等待超时")
                self._cond.wait(remain)
            oid = id(obj)
            self._borrowed_ids.add(oid)
            self._in_use += 1
            self.high_water = max(self.high_water, self._in_use)
            return obj

    def give_back(self, obj):
        with self._cond:
            oid = id(obj)
            if oid not in self._borrowed_ids:
                raise ValueError("重复归还或归还了非本池对象")
            self._borrowed_ids.discard(oid)
            self._idle.append(obj)
            self._in_use -= 1
            self._cond.notify()

    @property
    def created(self):
        with self._cond:
            return self._created


def main():
    counter = {"n": 0}

    def factory():
        counter["n"] += 1
        return {"conn": "conn-%d" % counter["n"]}

    pool = ObjectPool(factory, size=2)
    results = []
    res_lock = threading.Lock()

    def borrower():
        for _ in range(2):
            obj = pool.borrow(timeout=2.0)
            time.sleep(0.03)                  # 模拟使用
            pool.give_back(obj)
        with res_lock:
            results.append(True)

    ts = [threading.Thread(target=borrower) for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(timeout=5.0)
        assert not t.is_alive(), "借还循环不应卡死"

    print("工厂调用次数:", pool.created, "并发峰值 high_water:", pool.high_water)
    assert len(results) == 4, "全部借还完成"
    assert pool.created <= 2, "池上限是 2, 工厂不应超造"
    assert pool.high_water <= 2, "同时在用不得超过池上限"
    assert pool.created == 2, "4 个借还者复用 2 个对象即可"

    # 不变量: 重复归还必须被拒绝
    obj = pool.borrow(timeout=1.0)
    pool.give_back(obj)
    try:
        pool.give_back(obj)
        raise AssertionError("重复归还应被拒绝")
    except ValueError as e:
        print("重复归还被拒绝:", e)
    print("结论: 借出集合登记 id, 让池的状态机无懈可击")


if __name__ == "__main__":
    main()
