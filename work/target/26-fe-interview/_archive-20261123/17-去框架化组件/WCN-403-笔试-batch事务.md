---
title: [WCN-403] 笔试：给 signal 系统加 batch（事务语义）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-403：笔试：给 signal 系统加 batch（事务语义）。
**题目**：`batch(fn)`：内部多次写合并为一次 flush；嵌套 batch 只在最外层执行；返回 fn 返回值。

```javascript
let depth = 0;
export function batch(fn) {
  depth++;
  try { return fn(); }
  finally { depth--; if (depth === 0) flushNow(); }   // 最外层 flush
}
// flushNow 与 402 的微任务 flush 共用去重队列
// 设计决策讨论：batch 内读取 computed 拿旧值（事务可见性），
// 若要「读新值」需 flush 前置重算（成本高），文档写明即可得分。

```

**评分点**：
- 嵌套计数器（depth），最外层退出才 flush。
- batch 内 computed 不重算（读取返回旧值？——设计决策：惰性则读取触发重算破坏事务；说明取「读旧值」简化并讨论）。
- 异常安全：fn 抛错也要结束事务（finally flush 或放弃）。
- 测试：batch 内 3 次写 → effect 执行 1 次。
