---
title: [R19-235] 购物车批量勾选怎么用 useOptimistic 实现乐观更新？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-235：购物车批量勾选的乐观更新怎么做？
**答**：
- 操作模型：{ type: 'toggle', id, checked } 入队；reducer 按 id 映射更新 checked，选中态/总价/结算按钮全部由乐观列表派生。
- 派生值（总价）也在乐观层算：保证勾选反馈零延迟；服务端确认后总价随 serverState 刷新。
- 失败回滚：整批 toggle 回滚，toast 提示「网络异常，请重试」；部分项失败（服务端返回逐项结果）时按项修正。
- 大列表性能：id→item 的 Map 索引 + 只渲染勾选差异，避免 reducer 全列表重算。
- 追问钩子：购物车跨页同步（另一标签页）用 BroadcastChannel + serverState 版本号。
