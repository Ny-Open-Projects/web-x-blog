---
title: [FRP-004] shallowRef 为什么快？triggerRef 是如何工作的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-004：shallowRef 为什么快？triggerRef 是如何工作的？

**答**：
- `reactive`/深 ref 在首次访问每个嵌套属性时都会递归创建 Proxy——10 万条列表数据初始化要做 10 万次代理，成本可观。
- `shallowRef` 只对 `.value` **整体**做响应式：读 `.value` 收集、换 `.value` 引用触发；内部属性改动完全不可见，因此跳过全部深层代理。
- 代价：直接修改 `rows.value[3].name = x` 不会触发更新，必须整体替换引用，或改完调 `triggerRef()` 强制派发。
- 这就是大数据量列表"shallowRef + 整体替换"优化（12 章 OPT-038）的原理基础。

```javascript
// 简化实现，帮助理解 shallowRef 与 triggerRef
let activeEffect = null;
function effect(fn) {
  activeEffect = fn;
  fn();
  activeEffect = null;
}

class ShallowRefImpl {
  constructor(value) { this._value = value; this.dep = new Set(); this._force = false; }
  get value() {
    if (activeEffect) this.dep.add(activeEffect);
    return this._value;
  }
  set value(newVal) {
    this._value = newVal;
    this.dep.forEach((e) => e()); // 只有整体替换 .value 才触发
  }
}

function shallowRef(v) { return new ShallowRefImpl(v); }
function triggerRef(r) { r.dep.forEach((e) => e()); } // 强制派发：配合原地修改使用

const list = shallowRef([{ id: 1, done: false }]);

effect(() => console.log('done?', list.value[0].done));

list.value[0].done = true;   // 不会触发！内部属性改动不可见
triggerRef(list);            // 手动派发，打印 done? true
list.value = [{ id: 1, done: false }]; // 整体替换，触发更新
```

**追问**：

1. `shallowRef` 包一个大对象，改外层属性为什么也不触发？→ 它只代理 `.value` 这一个访问点，对象内部任何层级都不在依赖收集范围，改属性必须手动 `triggerRef` 或整体换引用。
2. 调了 `triggerRef` 视图还是没更新，通常是什么原因？→ 组件在 render 期间没读过这个 ref（只在事件里读），依赖没被 track，派发再多次也没有订阅者；另一个原因是同 tick 内被批处理合并，要 `await nextTick()` 后再看。
3. `shallowRef` 和 `markRaw` 存第三方实例有什么区别？→ `markRaw` 是让对象彻底不被代理、且不可逆，`shallowRef` 仍然参与依赖收集、整体替换时能触发更新，存 ECharts 实例并需要换图时应选后者。
