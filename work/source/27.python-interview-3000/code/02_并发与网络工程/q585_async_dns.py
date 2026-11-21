import asyncio
import socket
import time

HOSTS = ["localhost"] * 8 + ["127.0.0.1"] * 8  # 本机可解析, 不依赖外网


async def resolve_all_sequential() -> None:
    loop = asyncio.get_running_loop()
    for host in HOSTS:
        await loop.getaddrinfo(host, 80, family=socket.AF_INET)


async def resolve_all_concurrent() -> None:
    loop = asyncio.get_running_loop()
    await asyncio.gather(
        *[loop.getaddrinfo(host, 80, family=socket.AF_INET) for host in HOSTS]
    )


async def inspect_result() -> None:
    loop = asyncio.get_running_loop()
    infos = await loop.getaddrinfo("localhost", 80, family=socket.AF_INET)
    print("getaddrinfo 返回结构示例:", infos[0])
    # (family, type, proto, canonname, sockaddr) — 建连接时直接喂给 open_connection


async def main() -> None:
    await inspect_result()
    t0 = time.perf_counter()
    await resolve_all_sequential()
    t_seq = time.perf_counter() - t0

    t0 = time.perf_counter()
    await resolve_all_concurrent()
    t_con = time.perf_counter() - t0
    print(f"串行 {len(HOSTS)} 次: {t_seq:.3f}s, 并发: {t_con:.3f}s")
    print("并发来自线程池中的并行 getaddrinfo, 而非单线程复用")


asyncio.run(main())
