---
title: [Q581] call_soon / call_at / call_later 的调度层次
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q581 · call_soon / call_at / call_later 的调度层次

> 难度:★★★☆ | 标签:asyncio, 事件循环, 调度

**问**:call_soon、call_later、call_at、call_soon_threadsafe 之间是什么关系?事件循环每轮怎么消费它们?

**答**:call_soon 把回调放进 `_ready` 双端队列,下一轮迭代立即执行,是最快的;call_later 是 call_at 的语法糖(绝对时间 = now + delay),进 `_scheduled` 最小堆;每轮循环开始时把堆里已到期的搬到 _ready 尾部。执行顺序因此是:先清 _ready(含上一轮搬进来的),再 select 阻塞一小段,再处理到期定时器。`call_soon_threadsafe` 是唯一能从其他线程调用的版本,因为它在入队后会向自管道写一个字节唤醒可能正在 select 里睡眠的事件循环。写断言时注意:线程投递回调的落点是竞争条件,断言"第 N 个位置是谁"必然偶发失败,只能对确定性维度(_ready FIFO、到期时间顺序、同到期入堆顺序)做相对顺序断言。

```python
# file: code/02_并发与网络工程/q581_call_soon_layers.py
import asyncio
import threading

order = []


async def main() -> None:
    loop = asyncio.get_running_loop()

    # 三种调度全部注册, 观察消费顺序
    loop.call_soon(lambda: order.append("1.call_soon"))
    loop.call_later(0.05, lambda: order.append("4.call_later_0.05"))
    loop.call_at(loop.time() + 0.05, lambda: order.append("5.call_at_0.05"))
    loop.call_later(0.02, lambda: order.append("3.call_later_0.02"))
    loop.call_soon(lambda: order.append("2.call_soon"))

    # 从其他线程投递: 必须 threadsafe 版本
    def from_thread() -> None:
        loop.call_soon_threadsafe(lambda: order.append("6.threadsafe"))

    t = threading.Thread(target=from_thread)
    t.start()

    await asyncio.sleep(0.2)
    t.join()  # 回收投递线程, 避免悬挂
    for item in order:
        print(item)
    # _ready 是 FIFO: 两个 call_soon 保持注册顺序
    assert order.index("1.call_soon") < order.index("2.call_soon")
    # 定时器堆按到期时间消费: 0.02 先于两个 0.05
    assert order.index("3.call_later_0.02") < order.index("4.call_later_0.05")
    assert order.index("3.call_later_0.02") < order.index("5.call_at_0.05")
    # 同到期时间按入堆序号: 4 注册在 5 之前
    assert order.index("4.call_later_0.05") < order.index("5.call_at_0.05")
    # threadsafe 回调的落点是竞争条件, 不能断言位置, 只要求最终送达
    assert "6.threadsafe" in order
    print("调度层次验证通过")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 在普通线程里直接调 loop.call_soon 会怎样?——不保证唤醒正在 select 的循环,回调可能延迟到下次循环被别的事件唤醒才执行,甚至一直睡着;必须用 call_soon_threadsafe。2) 调度三层的层次?——call_soon:就绪队列立即(下一迭代);call_later/call_at:定时器堆;call_soon_threadsafe:跨线程安全(写自管道唤醒 select,Q600);回调执行顺序分层保证。3) 与 Future.set_result 的关系?——跨线程 set_result 内部就是 call_soon_threadsafe;同线程内是 call_soon(Q578)。4) 生产陷阱?——工作线程直接 call_soon「偶尔生效」的隐性 bug;跨线程改循环状态无防护;回调内抛异常无人接收(Q1561)。

---
