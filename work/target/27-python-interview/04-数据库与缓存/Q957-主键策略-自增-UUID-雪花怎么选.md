---
title: [Q957] 主键策略: 自增 / UUID / 雪花怎么选
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q957 · 主键策略: 自增 / UUID / 雪花怎么选

> 难度:★★★☆ | 标签:主键, 选型

**问**:主键用自增、UUID 还是雪花 ID?各自的坑是什么?

**答**:自增 bigint:顺序写入对聚簇索引最友好、8 字节紧凑;坑是分库分表后会冲突、暴露业务量(订单号可被猜测)、依赖单库生成。UUIDv4:全局唯一、客户端可生成;坑是随机性导致页分裂与索引膨胀(36 字符),索引体积与缓存效率都差。雪花 ID(snowflake):64 位 = 时间戳+机器号+序列,趋势递增、分布式可生成,是分库分表首选;坑是时钟回拨(等待或分配新机器号)与机器号管理。折衷方案:内部自增 bigint 做物理主键 + 业务唯一键(order_no)单独维护 + 对外暴露业务键;已有 UUID 表升级 UUIDv7(时间前缀,趋势递增)。

```python
# file: code/04_数据库与缓存/q957_pk_strategy.py
"""雪花 ID 最小实现: 趋势递增 + 时钟回拨保护"""
import threading
import time

class Snowflake:
    def __init__(self, worker: int, ts_bits=41, worker_bits=10, seq_bits=12):
        self.worker = worker
        self.seq = 0
        self.last = -1
        self.ts_bits, self.worker_bits, self.seq_bits = ts_bits, worker_bits, seq_bits
        self.epoch = 1700000000000
        self.lock = threading.Lock()

    def next_id(self) -> int:
        with self.lock:
            ts = int(time.time() * 1000)
            if ts < self.last:                       # 时钟回拨: 等待追平
                ts = self.last
            if ts == self.last:
                self.seq = (self.seq + 1) & ((1 << self.seq_bits) - 1)
                if self.seq == 0:                    # 本毫秒序列耗尽
                    while int(time.time() * 1000) <= self.last:
                        pass
            else:
                self.seq = 0
            self.last = ts
            return ((ts - self.epoch) << (self.worker_bits + self.seq_bits)
                    | (self.worker << self.seq_bits) | self.seq)

if __name__ == "__main__":
    sf = Snowflake(worker=1)
    ids = [sf.next_id() for _ in range(5)]
    print(ids)
    print("趋势递增:", ids == sorted(ids))
    print(f"41 位时间戳可用约 {(1 << 41) / 1000 / 86400 / 365:.0f} 年")
```

**追问**:
- 雪花的机器号怎么分配?——注册中心申请或按 IP/实例编号分配,重复会生成重复 ID,必须集中管理并防复用。
- 对外为什么不直接暴露自增 id?——可被枚举与推断业务量,接口暴露业务键(order_no/uuid),内部表关联才用自增。

---
