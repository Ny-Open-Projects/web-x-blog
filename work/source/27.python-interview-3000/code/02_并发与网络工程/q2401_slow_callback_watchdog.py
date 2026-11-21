# -*- coding: utf-8 -*-
"""慢回调看门狗: debug 模式给每个回调计时, 超标就点名。

- 事件循环是单线程的, 一个 200ms 的同步阻塞让所有任务一起卡住;
- loop.set_debug(True) 配 slow_callback_duration, 超时回调在日志里现形;
- 抓到之后对症下药: 阻塞调用丢线程池, 或拆小让出控制权。
"""
import asyncio
import io
import logging
import time


def blocking_callback():
    """罪魁祸首: 在回调里同步睡 200ms, 整个循环陪它停摆。"""
    time.sleep(0.2)


async def victim():
    """受害者视角: 一个 10ms 就能完成的等待被拖长。"""
    t0 = time.monotonic()
    await asyncio.sleep(0.01)
    return time.monotonic() - t0


async def main(capture):
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = 0.05           # 阈值调低到 50ms 便于演示
    loop.call_soon(blocking_callback)            # 塞一个阻塞回调进队列
    cost = await victim()
    await asyncio.sleep(0.05)
    return cost


def main_entry():
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    alog = logging.getLogger("asyncio")
    alog.addHandler(handler)
    alog.setLevel(logging.WARNING)
    cost = asyncio.run(main(stream), debug=True)
    alog.removeHandler(handler)
    text = stream.getvalue()
    flagged = [ln for ln in text.splitlines() if "took" in ln]
    print("受害者等待耗时: %.3fs (本应 0.01s)" % cost)
    for ln in flagged:
        print("看门狗点名:", ln.strip()[:100])
    assert flagged, "debug 模式必须点名慢回调"
    assert cost > 0.1, "阻塞回调期间, 无辜协程的等待被显著拖长"


if __name__ == "__main__":
    main_entry()
