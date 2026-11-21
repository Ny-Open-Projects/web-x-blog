---
title: [TS-193] 如何实现 DeepMerge 类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-193：如何实现 DeepMerge 类型？
**答**：
- 键集合取 `keyof A | keyof B`，同名键双存在且两边都是对象时递归合并，否则取 B（后写覆盖）。
- 数组按"整体覆盖"处理（B 的数组直接替换 A），需要按下标合并时另扩展分支。
- 合并前先把入参 Prettify 拍平，交叉类型参与键集合运算更可预测。

```typescript
type DeepMerge<A, B> = {
  [K in keyof A | keyof B]: K extends keyof B
    ? K extends keyof A
      ? A[K] extends object
        ? B[K] extends object
          ? DeepMerge<A[K], B[K]>
          : B[K]
        : B[K]
      : B[K]
    : K extends keyof A ? A[K] : never;
};

type Defaults = { api: { base: string; timeout: number }; retries: number };
type UserCfg  = { api: { timeout: 5000 }; retries: 3 };

type Cfg = DeepMerge<Defaults, UserCfg>;
// { api: { base: string; timeout: 5000 }; retries: 3 }
// —— 同名对象键递归合并，标量键取用户配置覆盖默认值
```
