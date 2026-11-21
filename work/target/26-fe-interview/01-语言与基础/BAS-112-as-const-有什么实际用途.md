---
title: [BAS-112] as const 有什么实际用途？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-112：as const 有什么实际用途？
**答**：
- 把对象/数组断言为最深层的只读字面量类型：数组变 readonly 元组，属性值收窄为字面量（'asc' 而不是 string）。
- 典型场景：常量数组收窄后推导联合类型，替代手写枚举。
- 注意 as const 后对象整体 readonly，不能改属性、不能 push。

```typescript
const DIRS = ['asc', 'desc'] as const;
type Dir = (typeof DIRS)[number];        // 'asc' | 'desc'
const config = { api: '/api', retry: 3 } as const;
// config.retry = 5;                     // 报错：readonly
function sort(list: number[], dir: Dir) {}
sort([3, 1], 'asc');                     // 只接受两个字面量
```
