---
title: [V3-006] ref 为什么需要 .value？它和 reactive 的本质区别是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-006：ref 为什么需要 .value？它和 reactive 的本质区别是什么？
**答**：
- Proxy 只能代理对象，无法代理基本类型，所以 ref 把值包装成 RefImpl 对象。
- RefImpl 内部通过 class 的 value getter/setter 实现 track/trigger，这就是必须 `.value` 的原因。
- 对象类型的 ref 内部会调用 reactive 做深层转换，读 `.value` 得到的是代理对象。
- reactive 是对象的 Proxy 代理，ref 是"带响应式的容器"，模板中 ref 会被自动解包所以不用写 value。

```javascript
import { ref, reactive } from "vue";

// RefImpl 内部大致是：
// get value() { track(this, 'value'); return this._value }
// set value(v) { this._value = v; trigger(this, 'value') }
const count = ref(0);
count.value++; // 通过 .value 触发依赖收集与派发

// 对象类型的 ref 内部会调用 reactive 深度转换
const state = ref({ list: [] });
state.value.list.push(1); // 内部是 reactive 对象，深层也是响应式

// reactive 对象解构会丢失响应式，ref 不会
const obj = reactive({ a: 1, b: 2 });
// const { a } = obj; // a 失去响应式
```
