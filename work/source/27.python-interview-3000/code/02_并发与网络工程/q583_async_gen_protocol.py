import asyncio


async def numbers(n: int):
    for i in range(n):
        await asyncio.sleep(0.01)  # 异步生成器: 产出前可能做 IO
        yield i


async def manual_drive() -> None:
    gen = numbers(3)
    print("手动 asend:", await gen.asend(None))  # 启动
    print("手动 asend:", await gen.asend(None))
    try:
        await gen.asend(None)
        await gen.asend(None)
    except StopAsyncIteration:
        print("耗尽: StopAsyncIteration")

    gen2 = numbers(10)
    await gen2.asend(None)
    try:
        await gen2.athrow(ValueError("提前中止"))
    except ValueError as e:
        print("athrow 注入并透出:", e)
    await gen2.aclose()  # 触发 GeneratorExit 执行清理


async def for_loop() -> None:
    async for i in numbers(3):  # 语法糖: 循环调用 __anext__
        print("async for:", i)


async def main() -> None:
    await manual_drive()
    await for_loop()


asyncio.run(main())
