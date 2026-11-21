"""Task 收尾纪律: done callback 与异常回收。

Task 的异常不会自己冒出来: 没人 result()/exception(), 循环就通过
exception_handler 报 "Task exception was never retrieved"。
纪律三件事:
- 持引用: 防任务被 GC 静默吞掉;
- done callback: 收尾的统一入口, result() / exception() 都在这里取;
- exception_handler: 兜底哨兵, 专抓漏网的孤儿。
"""
import asyncio
import gc


async def boom():
    raise RuntimeError("后台任务炸了")


async def good():
    await asyncio.sleep(0.02)
    return "result"


async def main():
    loop = asyncio.get_running_loop()
    reported = []
    loop.set_exception_handler(lambda l, ctx: reported.append(ctx))

    # 反面: 创建后不持引用也不取异常 -> 孤儿任务
    # 刻意不绑定返回值: 任务完成后引用归零, __del__ 触发
    # "Task exception was never retrieved" 上报 exception_handler
    asyncio.create_task(boom())

    # 正面: done callback 是收尾统一入口
    captured = []

    def on_done(t):
        if t.cancelled():
            captured.append(("cancelled", None))
            return
        try:
            captured.append(("ok", t.result()))
        except Exception as e:
            captured.append(("error", e))

    t_err = asyncio.create_task(boom())
    t_ok = asyncio.create_task(good())
    t_err.add_done_callback(on_done)
    t_ok.add_done_callback(on_done)

    keepalive = [t_err, t_ok]               # 持引用防 GC
    await asyncio.sleep(0.05)
    gc.collect()                            # 兜底: 确保孤儿任务走到 __del__

    orphans = [ctx["exception"] for ctx in reported if "exception" in ctx]
    print("异常处理器抓到的孤儿:", orphans)
    print("done callback 收尾:", captured)
    assert any(isinstance(e, RuntimeError) for e in orphans), "孤儿异常应上报处理器"
    assert len(captured) == 2, "挂了回调的任务必须各收尾一次"
    assert captured[0][0] == "error" and captured[1][0] == "ok"
    print(keepalive)
    print("结论: done callback 管规范收尾, exception_handler 管兜底哨兵")


if __name__ == "__main__":
    asyncio.run(main())
