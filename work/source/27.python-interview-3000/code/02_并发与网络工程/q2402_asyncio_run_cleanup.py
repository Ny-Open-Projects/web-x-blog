# -*- coding: utf-8 -*-
"""asyncio.run 的收尾纪律: 你忘了 await 的任务, 它替你取消。

- main 返回时还有没跑完的任务, asyncio.run 不静默丢弃;
- 它逐个 cancel, gather(return_exceptions=True) 等取消落实, 再关循环;
- 任务里的 finally 有机会执行, 这是收尾资源能释放的关键约定。
"""
import asyncio

events = []


async def orphan_worker():
    """被遗忘的后台任务: 睡 5 秒, 但 finally 必须有机会说话。"""
    try:
        events.append("worker 开跑")
        await asyncio.sleep(5.0)
        events.append("worker 自然完成")          # 永远到不了
    except asyncio.CancelledError:
        events.append("worker 被取消")
        raise
    finally:
        events.append("worker finally 清理")


async def main():
    task = asyncio.create_task(orphan_worker())
    events.append("main 故意不等它, 直接返回")
    await asyncio.sleep(0.05)
    assert not task.done()
    return "main-done"


def main_entry():
    result = asyncio.run(main())
    print("asyncio.run 返回:", result)
    for e in events:
        print("  事件:", e)
    assert "worker 被取消" in events, "遗留任务必须被 run 的收尾取消"
    assert "worker finally 清理" in events, "finally 必须被执行"
    assert "worker 自然完成" not in events, "取消的任务不应走到自然完成"
    print("结论: run 的收尾 = cancel 遗留任务 + 等落实 + 关循环")


if __name__ == "__main__":
    main_entry()
