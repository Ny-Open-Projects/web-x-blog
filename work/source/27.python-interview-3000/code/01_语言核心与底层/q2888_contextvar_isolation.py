"""上下文变量的任务隔离:ContextVar 在协程与线程里的传播边界。"""
import asyncio
import threading
from contextvars import ContextVar

request_id = ContextVar("request_id", default="-")


async def handle(tag):
    request_id.set(f"{tag}-req")
    await asyncio.sleep(0.01)
    # await 之后仍看到本任务 set 的值:任务启动时复制了上下文
    return request_id.get()


async def main():
    results = await asyncio.gather(handle("A"), handle("B"), handle("C"))
    print("协程任务各自隔离:", results)
    print("任务外仍是默认值:", request_id.get())


def thread_worker(tag, out):
    out[tag] = request_id.get()          # 线程读自己上下文里的值
    request_id.set(f"{tag}-req")         # 只影响本线程


if __name__ == "__main__":
    asyncio.run(main())

    out = {}
    threads = [threading.Thread(target=thread_worker, args=(t, out)) for t in ("T1", "T2")]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("线程各自读到默认值:", out)
    print("主线程不受影响:", request_id.get())
