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
