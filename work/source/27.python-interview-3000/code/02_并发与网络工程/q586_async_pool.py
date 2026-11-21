import asyncio
import time


class AsyncConnPool:
    def __init__(self, host: str, port: int, size: int = 3) -> None:
        self._host, self._port, self._size = host, port, size
        self._idle: asyncio.Queue = asyncio.Queue()
        self._sem = asyncio.Semaphore(size)  # 上限控制
        self._created = 0
        self._reused = 0

    async def acquire(self):
        await self._sem.acquire()
        try:
            conn = self._idle.get_nowait()
            self._reused += 1
            return conn
        except asyncio.QueueEmpty:
            reader, writer = await asyncio.open_connection(self._host, self._port)
            self._created += 1
            return reader, writer

    def release(self, conn) -> None:
        self._idle.put_nowait(conn)
        self._sem.release()

    def discard(self, conn) -> None:
        _reader, writer = conn
        writer.close()
        self._sem.release()

    async def close_all(self) -> None:
        while not self._idle.empty():
            _r, w = self._idle.get_nowait()
            w.close()
            await w.wait_closed()


async def echo_server(reader, writer) -> None:
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def do_request(pool: AsyncConnPool, msg: str) -> str:
    conn = await pool.acquire()
    try:
        reader, writer = conn
        writer.write(msg.encode())
        await writer.drain()
        data = await asyncio.wait_for(reader.read(100), 1.0)
        pool.release(conn)
        return data.decode()
    except Exception:
        pool.discard(conn)  # 出错的连接不回池
        raise


async def main() -> None:
    server = await asyncio.start_server(echo_server, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    pool = AsyncConnPool("127.0.0.1", port, size=3)

    results = await asyncio.gather(*[do_request(pool, f"req{i}") for i in range(10)])
    print("请求结果:", results)
    print(f"新建连接 {pool._created} 次, 复用 {pool._reused} 次 (10 个请求)")
    await pool.close_all()
    server.close()
    await server.wait_closed()


asyncio.run(main())
