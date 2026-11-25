---
title: [ZSM-068] TanStack Query 对 queryKey 的深比较是怎么做的？对象键序不同算同一个 key 吗？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-068：TanStack Query 对 queryKey 的深比较是怎么做的？对象键序不同算同一个 key 吗？
**答**：
- 算同一个：Query 把 key 做 JSON 稳定序列化（对象键排序后序列化成哈希），`['a', {x:1, y:2}]` 与 `['a', {y:2, x:1}]` 命中同一缓存。
- 比较是结构化的：数组按位置、对象按键、原始值按值；undefined 会丢失，敏感字段别依赖 undefined（写成显式 null 更稳）。
- 推论：key 里传对象没问题，但**值类型要稳定**——`page: 1` 与 `page: '1'` 是两个缓存，分页参数统一数字。
- 这也是 key 里不能放函数/类实例的原因：无法稳定序列化，每次都生成新哈希。

```javascript
// 以下命中同一缓存
useQuery({ queryKey: ['goods', { page: 1, kw: '手机' }], queryFn: f })
useQuery({ queryKey: ['goods', { kw: '手机', page: 1 }], queryFn: f })

// 以下不命中（类型不同）
useQuery({ queryKey: ['goods', { page: '1' }], queryFn: f }) // page 字符串

// undefined 陷阱
queryKey: ['goods', { cursor: undefined }] // 序列化后 cursor 消失
```
