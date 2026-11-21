import asyncio
import threading

order = []


async def main() -> None:
    loop = asyncio.get_running_loop()

    # 三种调度全部注册, 观察消费顺序
    loop.call_soon(lambda: order.append("1.call_soon"))
    loop.call_later(0.05, lambda: order.append("4.call_later_0.05"))
    loop.call_at(loop.time() + 0.05, lambda: order.append("5.call_at_0.05"))
    loop.call_later(0.02, lambda: order.append("3.call_later_0.02"))
    loop.call_soon(lambda: order.append("2.call_soon"))

    # 从其他线程投递: 必须 threadsafe 版本
    def from_thread() -> None:
        loop.call_soon_threadsafe(lambda: order.append("6.threadsafe"))

    t = threading.Thread(target=from_thread)
    t.start()

    await asyncio.sleep(0.2)
    t.join()  # 回收投递线程, 避免悬挂
    for item in order:
        print(item)
    # _ready 是 FIFO: 两个 call_soon 保持注册顺序
    assert order.index("1.call_soon") < order.index("2.call_soon")
    # 定时器堆按到期时间消费: 0.02 先于两个 0.05
    assert order.index("3.call_later_0.02") < order.index("4.call_later_0.05")
    assert order.index("3.call_later_0.02") < order.index("5.call_at_0.05")
    # 同到期时间按入堆序号: 4 注册在 5 之前
    assert order.index("4.call_later_0.05") < order.index("5.call_at_0.05")
    # threadsafe 回调的落点是竞争条件, 不能断言位置, 只要求最终送达
    assert "6.threadsafe" in order
    print("调度层次验证通过")


if __name__ == "__main__":
    asyncio.run(main())
