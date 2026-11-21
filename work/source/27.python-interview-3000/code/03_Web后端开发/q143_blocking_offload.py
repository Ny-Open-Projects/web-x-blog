import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
try:
    from fastapi import FastAPI
    from fastapi.concurrency import run_in_threadpool
    import httpx   # pip install httpx
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
process_pool = ProcessPoolExecutor(max_workers=2)

def heavy_cpu(n: int) -> int:          # CPU 密集,放进程池
    return sum(i * i for i in range(n))

def blocking_io() -> str:              # 阻塞 IO,放线程池
    time.sleep(1)
    return 'done'

@app.get('/cpu/{n}')
async def cpu_route(n: int):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(process_pool, heavy_cpu, n)
    return {'result': result}

@app.get('/io')
async def io_route():
    # 错误示范: time.sleep(1) 直接写在 async 里会阻塞事件循环
    out = await run_in_threadpool(blocking_io)
    async with httpx.AsyncClient() as client:   # 正确: 异步 HTTP
        await client.get('https://httpbin.org/get')
    return {'out': out}
