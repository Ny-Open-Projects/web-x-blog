---
title: [R19-227] useOptimistic 失败回滚的完整闭环怎么设计？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-227：useOptimistic 失败回滚的完整闭环怎么设计？
**答**：
- 回滚机制内建：action throw/返回错误时，对应乐观队列清空，UI 回到 serverState——前提是「真实状态」存在且完整。
- 闭环三步：乐观 UI（立即展示）→ 失败信号（action 抛错/返回 code）→ 回滚展示（自动）+ 补偿提示（需要 UI 层做，如 toast「点赞失败已恢复」）。
- 关键前提：optimistic 的 base state 必须与服务端权威一致；如果服务端返回的 state 与乐观前的本地 serverState 不同步，回滚后会「跳变」。
- 实践：action 成功返回「服务端确认后的 state」，而不是让前端自己猜；失败时返回失败原因供 toast。
- 对比手写回滚：useOptimistic 省掉 snapshot/undo 栈，代价是「回滚粒度=整个 action」。
