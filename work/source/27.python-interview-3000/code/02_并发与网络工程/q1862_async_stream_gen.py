# -*- coding: utf-8 -*-
"""异步生成器流式接口: 取多少算多少, break 后 aclose 触发 finally 清理。

- async for 每次只向源头要一条, 消费慢时源头自然停在 yield 处, 天然背压;
- 分块预取的生成器: break 提前退出时, 未取的块永远不会被取回;
- 显式 await agen.aclose() 让 finally 立刻执行, 不依赖 GC 心情。
"""
import asyncio

CLEANED = {"flag": False, "produced": 0}


async def source(total=12, batch=4):
    produced = 0
    try:
        for start in range(0, total, batch):
            await asyncio.sleep(0.03)          # 模拟取块的网络延迟
            chunk = list(range(start, min(start + batch, total)))
            produced += len(chunk)
            for x in chunk:
                yield x
    finally:
        CLEANED["flag"] = True
        CLEANED["produced"] = produced
        print("  生成器 finally 清理: 实际产出 %d 条" % produced)


async def main():
    # 全量消费: 自然耗尽同样触发 finally
    got = []
    async for x in source():
        got.append(x)
    print("全量消费 %d 条" % len(got))
    assert got == list(range(12))
    assert CLEANED["flag"], "耗尽时 finally 也应执行"
    assert CLEANED["produced"] == 12

    # 中途 break: 只预取到第二块, 第三块永远不会被取回
    CLEANED["flag"] = False
    got2 = []
    agen = source()
    async for x in agen:
        got2.append(x)
        if x == 5:
            break
    await agen.aclose()
    print("中途 break 拿到:", got2)
    assert got2 == [0, 1, 2, 3, 4, 5]
    assert CLEANED["flag"], "break 后必须 aclose 触发清理"
    assert CLEANED["produced"] == 8, "只取了两块共 8 条, 后面 4 条从未取回"
    print("结论: 异步生成器是拉模型, break 就是把水龙头关在源头")


if __name__ == "__main__":
    asyncio.run(main())
