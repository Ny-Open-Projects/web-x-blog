import asyncio


async def paginated_fetch(total_pages: int) -> int:
    for page in range(total_pages):
        await asyncio.sleep(0.1)  # 模拟请求一页
        yield page * 100


async def consume() -> None:
    async for item in paginated_fetch(3):
        print("拿到一页数据:", item)


async def main() -> None:
    gen = paginated_fetch(2)
    print("异步生成器对象:", gen)
    await consume()


if __name__ == "__main__":
    asyncio.run(main())
