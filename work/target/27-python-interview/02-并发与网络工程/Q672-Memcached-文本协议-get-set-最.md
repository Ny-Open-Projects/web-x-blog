---
title: [Q672] Memcached 文本协议:get/set 最小客户端
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q672 · Memcached 文本协议:get/set 最小客户端

> 难度:★★☆ | 标签:Memcached, 文本协议, 缓存

**问**:Memcached 的 ASCII 协议长什么样?和 RESP 比,设计取向有什么不同?

**答**:Memcached 文本协议是"行命令+裸数据"风格:set 的请求是 `set key flags exptime bytes\r\n` + 恰好 bytes 字节的裸数据 + `\r\n`,回复 `STORED`;get 是 `get key1 key2\r\n`,回复若干 `VALUE key flags bytes\r\n<data>\r\n` 块,最后 `END\r\n`。与 RESP 的差异:Memcached 更"扁平"(无类型标签,靠命令区分),get 支持一次多 key,协议人肉 telnet 就能调;但二进制安全靠显式字节数声明,出错就整条流错位——所有长度必须精确。新版本也提供 binary 协议(见 Q673)。

```python
# file: code/02_并发与网络工程/q672_memcached_text.py
import socket
import threading


def memcached_server(stop: threading.Event, port_box: list) -> None:
    store: dict = {}
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)

    def handle(conn: socket.socket) -> None:
        conn.settimeout(2)
        buf = b""
        try:
            while True:
                data = conn.recv(65536)
                if not data:
                    break
                buf += data
                while b"\r\n" in buf:
                    line, buf = buf.split(b"\r\n", 1)
                    parts = line.decode().split()
                    if parts[0] == "set":
                        _cmd, key, flags, exptime, nbytes = parts
                        nbytes = int(nbytes)
                        while len(buf) < nbytes + 2:  # 数据 + \r\n 可能未到齐
                            chunk = conn.recv(65536)
                            if not chunk:
                                return
                            buf += chunk
                        value, buf = buf[:nbytes], buf[nbytes + 2:]
                        store[key] = (int(flags), value)
                        conn.sendall(b"STORED\r\n")
                    elif parts[0] == "get":
                        out = b""
                        for key in parts[1:]:
                            if key in store:
                                flags, value = store[key]
                                out += (f"VALUE {key} {flags} {len(value)}\r\n").encode() + value + b"\r\n"
                        out += b"END\r\n"
                        conn.sendall(out)
                    else:
                        conn.sendall(b"ERROR\r\n")
        except OSError:
            pass
        finally:
            conn.close()

    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        threading.Thread(target=handle, args=(conn,), daemon=True).start()
    srv.close()


class MemcachedClient:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.create_connection((host, port), timeout=2)
        self.sock.settimeout(2)
        self.buf = b""  # 接收缓冲: 一次 recv 可能吞进多行, 必须按帧切分

    def _fill(self) -> None:
        chunk = self.sock.recv(4096)
        if not chunk:
            raise ConnectionError("server closed connection")
        self.buf += chunk

    def _readline(self) -> bytes:
        """读到一行 (含 CRLF); 多读的字节留在缓冲区给后续读取。"""
        while b"\r\n" not in self.buf:
            self._fill()
        line, self.buf = self.buf.split(b"\r\n", 1)
        return line + b"\r\n"

    def _read_exact(self, n: int) -> bytes:
        while len(self.buf) < n:
            self._fill()
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def set(self, key: str, value: bytes, flags: int = 0, exptime: int = 0) -> bool:
        head = f"set {key} {flags} {exptime} {len(value)}\r\n".encode()
        self.sock.sendall(head + value + b"\r\n")
        return self._readline() == b"STORED\r\n"

    def get(self, *keys: str) -> dict:
        self.sock.sendall(("get " + " ".join(keys) + "\r\n").encode())
        result = {}
        while True:
            line = self._readline()
            if line == b"END\r\n":
                break
            _tag, key, _flags, nbytes = line.decode().split()
            nbytes = int(nbytes)
            data = self._read_exact(nbytes + 2)  # 裸数据 + 尾部 CRLF
            result[key] = data[:nbytes]
        return result


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    threading.Thread(target=memcached_server, args=(stop, box), daemon=True).start()
    while not box:
        import time
        time.sleep(0.01)

    c = MemcachedClient("127.0.0.1", box[0])
    print("set:", c.set("user:1", b'{"name":"ada"}'))
    print("set:", c.set("user:2", b"\x00\x01\x02binary"))
    got = c.get("user:1", "user:2", "missing")
    for k, v in got.items():
        print(f"get {k}: {v!r}")
    assert got["user:2"] == b"\x00\x01\x02binary"
    print("一次 get 多 key + 二进制安全验证通过")
    c.sock.close()
    stop.set()
```

**追问**:1) 为什么 get 的多 key 返回里"不存在的 key 完全不出现"?——省流量且语义明确(没有 VALUE 行=未命中);代价是调用方不能区分"未命中"与"该 key 曾被 CAS 删除后立刻过期",需要时得用 gets 带 cas 值。2) 「裸数据+显式字节数」出错会怎样?——长度声明与实际不符时整条流错位且无重同步机制,后续所有回复解析全乱;这是文本协议携带二进制的通病,RESP 用类型标签+长度前缀缓解。3) get 多 key 的返回怎么解析?——逐个 VALUE 块(头行+裸数据)读到 END;返回顺序不保证与请求一致,按 VALUE 行里的 key 归位;不存在的 key 静默缺失(见原问),要区分「未命中」语义就用 gets 带 cas。4) 生产陷阱?——value 超过单 key 上限(默认 1MB)写入失败但错误状态没人看;flags/exptime 非法值整条命令被拒;ASCII 协议端口对外暴露,telnet 即可改缓存。

---
