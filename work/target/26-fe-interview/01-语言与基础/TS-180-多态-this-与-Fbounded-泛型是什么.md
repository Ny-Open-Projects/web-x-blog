---
title: [TS-180] 多态 this 与 F-bounded 泛型是什么关系？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-180：多态 this 与 F-bounded 泛型是什么关系？
**答**：
- 多态 this：类方法返回 `this`，编译期代表"当前调用者的精确类型"，子类自动获得。
- F-bounded 泛型：把"返回/接收自身子类"显式化为 `<S extends Base>(s: S) => S`，适合静态方法与工厂函数。
- 典型收益：`new Circle().setFill("red").setRadius(2)` 链式后类型仍是 Circle，而不是塌缩回 Shape。

```typescript
class Shape {
  setFill(color: string): this {
    return this;
  }
}

class Circle extends Shape {
  setRadius(r: number): this {
    return this;
  }
}

const c = new Circle().setFill("red").setRadius(2); // Circle —— 若返回写 Shape 则 setRadius 丢失

// F-bounded 泛型：等价能力的显式形式，适合函数场景
function styled<S extends Shape>(s: S): S {
  return s;
}
const c2 = styled(new Circle()).setRadius(3); // Circle

// 坑：this 类型不能出现在"返回 this 的对象被存起来再调用"之外的复杂位置，
// 序列化/深拷贝后类型信息自然丢失，需重新断言
```
