---
title: [Q1451] 幂等写入器:按业务键 upsert
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1451 · 幂等写入器:按业务键 upsert

> 难度:★★★☆ | 标签:幂等, 写入器

**问**:数据管道重跑是常态,你怎么保证同一个批次跑三遍,结果和跑一遍一样?

**答**:关键是让写入器以"业务键"为准做 upsert,而不是向下游追加。每条数据必须带稳定的业务主键(订单号 + 更新时间这类),写入时同键覆盖,可选"更新时间更大才覆盖"的合并规则;这样无论批次重放多少次,终端状态一致,这就是幂等。反例是 append-only 写入:一次任务失败重跑,下游就多出一份重复数据,报表翻倍。配套三个工程习惯:写入前对批次做批次号登记,重放可整体跳过;合并规则要能处理乱序(旧数据晚到不覆盖新状态);用"写入前后对状态取哈希"做幂等性自测,回归测试里必须有"执行两次哈希不变"这条断言。涉及删除的同步还要额外处理墓碑消息,否则删除会被重放的旧数据复活。

```python
# file: code/05_数据分析与工程化/q1451_idempotent_writer.py
"""幂等写入器:按业务键 upsert,重放同一批次结果不变"""


class AppendSink:
    """反例:只追加的写入器,重放会产生重复数据"""

    def __init__(self):
        self.rows = []

    def write(self, batch):
        self.rows.extend(batch)


class UpsertSink:
    """正确做法:以业务键为准的 upsert,天然幂等"""

    def __init__(self):
        self.rows = {}

    def write(self, batch):
        for row in batch:
            key = row["order_id"]
            old = self.rows.get(key)
            # 业务规则:同键取更新时间更大的那条
            if old is None or row["updated_at"] > old["updated_at"]:
                self.rows[key] = row

    def snapshot(self):
        return {k: (v["amount"], v["updated_at"]) for k, v in sorted(self.rows.items())}


BATCH = [
    {"order_id": "o1", "amount": 100, "updated_at": "2025-06-01T10:00:00"},
    {"order_id": "o2", "amount": 200, "updated_at": "2025-06-01T10:05:00"},
]
UPDATE = [{"order_id": "o1", "amount": 150, "updated_at": "2025-06-01T11:00:00"}]


def state_hash(snap):
    import hashlib
    return hashlib.md5(repr(snap).encode()).hexdigest()


if __name__ == "__main__":
    sink = UpsertSink()
    h1 = state_hash(sink.snapshot())
    sink.write(BATCH)
    sink.write(UPDATE)
    good_once = state_hash(sink.snapshot())
    sink.write(BATCH)   # 故意重放旧批次
    good_twice = state_hash(sink.snapshot())
    print("upsert: 首次写入哈希 =", good_once, " 重放后哈希 =", good_twice,
          " 幂等:", good_once == good_twice)

    bad = AppendSink()
    bad.write(BATCH)
    bad.write(UPDATE)
    bad.write(BATCH)    # 重放导致重复行
    print("append: 行数 =", len(bad.rows), "-> 重放产生重复,这就是要避免的写法")
```

**追问**:
- 追问 1:没有天然业务键的数据怎么办?—— 用"来源 + 分区 + 行号"合成键,或对内容做稳定哈希,前提是上游能保证同一逻辑行生成同一键。
- 追问 2:upsert 和幂等的边界在哪?—— upsert 解决行级重放,任务级幂等还要靠分区覆盖写或批次登记,两者通常组合使用。
