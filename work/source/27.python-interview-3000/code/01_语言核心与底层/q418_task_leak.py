import asyncio
import sys

async def risky(i):
    await asyncio.sleep(0.01)
    if i % 2 == 0:
        raise ValueError(f"boom {i}")
    return i

async def leaky():
    for i in range(4):
        asyncio.create_task(risky(i))      # 返回值丢弃:异常无人取

async def main():
    await leaky()
    await asyncio.sleep(0.05)   # 给泄漏任务跑完并触发 never-retrieved 警告

asyncio.run(main())

# TaskGroup 与 except* 都是 3.11+;except* 是新语法,低版本解释器无法解析,
# 因此这段演示放在字符串里按需编译执行,低于 3.11 时打印说明跳过
if sys.version_info >= (3, 11):
    structured_demo = """
async def structured():
    results = []
    async with asyncio.TaskGroup() as tg:       # 3.11+ 结构化并发
        for i in range(4):
            tg.create_task(risky(i)).add_done_callback(
                lambda t: results.append(f"err: {t.exception()}" if t.exception() else t.result())
            )
    return results

async def main2():
    try:
        await structured()
    except* ValueError as eg:                   # ExceptionGroup 解包
        print("group caught:", [str(x) for x in eg.exceptions])

asyncio.run(main2())
"""
    exec(structured_demo, globals())
else:
    print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
