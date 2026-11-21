---
title: [Q245] Agent 的幂等与重试设计
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q245 · Agent 的幂等与重试设计

> 难度:★★★★ | 标签:Agent, 可靠性

**问**:Agent 中途崩溃重跑,如何避免重复下单、重复发邮件这类副作用?

**答**:核心是幂等键 + 状态持久化:每个有副作用的工具调用带上由"任务ID+步骤号+参数摘要"生成的幂等键,服务端按键去重(第一次执行,重复请求返回原结果)。配合把 Agent 执行状态(已完成步骤、中间结果)checkpoint 到存储,重跑时从断点恢复而不是从头执行。重试策略要区分:读操作可自动重试(指数退避),写操作必须先确认是否已成功再重试。

```python
# file: code/06_Agent与LLM及系统设计/q245_idempotent.py
"""演示幂等工具:同一幂等键重复调用只执行一次,并支持断点恢复。"""
import hashlib


class IdempotentToolbox:
    def __init__(self):
        self.executed: dict[str, str] = {}   # 幂等键 -> 结果
        self.checkpoint: set[str] = set()    # 已完成步骤

    @staticmethod
    def make_key(task_id: str, step: int, params: dict) -> str:
        raw = f"{task_id}|{step}|{sorted(params.items())}"
        return hashlib.sha256(raw.encode()).hexdigest()[:12]

    def send_email(self, key: str, to: str, body: str) -> str:
        if key in self.executed:
            return f"[幂等命中] 返回缓存结果:{self.executed[key]}"
        result = f"邮件已发送给 {to}"
        self.executed[key] = result
        return result


if __name__ == "__main__":
    box = IdempotentToolbox()
    key = box.make_key("task_A", 3, {"to": "boss@x.com", "body": "日报"})
    print(box.send_email(key, "boss@x.com", "日报"))
    # 模拟崩溃后重跑,同一 key 再次调用
    print(box.send_email(key, "boss@x.com", "日报"))
```

**追问**:
- 幂等键为什么含参数摘要?——同一任务同一步骤但参数不同(重试时重算)需要区分;摘要让服务端能识别「真的重复」与「新调用」。
- checkpoint 存什么?——步骤号、每步入参与结果摘要、最终状态;恢复时回放历史而非重调 LLM,省钱且结果一致。
- 读操作也要幂等吗?——读天然幂等,但重试要有退避与上限;区分读写重试策略,写操作永远先确认再重试。
