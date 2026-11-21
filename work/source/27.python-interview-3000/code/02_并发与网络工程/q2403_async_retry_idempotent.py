# -*- coding: utf-8 -*-
"""异步重试的幂等边界: 失败的请求可能已经生效, 盲目重试就是双倍扣款。

- 最危险的失败形态是"已执行但响应丢失", 客户端看到错误, 服务端已扣款;
- 天然幂等的操作(查询类)可以放心重试; 非幂等操作必须带幂等键;
- 幂等键让服务端把第二次到达识别成重放, 返回第一次的结果而不是再执行。
"""
import asyncio


class TransientError(Exception):
    pass


class PaymentService:
    """假支付服务: 每次真实扣款都记账; 带键且键已见过的请求只回放。"""

    def __init__(self):
        self.ledger = {}
        self.replays = 0

    async def charge(self, amount, idem_key=None):
        if idem_key is not None and idem_key in self.ledger:
            self.replays += 1
            return "replay-%s" % idem_key
        self.ledger[idem_key or "anon-%d" % len(self.ledger)] = amount
        await asyncio.sleep(0.01)
        raise TransientError("已扣款, 但响应在网络中丢失")   # 教科书式故障


async def retry_call(op, *args, attempts=2, **kwargs):
    last = None
    for n in range(1, attempts + 1):
        try:
            return await op(*args, **kwargs), n
        except TransientError as e:
            last = e
            await asyncio.sleep(0.01)
    raise last


async def main():
    svc = PaymentService()

    # 场景一: 查询类天然幂等, 重试无害
    reads = []

    async def query():
        reads.append(1)
        if len(reads) == 1:
            raise TransientError("瞬断")
        return "data"

    _, n = await retry_call(query)
    print("查询重试 %d 次成功, 无副作用问题" % n)

    # 场景二: 非幂等又没带键, 盲目重试 = 双倍扣款
    try:
        await retry_call(svc.charge, 100)
    except TransientError:
        pass
    print("不带幂等键: 实际扣款 %d 次, 账上 %s" %
          (len([k for k in svc.ledger if k.startswith("anon")]),
           [v for k, v in svc.ledger.items() if k.startswith("anon")]))

    # 场景三: 带幂等键, 第二次到达被识别为重放
    res, n = await retry_call(svc.charge, 100, idem_key="order-42")
    print("带幂等键: 尝试 %d 次, 最终结果 %s, 服务端回放 %d 次" %
          (n, res, svc.replays))

    anon = len([k for k in svc.ledger if k.startswith("anon")])
    assert anon == 2, "无键重试必然重复扣款"
    assert len([k for k in svc.ledger if not k.startswith("anon")]) == 1, \
        "带键重试只应扣一次"
    assert res.startswith("replay") and n == 2, "客户端拿到的是回放结果"


if __name__ == "__main__":
    asyncio.run(main())
