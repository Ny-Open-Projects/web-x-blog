---
title: [DP-046] Vue 响应式里的观察者：dep 和 subscriber 是什么关系？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-046：Vue 响应式里的观察者：dep 和 subscriber 是什么关系？（高频）
**答**：
- Vue2/3 响应式核心是观察者模式：每个响应式属性有一个 dep（被观察者/Subject），用到它的渲染函数/ watcher 是订阅者（Observer）。
- 流程：渲染时读取属性 → `dep.depend()` 收集当前 watcher → 属性变化 → `dep.notify()` 通知 watcher 重新渲染。
- Vue3 的 `effect` + `track/trigger` 是同一模式的现代写法（WeakMap 存储 target→key→dep）。
- 加分：computed 也是 watcher（dirty 标记惰性求值），watch 是显式订阅某个 dep。

```javascript
// Vue 风格 dep-subscriber（观察者模式直通车）
class Dep {
  #subs = new Set();
  static current = null;                 // 正在执行的订阅者
  depend() { if (Dep.current) this.#subs.add(Dep.current); } // 收集
  notify() { [...this.#subs].forEach((w) => w.update()); }   // 通知
}
class Watcher { // 订阅者
  constructor(getter, cb) {
    this.getter = getter;
    this.cb = cb;
    this.value = this.get();             // 首次求值即完成依赖收集
  }
  get() {
    Dep.current = this;                  // 打开收集开关
    const v = this.getter();
    Dep.current = null;                  // 关闭
    return v;
  }
  update() {                             // 被 dep.notify 调起
    const old = this.value;
    this.value = this.get();             // 重新求值、重新收集（依赖可能变了）
    this.cb(this.value, old);
  }
}
// 数据层：每个 key 挂一个 dep
function defineReactive(obj, key) {
  const dep = new Dep();
  let val = obj[key];
  Object.defineProperty(obj, key, {
    get() { dep.depend(); return val; },      // 读：收集当前 Watcher
    set(nv) { val = nv; dep.notify(); },      // 写：通知所有 Watcher
  });
}
const state = { count: 0 };
defineReactive(state, 'count');
// 渲染 Watcher：依赖 state.count
new Watcher(() => state.count, (nv, ov) => console.log(`视图更新 ${ov} -> ${nv}`));
state.count = 5; // 视图更新 0 -> 5 —— 全自动
```
