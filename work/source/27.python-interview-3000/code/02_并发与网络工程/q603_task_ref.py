import asyncio
import gc
import weakref

log: list = []


async def background_job() -> None:
    await asyncio.sleep(0.05)
    log.append("job-done")  # 如果 Task 被 GC, 这行永远不会执行


async def main() -> None:
    # 陷阱: 创建后立刻丢弃唯一引用
    weak = weakref.ref(asyncio.create_task(background_job()))
    gc.collect()  # 触发一轮回收, 观察无强引用任务的命运
    alive = weak() is not None
    await asyncio.sleep(0.1)
    print(f"无引用任务: 存活={alive}, 日志={log}")
    print("(能否侥幸跑完取决于 GC 时机与 await 对象的引用链, 不能依赖 —— 这正是文档警告的原因)")

    # 正确姿势: 引用集合 + done callback 自清理
    bg_tasks: set = set()
    for i in range(3):
        t = asyncio.create_task(background_job())
        bg_tasks.add(t)
        t.add_done_callback(bg_tasks.discard)
    await asyncio.sleep(0.1)
    print(f"受保护任务: 完成 {len(log)} 个, 集合剩 {len(bg_tasks)} 个已自动清理")
    assert log.count("job-done") >= 3


asyncio.run(main())
