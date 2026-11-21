---
title: [TS-058] 什么是协变与逆变？TypeScript 的函数参数是逆变吗？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-058：什么是协变与逆变？TypeScript 的函数参数是逆变吗？
**答**：
- 协变：子类型关系与包装方向一致，如 `Dog[]` 可赋给 `Animal[]`，TS 的对象、数组都是协变。
- 逆变：方向相反，函数参数在 `strictFunctionTypes` 下是逆变的，`Feed<Animal>` 可赋给 `Feed<Dog>`。
- 方法简写语法（method shorthand）保持双变以兼容旧代码，属性箭头函数形式才严格逆变。
- 理解协变逆变是看懂 `subscribe`、`Map<K, V>` 型变标注（in/out）的基础。

```typescript
interface Animal {
  name: string;
}
interface Dog extends Animal {
  breed: string;
}

// 协变：数组方向一致
let dogs: Dog[] = [];
let animals: Animal[] = [];
animals = dogs; // OK

// 逆变：函数参数方向相反
type Feed<T> = (t: T) => void;

const feedAnimal: Feed<Animal> = (a) => console.log(a.name);
const feedDog: Feed<Dog> = feedAnimal; // OK：能喂所有动物就能喂狗（逆变）
// const feedAnimal2: Feed<Animal> = (d: Dog) => d.breed; // 报错：只喂狗的函数不能喂所有动物

// strictFunctionTypes 下属性形式的回调参数是逆变的
interface Handler<T> {
  handle: (t: T) => void; // 属性箭头形式：逆变
  // handle(t: T): void;  // 方法简写形式：双变（兼容旧代码）
}
```

## 第十八章 类型体操典型题
