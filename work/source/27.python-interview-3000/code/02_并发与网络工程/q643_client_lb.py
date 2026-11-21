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
