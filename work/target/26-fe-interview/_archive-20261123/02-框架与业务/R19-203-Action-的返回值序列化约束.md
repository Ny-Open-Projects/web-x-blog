---
title: [R19-203] Server Action 的返回值有哪些序列化约束？函数/Map/Date 会怎样？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-203：Server Action 的返回值有哪些序列化约束？
**答**：
- Server Action 参数与返回值走 RSC 序列化（Flight 协议）：支持 JSON 可序列化类型 + Flight 扩展（Promise、Map、Set、Date、BigInt、循环引用、原实例引用）。
- 不支持：类实例方法（会丢原型）、Symbol、DOM 节点、Stream 对象直接透传。
- 返回 Promise 可以：客户端拿到的是真实 Promise，throw 的错误边界照常工作。
- 约束实践：返回「纯数据 + 轻量错误码」而非自定义 Error 类实例；大对象考虑拆字段或分页。
- 调试：序列化失败通常报 "Only plain objects..." 类错误，检查是否在闭包里返回了函数或类实例。
