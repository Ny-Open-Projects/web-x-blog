from enum import Enum


class State(Enum):
    WAIT_TYPE = 0     # 等 1 字节消息类型
    WAIT_LEN_HI = 1   # 等 2 字节长度的高位
    WAIT_LEN_LO = 2   # 等长度的低位
    WAIT_PAYLOAD = 3  # 等 length 字节负载


class FrameStateMachine:
    def __init__(self, max_payload: int = 4096) -> None:
        self.state = State.WAIT_TYPE
        self.msg_type = 0
        self.length = 0
        self._payload = bytearray()
        self._max = max_payload
        self.trace = []

    def feed(self, data: bytes) -> list:
        frames = []
        for b in data:
            frame = self._step(b)
            if frame is not None:
                frames.append(frame)
        return frames

    def _step(self, b: int):
        if self.state == State.WAIT_TYPE:
            self.msg_type = b
            self.state = State.WAIT_LEN_HI
        elif self.state == State.WAIT_LEN_HI:
            self.length = b << 8
            self.state = State.WAIT_LEN_LO
        elif self.state == State.WAIT_LEN_LO:
            self.length |= b
            if self.length > self._max:
                raise ValueError(f"长度 {self.length} 超上限, 状态机报废")
            self._payload = bytearray()
            if self.length == 0:          # 零长度帧立即完成, 不能停在 WAIT_PAYLOAD
                frame = (self.msg_type, b"")
                self.state = State.WAIT_TYPE
                return frame
            self.state = State.WAIT_PAYLOAD
        elif self.state == State.WAIT_PAYLOAD:
            self._payload.append(b)
            if len(self._payload) == self.length:
                frame = (self.msg_type, bytes(self._payload))
                self.state = State.WAIT_TYPE
                return frame
        return None


def main() -> None:
    frames_in = [(0x01, b"ping"), (0x02, b""), (0x03, b"y" * 100)]
    wire = b"".join(bytes([t]) + len(p).to_bytes(2, "big") + p for t, p in frames_in)

    fsm = FrameStateMachine()
    got = []
    for i, b in enumerate(wire):          # 极端拆分: 一次喂一个字节
        got.extend(fsm.feed(bytes([b])))
        if i < 6:
            fsm.trace.append(f"byte#{i} -> state={fsm.state.name}")
    assert got == frames_in
    print("逐字节投喂解出全部帧:", [(t, p[:8]) for t, p in got])
    for line in fsm.trace:
        print(" ", line)

    # 一次整包投喂结果必须一致: 状态机与碎裂粒度无关
    fsm2 = FrameStateMachine()
    assert fsm2.feed(wire) == frames_in
    print("整包投喂结果一致, 证明状态机对碎裂粒度不敏感")


if __name__ == "__main__":
    main()
