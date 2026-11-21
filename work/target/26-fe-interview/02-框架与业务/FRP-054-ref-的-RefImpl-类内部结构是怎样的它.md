---
title: [FRP-054] ref 的 RefImpl 类内部结构是怎样的？它和 Dep 类如何配合？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-054：ref 的 RefImpl 类内部结构是怎样的？它和 Dep 类如何配合？

**答**：
- `ref(v)` 返回一个 **RefImpl 实例**：`_value`（若 v 是对象则被 reactive 包装）、`dep`（一个 Dep 实例，替代了 reactive 中按 key 组织的 Map）、以及 `__v_isRef = true` 标记。
- 依赖收集挂在 **getter `value`** 上：访问 `.value` 时 `dep.track()`；修改时 setter 先 `hasChanged` 比较（`Object.is`），变化才更新 `_value` 并 `dep.trigger()`。
- Dep 类把"订阅者集合 + track/trigger"封装成独立单元（Vue3.4+ 中 Dep 还会链到全局 activeSub 栈），ref 不需要 Proxy，因为只有一个"value"属性。
- 这解释了两个常见现象：解构 ref 会丢失响应性（丢的是 RefImpl 对象本身）、模板里自动脱 ref 是编译期加了 `.value`。

```javascript
// 简化实现，帮助理解 RefImpl 与 Dep 类
let activeEffect = null;

class Dep {
  constructor() { this.subs = new Set(); } // 订阅该 dep 的 effect 集合
  track() {
    if (activeEffect) this.subs.add(activeEffect);
  }
  trigger() {
    [...this.subs].forEach((eff) => eff());
  }
}

class RefImpl {
  constructor(value) {
    this._value = isObject(value) ? reactive(value) : value; // 对象值深层代理
    this.dep = new Dep();       // 每个 ref 自带一个 dep
    this.__v_isRef = true;
  }
  get value() {
    this.dep.track();           // 读 .value 才收集
    return this._value;
  }
  set value(newVal) {
    if (Object.is(newVal, this._value)) return; // hasChanged 短路
    this._value = isObject(newVal) ? reactive(newVal) : newVal;
    this.dep.trigger();
  }
}

function ref(value) { return new RefImpl(value); }
function isRef(v) { return !!(v && v.__v_isRef); }

// 验证：改 count.value 触发依赖它的 effect
const count = ref(0);
effect(() => console.log('count =', count.value)); // count = 0
count.value = 1;                                   // count = 1
count.value = 1;                                   // 无输出（Object.is 相同值短路）
```
