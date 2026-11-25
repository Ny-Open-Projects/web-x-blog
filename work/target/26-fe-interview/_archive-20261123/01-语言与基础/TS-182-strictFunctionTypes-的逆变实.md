---
title: [TS-182] strictFunctionTypes 的逆变实践有哪些案例？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-182：strictFunctionTypes 的逆变实践有哪些案例？
**答**：
- 开启后"函数类型位置"的参数检查变为逆变：参数更宽的函数才能赋给参数更窄的签名。
- 方法简写（`handle(e: X): void`）出于历史兼容仍是双变，属性签名（`onClick: (e: X) => void`）才受严格检查。
- React 事件 Props 用属性签名才能获得完整检查；可变数组的元素赋值仍是已知妥协点。

```typescript
// strictFunctionTypes: true
interface Handler { (e: string | number): void }

declare const broad: (e: string | number) => void;
declare const narrow: (e: string) => void;

let h1: Handler = broad;  // ✅ 逆变：参数更宽的可以给更窄的
let h2: Handler = narrow; // ❌ 报错：narrow 处理不了 number，运行时会炸

// 方法简写 vs 属性签名
type Props = { onClick: (e: React.MouseEvent) => void }; // 属性签名：严格逆变检查
type Bad  = { onClick(e: React.MouseEvent): void };      // 方法简写：双变，检查放松

// 实践规范：回调一律用属性箭头签名声明，别用方法简写骗过检查
```
