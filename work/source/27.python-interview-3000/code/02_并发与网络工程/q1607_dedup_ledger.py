"""幂等消费台账: 至少一次投递的去重与断点。

至少一次投递(broker 重试)必然产生重复消息; 消费端用台账保幂等:
- processed 集合: 见过的序号直接跳过, 业务副作用只生效一次;
- checkpoint: 台账定期落盘; 崩溃重启后加载台账, 重复投递的消息
  再来一遍也不会产生第二次副作用。
"""
import random

N = 40
DUP_RATE = 0.3


def produce(n, dup_rate, seed=7):
    rng = random.Random(seed)
    stream = []
    for seq in range(1, n + 1):
        stream.append(seq)
        if rng.random() < dup_rate:
            stream.append(seq)          # broker 重发: 同一序号再来一次
    return stream


class Consumer:
    """台账 = 已处理序号集合 + 业务投影。"""

    def __init__(self, checkpoint=None):
        self.processed = set(checkpoint or [])
        self.projection = []            # 业务副作用: 每序号只应出现一次
        self.dup_skipped = 0

    def handle(self, seq):
        if seq in self.processed:
            self.dup_skipped += 1
            return "dup-skip"
        self.processed.add(seq)
        self.projection.append(seq)
        return "applied"

    def checkpoint(self):
        return sorted(self.processed)   # 生产中落盘/写 DB


def main():
    stream = produce(N, DUP_RATE)
    print("投递流: %d 条消息, 其中含重复" % len(stream))

    # 第一段消费: 消费到一半就"崩溃"
    consumer = Consumer()
    for seq in stream[:24]:
        consumer.handle(seq)
    saved = consumer.checkpoint()
    effects_before_crash = list(consumer.projection)   # 已生效的副作用
    print("崩溃前已处理 %d 个序号, 台账落盘" % len(saved))

    # 重启: 从台账恢复, broker 把整条流重新投一遍(至少一次语义)
    consumer = Consumer(checkpoint=saved)
    stats = {"applied": 0, "dup-skip": 0}
    for seq in stream:
        stats[consumer.handle(seq)] += 1
    print("重启后重放全量投递: 新生效 %d 次, 跳过重复 %d 次"
          % (stats["applied"], stats["dup-skip"]))

    # 副作用总账: 崩溃前已生效 + 重启后新生效, 必须恰好覆盖全部序号
    effects_total = effects_before_crash + consumer.projection
    print("副作用总账覆盖:", len(set(effects_total)), "个序号, 总条数",
          len(effects_total))
    assert stats["dup-skip"] > 0, "重放必然命中台账里的旧序号"
    assert sorted(effects_total) == list(range(1, N + 1)), (
        "每个业务序号必须恰好生效一次, 不多不少")
    assert len(set(effects_total)) == len(effects_total), "副作用不能重复生效"
    print("结论: 至少一次投递 + 消费端台账 = 效果上的恰好一次副作用")


if __name__ == "__main__":
    main()
