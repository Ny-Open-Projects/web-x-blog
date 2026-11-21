import asyncio
import time

def sync_fetch(name: str) -> str:
    time.sleep(1)          # 模拟阻塞 IO,占用线程
    return f'{name} done'

async def async_fetch(name: str) -> str:
    await asyncio.sleep(1)  # 模拟非阻塞 IO,让出事件循环
    return f'{name} done'

def run_wsgi_style():
    start = time.time()
    results = [sync_fetch(f'job-{i}') for i in range(3)]  # 串行,约 3s
    print(results, round(time.time() - start, 2))

async def run_asgi_style():
    start = time.time()
    results = await asyncio.gather(*(async_fetch(f'job-{i}') for i in range(3)))
    print(results, round(time.time() - start, 2))  # 并发,约 1s

if __name__ == '__main__':
    run_wsgi_style()
    asyncio.run(run_asgi_style())
