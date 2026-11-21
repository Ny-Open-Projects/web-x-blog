---
title: [R19-308] RSC payload 序列化的常见陷阱（Date/Map/循环引用）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-308：RSC payload 序列化的常见陷阱？
**答**：
- Date/Map/Set/BigInt：Flight 支持，但下游三方组件（图表库）可能不识别——传给 client 前转 ISO 字符串/普通对象更稳。
- 循环引用：Flight 能表达（引用标记），但 JSON.stringify 调试时崩——日志打印前用安全序列化。
- 类实例：原型丢失（变普通对象），方法不可调——数据层用 DTO，不用 ORM 实体直接穿透到客户端。
- NaN/Infinity：JSON 不支持，Flight 有特殊编码但下游兼容性差——序列化前归零/判空。
- 实践：在服务端组件边界统一做「可序列化整形」（serializeForClient 函数），边界即契约。
