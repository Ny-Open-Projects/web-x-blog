import asyncio

class AsyncCounter:
    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        self.cur = 0
        return self

    async def __anext__(self):
        if self.cur >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(0)        # 每步之间都可以挂起
        self.cur += 1
        return self.cur

async def async_gen():
    for i in range(3):
        await asyncio.sleep(0)
        yield f"item-{i}"

async def main():
    async for v in AsyncCounter(2):
        print("counter:", v)
    async for v in async_gen():
        print("gen:", v)

if __name__ == "__main__":
    asyncio.run(main())
