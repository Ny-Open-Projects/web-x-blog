import socket
import threading
import time


class NatBox:
    """模拟锥形 NAT (EIM): 一个公网 socket 服务于内网主机的所有远端。"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.public = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.public.bind(("127.0.0.1", 0))  # NAT 公网侧端口
        self.private_addr: tuple = ()
        self.forwarded: list = []
        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self) -> None:
        self.public.settimeout(0.2)
        while True:
            try:
                data, src = self.public.recvfrom(2048)
            except socket.timeout:
                continue
            except OSError:
                return
            if self.private_addr:
                self.forwarded.append((self.name, src, data))
                self.private_sock.sendto(f"via-{self.name}-NAT: {data.decode()}".encode(),
                                         self.private_addr)

    def bind_client(self, private_sock) -> None:
        self.private_sock = private_sock
        self.private_addr = private_sock.getsockname()

    def send(self, data: bytes, dst: tuple) -> None:
        self.public.sendto(data, dst)  # 经 NAT 转换源地址后发出

    @property
    def public_addr(self) -> tuple:
        return self.public.getsockname()


def rendezvous(stop: threading.Event, port_box: list, registry: dict) -> None:
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    srv.bind(("127.0.0.1", 0))
    port_box.append(srv.getsockname()[1])
    srv.settimeout(0.2)
    while not stop.is_set():
        try:
            data, addr = srv.recvfrom(2048)
        except socket.timeout:
            continue
        msg = data.decode()
        if msg.startswith("REG"):
            name = msg.split()[1]
            registry[name] = addr  # 记录各端在 NAT 上的公网映射
            print(f"[rendezvous] {name} 公网映射: {addr}")
        elif msg.startswith("WHO"):
            target = msg.split()[1]
            peer = registry.get(target)
            srv.sendto(f"PEER {peer[0]} {peer[1]}".encode(), addr)
    srv.close()


if __name__ == "__main__":
    stop = threading.Event()
    box: list = []
    registry: dict = {}
    threading.Thread(target=rendezvous, args=(stop, box, registry), daemon=True).start()
    while not box:
        time.sleep(0.01)

    # 两个内网主机, 各自位于一台 NAT 之后
    nat_a, nat_b = NatBox("A"), NatBox("B")
    priv_a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    priv_a.bind(("127.0.0.1", 0))
    priv_b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    priv_b.bind(("127.0.0.1", 0))
    nat_a.bind_client(priv_a)
    nat_b.bind_client(priv_b)
    time.sleep(0.1)

    # 双方向 rendezvous 注册 (出站 → NAT 生成映射)
    for nat, name in ((nat_a, "alice"), (nat_b, "bob")):
        nat.send(f"REG {name}".encode(), ("127.0.0.1", box[0]))
    time.sleep(0.2)

    # 双方交换彼此公网映射 (打洞的撮合阶段)
    nat_a.send(b"WHO bob", ("127.0.0.1", box[0]))
    nat_b.send(b"WHO alice", ("127.0.0.1", box[0]))
    time.sleep(0.2)
    peer_a = registry["bob"]
    peer_b = registry["alice"]

    # 打洞: 双方同时向对方公网映射发包
    nat_a.send(b"punch-A", peer_a)
    nat_b.send(b"punch-B", peer_b)
    time.sleep(0.3)

    # 此后直接 P2P 通信 (各 NAT 的映射已就位)
    nat_a.send(b"direct-hello", peer_a)
    time.sleep(0.2)
    print("\n转发记录:")
    for item in nat_a.forwarded + nat_b.forwarded:
        print(" ", item)
    print("结论: 锥形 NAT 下双方各开一次洞即可直连; 对称 NAT 需退回中继 (Q661)")
    stop.set()
