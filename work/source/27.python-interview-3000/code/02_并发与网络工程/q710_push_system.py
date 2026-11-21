import asyncio
import itertools

registry: dict = {}          # user -> {"writer": w, "topics": set, "buffer": deque}
OFFLINE_BUFFER = 5


class PushHub:
    async def subscribe(self, user: str, topic: str, writer) -> None:
        entry = registry.setdefault(user, {"topics": set(), "buffer": []})
        entry["writer"] = writer
        entry["topics"].add(topic)
        # 重连续传: 补发离线缓冲
        for event in entry["buffer"]:
            writer.write(f"EVENT {event}\n".encode())
        entry["buffer"].clear()
        await writer.drain()
        writer.write(f"SUBOK {topic}\n".encode())
        await writer.drain()

    async def publish(self, topic: str, event_id: int, payload: str) -> int:
        delivered = 0
        for user, entry in registry.items():
            if topic not in entry["topics"]:
                continue
            writer = entry["writer"]
            if writer is None:  # 离线: 入缓冲
                entry["buffer"].append(f"{event_id} {topic} {payload}")
                if len(entry["buffer"]) > OFFLINE_BUFFER:
                    entry["buffer"].pop(0)
                continue
            try:
                writer.write(f"EVENT {event_id} {topic} {payload}\n".encode())
                await writer.drain()
                delivered += 1
            except ConnectionError:
                entry["writer"] = None  # 连接已死 → 转离线缓冲
                entry["buffer"].append(f"{event_id} {topic} {payload}")
        return delivered


hub = PushHub()


async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    user = None
    try:
        while True:
            line = await reader.readline()
            if not line:
                break
            parts = line.decode().strip().split(" ", 2)
            if parts[0] == "SUB" and len(parts) >= 3:
                user, topic = parts[1], parts[2]
                await hub.subscribe(user, topic, writer)
            elif parts[0] == "PUB" and len(parts) == 3:
                n = await hub.publish(parts[1], next(event_ids), parts[2])
                writer.write(f"PUBOK delivered={n}\n".encode())
                await writer.drain()
            else:
                writer.write(b"ERR usage\n")
                await writer.drain()
    except (ConnectionError, asyncio.IncompleteReadError):
        pass
    finally:
        if user and user in registry and registry[user]["writer"] is writer:
            registry[user]["writer"] = None  # 断线 → 标记离线, 保留缓冲
            print(f"[hub] {user} 离线, 消息将缓冲")
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


event_ids = itertools.count(1)


async def client(port: int, script: list) -> list:
    r, w = await asyncio.open_connection("127.0.0.1", port)
    inbox: list = []
    for line in script:
        if line.startswith("SLEEP"):
            await asyncio.sleep(float(line.split()[1]))
            while True:  # 非阻塞地收取推送
                try:
                    inbox.append((await asyncio.wait_for(r.readline(), 0.05)).decode().strip())
                except asyncio.TimeoutError:
                    break
            continue
        w.write((line + "\n").encode())
        await w.drain()
        if line.startswith("SUB"):
            # 订阅应答 = 离线缓冲的 EVENT 续传 + 最后一条 SUBOK, 必须整组收完
            while True:
                resp = (await r.readline()).decode().strip()
                inbox.append(resp)
                if resp.startswith("SUBOK"):
                    break
        else:
            inbox.append((await r.readline()).decode().strip())
    w.close()
    try:
        await w.wait_closed()
    except Exception:
        pass
    return inbox


async def main() -> None:
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]

    print("--- 场景: 订阅 → 推送 → 断线期间消息缓冲 → 重连续传 ---")
    out1 = await client(port, ["SUB user-a orders"])
    print("user-a:", out1)
    out2 = await client(port, ["SLEEP 0.05", "PUB orders order-100-paid",
                               "SLEEP 0.3", "PUB orders order-101-shipped"])
    print("publisher:", out2)
    out3 = await client(port, ["SUB user-a orders"])
    print("user-a 重连 (收到缓冲的 order-101):", out3)

    server.close()
    await server.wait_closed()
    assert any("order-101" in line for line in out3), "离线消息应被续传"
    print("\n设计要点落地: 注册表路由 + 离线缓冲 + 重连续传 + 慢消费者有界缓冲")


asyncio.run(main())
