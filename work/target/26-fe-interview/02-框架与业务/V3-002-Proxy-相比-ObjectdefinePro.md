---
title: [V3-002] Proxy 相比 Object.defineProperty 有哪些优势？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-002：Proxy 相比 Object.defineProperty 有哪些优势？
**答**：
- defineProperty 只能劫持初始化时已存在的属性，新增/删除属性无法拦截，需要 \$set/\$delete。
- 数组索引赋值和 length 修改拦截不到，Vue2 需要重写 7 个数组方法打补丁。
- Proxy 代理整个对象，支持 13 种拦截器，还能代理 Map/Set，嵌套对象可惰性代理提升初始化性能。
- 局限：Proxy 无法 polyfill 到 IE11，所以 Vue3 放弃了 IE。

```javascript
const data = { count: 0, list: [1, 2] };

const state = new Proxy(data, {
  get(target, key, receiver) {
    track(target, key); // 依赖收集
    return Reflect.get(target, key, receiver);
  },
  set(target, key, value, receiver) {
    const result = Reflect.set(target, key, value, receiver);
    trigger(target, key); // 派发更新
    return result;
  },
});

// Proxy 的优势：新增/删除属性、数组索引、length 都能拦截
state.list.push(3); // Vue2 时代需要重写数组方法
state.newKey = 1; // Vue2 时代需要 $set
delete state.newKey; // Proxy 可拦截 deleteProperty
```
