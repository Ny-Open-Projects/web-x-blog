import asyncio

counter = 0
# asyncio 锁与循环的绑定: 3.10 起原语在首次 await 时惰性绑定运行中的循环,
# import 期创建通常可行; 但在循环 A 用过的锁拿到循环 B(asyncio.run 新开)里
# await 仍会报 "got Future attached to a different loop"。
# 稳妥做法: 在事件循环运行期间创建(本例在 main 里创建)。
lock = None


async def unsafe_increment(n: int) -> None:
    global counter
    for _ in range(n):
        v = counter       # 读
        await asyncio.sleep(0)  # 中断点: 其他协程插入执行
        counter = v + 1   # 写回旧值 → 丢失更新


async def safe_increment(n: int) -> None:
    global counter
    for _ in range(n):
        async with lock:
            v = counter
            await asyncio.sleep(0)  # 即使有中断点, 临界区内没有竞争者
            counter = v + 1


async def atomic_without_await(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1  # 无 await: 事件循环保证原子, 不需要锁


async def run(target, n: int, label: str) -> None:
    global counter
    counter = 0
    await asyncio.gather(*[target(100) for _ in range(n)])
    print(f"{label}: {counter} / 期望 {n * 100}")


async def main() -> None:
    global lock
    lock = asyncio.Lock()  # 在运行中的循环里创建
    await run(unsafe_increment, 10, "含 await 无锁(丢失更新)")
    await run(safe_increment, 10, "含 await 加锁")
    assert counter == 10 * 100, "加锁路径不允许丢失更新"
    await run(atomic_without_await, 10, "无 await 裸写(天然原子)")
    assert counter == 10 * 100, "无 await 路径天然原子"


if __name__ == "__main__":
    asyncio.run(main())
