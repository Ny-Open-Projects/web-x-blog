"""会话背压:积压合并 coalesce + 溢出降级摘要 + 消费速率自适应节流。"""


class BackpressuredInbox:
    """会话收件箱:上限 N 条;同键消息只保留最新(合并);溢出时旧消息折叠为摘要。"""

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = []                    # [(key, text)] 有序队列
        self.coalesced = 0
        self.folded = 0

    def push(self, key, text):
        # 同 key 合并:保留最新,丢弃过期中间态(如连续的打字中通知)
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i][0] == key:
                self.items.pop(i)
                self.coalesced += 1
                break
        self.items.append((key, text))
        if len(self.items) > self.capacity:
            self._fold()

    def _fold(self):
        """溢出折叠:把最旧的一半压成一条摘要,保住最新消息的实时性。"""
        half = len(self.items) // 2
        old = self.items[:half]
        self.items = [("digest", "折叠了" + str(len(old)) + "条旧消息")] + self.items[half:]
        self.folded += len(old)

    def drain(self):
        out, self.items = list(self.items), []
        return out

    def should_throttle(self, avg_process_ms, arrival_ms):
        """处理耗时逼近到达间隔时建议节流:留 20% 余量。"""
        return avg_process_ms > arrival_ms * 0.8


if __name__ == "__main__":
    box = BackpressuredInbox(capacity=5)
    box.push("typing", "用户正在输入")
    box.push("typing", "用户还在输入")
    box.push("typing", "用户输入完毕")
    assert box.coalesced == 2 and len(box.items) == 1

    for i in range(6):
        box.push("msg-" + str(i), "消息" + str(i))
    assert len(box.items) <= 5, "容量硬上限"
    assert box.folded > 0 and box.items[0][0] == "digest"
    assert box.items[-1] == ("msg-5", "消息5"), "最新消息必须保住"

    drained = box.drain()
    assert drained == box.items == [] or (drained and box.items == [])

    assert box.should_throttle(avg_process_ms=90, arrival_ms=100) is True   # 90 > 80 节流
    assert box.should_throttle(avg_process_ms=50, arrival_ms=100) is False
    print("背压通过:同键合并 2 次 溢出折叠保最新 消费端节流建议正确")
