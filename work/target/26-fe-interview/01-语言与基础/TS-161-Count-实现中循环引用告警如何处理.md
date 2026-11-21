---
title: [TS-161] Count 实现中循环引用告警如何处理？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-161：Count 实现中循环引用告警如何处理？
**答**：
- 报错 `Type alias X circularly references itself`：type alias 的立即求值位置（数组字面量、索引访问直引）不允许自引。
- 正解一：泛型引用是惰性的（`Array<Json>` 可以，`Json[]` 不行）；正解二：累加器走参数位，结果只在基线处求值；正解三：interface 属性位惰性。
- 递归结果"又当作类型参数立即展开"是最常见的触发写法。

```typescript
// ❌ 立即求值自引：数组字面量 Json[]
// type Json = string | Json[];

// ✅ 泛型引用惰性
type Json = string | number | boolean | null | Array<Json> | { [k: string]: Json };

// ❌ 结果类型立即依赖未完成的自己（把递归结果直接嵌进元组求值）
// 部分写法会触发 circularly references itself

// ✅ Count 的安全写法：累加器走参数位（惰性），基线处才求 length
type Count<T extends unknown[], Acc extends unknown[] = []> =
  T extends [any, ...infer R] ? Count<R, [unknown, ...Acc]> : Acc["length"];
type N = Count<[1, 2, 3]>; // 3

// 排查三板斧（同 TS-129）：换 interface、改泛型引用、抽公共文件断环
```
