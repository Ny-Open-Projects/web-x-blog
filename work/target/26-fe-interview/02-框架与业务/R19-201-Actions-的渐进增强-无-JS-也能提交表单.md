---
title: [R19-201] Actions 的渐进增强是什么？为什么没有 JS 也能提交表单？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-201：Actions 的渐进增强是什么？为什么没有 JS 也能提交表单？
**答**：
- `<form action={serverAction}>` 编译为原生 form 的 action 属性（Server Actions 场景），HTML 原生提交不依赖 JS——断网/JS 未加载时表单仍可工作。
- JS 可用时 React 拦截提交事件，走 fetch 序列化 FormData，避免整页刷新，并获得 pending/optimistic 等能力。
- 渐进增强的实践价值：弱网首屏 JS 未就绪时用户仍能登录/搜索，核心转化链路不因 JS 失败而中断。
- 客户端 action（普通函数）同样挂在 form action 上，但无 JS 时无法执行——真正「无 JS 可用」仅限 Server Actions。
- 追问钩子：无 JS 提交后如何回显结果？依赖 redirect + revalidate 的服务端导航闭环。
