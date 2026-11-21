"""热点账户: 流水先行 + 定时聚合入账"""
import itertools
import threading
import time

class HotAccount:
    def __init__(self, balance=1000):
        self.balance = balance
        self.pending = []                       # 待聚合流水
        self.lock = threading.Lock()

    def record(self, delta, memo):
        """记账只写流水: 单线程 append, 无行锁竞争"""
        with self.lock:
            self.pending.append((delta, memo))

    def settle(self):
        """定时聚合: 一次 UPDATE 应用全部流水"""
        with self.lock:
            total = sum(d for d, _ in self.pending)
            n, self.pending = len(self.pending), []
        self.balance += total
        return n, total

if __name__ == "__main__":
    acct = HotAccount()
    for i in range(100):                        # 模拟每秒几千笔中的一段
        acct.record(+1 if i % 3 else -2, f"tx{i}")
    n, total = acct.settle()
    print(f"聚合 {n} 笔, 净变动 {total}, 余额 {acct.balance}")
    print("要点: 明细与余额分离, 余额更新频率与热点解耦")
