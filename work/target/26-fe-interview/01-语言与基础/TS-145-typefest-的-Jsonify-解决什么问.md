---
title: [TS-145] type-fest 的 Jsonify 解决什么问题？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-145：type-fest 的 Jsonify 解决什么问题？
**答**：
- 把任意类型转成"JSON.stringify 往返之后"的形状：Date→string、bigint/symbol/Function 消失、方法剔除、嵌套递归。
- 用途：给 fetch 响应、postMessage 载荷标注真实线上类型，而不是"接口文档里的理想类型"。
- 生产版还处理 toJSON() 方法、readonly 数组、索引签名，思路一致。

```typescript
// type-fest Jsonify 思路版
type Jsonify<T> = T extends bigint | symbol ? never
  : T extends Date ? string
  : T extends (infer U)[] ? Jsonify<U>[]
  : T extends object
    ? { [K in keyof T as T[K] extends Function ? never : K]: Jsonify<T[K]> }
    : T;

interface ApiModel {
  id: bigint;
  createdAt: Date;
  save(): void;
  tags: string[];
}

type Wire = Jsonify<ApiModel>;
// { tags: string[] } —— id 为 never、方法被剔除、Date 变 string
// 与 JSON.parse(JSON.stringify(model)) 后的真实形状一致，fetch 断言不再撒谎
const wire = (await res.json()) as Jsonify<ApiModel>;
```
