# -*- coding: utf-8 -*-
"""慢消费者的丢弃会计: 计数器说话, 决策才站得住。

- 每个消费者一本账: 送达数、丢弃数、队列水位;
- 丢弃率是慢消费者的体检指标, 超阈值就摘除而不是拖垮出口;
- 丢弃不是失败, 是治理动作, 但必须可观测、可核算。
"""
from collections import deque

CAP = 8
TICKS = 100
PER_TICK = 6
SHED_RATE = 0.5
MIN_SAMPLE = 30                              # 样本不足不下结论


class Consumer:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate                  # 每拍能处理几条
        self.q = deque(maxlen=CAP)        # 满了挤掉最老的
        self.delivered = 0
        self.dropped = 0

    def publish(self, msg):
        if len(self.q) == self.q.maxlen:
            self.dropped += 1             # 挤掉一条最老的, 记账
        self.q.append(msg)

    def tick(self):
        for _ in range(min(self.rate, len(self.q))):
            self.q.popleft()
            self.delivered += 1

    @property
    def drop_rate(self):
        total = self.delivered + self.dropped
        return self.dropped / total if total else 0.0


if __name__ == "__main__":
    consumers = [Consumer("fast", PER_TICK), Consumer("slow", 1)]
    shed = set()
    for t in range(TICKS):
        for c in consumers:
            if c.name in shed:
                continue                  # 已摘除: 不再投喂
            for m in range(PER_TICK):
                c.publish("msg-%d-%d" % (t, m))
        for c in consumers:
            c.tick()
            sampled = c.delivered + c.dropped
            if (c.name not in shed and sampled >= MIN_SAMPLE
                    and c.drop_rate > SHED_RATE):
                shed.add(c.name)          # 证据够了且超阈值: 摘除
                print("tick %d: %s 已采样 %d, 丢弃率 %.0f%% 超阈值 %d%%, 执行摘除"
                      % (t, c.name, sampled, c.drop_rate * 100, SHED_RATE * 100))

    print("%-6s %9s %9s %9s" % ("name", "delivered", "dropped", "drop%"))
    for c in consumers:
        print("%-6s %9d %9d %8.0f%%"
              % (c.name, c.delivered, c.dropped, c.drop_rate * 100))
    print("要点: 计数器把'感觉慢'变成'丢多少', 治理动作才有依据")
