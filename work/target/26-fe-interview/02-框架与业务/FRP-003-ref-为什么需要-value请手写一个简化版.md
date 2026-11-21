---
title: [FRP-003] ref 为什么需要 .value？请手写一个简化版 ref。
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-003：ref 为什么需要 .value？请手写一个简化版 ref。

**答**：
- Proxy 的 get/set 拦截只能代理**对象**，无法拦截对原始值（number/string）属性的读写；`ref` 用一个 `{ value }` 包装对象让原始值也能被代理。
- 读取 `ref.value` 触发 getter 收集依赖，赋值触发 setter 派发更新——`.value` 就是那个被拦截的属性。
- 直接解构 `const { value } = ref` 后得到的原始值脱离了拦截，响应性丢失，这正是"响应式丢失"问题的根源之一。
- 源码里 RefImpl 用 class + get/set 访问器实现，比 Proxy 更轻；`reactive` 对象赋值给 ref 时会内部再走 `toReactive` 深层代理。

```javascript
// 简化实现，帮助理解 ref 的 .value 本质
let activeEffect = null;
function effect(fn) {
  activeEffect = fn;
  fn();
  activeEffect = null;
}

class RefImpl {
  constructor(rawValue) {
    this._rawValue = rawValue;
    this._value = rawValue;
    this.dep = new Set(); // ref 不需要 targetMap，一个 ref 一份依赖即可
  }
  get value() {           // 读 .value 时收集依赖
    if (activeEffect) this.dep.add(activeEffect);
    return this._value;
  }
  set value(newValue) {   // 写 .value 时派发更新
    if (newValue === this._rawValue) return; // 简化用 ===；源码（hasChanged）用 Object.is，NaN 场景行为不同
    this._rawValue = newValue;
    this._value = newValue;
    this.dep.forEach((effect) => effect());
  }
}

function ref(raw) {
  return new RefImpl(raw);
}

const count = ref(0);
effect(() => console.log('count is', count.value)); // count is 0
count.value++;                                      // count is 1
// 若写成 const { value } = count; 则 value 是裸数字，改动不会再触发更新
```
