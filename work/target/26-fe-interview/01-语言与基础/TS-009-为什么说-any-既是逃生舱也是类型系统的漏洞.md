---
title: [TS-009] 为什么说 any 既是逃生舱也是类型系统的漏洞？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-009：为什么说 any 既是逃生舱也是类型系统的漏洞？
**答**：
- `any` 会跳过所有类型检查：任意属性访问、任意赋值、任意调用都不报错。
- `any` 具有传染性：一个 any 参与运算或赋值后，下游类型全部退化为 any。
- 会静默掩盖拼写错误、空指针等问题，把错误推迟到运行时。
- 代码审查中应把 any 视为待消除项，不可信数据优先用 `unknown`。

```typescript
let anything: any = "hello";
anything.foo.bar; // 不报错，运行时才炸
anything = 42;

// any 具有传染性
const list: any[] = JSON.parse("[1,2,3]");
const first = list[0]; // any：后续全部失去检查
```
