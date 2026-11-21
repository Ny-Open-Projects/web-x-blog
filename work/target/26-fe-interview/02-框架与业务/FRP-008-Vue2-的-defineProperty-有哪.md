---
title: [FRP-008] Vue2 的 defineProperty 有哪些缺陷？Vue3 的 Proxy 如何解决？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-008：Vue2 的 defineProperty 有哪些缺陷？Vue3 的 Proxy 如何解决？

**答**：
- defineProperty 只能劫持**已知属性**：新增/删除属性（`Vue.set/Vue.delete` 的由来）、数组索引赋值与 length 修改都监听不到（Vue2 要重写 7 个数组方法打补丁）。
- 初始化时需要**递归遍历**所有属性做劫持（data 定义多大就多大开销）；Proxy 是访问时才代理（lazy），按需触发。
- defineProperty 无法拦截 Map/Set、无法监听属性访问（Proxy 的 get 可以，这让依赖收集更精确）。
- 代价：Proxy 无法 polyfill 到 IE11，这是 Vue3 放弃 IE 支持的直接原因。

```javascript
// 一一对应：defineProperty 的三个经典缺陷
const data = { list: [1, 2, 3] };

function defineReactive(obj, key) {
  let val = obj[key];
  Object.defineProperty(obj, key, {
    get() { console.log('get', key); return val; },
    set(newVal) {
      console.log('set', key, newVal);
      val = newVal;
    },
  });
}
Object.keys(data).forEach((k) => defineReactive(data, k));

// 缺陷 1：已有属性可以监听
data.list = [1, 2, 3];        // set list 被打印

// 缺陷 2：新增属性监听不到 —— Vue2 需要 Vue.set
data.newProp = 1;             // 没有任何输出，视图不更新

// 缺陷 3：数组索引与 length 监听不到 —— Vue2 重写 push 等方法兜底
data.list[0] = 99;            // 没有任何输出

// Vue3 Proxy 全部解决：
const p = new Proxy(data, {
  get: (t, k) => (console.log('get', k), t[k]),
  set: (t, k, v) => (console.log('set', k, v), (t[k] = v), true),
  deleteProperty: (t, k) => (delete t[k], true), // 删除也能监听
});
p.newProp = 1;    // set newProp 1
p.list[0] = 99;   // get list（数组内部变化由深层 reactive 代理）
```

## 二、Vue 更新机制与编译优化
