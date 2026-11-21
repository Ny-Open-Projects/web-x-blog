import asyncio
import gc
import logging
import time

logging.basicConfig(level=logging.WARNING)

async def blocker():
    time.sleep(0.3)            # 同步阻塞整个事件循环 —— debug 会点名

async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.05    # 阈值默认 0.1s,调低更敏感
    await blocker()            # 警告: Executing <Task ...> took 0.3 seconds

# debug=True 同时开启 慢回调检测 未await协程来源 非线程安全检测
asyncio.run(main(), debug=True)

# 未 await 协程:协程对象销毁时警告,debug 版会附创建 traceback
coro = blocker()
del coro                      # 触发 coroutine was never awaited
gc.collect()
