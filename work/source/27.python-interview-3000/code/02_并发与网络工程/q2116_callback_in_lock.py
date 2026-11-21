# -*- coding: utf-8 -*-
"""锁内调用回调的重入风险: 回调再拿同一把锁就自锁。

- Lock 不可重入: 持锁者调用外部回调, 回调回头再拿这把锁, 必然自锁;
- 危险在于锁的边界长在库代码里, 回调是调用方注入的, 库无法预知;
- 修复模式: 先在锁内拷贝快照, 出锁后再调用回调。
"""
import threading
import time


class Inventory:
    def __init__(self):
        self._lock = threading.Lock()
        self._items = {}

    def set(self, sku, qty):
        with self._lock:
            self._items[sku] = qty

    def get(self, sku, timeout=1.0):
        # timeout 参数是给实验用的: 真实场景往往就是无限等, 直接死锁
        if not self._lock.acquire(timeout=timeout):
            raise RuntimeError("get 等锁超时: 锁被别处长期持有")
        try:
            return self._items.get(sku)
        finally:
            self._lock.release()

    def change_with_callback(self, sku, delta, on_change):
        with self._lock:                      # 持锁状态
            self._items[sku] = self._items.get(sku, 0) + delta
            on_change(sku, self._items[sku])  # 危险: 回调在锁内执行

    def change_snapshot_callback(self, sku, delta, on_change):
        with self._lock:
            self._items[sku] = self._items.get(sku, 0) + delta
            snapshot = dict(self._items)      # 锁内只做拷贝
        on_change(sku, snapshot)              # 出锁后再调用


def audit_callback(sku, value):
    # 审计方想知道当前全量库存: 回头调 get -> 与外层同一把锁 -> 重入
    inv.get(sku, timeout=1.0)


def main():
    global inv
    inv = Inventory()
    inv.set("apple", 10)

    try:
        inv.change_with_callback("apple", 5, audit_callback)
        print("意外: 锁内回调竟然成功了")
    except RuntimeError as e:
        print("重入死锁被超时拦截:", e)

    inv.change_snapshot_callback("apple", 5,
                                 lambda sku, snap: print(
                                     "快照回调拿到:", sku, snap["apple"]))
    print("修复后当前库存:", inv.get("apple", timeout=1.0))


if __name__ == "__main__":
    main()
