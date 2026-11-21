---
title: [Q643] 客户端负载均衡:DNS 轮询与故障摘除
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q643 · 客户端负载均衡:DNS 轮询与故障摘除

> 难度:★★★★ | 标签:负载均衡, 故障摘除, 轮询

**问**:没有 LB 时,客户端怎么做多实例的负载均衡和故障摘除?

**答**:客户端负载均衡三件套:1) 地址池——来自 DNS 多 A 记录或配置中心,客户端维护 [(ip, port, 健康状态)] 列表;2) 选择策略——轮询(round-robin)最简单,加权/最少连接按需;3) 故障摘除与恢复——请求失败标记节点不健康并冷却一段时间,冷却后用探测请求(半开)试恢复,避免坏节点反复拖慢请求。与 DNS 轮询的区别:DNS 层轮询无法感知实例死亡(TTL 内照样下发),客户端健康检查才是真正的故障转移。生产对应品:gRPC 的 pick_first/round_robin 策略。

```python
# file: code/02_并发与网络工程/q643_client_lb.py
import itertools
import socket
import threading
import time


class EchoServer:
    def __init__(self) -> None:
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.srv.bind(("127.0.0.1", 0))
        self.srv.listen(8)
        self.port = self.srv.getsockname()[1]
        self.alive = True
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self) -> None:
        self.srv.settimeout(0.2)
        while self.alive:
            try:
                conn, _ = self.srv.accept()
            except socket.timeout:
                continue
            try:
                data = conn.recv(1024)
                conn.sendall(f"[{self.port}] echo: ".encode() + data)
            except OSError:
                pass
            conn.close()


class ClientLB:
    def __init__(self, endpoints: list) -> None:
        self.endpoints = [{"addr": e, "healthy": True, "cooldown_until": 0.0} for e in endpoints]
        self._rr = itertools.cycle(range(len(endpoints)))
        self.stats: dict = {}

    def _pick(self) -> dict:
        n = len(self.endpoints)
        for _ in range(n):  # 轮询跳过不健康节点
            idx = next(self._rr)
            ep = self.endpoints[idx]
            if ep["healthy"] or time.monotonic() > ep["cooldown_until"]:
                ep["healthy"] = True
                return ep
        raise RuntimeError("无可用节点")

    def request(self, payload: bytes, timeout: float = 0.5) -> str:
        ep = self._pick()
        try:
            host, port = ep["addr"]
            c = socket.create_connection((host, port), timeout=timeout)
            c.sendall(payload)
            c.settimeout(timeout)
            resp = c.recv(1024).decode()
            c.close()
            self.stats[port] = self.stats.get(port, 0) + 1
            return resp
        except OSError:
            ep["healthy"] = False
            ep["cooldown_until"] = time.monotonic() + 2.0  # 冷却 2s 后半开恢复
            raise


if __name__ == "__main__":
    servers = [EchoServer() for _ in range(3)]
    lb = ClientLB([( "127.0.0.1", s.port) for s in servers])

    print("--- 正常轮询 ---")
    for i in range(6):
        print(f"  req{i} →", lb.request(b"ping"))

    print("--- 杀掉一个节点 ---")
    servers[1].alive = False
    servers[1].srv.close()
    for i in range(6):
        try:
            print(f"  req{i} →", lb.request(b"ping"))
        except (OSError, RuntimeError) as e:
            print(f"  req{i} 失败: {e}")
    print("请求分布:", {f"port{k}": v for k, v in lb.stats.items()})
    print("坏节点已被摘除, 流量全部落到健康节点")
```

**追问**:1) 为什么冷却后要"半开"而不是直接恢复?——直接恢复会让下一次流量洪峰再次打到坏节点;半开先放一个探测请求,成功才整流回归,失败继续冷却。2) 摘除与重试的边界怎么划?——摘除是「让坏节点退出轮转」(失败计数+冷却期),重试是「单次请求的容错」(幂等前提+超时预算内);不摘除只重试,故障节点会持续放大延迟;不重试只摘除,瞬态错误直接打给用户,两者是互补机制。3) 与服务端 LB 的取舍?——客户端 LB 省一跳、策略细(gRPC pick_first/round_robin),但每个客户端都要实现与配置下发;服务端 LB 集中治理但加一跳延迟;DNS 轮询是最粗粒度、TTL 内无法感知实例死亡。4) 生产陷阱?——摘除阈值过敏感(一次超时就摘)造成流量震荡;半开探测没做,节点摘了永远回不来;地址池随 DNS 但缓存 TTL(Q642)过长,扩容新实例长期不参与分摊。

---
