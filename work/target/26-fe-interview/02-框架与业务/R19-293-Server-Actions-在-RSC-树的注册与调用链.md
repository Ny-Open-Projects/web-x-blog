---
title: [R19-293] Server Action 从「声明」到「被调用」的完整链路是什么？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-293：Server Action 从声明到被调用的完整链路？
**答**：
- 声明：'use server' 文件导出函数，构建期生成唯一 action id（加密签名）。
- 下发：RSC 树中把 action 作为 prop/事件传给客户端组件，Flight 流里是函数引用标记 `$F1`。
- 调用：客户端触发时 POST 到当前页面 URL（Next），body 为 Flight 编码参数 + action id header。
- 执行：服务端按 id 找到函数执行，返回值以 Flight 流回传；redirect/revalidate 随响应下发。
- 安全链：id 签名防伪造，但仍需业务鉴权——id 可被合法用户重放调用。
