---
title: [TS-129] 循环引用导致的 interface 报错如何排查？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-129：循环引用导致的 interface 报错如何排查？
**答**：
- 典型报错："'X' circularly references itself" 或 "'X' implicitly has type 'any' because it does not have a type annotation and is referenced directly or indirectly in its own initializer"。
- interface 声明是惰性解析的，属性里引用自己/对方通常没问题；真正的循环来自：type alias 的立即求值（如 type A = B & ... 相互展开）、模块 import 形成环、const 初始化依赖自身推断。
- 排查手段：把 type alias 换成 interface（属性位置可以引用环）、把相互引用抽到公共文件打破模块环、给常量显式标注类型切断推断环。

```typescript
// 反例一：type alias 自循环立即求值，报 circularly references itself
// type Json = string | number | Json[] | { [k: string]: Json }; // 需要用 interface 打破

// 正解：interface 属性位置允许引用自身
interface Json {
  value: string | number | boolean | Json[] | { [k: string]: Json };
}

// 反例二：推断环
// const config = { port: config.port || 8080 }; // 报错：初始化器引用自身
// 正解：显式标注
const config: { port: number } = { port: 8080 };

// 反例三：模块环 a.ts import b.ts，b.ts import a.ts，且双方在顶层就使用对方类型求值
// 正解：类型互引时尽量用 interface（惰性），或把共享类型抽到 types.ts
```
