import random


class WindowReceiver:
    def __init__(self, window: int = 8) -> None:
        self.next_seq = 0
        self.window = window
        self.buffered = {}       # seq -> payload, 等缺口的乱序帧
        self.delivered = []
        self.dupes = 0
        self.acked = 0           # 累计 ACK: 已连续交付到的 seq

    def accept(self, seq: int, payload) -> str:
        if seq < self.next_seq or seq in self.buffered:
            self.dupes += 1
            return "DUPLICATE"
        if seq == self.next_seq:
            self.delivered.append(payload)
            self.next_seq += 1
            while self.next_seq in self.buffered:   # 缺口补上, 清仓连续段
                self.delivered.append(self.buffered.pop(self.next_seq))
                self.next_seq += 1
            self.acked = self.next_seq
            return "DELIVERED"
        if seq < self.next_seq + self.window:
            self.buffered[seq] = payload
            return f"BUFFERED 乱序缓存 等缺口 {self.next_seq}"
        return f"OUT_OF_WINDOW 越窗 seq={seq}"


def main() -> None:
    rnd = random.Random(2024)
    total, window = 30, 8
    packets = [(i, f"data-{i}") for i in range(total)]

    # 模拟链路: 发送方守窗口, 每个窗口内乱序并注入重复帧
    wire = []
    dupes_injected = 0
    for start in range(0, total, window):
        chunk = packets[start:start + window]
        chunk += list(chunk[:2])          # 每窗口复制前 2 帧制造重复
        dupes_injected += min(2, len(chunk))
        rnd.shuffle(chunk)
        wire.extend(chunk)

    rx = WindowReceiver(window=window)
    outcomes = {}
    for seq, p in wire:
        verdict = rx.accept(seq, p)
        key = verdict.split()[0]
        outcomes[key] = outcomes.get(key, 0) + 1

    print(f"链路注入 {len(wire)} 帧(含重复 {dupes_injected}), 交付 {len(rx.delivered)} 帧")
    print(f"结果分布: {outcomes}")
    print(f"交付顺序前 8: {[p.split('-')[1] for p in rx.delivered[:8]]}")
    assert rx.delivered == [f"data-{i}" for i in range(total)], "必须严格有序不重不漏"
    assert rx.dupes == dupes_injected, f"{dupes_injected} 个重复帧应被识别, 实际 {rx.dupes}"
    print(f"累计 ACK 停在 {rx.acked}, 乱序缓冲剩余 {len(rx.buffered)}")
    print("乱序重组 + 去重验证通过: 发送方守窗口时接收端零丢帧")


if __name__ == "__main__":
    main()
