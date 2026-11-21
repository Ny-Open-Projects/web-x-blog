import asyncio


async def fetch(host: str, port: int, path: str) -> str:
    reader, writer = await asyncio.open_connection(host, port)
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    writer.write(request.encode())
    await writer.drain()
    data = await reader.read(4096)
    writer.close()
    try:
        await writer.wait_closed()
    except ConnectionResetError:
        pass
    status = data.split(b"\r\n", 1)[0].decode(errors="replace")
    return status


async def bounded_fetch(i: int, sem: asyncio.Semaphore) -> str:
    async with sem:
        try:
            return await fetch("example.com", 80, f"/page{i}")
        except OSError as e:
            return f"page{i} 失败: {e!r}"


async def main() -> None:
    sem = asyncio.Semaphore(5)  # 并发上限, 等价线程数
    results = await asyncio.gather(*(bounded_fetch(i, sem) for i in range(8)))
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
