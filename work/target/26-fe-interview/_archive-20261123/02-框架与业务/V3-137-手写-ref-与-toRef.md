---
title: [V3-137] 手写 ref 与 toRef？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-137：手写 ref 与 toRef？
**答**：
- RefImpl 类：`_value` 存 .value 的实际值（对象要 reactive 转换），dep 是收集 effect 的 Set。
- get value 时 track，set value 时用 Object.is 与原始值比较，相等不触发，这就是 ref 默认浅比较的来源。
- toRef 是"引用桥"：不复制值，get/set 直接转发到源对象，与 reactive 数据天然同步。
- shallowRef 即 `_value` 直接存原值不做深层转换；toRefs 就是把对象每个 key 都 toRef 一遍。

```javascript
// mini-ref.js
let activeEffect = null;
const isObject = (v) => typeof v === "object" && v !== null;

function reactive(obj) {
  return new Proxy(obj, {
    get(target, key) {
      track(target, key);
      return Reflect.get(target, key);
    },
    set(target, key, value) {
      Reflect.set(target, key, value);
      trigger(target, key);
      return true;
    },
  });
}
function track(target, key) { /* 同 V3-136，此处省略 */ }
function trigger(target, key) { /* 同 V3-136，此处省略 */ }

class RefImpl {
  constructor(value, shallow = false) {
    this._raw = value; // 原始值，用于相等比较
    this._value = shallow ? value : isObject(value) ? reactive(value) : value;
    this.dep = new Set();
  }
  get value() {
    if (activeEffect) this.dep.add(activeEffect); // track
    return this._value;
  }
  set value(newVal) {
    if (Object.is(newVal, this._raw)) return; // 值相等不触发
    this._raw = newVal;
    this._value = isObject(newVal) ? reactive(newVal) : newVal;
    [...this.dep].forEach((fn) => (fn.scheduler || fn.run)()); // trigger
  }
}

const ref = (v) => new RefImpl(v);
const shallowRef = (v) => new RefImpl(v, true);

// toRef：桥接对象，读写全部转发到源对象
function toRef(source, key) {
  return {
    get value() {
      if (activeEffect) track(source, key); // 依赖收集落到源对象上
      return source[key];
    },
    set value(newVal) {
      source[key] = newVal; // 写回源对象，触发源对象的 trigger
    },
  };
}
const toRefs = (obj) => Object.fromEntries(Object.keys(obj).map((k) => [k, toRef(obj, k)]));

// 验证
const state = reactive({ n: 1 });
const nRef = toRef(state, "n");
nRef.value++;                   // 等价于 state.n++
console.log(state.n, nRef.value); // 2 2

const count = ref({ list: [] });
count.value.list.push(1);       // 对象内部被 reactive 包装，深层修改也响应
```
