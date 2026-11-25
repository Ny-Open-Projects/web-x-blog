---
title: [928] 多 Agent 系统的共享状态怎么管理，黑板模式是什么
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 状态管理]
type: 面试题
---

## 928：多 Agent 系统的共享状态怎么管理，黑板模式是什么

**答**：
- 黑板模式（Blackboard）：所有 Agent 读写同一个结构化工作区（任务列表、中间产物、决策日志），事件驱动各 Agent 订阅自己关心的变化——比点对点传消息多了「全局可观测」。
- 状态分层：会话状态（用户可见）、任务状态（编排器管）、 scratchpad（各 Agent 私有草稿）；混在一起就会出现「子 Agent 覆盖主任务结论」这类事故。
- 并发写冲突：同一黑板条目用乐观锁（版本号）或单写者约束（某条目只有指定 Agent 可写）。
- 追问钩子：为什么不用数据库就够？——黑板要的是「变化通知 + 依赖触发」，数据库缺订阅语义，通常 DB 存真相 + 事件总线广播。

```ts
class Blackboard {
  private state = new Map<string, { ver: number; val: unknown; owner: string }>();
  write(key, val, agent) {
    const cur = this.state.get(key);
    if (cur && cur.owner !== agent) throw new Error('single-writer violation');
    this.state.set(key, { ver: (cur?.ver || 0) + 1, val, owner: agent });
    this.emit(key, { ver: cur?.ver || 0 });       // 通知订阅者
  }
  subscribe(key, fn) { this.on(key, fn); }        // 事件驱动触发下游 Agent
}
```

