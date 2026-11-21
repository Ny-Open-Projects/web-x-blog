import asyncio
import os
import signal
import threading

active: set = set()


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    task = asyncio.current_task()
    active.add(task)
    try:
        data = await asyncio.wait_for(reader.readline(), timeout=5)
        await asyncio.sleep(0.3)  # 模拟业务处理
        writer.write(b"processed:" + data)
        await writer.drain()
    except asyncio.CancelledError:
        writer.write(b"server-closing\n")  # 尽力通知
        try:
            await asyncio.wait_for(writer.drain(), 0.1)
        except (asyncio.TimeoutError, ConnectionError):
            pass
        raise
    finally:
        active.discard(task)
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def main() -> None:
    loop = asyncio.get_running_loop()
    stop: asyncio.Future = loop.create_future()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, stop.set_result, sig.name)

    # 模拟运维在 0.8s 后发 SIGTERM
    threading.Timer(0.8, lambda: os.kill(os.getpid(), signal.SIGTERM)).start()

    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    print(f"[1] 服务启动 port={port}")

    async def client() -> None:
        r, w = await asyncio.open_connection("127.0.0.1", port)
        w.write(b"hello\n")
        await w.drain()
        print("client 收到:", (await r.readline()).decode().strip())
        w.close()
        await w.wait_closed()

    client_task = asyncio.create_task(client())

    sig = await stop
    print(f"[2] 收到 {sig}: 停止接受新连接")
    server.close()
    await server.wait_closed()

    print("[3] 排空在途任务 (grace=2s)")
    if active:
        done, pending = await asyncio.wait(list(active), timeout=2)
        if pending:
            print(f"[4] 强制取消 {len(pending)} 个残留任务")
            for t in pending:
                t.cancel()
            await asyncio.gather(*pending, return_exceptions=True)

    await client_task
    print("[5] 资源回收完毕, 退出")


asyncio.run(main())
