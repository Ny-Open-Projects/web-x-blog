# -*- coding: utf-8 -*-
"""悬挂协程的检测钩子: 任务档案 + cr_frame 尸检。

- 任务工厂在创建时登记"出生时刻", 完成回调注销, 得到在途清单;
- 巡检器扫出"年龄超过阈值还没完"的任务, 直接剖开 cr_frame;
- cr_frame 的 f_lineno 就是它卡住的那一行, 尸检报告精确到行号。
"""
import asyncio
import os

BORN = {}                                # task -> 出生时刻
STUCK_LIMIT = 0.3


def factory(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    BORN[task] = loop.time()
    task.add_done_callback(BORN.pop)
    return task


def inspect_stuck(now):
    report = []
    for t, born in BORN.items():
        if t.done():
            continue
        age = now - born
        if age <= STUCK_LIMIT:
            continue
        coro = t.get_coro()
        fr = getattr(coro, "cr_frame", None)
        if fr is not None:
            where = "%s:%d" % (os.path.basename(fr.f_code.co_filename),
                               fr.f_lineno)
        else:
            where = "unknown"
        report.append((t.get_name(), age, where))
    return report


async def suspect():
    await asyncio.sleep(0.6)             # 嫌疑犯: 卡在这一行 0.6 秒
    return "done"


async def healthy():
    await asyncio.sleep(0.05)
    return "ok"


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(factory)

    bad = asyncio.create_task(suspect(), name="suspect")
    good = asyncio.create_task(healthy(), name="healthy")
    await good

    for _ in range(4):                   # 周期巡检
        await asyncio.sleep(0.15)
        for name, age, where in inspect_stuck(loop.time()):
            print("检测到悬挂: %s 已挂 %.2fs, 卡在 %s" % (name, age, where))

    await bad
    print("收尾后登记表大小:", len(BORN), "(完成即注销)")
    print("要点: 心跳看门狗知道'卡了', cr_frame 尸检知道'卡在哪'")


if __name__ == "__main__":
    asyncio.run(main())
