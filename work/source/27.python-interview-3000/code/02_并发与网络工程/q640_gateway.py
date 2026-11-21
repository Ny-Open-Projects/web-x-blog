import asyncio

registry: dict = {}  # user -> StreamWriter (单机版核心数据结构)


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    user = None
    try:
        while True:
            line = await reader.readline()
            if not line:
                break
            parts = line.decode().strip().split(" ", 2)
            cmd = parts[0]
            if cmd == "REG" and len(parts) >= 2:
                user = parts[1]
                registry[user] = writer
                writer.write(b"OK registered\n")
                print(f"[gateway] {user} 上线, 在线数 {len(registry)}")
            elif cmd == "PUB" and len(parts) == 3:
                target, msg = parts[1], parts[2]
                tw = registry.get(target)
                if tw is None:
                    writer.write(f"ERR offline {target}\n".encode())
                else:
                    tw.write(f"MSG {user} {msg}\n".encode())  # 推送
                    await tw.drain()
                    writer.write(b"OK sent\n")
            elif cmd == "LIST":
                writer.write(f"OK {[u for u in registry]}\n".encode())
            else:
                writer.write(b"ERR bad command\n")
            await writer.drain()
    except (ConnectionError, asyncio.IncompleteReadError):
        pass
    finally:
        if user and registry.get(user) is writer:
            del registry[user]
            print(f"[gateway] {user} 下线, 在线数 {len(registry)}")
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def client(port: int, name: str, script: list) -> None:
    r, w = await asyncio.open_connection("127.0.0.1", port)
    for line in script:
        w.write((line + "\n").encode())
        await w.drain()
        resp = await r.readline()
        print(f"[{name}] {line} → {resp.decode().strip()}")
    w.close()
    try:
        await w.wait_closed()
    except Exception:
        pass


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    await client(port, "alice", ["REG alice", "LIST"])
    await client(port, "bob", ["REG bob", "PUB alice hello-alice", "PUB carol hi-offline"])
    await client(port, "alice", ["PUB bob hello-bob", "LIST"])
    server.close()
    await server.wait_closed()


asyncio.run(main())
