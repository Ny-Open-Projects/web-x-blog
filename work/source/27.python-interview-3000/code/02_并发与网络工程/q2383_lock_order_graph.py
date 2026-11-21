# -*- coding: utf-8 -*-
"""锁顺序图与死锁预防: 全局定序, 按序加锁。

- 死锁四条件的破坏点选"循环等待": 给所有锁一个全序编号;
- 加锁永远从小号到大号, 两把锁的获取顺序在任何线程里都一致;
- 演示按参数顺序加锁的两个转账互锁, 与按 id 排序的正确版对照。
"""
import threading
import time


class Account:
    def __init__(self, acc_id, balance):
        self.acc_id = acc_id
        self.balance = balance
        self.lock = threading.Lock()


def transfer_naive(src, dst, amount, timeout=0.2):
    """按参数顺序加锁, 调用方传参顺序不同就可能互锁。"""
    if not src.lock.acquire(timeout=timeout):
        return False, "拿不到源账户"
    try:
        time.sleep(0.05)                     # 扩大交叉窗口, 模拟真实记账耗时
        if not dst.lock.acquire(timeout=timeout):
            return False, "拿不到目标账户, 疑似循环等待"
        try:
            src.balance -= amount
            dst.balance += amount
            return True, "ok"
        finally:
            dst.lock.release()
    finally:
        src.lock.release()


def transfer_ordered(src, dst, amount):
    """按 acc_id 全序加锁: 小号在前, 与传参方向无关。"""
    first, second = (src, dst) if src.acc_id < dst.acc_id else (dst, src)
    with first.lock:
        with second.lock:
            if first is src:
                src.balance -= amount
                dst.balance += amount
            else:                # 先拿到的是 dst, 锁的语义不变, 记账方向不变
                src.balance -= amount
                dst.balance += amount
            return True, "ok"


def main():
    a, b = Account(1, 100), Account(2, 100)
    results = {}

    def t_ab():
        results["ab"] = transfer_naive(a, b, 10)     # 先拿 a 再拿 b
    def t_ba():
        results["ba"] = transfer_naive(b, a, 10)     # 先拿 b 再拿 a

    t1, t2 = threading.Thread(target=t_ab), threading.Thread(target=t_ba)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("naive 双向转账:", results["ab"][1], "/", results["ba"][1])
    assert (not results["ab"][0]) or (not results["ba"][0]), \
        "交叉持锁窗口下, naive 版至少一方要撞上循环等待"
    print("  账目守恒 a+b =", a.balance + b.balance, "失败方未动账, 无脏数据")

    for _ in range(5):
        a2, b2 = Account(1, 100), Account(2, 100)
        r = {}

        def t2_ab():
            r["ab"] = transfer_ordered(a2, b2, 10)
        def t2_ba():
            r["ba"] = transfer_ordered(b2, a2, 10)

        ta, tb = threading.Thread(target=t2_ab), threading.Thread(target=t2_ba)
        ta.start(); tb.start()
        ta.join(); tb.join()
        assert r["ab"] == (True, "ok") and r["ba"] == (True, "ok"), "按序加锁必须双双成功"
        assert a2.balance == 100 and b2.balance == 100, "两笔对转账应互相抵消"
    print("ordered 双向转账 x5: 全部成功, 余额守恒")


if __name__ == "__main__":
    main()
