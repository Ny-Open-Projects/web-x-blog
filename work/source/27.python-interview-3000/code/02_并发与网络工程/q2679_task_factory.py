# -*- coding: utf-8 -*-
"""自定义 Task 工厂: set_task_factory 给每个任务挂档案。

- 工厂在 create_task 时被调用: 任务创建的必经之路, 一个不漏;
- 按 task 对象登记, done_callback 注销, 得到实时在途清单;
- 3.9 注意: 自定义工厂会忽略 create_task 的 name 参数, 名字让协程自己报。
"""
import asyncio

REGISTRY = {}


def factory(loop, coro):
    task = asyncio.Task(coro, loop=loop)
    REGISTRY[task] = loop.time()             # 出生登记
    task.add_done_callback(REGISTRY.pop)     # 死亡注销, 按对象键删除
    return task


async def worker(name, dur):
    asyncio.current_task().set_name(name)    # 3.9 下名字得自己挂
    await asyncio.sleep(dur)
    return name


async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(factory)

    t1 = asyncio.create_task(worker("fast", 0.05))
    t2 = asyncio.create_task(worker("slow", 0.3))
    t3 = asyncio.create_task(worker("mid", 0.2))

    await asyncio.sleep(0.1)                 # fast 已完成
    live = sorted(t.get_name() for t in REGISTRY if not t.done())
    print("0.1s 时在途任务:", live)
    print("fast 已完成:", t1.done(), "/ slow 仍在途:", not t2.done())

    await asyncio.gather(t2, t3)
    print("收尾后注册表大小:", len(REGISTRY), "(全部被 done_callback 注销)")
    print("要点: 工厂是任务的可观测性入口, 档案挂上后想怎么巡检都行")


if __name__ == "__main__":
    asyncio.run(main())
