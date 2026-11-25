---
title: [R19-298] RSC/SSR 错误的上报与 source map 还原怎么做？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-298：RSC/SSR 错误上报与还原？
**答**：
- 服务端错误：Next 的 onError（renderToPipeableStream）与全局 uncaughtException 捕获，上报（requestId + route + 堆栈）到 APM。
- source map：构建产物带 map 但不下发浏览器（防源码泄露），错误还原在服务端用 stacktrace-parser + sourcemap 离线还原。
- 客户端 chunk 错误：Sentry 类工具配 release 版本 + artifact 上传自动还原。
- 边界错误（ErrorBoundary）同样上报：带 route/边界位置。
- 脱敏：上报前抹用户数据字段；堆栈截断防超大 payload。
