---
title: [R19-274] RSC payload 里的 Promise 怎么传到客户端并被 use 消费？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-274：RSC payload 里的 Promise 怎么传到客户端并被 use 消费？
**答**：
- RSC 渲染时遇到异步组件返回 Promise：不等待，把「pending 的 promise 引用」序列化进 Flight 流（带流 id），继续渲染其他部分。
- 客户端反序列化时得到占位 promise，数据 chunk 到达后 resolve——客户端组件用 use(promise) 或该 promise 直接挂 Suspense。
- 流式收益：慢数据不阻塞快数据的输出，TTFB 内先看到骨架与主内容框架。
- 错误传播：服务端 promise reject → 流内错误块 → 客户端 promise reject → 客户端 ErrorBoundary。
- 面试表达：Flight 协议让「跨网络的 promise」与「本地 promise」语义一致，这是 use 设计的网络级支撑。
