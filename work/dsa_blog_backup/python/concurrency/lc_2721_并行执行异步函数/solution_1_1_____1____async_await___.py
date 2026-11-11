# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
"""LeetCode 2721. 并行执行异步函数 - 方案1: 使用 async/await 风格（Python asyncio 实现）"""
import asyncio  # 引入依赖


async def promise_all(functions):  # 定义函数 promise_all（参数：functions）
    """并行执行异步函数列表，返回结果列表"""
    tasks = [fn() for fn in functions]  # 把 [fn() for fn in functions] 存入 tasks
    return await asyncio.gather(*tasks)  # 返回 await asyncio.gather( 乘 tasks)


async def demo():  # 定义函数 demo（参数：无）
    """Demo: 验证并行执行"""

    async def delay(seconds, value):  # 定义函数 delay（参数：seconds, value）
        await asyncio.sleep(seconds)  # await asyncio.sleep(seconds)
        return value  # 返回 value

    results = await promise_all(
        [
            lambda: delay(1, 1),
            lambda: delay(1, 2),
            lambda: delay(1, 3),
        ]
    )  # ])
    assert results == [1, 2, 3]  # 断言校验
    print("parallel results:", results)  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    asyncio.run(demo())  # asyncio.run(demo())
