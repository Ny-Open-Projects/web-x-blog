---
title: [R19-226] useOptimistic 的队列语义：连续多次乐观更新怎么合并？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-226：useOptimistic 的队列语义：连续多次乐观更新怎么合并？
**答**：
- useOptimistic 维护「乐观更新队列」：每次 addOptimistic 入队一条，渲染时按顺序 reducer 折叠到 serverState 上。
- 连续点赞三次（未确认）：队列三条，UI 显示 3 次叠加结果；reducer 收到 (serverCount, [a,b,c]) 依次应用。
- 事务完成时：队列清空、serverState 更新为服务端真值，乐观层自动消失——reducer 只描述「一条乐观操作怎么改变视图」。
- 部分失败：React 不会自动回滚「部分」——一个 action 失败会清除整个对应队列并回到 serverState，需要 UI 层提示。
- 设计要点：reducer 必须是纯函数，且乐观操作应「可重放」到任何 serverState 上。
