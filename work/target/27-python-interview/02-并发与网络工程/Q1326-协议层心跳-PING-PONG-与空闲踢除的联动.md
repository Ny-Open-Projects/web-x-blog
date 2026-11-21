---
title: [Q1326] 协议层心跳:PING/PONG 与空闲踢除的联动
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1326 · 协议层心跳:PING/PONG 与空闲踢除的联动

> 难度:★★★☆ | 标签:心跳, 空闲超时, 应用层协议

**问**:在自研协议里做心跳,TCP keepalive 不够吗?服务端踢人怎么和心跳配合?

**答**:TCP keepalive(默认 2 小时)只证明"内核到内核的链路通",证明不了"应用还活着、事件循环没卡死"——应用死锁时 TCP 栈照样回 ACK,这就是必须做应用层 PING/PONG 的原因。设计三件套:客户端周期发 PING,服务端立刻回 PONG(双向都刷新活跃时间);服务端维护每连接 last_recv 时间戳,后台 reaper 扫描,空闲超过阈值先发 BYE 帧再断开,给客户端一个"是被请走的"的确定性信号;踢除动作由服务端发起,而不是等客户端超时,否则半死连接会占住资源。心跳间隔的工程共识是空闲阈值的 1/3,允许丢一次。下面的演示里,一个客户端按时 PING 存活,另一个沉默被抓出踢除。

```python
# file: code/02_并发与网络工程/q1326_protocol_heartbeat.py
import socket
import threading
import time

PING, PONG, BYE = 0x02, 0x03, 0x04
IDLE_TIMEOUT = 0.6


def frame(t: int, payload: bytes = b"") -> bytes:
    return bytes([t]) + len(payload).to_bytes(2, "big") + payload


class Server:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.alive = {}          # conn -> last_recv 时间戳
        self.kicked = []

    def serve(self, port: int, ready: threading.Event) -> None:
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", port))
        srv.listen(4)
        ready.set()
        srv.settimeout(0.2)
        while not self.stop.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            with self.lock:
                self.alive[conn] = time.monotonic()
            threading.Thread(target=self.handle, args=(conn,), daemon=True).start()

    def handle(self, conn: socket.socket) -> None:
        try:
            while True:
                head = conn.recv(3)
                if len(head) < 3:
                    break
                t, ln = head[0], int.from_bytes(head[1:3], "big")
                payload = b""
                while len(payload) < ln:
                    payload += conn.recv(ln - len(payload))
                with self.lock:
                    self.alive[conn] = time.monotonic()
                if t == PING:
                    conn.sendall(frame(PONG))
                elif t == BYE:
                    break
        except OSError:
            pass
        finally:
            with self.lock:
                self.alive.pop(conn, None)
            conn.close()

    def reap(self) -> None:
        while not self.stop.is_set():
            time.sleep(0.1)
            now = time.monotonic()
            with self.lock:
                stale = [c for c, ts in self.alive.items() if now - ts > IDLE_TIMEOUT]
                for c in stale:
                    try:
                        c.sendall(frame(BYE, b"idle"))
                    except OSError:
                        pass
                    self.kicked.append(c)
                    self.alive.pop(c, None)
                    c.close()          # 关闭会让对端 recv 立刻 EOF

    def start(self, port: int) -> threading.Thread:
        self.stop = threading.Event()
        ready = threading.Event()
        threading.Thread(target=self.serve, args=(port, ready), daemon=True).start()
        threading.Thread(target=self.reap, daemon=True).start()
        ready.wait(2)
        return


def client_loop(port: int, ping: bool, out: list) -> None:
    s = socket.create_connection(("127.0.0.1", port), timeout=2)
    s.settimeout(0.1)
    deadline = time.monotonic() + 1.2
    try:
        while time.monotonic() < deadline:
            if ping:
                s.sendall(frame(PING))
            try:
                data = s.recv(64)
            except socket.timeout:
                continue
            if not data:
                out.append("EOF 被服务端断开")
                break
            if data[0] == PONG:
                out.append("PONG")
            elif data[0] == BYE:
                out.append("BYE 被踢")
                break
            time.sleep(0.15)
    except OSError:
        out.append("连接异常关闭")
    finally:
        s.close()


def main() -> None:
    port = 59710
    server = Server()
    server.start(port)

    out_a, out_b = [], []
    ta = threading.Thread(target=client_loop, args=(port, True, out_a))
    tb = threading.Thread(target=client_loop, args=(port, False, out_b))
    ta.start(); tb.start(); ta.join(); tb.join()
    server.stop.set()
    time.sleep(0.3)

    print(f"勤快客户端: {out_a[:5]} -> 存活, 心跳 {out_a.count('PONG')} 次")
    print(f"沉默客户端: {out_b[:3]} -> 被踢除")
    assert "PONG" in out_a and "EOF 被服务端断开" not in out_a[:3]
    assert out_b and ("BYE 被踢" in out_b or "EOF 被服务端断开" in out_b)
    print("心跳保活与空闲踢除联动验证通过")


if __name__ == "__main__":
    main()
```

**追问**:1) PONG 要不要也校验"请求-响应配对"?——要:心跳载荷带一个 nonce,PONG 原样带回,防止某类代理缓存了旧 PONG 让死链路假装活着。2) 应用层 PING 与 TCP keepalive 怎么分工?——keepalive 探「链路」(内核级,免费但默认 2h 且间隔参数平台相关),PING 探「应用活性」(进程活着、事件循环没卡);两层都要:keepalive 当兜底(调小 idle),PING 当主判据(Q617 的完整展开)。3) 空闲踢除的 reaper 怎么设计?——后台线程周期扫 last_recv(单调时钟),超阈值先发 BYE 再 close(给对端确定性信号);扫描频率与踢除阈值成比例,扫描代价与连接数线性——万级连接考虑堆按 last_recv 排序避免全量扫。4) 生产陷阱?——PONG 无 nonce 校验,代理缓存的旧 PONG 让死链路假装活着(见原问);踢除后没通知路由层,推送继续写死连接(Q624 同源);PING 间隔与空闲阈值比例失当(丢一次 PING 就踢,弱网误杀);reaper 与 IO 线程并发改 last_recv 无原子保障。

---
