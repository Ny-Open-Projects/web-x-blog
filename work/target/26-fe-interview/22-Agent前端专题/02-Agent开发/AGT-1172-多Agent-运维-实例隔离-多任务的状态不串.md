---
title: [1172] 两个并发任务的 Agent 状态串了（A 的产物出现在 B 里），怎么防
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 隔离]
type: 面试题
---

## 1172：两个并发任务的 Agent 状态串了（A 的产物出现在 B 里），怎么防

**答**：
- 隔离根因排查：上下文对象被共享引用（JS 的对象按引用传递，一处 mutation 全局可见）、缓存 key 缺任务维度、全局单例（黑板/记忆做成了 module 单例）。
- 防御三件：任务级上下文对象（每任务独立实例，禁止模块级可变状态）、缓存 key 强制含 taskId（lint 规则卡）、上下文不可变（传递用浅拷贝快照，写操作走显式 store）。
- 检测手段：集成测试加「并发隔离用例」（两个任务交错跑，断言互不污染）；运行时「状态泄漏探针」（产物元数据校验所属任务）。
- 追问钩子：为什么「缓存 key 缺任务维度」最隐蔽？——单任务测试全绿，只在并发/重试场景出现；而且表现是「答案串味」没有报错，靠用户投诉发现，必须在测试层主动覆盖。

```ts
// 反例：模块级单例黑板 -> 任务串味
// const blackboard = new Map();  // BAD
// 正例：任务级实例
class TaskCtx {
  static create(taskId) { return new TaskCtx(taskId); }
  constructor(taskId) { this.taskId = taskId; this.board = new Map(); }
}
async function runTask(task) {
  const ctx = TaskCtx.create(task.id);           // 每任务独立
  cacheKeyRule(ctx);                              // 缓存 key 必含 taskId（lint 卡）
  return orchestrator.run(task, { ctx });
}
```
