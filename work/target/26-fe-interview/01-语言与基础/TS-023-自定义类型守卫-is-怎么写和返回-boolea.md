---
title: [TS-023] 自定义类型守卫 is 怎么写？和返回 boolean 有什么区别？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-023：自定义类型守卫 is 怎么写？和返回 boolean 有什么区别？
**答**：
- 形如 `value is T` 的返回类型是类型守卫，调用后编译器按 T 收窄参数。
- 普通返回 boolean 的函数无法让编译器收窄，因为返回 true 与类型判断之间没有关联。
- 守卫函数内部依然由开发者负责保证正确性，TS 不校验实现。
- 数组 filter 配合守卫可以把 `(A | B)[]` 过滤成 `B[]`。

```typescript
interface Fish {
  swim: () => void;
}
interface Bird {
  fly: () => void;
}

function isFish(pet: Fish | Bird): pet is Fish {
  return "swim" in pet;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    pet.swim(); // 收窄为 Fish
  } else {
    pet.fly(); // 收窄为 Bird
  }
}

const zoo: (Fish | Bird)[] = [];
const fishes = zoo.filter(isFish); // Fish[]
```
