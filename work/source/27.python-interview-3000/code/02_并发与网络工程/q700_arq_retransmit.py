import queue
import random
import select
import socket
import threading
import time

LOSS = 0.3  # 模拟 30% 丢包
random.seed(42)


class ReliableUdpReceiver(threading.Thread):
    def __init__(self, sock: socket.socket) -> None:
        super().__init__(daemon=True)
        self.sock = sock
        self.delivered: list = []
        self.seen: set = set()
        self.dups = 0
        self.stop = threading.Event()

    def run(self) -> None:
        self.sock.settimeout(0.1)
        while not self.stop.is_set():
            try:
                data, addr = self.sock.recvfrom(2048)
            except socket.timeout:
                continue
            seq, payload = data.split(b":", 1)
            n = int(seq)
            if n in self.seen:
                self.dups += 1  # 重传导致重复: 去重但必须重发 ACK
            else:
                self.seen.add(n)
                self.delivered.append(payload.decode())
            self.sock.sendto(b"ACK" + seq, addr)  # ACK 也可能丢


def sender(sock: socket.socket, peer: tuple, messages: list,
           timeout: float = 0.05) -> dict:
    sock.settimeout(0.01)  # ACK 读取窗口; 超时后回头检查重传时钟
    pending: dict = {}  # seq -> (send_time, payload)
    next_seq = 0
    sent_count = 0
    done = 0
    while done < len(messages):
        now = time.monotonic()
        # 补发: 未确认且超时
        for seq, (t0, payload) in list(pending.items()):
            if now - t0 > timeout:
                sock.sendto(f"{seq}:".encode() + payload, peer)
                sent_count += 1
                pending[seq] = (now, payload)
        # 发新包 (窗口=1 停等: 未确认时不发新)
        if not pending and next_seq < len(messages):
            payload = messages[next_seq]
            sock.sendto(f"{next_seq}:".encode() + payload, peer)
            sent_count += 1
            pending[next_seq] = (now, payload)
            next_seq += 1
        # 收 ACK
        try:
            ack, _ = sock.recvfrom(64)
            seq = int(ack[3:])
            if seq in pending:
                del pending[seq]
                done += 1
        except socket.timeout:
            pass
        time.sleep(0.002)
    return {"sent": sent_count, "delivered": done}


def lossy_network(stop: threading.Event, sender_side: socket.socket,
                  receiver_side: socket.socket, rx_addr: tuple) -> None:
    """双向有损转发, 模拟不可靠网络 (数据与 ACK 一视同仁地丢)。
    sender_side: 发送方发数据的入口; receiver_side: 固定端口的出口 —
    接收方按"数据来源地址"回 ACK, 恰好回到这里, 再经同样丢包回给发送方。"""
    sender_side.settimeout(0.1)
    receiver_side.settimeout(0.1)
    tx_addr = None  # 首个数据包的来源地址, 即发送方的回程地址
    while not stop.is_set():
        ready, _, _ = select.select([sender_side, receiver_side], [], [], 0.1)
        for s in ready:
            try:
                data, addr = s.recvfrom(2048)
            except OSError:
                continue
            if random.random() < LOSS:
                continue
            if s is sender_side:
                tx_addr = addr
                receiver_side.sendto(data, rx_addr)
            elif tx_addr:
                sender_side.sendto(data, tx_addr)


if __name__ == "__main__":
    rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx_sock.bind(("127.0.0.1", 0))
    mid_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mid_sock.bind(("127.0.0.1", 0))
    net_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 面向接收方的固定出口
    net_sock.bind(("127.0.0.1", 0))
    tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tx_sock.bind(("127.0.0.1", 0))

    receiver = ReliableUdpReceiver(rx_sock)
    receiver.start()
    stop = threading.Event()
    threading.Thread(target=lossy_network,
                     args=(stop, mid_sock, net_sock, rx_sock.getsockname()),
                     daemon=True).start()

    messages = [f"msg-{i}".encode() for i in range(20)]
    # 发送方 → 有损网络 → 接收方
    t0 = time.monotonic()
    stats = sender(tx_sock, mid_sock.getsockname(), messages)
    dt = time.monotonic() - t0
    time.sleep(0.2)
    stop.set()
    receiver.stop.set()
    receiver.join(timeout=1)

    print(f"原始 {len(messages)} 条, 实际发送 {stats['sent']} 次 "
          f"(重传 {stats['sent'] - len(messages)} 次), 耗时 {dt * 1000:.0f}ms")
    print(f"接收端交付 {len(receiver.delivered)} 条, 去重 {receiver.dups} 次")
    assert sorted(receiver.delivered) == sorted(m.decode() for m in messages)
    print("全部消息最终送达: 序号+ACK+超时重传+去重 = 可靠性, 代价是停等的低吞吐")
