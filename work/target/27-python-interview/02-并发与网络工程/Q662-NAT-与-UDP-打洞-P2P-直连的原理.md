---
title: [Q662] NAT 与 UDP 打洞:P2P 直连的原理
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q662 · NAT 与 UDP 打洞:P2P 直连的原理

> 难度:★★★★ | 标签:NAT, 打洞, P2P

**问**:两台都在 NAT 后面的设备怎么直接通信?什么情况下打洞会失败?

**答**:NAT 的关键性质:内网主机向外发包时,NAT 建立"公网端口映射",之后该端口会转发对应回包。打洞流程:A、B 都先向公网 rendezvous 服务器注册,服务器把对方的公网映射地址告诉双方;A 直接向 B 的公网映射发包——虽然第一次大概率被 B 的 NAT 丢弃(还不是合法回包),但这次发包在 A 的 NAT 上开好了洞;B 同理向 A 发,双方各开一次洞后,包就能直接对流。失败情形:对称型 NAT(每个目标分配不同公网端口,映射对不上)——企业防火墙常见,只能退回中继;严格厂商防火墙同理。锥形 NAT(家用路由主流)打洞成功率很高。

```python
# file: code/02_并发与网络工程/q662_nat_punch.py
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
```

**追问**:1) ICE/STUN/TURN 分别是什么角色?——STUN 探测自己在 NAT 上的公网映射,ICE 把多种候选地址(直连/打洞/中继)统一排序试连,TURN 是打洞失败时的中继兜底,三者组合是 WebRTC 的连接层。2) 对称型 NAT 为什么必然失败?——对称型对每个目标分配不同公网端口映射,B 看到的 A 的映射与 A 向 rendezvous 注册的映射不一致,洞对不上;锥形 NAT(家用路由主流)全映射一致,打洞成功率高;企业防火墙多为对称型,只能 TURN 中继。3) 为什么要「双方同时互发」?——先发的包大概率被对方 NAT 丢弃(还不是合法回包),但这让己方 NAT 开了洞;双方各开一次后互为合法回包,流即可直接对通;不协同就出现「一方洞开好了对方没发」,窗口期一过映射过期。4) 生产陷阱?——rendezvous 单点,撮合挂了全部 P2P 不可用;打洞成功当长期保证(NAT 映射有超时,要心跳保活);UDP 大包被 MTU 分片丢弃(PMTU 意识,应用层分片);IPv6 环境绕过 NAT 直接可连,别浪费打洞逻辑。

---
