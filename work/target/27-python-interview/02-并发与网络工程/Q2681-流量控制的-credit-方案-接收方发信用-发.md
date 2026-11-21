---
title: [Q2681] 流量控制的 credit 方案:接收方发信用,发送方凭票发货
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2681 · 流量控制的 credit 方案:接收方发信用,发送方凭票发货

> 难度:★★★ | 标签:流量控制, credit, 背压

**问**:TCP 已有滑动窗口了,应用层为什么还需要 credit 流量控制?

**答**:TCP 的窗口保护的是内核缓冲区不淹,保护不了应用处理不过来:数据到了内核,应用侧照样堆成山。credit 是应用层方案:接收方每处理一帧归还一单位信用,发送方信用归零就地挂起。实测 30 帧传输,处理慢的接收方让发送方累计被卡 26 次,信用数最终守恒回到初始值——发出多少就归还多少,数不平即泄漏。

- credit 把"我处理完了"变成显式信号,背压一路顶回发送方;

- 与 StreamWriter.drain 的分工:drain 管 socket 缓冲,credit 管业务队列;

- 信用初始值就是允许的最大在途数,按接收方的处理能力定;

- 信用泄漏(归还丢失)会让吞吐缓慢归零,所以守恒对账要进日志。

```python
# file: code/02_并发与网络工程/q2681_credit_flow.py
# -*- coding: utf-8 -*-
"""流量控制的 credit 方案: 接收方发信用, 发送方凭票发货。

- credit 是应用层的流量控制: 收方每处理一帧, 归还一单位信用;
- 信用归零, 发送方就地挂起, 数据不会砸向处理不过来的对端;
- 与 TCP 的滑动窗口互补: TCP 管字节不淹内核, credit 管业务不压垮应用。
"""
import asyncio

INIT_CREDIT = 4
TOTAL = 30
PROCESS_MS = 0.02


async def main():
    credits = {"n": INIT_CREDIT}
    processed = {"n": 0}
    blocked = {"n": 0}
    cond = asyncio.Condition()
    queue = asyncio.Queue()

    async def receiver():
        while True:
            await queue.get()
            await asyncio.sleep(PROCESS_MS)      # 处理一帧的耗时
            processed["n"] += 1
            async with cond:
                credits["n"] += 1                # 归还一单位信用
                cond.notify_all()
            queue.task_done()

    async def sender():
        sent = 0
        while sent < TOTAL:
            async with cond:
                while credits["n"] == 0:
                    blocked["n"] += 1            # 被信用卡住又一遍
                    await cond.wait()            # 挂起等新信用
                credits["n"] -= 1                # 凭一单位信用发货
            await queue.put(sent)
            sent += 1
        return sent

    recv = asyncio.create_task(receiver())
    sent = await sender()
    await queue.join()
    recv.cancel()

    print("发货 %d 帧, 处理 %d 帧, 最终信用 %d(应回到初始 %d)"
          % (sent, processed["n"], credits["n"], INIT_CREDIT))
    print("发送方累计被信用卡住 %d 次(处理越慢, 卡的次数越多)" % blocked["n"])
    print("要点: 信用守恒——发出多少 credit 就归还多少, 数不平即泄漏")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) credit 和滑动窗口是什么关系?——同构:信用数就是窗口大小,归还就是 ACK,credit 是应用层的窗口协议。2) 慢接收方永远不还信用怎么办?——加租约:信用发放带超时,超时未归还按接收方故障处理,回收或断链。3) 底层机制:credit 与 StreamWriter.drain 的分工边界?——drain 只看传输层写缓冲水位,缓冲不淹就放行,应用侧堆积它看不见;credit 把"处理完一帧"变成显式信号顶回发送方,背压穿透到业务源头;两层叠加才完整,只留一层就会在另一层堆死。4) 生产陷阱?——异常路径漏归还,吞吐缓慢归零还不报错(守恒对账要进日志);初始信用按发送方容量而非接收方处理能力定,保护方向反了;把 credit 当 TCP 窗口的替代品,忘了它管的是应用队列。

---
