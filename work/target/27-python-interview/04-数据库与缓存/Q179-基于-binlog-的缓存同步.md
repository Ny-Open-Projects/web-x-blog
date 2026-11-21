---
title: [Q179] 基于 binlog 的缓存同步
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q179 · 基于 binlog 的缓存同步

> 难度:★★★ | 标签:MySQL, binlog, 缓存一致性

**问**:如何用 binlog 保证缓存与数据库的最终一致?

**答**:MySQL binlog 记录行级变更,通过 canal/Debezium 之类的 CDC 组件伪装成从库订阅变更,投递到 MQ,消费者解析变更并删除/更新对应缓存。优点:与 DB 提交顺序一致、业务零侵入、消费失败可重试。注意幂等消费(见 Q180)与乱序处理(按主键分区分区保序)。

```python
# file: code/04_数据库与缓存/q179_binlog_sync.py
"""binlog 变更事件消费同步缓存(模拟 CDC 投递), 真实场景用 canal/MQ"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ChangeEvent:
    table: str
    op: str            # INSERT / UPDATE / DELETE
    key: str
    after: Optional[dict] = None


class CacheSyncer:
    def __init__(self):
        self.cache: dict = {}
        self.processed: set = set()          # 幂等: 事件 id 去重

    def on_change(self, event_id: str, event: ChangeEvent) -> None:
        if event_id in self.processed:       # MQ 至少一次投递 -> 必须幂等
            return
        self.processed.add(event_id)
        if event.op == "DELETE":
            self.cache.pop(f"{event.table}:{event.key}", None)
        else:
            self.cache[f"{event.table}:{event.key}"] = event.after


def fake_binlog_stream():
    """模拟 canal 投递到 MQ 的两次重复事件 + 一次更新"""
    yield ("evt-1", ChangeEvent("users", "UPDATE", "1", {"name": "alice"}))
    yield ("evt-1", ChangeEvent("users", "UPDATE", "1", {"name": "alice"}))  # 重复投递
    yield ("evt-2", ChangeEvent("users", "UPDATE", "1", {"name": "alice2"}))


if __name__ == "__main__":
    syncer = CacheSyncer()
    for event_id, event in fake_binlog_stream():
        syncer.on_change(event_id, event)
    print("缓存最终值:", syncer.cache)          # alice2, 重复事件被幂等吸收
```

**追问**:
- 直接更新缓存而不是删,配合 CDC 可以吗?——可以但要求事件严格有序且带上完整终值,乱序会把旧值写回,删除 + TTL 更稳。
- binlog 格式选哪种?——ROW 格式,能拿到行级前后镜像,STATEMENT 拿不到具体值。

---
