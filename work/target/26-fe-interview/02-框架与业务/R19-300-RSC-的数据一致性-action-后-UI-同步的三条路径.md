---
title: [R19-300] Action 修改数据后，RSC 页面 UI 怎么同步？（三条路径对比）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-300：Action 修改数据后 UI 怎么同步？
**答**：
- 路径一：action 内 revalidateTag/Path —— 服务端重新渲染受影响段，随 action 响应下发新 RSC payload，客户端无缝替换（推荐默认）。
- 路径二：action 返回新数据 —— 客户端 setState 局部更新（适合只需更新局部小状态，省一次整段渲染）。
- 路径三：router.refresh() —— 客户端主动请求当前路由新 payload（适合 action 无法 revalidate 的跨服务场景）。
- 选择：能用路径一就用（框架闭环）；「响应里直接带结果」的表单用路径二减少往返；兜底用路径三。
- 一致性保障：无论哪条，UI 最终以服务端 payload 为准，客户端不做长期副本。
