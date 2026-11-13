# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
"""LeetCode 2721. 并行执行异步函数 - 方案2: 使用 then/catch 风格（Python 中用 await + try/except 模拟）"""
import asyncio  # 引入依赖


async def promise_all(functions):  # 定义函数 promise_all（参数：functions）
    """并行执行异步函数列表，带错误捕获（模拟 then/catch 链）"""
    results = []  # 把 [] 存入 results

    async def run_and_catch(fn):  # 定义函数 run_and_catch（参数：fn）
        try:  # try:
            result = await fn()  # then: 等待结果
            return {"ok": True, "value": result}  # 返回 {「ok」: True, 「ok」: 结果}
        except Exception as e:  # catch: 捕获异常
            return {"ok": False, "error": e}  # 返回 {「ok」: False, 「ok」: e}

    tasks = [run_and_catch(fn) for fn in functions]  # 把 [run_and_catch(fn) for fn in functions] 存入 tasks
    for t in await asyncio.gather(*tasks):  # 逐个取出 await 的元素（另一字符串）
        results.append(t)  # 把 另一字符串 追加到列表尾部
    return results  # 返回 results


async def demo():  # 定义函数 demo（参数：无）
    """Demo: 验证并行执行与错误捕获"""

    async def success(value):  # 定义函数 success（参数：value）
        await asyncio.sleep(0.1)  # await asyncio.sleep(0.1)
        return value  # 返回 value

    async def fail():  # 定义函数 fail（参数：无）
        await asyncio.sleep(0.1)  # await asyncio.sleep(0.1)
        raise ValueError("boom")  # raise ValueError(「boom」)

    results = await promise_all([lambda: success(1), lambda: fail(), lambda: success(3)])
    assert results[0]["ok"] and results[0]["value"] == 1  # 断言校验
    assert not results[1]["ok"]  # 断言校验
    assert results[2]["ok"] and results[2]["value"] == 3  # 断言校验
    print("results:", [(r["ok"], r.get("value")) for r in results])  # 打印输出


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    asyncio.run(demo())  # asyncio.run(demo())
