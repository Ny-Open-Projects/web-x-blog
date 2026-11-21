import asyncio

opened = []

async def stream():
    conn = f"conn-{id(stream):x}"
    opened.append(conn)
    try:
        for i in range(10):
            await asyncio.sleep(0)
            yield f"{conn}:{i}"
    finally:
        opened.remove(conn)         # 只有 aclose 被驱动才会执行
        print("closed:", conn)

async def main():
    agen = stream()
    async for v in agen:
        if v.endswith("1"):         # 提前 break,生成器悬挂在 yield
            break
    print("still open:", opened)
    await agen.aclose()             # 显式收尾
    print("after aclose:", opened)

asyncio.run(main())                 # run 内部最后调用 loop.shutdown_asyncgens
