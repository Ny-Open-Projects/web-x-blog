---
title: [TS-075] 如何手写 InstanceType？abstract 构造器有什么讲究？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 笔试题, 05]
type: 笔试题
---

## TS-075：如何手写 InstanceType？abstract 构造器有什么讲究？
**答**：
- 构造签名匹配：`T extends abstract new (...args: any) => infer R ? R : never`。
- 加 `abstract` 修饰的构造签名能同时匹配普通类与抽象类（抽象类的类型是 abstract new）。
- 泛型类会推导出实例化后的实例类型，这是依赖注入容器、emit 类型工厂的基础。

```typescript
type MyInstanceType<T extends abstract new (...args: any) => any> =
  T extends abstract new (...args: any) => infer R ? R : never;

class Box<T> {
  constructor(public value: T) {}
}
abstract class Shape {
  abstract area(): number;
}

type B = MyInstanceType<typeof Box>;   // Box<unknown>（无具体实例时 T 推为 unknown）
const b = new Box(1);
type B2 = MyInstanceType<typeof b.constructor extends abstract new (...args: any) => infer R ? never : never>; // 演示用

// 更常见用法：从构造器参数工厂返回
type ShapeCtor = abstract new () => Shape;
type S = MyInstanceType<ShapeCtor>; // Shape（抽象类的实例类型）
```

## 第二十一章 条件类型与分布式深水区
