import queue
import threading
import time


class Qos1Channel:
    """模拟 QoS1 通道: 指定前 N 个 ACK 丢弃(确定性), 发送方重传, 接收端去重。

    注意别用 random 概率丢包: 丢包率 1.0 会把所有 ACK 全丢光,
    重传路径上产生的重复次数就不止 1, 断言不稳定。
    """

    def __init__(self, drop_first_ack: int = 1) -> None:
        self.drop_first_ack = drop_first_ack
        self._ack_seq = 0
        self.inbound: "queue.Queue[dict]" = queue.Queue()
        self.acks: "queue.Queue[int]" = queue.Queue()
        self.delivered: list = []
        self.seen_ids: set = set()
        self.dup_detected = 0
        self._stop = threading.Event()
        threading.Thread(target=self._receiver, daemon=True).start()

    def _receiver(self) -> None:
        while not self._stop.is_set():
            try:
                msg = self.inbound.get(timeout=0.1)
            except queue.Empty:
                continue
            pid = msg["packet_id"]
            if pid in self.seen_ids:
                self.dup_detected += 1
                print(f"[receiver] 重复 PUBLISH id={pid} → 去重, 仅重发 ACK")
            else:
                self.seen_ids.add(pid)
                self.delivered.append(msg["payload"])
                print(f"[receiver] 首次交付: {msg['payload']} (id={pid})")
            self._ack_seq += 1
            if self._ack_seq <= self.drop_first_ack:
                print(f"[network] PUBACK id={pid} 丢失 → 发送方将重传")
            else:
                self.acks.put(pid)  # PUBACK

    def send_with_retry(self, payload: str, packet_id: int,
                        timeout: float = 0.1, max_retry: int = 3) -> bool:
        for attempt in range(1, max_retry + 1):
            print(f"[sender] PUBLISH 尝试 {attempt}: {payload} (id={packet_id})")
            self.inbound.put({"packet_id": packet_id, "payload": payload})
            try:
                acked = self.acks.get(timeout=timeout)
                if acked == packet_id:
                    print(f"[sender] 收到 PUBACK id={packet_id}, 交付确认")
                    return True
            except queue.Empty:
                continue  # 超时重传同一 packet_id
        return False

    def close(self) -> None:
        self._stop.set()


if __name__ == "__main__":
    ch = Qos1Channel(drop_first_ack=1)  # 首个 ACK 必丢, 强制走一次重传路径
    ok = ch.send_with_retry("temp=23.5", packet_id=42)
    time.sleep(0.2)
    ch.close()
    print(f"\n交付结果: {ch.delivered}")
    print(f"重复检测: 接收端发现 {ch.dup_detected} 次重复, 业务只处理 1 次")
    print(f"发送方确认: {ok}")
    assert ok, "重传后应收到 PUBACK"
    assert ch.delivered == ["temp=23.5"], "去重保证恰好处理一次"
    assert ch.dup_detected == 1
