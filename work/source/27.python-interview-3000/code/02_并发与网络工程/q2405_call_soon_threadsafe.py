# -*- coding: utf-8 -*-
"""跨线程唤醒事件循环: call_soon_threadsafe 是唯一的正门。

- Future/回调都绑定在事件循环线程上, 别的线程直接 set_result 是数据竞争;
- debug 模式下这种越界会被 RuntimeError 当场抓获, 非调试则可能静默出错;
- call_soon_threadsafe 先把回调排进循环的线程安全队列, 再敲醒 selectors。
"""
import asyncio
import threading
import time


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    fut_bad = loop.create_future()          # 只用来演示错误姿势, 不去等它
    fut_bad.add_done_callback(lambda f: None)   # 有等待者, 才会让越界写现形
    errors = []

    def worker():
        time.sleep(0.1)
        # 错误姿势: 直接在别的线程 set_result
        try:
            fut_bad.set_result(1)
        except RuntimeError as e:
            errors.append(type(e).__name__)
        # 正确姿势: 线程安全投递, 顺带敲醒正在 await 的循环
        def deliver():
            if not fut.done():
                fut.set_result(42)
        loop.call_soon_threadsafe(deliver)

    t = threading.Thread(target=worker)
    t.start()
    result = await fut                       # 循环线程在此挂起, 等 cross-thread 唤醒
    t.join()
    await asyncio.sleep(0)                   # 让异常点名的日志先落地
    print("await 拿到跨线程结果:", result)
    print("越界 set_result 被抓获:", errors)
    assert result == 42, "call_soon_threadsafe 必须把结果送达"
    assert errors == ["RuntimeError"], "debug 模式必须能抓住越界写"


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
