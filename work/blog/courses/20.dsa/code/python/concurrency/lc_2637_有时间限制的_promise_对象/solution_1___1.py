# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145371693
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import asyncio  # 引入依赖


def timeLimit(fn, t):  # 定义函数 timeLimit（参数：fn, 另一字符串）
    async def limited(*args):  # 定义函数 limited（参数：乘 args）
        try:  # try:
            return await asyncio.wait_for(fn(*args), timeout=t / 1000)
        except asyncio.TimeoutError:  # except asyncio.TimeoutError:
            raise Exception("Time Limit Exceeded")  # raise Exception(「Time Limit Exceeded」)

    return limited  # 返回 limited


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'

    async def slow(t):  # 定义函数 slow（参数：另一字符串）
        await asyncio.sleep(t / 1000)  # await asyncio.sleep(另一字符串 除以 1000)
        return t  # 返回 另一字符串

    limited = timeLimit(slow, 100)  # 把 timeLimit(慢指针, 100) 存入 limited
    try:  # try:
        print(asyncio.run(limited(150)))  # 打印输出
    except Exception as e:  # except Exception as e:
        print(e)  # 打印输出
