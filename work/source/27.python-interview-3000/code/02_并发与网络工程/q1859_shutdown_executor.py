# -*- coding: utf-8 -*-
"""shutdown_default_executor 语义: 默认执行器线程的收尾责任人。

- loop.run_in_executor(None, ...) 惰性创建默认执行器线程, 任务跑完线程还挂着;
- 手动管理 loop 时必须显式 await loop.shutdown_default_executor() 才能收走线程;
- asyncio.run 从 3.9 起在退出前自动调用它, 这是两种跑法的核心差别。
"""
import asyncio
import threading
import time


def blocking_job():
    time.sleep(0.25)
    return threading.current_thread().name      # 默认执行器线程名 asyncio_0


async def use_default_executor():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, blocking_job)


def main():
    baseline = threading.active_count()

    # 场景一: 手动管理 loop, 必须显式 shutdown
    loop = asyncio.new_event_loop()
    try:
        name = loop.run_until_complete(use_default_executor())
        during = threading.active_count()
        loop.run_until_complete(loop.shutdown_default_executor())
        after = threading.active_count()
    finally:
        loop.close()
    print("手动 loop: 执行线程=%s, 执行后活跃线程=%d, shutdown后=%d"
          % (name, during, after))
    assert name.startswith("asyncio_"), "默认执行器线程名以 asyncio_ 开头"
    assert during == baseline + 1, "执行器线程已创建"
    assert after == baseline, "shutdown_default_executor 负责收走线程"

    # 场景二: asyncio.run 自动收尾, 无需手动调用
    def run_and_count():
        asyncio.run(use_default_executor())
        return threading.active_count()

    after_b = run_and_count()
    print("asyncio.run 之后活跃线程: %d (基线 %d)" % (after_b, baseline))
    assert after_b == baseline, "asyncio.run 退出前自动 shutdown 默认执行器"

    print("结论: 默认执行器不会自己消失, 收尾责任在 loop 的主人")


if __name__ == "__main__":
    main()
