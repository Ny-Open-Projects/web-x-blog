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
