---
title: [Q1623] Webhook 死信队列与人工重投
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1623 · Webhook 死信队列与人工重投

> 难度:★★★☆ | 标签:Webhook, 运维

**问**:Webhook 重试耗尽之后事件去哪了?死信队列要记录什么,怎么重投?

**答**:重试耗尽的事件进入死信队列,每条死信必须记录事件 ID、原始 payload、已尝试次数、最后响应状态码、失败原因与最终失败时间——没有这些,人工排查就是翻日志考古。event_id 在 pending 与 dead 里都作唯一键,防止重复入队;重投是把死信放回 pending 并清零尝试计数,走正常投递通道;投递成功后从两边移除。死信要有容量上限与告警(死信突增通常是对端挂了),重投接口必须有权限与审计,不能变成无鉴权的重放接口。按订阅方维度隔离,一个挂掉的消费方不能拖垮其他订阅。

```python
# file: code/03_Web后端开发/q1623_webhook_dlq.py
"""Webhook 死信队列: 入队、盘点与人工重投(纯标准库)。"""


class Dlq:
    def __init__(self, max_attempts):
        self.max = max_attempts
        self.pending = {}     # event_id -> {payload, attempts, ...}
        self.dead = {}        # event_id -> {..., reason}

    def record_failure(self, event_id, payload, status):
        item = self.pending.setdefault(event_id, {"payload": payload, "attempts": 0})
        item["attempts"] += 1
        item["last_status"] = status
        if item["attempts"] >= self.max:
            item["reason"] = "接收方持续 5xx, 重试耗尽" if status >= 500 else "接收方明确拒绝"
            self.dead[event_id] = self.pending.pop(event_id)

    def record_success(self, event_id):
        self.pending.pop(event_id, None)
        self.dead.pop(event_id, None)            # 重投成功可从死信移除

    def replay(self, event_id):
        if event_id in self.dead:
            item = self.dead.pop(event_id)
            item["attempts"] = 0
            self.pending[event_id] = item
            return True
        return False


dlq = Dlq(max_attempts=3)
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
dlq.record_failure("ev2", {"type": "user.signup"}, 503)
dlq.record_failure("ev2", {"type": "user.signup"}, 503)
dlq.record_success("ev2")                        # 第三次成了
dlq.record_failure("ev1", {"type": "order.paid"}, 503)
print("死信:", {k: (v["attempts"], v["reason"]) for k, v in dlq.dead.items()})
print("重投 ev1:", dlq.replay("ev1"), "重投不存在:", dlq.replay("ev9"))
dlq.record_failure("ev1", {"type": "order.paid"}, 200)
print("重投成功后 pending:", list(dlq.pending), "dead:", list(dlq.dead))
print("要点: event_id 唯一防重复入队; 死信要带原因与最后状态; 人工重投走白名单接口")
```

**追问**:
- 死信能自动重投吗?——可加冷却后自动重投一次的策略,但要限速,最终仍需人工确认。
- 接收方明确 4xx 也进死信吗?——进,但原因标记为明确拒绝,通常说明契约错了,重投无意义,要修调用方。
