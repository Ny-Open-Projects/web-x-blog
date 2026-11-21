# -*- coding: utf-8 -*-
"""await 竞态与让步点: 醒来顺序的确定性。

- async def 调用只创建协程, 首个 send/await 才执行到第一个让步点;
- 同一截止时刻到期的回调按注册顺序执行, 先挂起者先醒;
- 让步点是顺序的钥匙: 没有 await 的同步段不会被打断。
"""
import asyncio


async def racer(tag, out, delay):
    await asyncio.sleep(delay)     # 让步点: 控制权回到事件循环
    out.append(tag)


async def sync_head(tag, out):
    x = sum(i * i for i in range(1000))   # 首个 await 之前的同步段
    out.append((tag, x))
    await asyncio.sleep(0)                # 第一个让步点在这里


async def main():
    out = []
    await asyncio.gather(
        racer("A", out, 0.05),
        racer("B", out, 0.05),
        racer("C", out, 0.05),
    )
    print("相同延迟的醒来顺序:", out, "-> 先挂起者先醒, FIFO")

    out2 = []
    c = sync_head("X", out2)
    c.send(None)                  # 手动驱动: 跑到第一个让步点
    print("首个让步点前:", out2, "-> 同步段一次跑完, 不可被打断")
    try:
        c.send(None)              # 从 sleep(0) 之后续跑
    except StopIteration:
        pass
    print("续跑完成:", out2)

    out3 = []
    await asyncio.gather(
        sync_head("P", out3),
        sync_head("Q", out3),
    )
    print("gather 首段顺序:", [x[0] for x in out3], "-> 创建顺序即首段顺序")
    print("结论: 竞态结果的顺序由让步点安排, 而不是由概率决定")


if __name__ == "__main__":
    asyncio.run(main())
