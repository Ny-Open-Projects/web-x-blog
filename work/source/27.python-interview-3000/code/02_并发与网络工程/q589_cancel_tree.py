import asyncio
import sys


async def leaf(name: str, delay: float) -> str:
    try:
        await asyncio.sleep(delay)
        print(f"{name} 正常完成")
        return name
    except asyncio.CancelledError:
        print(f"{name} 被取消, 执行清理")
        await asyncio.sleep(0)  # 清理中也要给循环让位
        raise                    # 必须重新抛出


async def middle_branch_compat() -> None:
    """3.11 以下等价: gather 宿主被取消时会连带取消所有子任务。"""
    leaves = [
        asyncio.create_task(leaf("leaf-1", 0.05)),
        asyncio.create_task(leaf("leaf-2", 5.0)),   # 长任务: 会被连带取消
        asyncio.create_task(leaf("leaf-3", 5.0)),
    ]
    await asyncio.gather(*leaves)


# TaskGroup/except* 是 3.11+ 语法级特性, 放字符串按需编译
CANCEL_TREE_DEMO_311 = '''
async def middle_branch() -> None:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(leaf("leaf-1", 0.05))
        tg.create_task(leaf("leaf-2", 5.0))   # 长任务: 会被连带取消
        tg.create_task(leaf("leaf-3", 5.0))


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as outer:
            outer.create_task(middle_branch())
            outer.create_task(asyncio.sleep(10, result="root-slow"))
            await asyncio.sleep(0.1)
            raise RuntimeError("根任务主动失败, 触发整树取消")
    except* RuntimeError as eg:
        print("捕获根因:", eg.exceptions[0])
    except* asyncio.CancelledError:
        print("不应出现: 根任务自己不会收到取消")
    print("main 结束: 所有嵌套任务已退出")
'''


async def main_compat() -> None:
    # 3.9 等价演示: 手动逐层 cancel, 观察"向下一整层"的传播
    root = asyncio.create_task(middle_branch_compat())
    slow = asyncio.create_task(asyncio.sleep(10, result="root-slow"))
    await asyncio.sleep(0.05)
    print("根任务失败(以 cancel 模拟), 触发整树取消")
    root.cancel()
    slow.cancel()
    for name, t in (("middle_branch", root), ("root-slow", slow)):
        try:
            await t
        except asyncio.CancelledError:
            print(f"{name} 子树已随取消退出")
    print("main 结束: 所有嵌套任务已退出")


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        exec(compile(CANCEL_TREE_DEMO_311, "<cancel_tree_311>", "exec"), globals())
        asyncio.run(main())  # noqa: F821  由 CANCEL_TREE_DEMO_311 动态定义
    else:
        print(
            f"TaskGroup/except* 需要 Python 3.11+, "
            f"当前 {sys.version_info.major}.{sys.version_info.minor}, "
            f"演示跳过, 改用 gather+cancel 等价演示"
        )
        asyncio.run(main_compat())
