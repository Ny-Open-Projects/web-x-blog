---
title: [R19-207] Actions 的错误处理：ErrorBoundary 与 useActionState 的双通道怎么分工？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-207：Actions 的错误处理：ErrorBoundary 与 useActionState 的双通道怎么分工？
**答**：
- useActionState 通道：action 返回错误对象（业务错误：校验失败、库存不足），state 更新驱动 UI 展示，页面不崩。
- ErrorBoundary 通道：action throw（程序错误、服务端 5xx）冒泡为渲染错误，被最近的边界捕获渲染兜底 UI。
- 规范：预期内错误用返回值、预期外错误才 throw——避免把「手机号格式错」throw 成白屏。
- Server Action throw 的错误在生产环境会被脱敏（不泄露堆栈），需在服务端日志记录完整信息。
- 组合：action 返回 { ok, code } + 边界兜底「网络层失败」，两层都有 UI。
