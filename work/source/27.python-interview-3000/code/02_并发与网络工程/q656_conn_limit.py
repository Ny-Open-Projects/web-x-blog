import asyncio
from collections import defaultdict

GLOBAL_LIMIT = 3
PER_IP_LIMIT = 2
active: set = set()
per_ip: dict = defaultdict(int)
rejected: list = []


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    peer = writer.get_extra_info("peername")
    ip = peer[0] if peer else "unknown"
    reason = None
    if len(active) >= GLOBAL_LIMIT:
        reason = "global limit"
    elif per_ip[ip] >= PER_IP_LIMIT:
        reason = "per-ip limit"
    if reason:
        rejected.append((ip, reason))
        writer.write(f"REJECTED {reason} retry-later\n".encode())
        await writer.drain()
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass
        return

    active.add(writer)
    per_ip[ip] += 1
    try:
        writer.write(f"ACCEPTED active={len(active)} ip_active={per_ip[ip]}\n".encode())
        await writer.drain()
        await asyncio.sleep(0.3)  # 模拟业务占用连接
        await reader.read(64)
    finally:
        active.discard(writer)
        per_ip[ip] -= 1
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def client(port: int, name: str) -> None:
    try:
        r, w = await asyncio.open_connection("127.0.0.1", port)
        resp = await r.readline()
        print(f"[{name}] {resp.decode().strip()}")
        w.close()
        await w.wait_closed()
    except (ConnectionError, asyncio.IncompleteReadError):
        print(f"[{name}] 连接被立即关闭 (RST 型拒绝)")


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    # 6 个并发客户端: 3 个进入, 其余按 全局/IP 限制被拒
    await asyncio.gather(*[client(port, f"c{i}") for i in range(6)])
    await asyncio.sleep(0.5)
    print("拒绝记录:", rejected)
    server.close()
    await server.wait_closed()


asyncio.run(main())
