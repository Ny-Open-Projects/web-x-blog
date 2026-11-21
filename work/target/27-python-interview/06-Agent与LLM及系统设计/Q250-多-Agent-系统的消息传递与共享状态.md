---
title: [Q250] 多 Agent 系统的消息传递与共享状态
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q250 · 多 Agent 系统的消息传递与共享状态

> 难度:★★★★ | 标签:Agent, 多Agent

**问**:多 Agent 之间传递信息,用消息传递还是共享黑板?怎么避免上下文爆炸?

**答**:两种范式:消息传递(每个 Agent 收到定向消息,类似 actor 模型)隔离性好、易回放调试;共享黑板(所有 Agent 读写同一状态,类似 blackboard)信息全量可见但容易脏写。生产中常折中:黑板存"任务状态与产物引用",消息只传"通知与指针",避免把完整上下文塞进每条消息。防上下文爆炸的手段:传摘要而非全文、传 artifact 引用由接收方按需拉取、限制历史窗口。

```python
# file: code/06_Agent与LLM及系统设计/q250_message_bus.py
"""消息总线 + 共享黑板:Agent 间只传引用与摘要,产物存黑板按需拉取。"""


class Blackboard:
    def __init__(self):
        self.artifacts: dict[str, str] = {}

    def put(self, key: str, content: str) -> str:
        ref = f"artifact::{key}"
        self.artifacts[key] = content
        return ref

    def get(self, ref: str) -> str:
        return self.artifacts.get(ref.removeprefix("artifact::"), "")


class MessageBus:
    def __init__(self, blackboard: Blackboard):
        self.board = blackboard
        self.inbox: dict[str, list[dict]] = {}

    def send(self, to: str, summary: str, ref: str = ""):
        self.inbox.setdefault(to, []).append({"summary": summary, "ref": ref})

    def receive(self, agent: str) -> list[dict]:
        msgs = self.inbox.pop(agent, [])
        for m in msgs:  # 接收方按需拉取全文
            if m["ref"]:
                m["full"] = self.board.get(m["ref"])[:20] + "..."
        return msgs


if __name__ == "__main__":
    board = Blackboard()          # 先建黑板再建总线,避免元组赋值右侧引用未定义名
    bus = MessageBus(board)
    ref = board.put("report_v1", "这是一份很长的行业分析报告全文..." * 3)
    bus.send("writer", "调研完成,请基于报告写稿", ref=ref)
    print("writer 收到:", bus.receive("writer"))
```

**追问**:
- 脏写怎么防?——黑板写操作带版本号/锁,或限定「谁可写哪个字段」;自由读写共享状态在并发下必出竞态。
- artifact 引用怎么设计?——产物存对象存储,消息只传 URI+摘要;接收方按需拉取,上下文只留指针。
- 消息乱序怎么处理?——每条消息带序号与 causality 引用,消费端按序重放;actor 模型的回放调试依赖这一点。
