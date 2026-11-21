# -*- coding: utf-8 -*-
"""重试与幂等键的联合: 键在首发前生成, 全程只此一枚。

- 键的生命周期必须覆盖"一次业务操作的所有尝试", 不是"一次 HTTP 请求";
- 每次重试都重新生成键, 等于把服务端的去重台账当成摆设;
- 客户端生成、首发前落定、重试间复用, 三条纪律缺一不可。
"""
import random
import threading
import uuid


class BankServer:
    """假银行: 以幂等键去重, 同键重复到达返回原流水号。"""

    def __init__(self):
        self.txns = {}
        self.lock = threading.Lock()

    def pay(self, amount, idem_key):
        with self.lock:
            if idem_key in self.txns:
                return self.txns[idem_key], True
            txn_id = "TXN-%d" % (len(self.txns) + 1)
            self.txns[idem_key] = txn_id
            return txn_id, False


class FlakyNetwork:
    """第一次请求在服务端执行后吞掉响应, 客户端只看到超时。"""

    def __init__(self, server):
        self.server = server
        self.calls = 0

    def send(self, request):
        self.calls += 1
        result = self.server.pay(request["amount"], request["key"])
        if self.calls % 2 == 1:              # 每对请求的第一发必丢
            raise TimeoutError("服务端已执行, 但响应丢失")
        return result


def disciplined_retry(server, net, amount):
    """正确姿势: 键在循环外生成, 所有重试共用。"""
    key = "pay-" + str(uuid.uuid4())         # 首发前落定
    for attempt in range(1, 4):
        try:
            return net.send({"amount": amount, "key": key}), key, attempt
        except TimeoutError:
            continue
    raise RuntimeError("重试预算耗尽")


def reckless_retry(server, net, amount):
    """错误姿势: 每次重试都换新键, 服务端无法识别重放。"""
    for attempt in range(1, 4):
        key = "pay-" + str(uuid.uuid4())     # 键随尝试漂移
        try:
            return net.send({"amount": amount, "key": key}), key, attempt
        except TimeoutError:
            continue
    raise RuntimeError("重试预算耗尽")


def main():
    random.seed(7)

    net1 = FlakyNetwork(BankServer())
    server1 = net1.server
    (txn, _), key, attempt = disciplined_retry(server1, net1, 100)
    print("纪律版: 第 %d 次尝试成功, 流水号 %s, 键 %s..." % (attempt, txn, key[:12]))
    print("  服务端账本:", server1.txns)
    assert len(server1.txns) == 1, "共享一枚键, 服务端只应扣一次款"

    net2 = FlakyNetwork(BankServer())
    server2 = net2.server
    (txn2, _), _, _ = reckless_retry(server2, net2, 100)
    print("鲁莽版: 第 2 次尝试成功, 流水号 %s" % txn2)
    print("  服务端账本:", server2.txns)
    assert len(server2.txns) == 2, "每次重试换键, 服务端会扣两次款"
    print("结论: 幂等键是重试的配套件, 一起设计才敢开重试")


if __name__ == "__main__":
    main()
