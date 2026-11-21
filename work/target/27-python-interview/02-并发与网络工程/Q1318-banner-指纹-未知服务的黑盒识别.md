---
title: [Q1318] banner 指纹:未知服务的黑盒识别
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1318 · banner 指纹:未知服务的黑盒识别

> 难度:★★☆☆ | 标签:banner, 指纹, 安全巡检

**问**:扫描发现一个陌生开放端口,怎么在不发有害流量的前提下识别它是什么服务?

**答**:分两类收集。主动型服务(FTP、SMTP、SSH、Redis)接受连接就先说话,connect 后直接 recv 就能拿到 banner;被动型服务(HTTP)要发一个最小合法请求才回话,发一个不含任何攻击载荷的 HEAD 或 GET / 即可。识别靠签名表:SSH- 前缀、HTTP/ 状态行、Redis 的 -ERR/+PONG、SMTP 的 220 应答都是强特征。三个纪律:读 banner 要设超时并限制字节数,防止个别服务不发 banner 导致脚本挂死;对生产端口只做一次识别请求;识别结果要标"置信度",签名匹配是高置信,端口约定(如 6379 是 Redis)只是低置信猜测。下面的演示在回环上布置三个假想服务并逐一识别。

```python
# file: code/02_并发与网络工程/q1318_banner_fingerprint.py
import socket
import threading


SIGNATURES = [
    ("SSH", lambda b: b.startswith(b"SSH-")),
    ("HTTP", lambda b: b.startswith(b"HTTP/")),
    ("SMTP", lambda b: b.startswith(b"220 ") or b.startswith(b"220-")),
    ("Redis", lambda b: b[:1] in b"+-$*" and b"ERR" in b or b == b"+PONG\r\n"),
]


def grab_banner(host: str, port: int, probe_http: bool = False) -> bytes:
    s = socket.create_connection((host, port), timeout=1)
    s.settimeout(0.5)
    try:
        if probe_http:
            s.sendall(b"HEAD / HTTP/1.0\r\nHost: probe\r\n\r\n")
        banner = s.recv(256)
    except socket.timeout:
        banner = b""
    finally:
        s.close()
    return banner


def fingerprint(banner: bytes) -> str:
    if not banner:
        return "无 banner, 低置信: 仅端口约定可猜"
    for name, match in SIGNATURES:
        if match(banner):
            return f"{name} 高置信: {banner[:48]!r}"
    return f"未知服务, 需人工确认: {banner[:48]!r}"


def main() -> None:
    servers = {}

    def start(name: str, greeting: bytes, wait_req: bool) -> int:
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        port = srv.getsockname()[1]
        srv.listen(2)
        servers[name] = srv

        def loop():
            for _ in range(2):
                try:
                    conn, _ = srv.accept()
                except OSError:
                    return
                if wait_req:
                    try:
                        conn.recv(256)
                    except OSError:
                        pass
                try:
                    conn.sendall(greeting)
                    conn.close()
                except OSError:
                    pass
        threading.Thread(target=loop, daemon=True).start()
        return port

    ssh_port = start("ssh", b"SSH-2.0-OpenSSH_9.6\r\n", False)
    http_port = start("http", b"HTTP/1.1 400 Bad Request\r\n\r\n", True)
    redis_port = start("redis", b"-ERR unknown command\r\n", False)

    for name, port, need_req in [("端口 22 想象位", ssh_port, False),
                                 ("端口 80 想象位", http_port, True),
                                 ("端口 6379 想象位", redis_port, False)]:
        banner = grab_banner("127.0.0.1", port, probe_http=need_req)
        print(f"{name} -> {fingerprint(banner)}")
    for srv in servers.values():
        srv.close()


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么先 recv 后发请求的顺序不能反?——主动型服务的 banner 在你发言之前就到了,你先 send 会把 banner 和对回显混在一起,解析时序就乱了。2) banner 的超时与限额为什么必须设?——被动型服务不发 banner,无超时的 recv 会挂死脚本;恶意/异常服务可以发无限字节;设超时+读上限(如 256 字节)让识别器自身健壮——「工具先保证自己不死」是运维工具第一原则。3) 置信度分层怎么落地?——协议特征(banner 字符串)是高置信;端口约定(6379=Redis)是低置信;行为特征(响应特定命令)是中置信;输出时标注置信度,自动化决策只信高置信,低置信的交给人工。4) 生产陷阱?——对生产端口发激进探测包(触发 IDS/影响业务);识别结果不记录时间与版本(指纹过时);把「端口开着」当「服务健康」(banner 拿到了但服务内部已坏);混淆 banner 指纹与安全漏洞(有版本号不等于有漏洞)。

---
