---
title: [JS-099] 为什么 Proxy 内部必须配 Reflect？receiver 修正是关键
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-099：为什么 Proxy 内部必须配 Reflect？receiver 修正是关键

**答**：
- Proxy 的 trap 都带有 receiver 参数（最初发起访问的对象），Reflect 原样转发 receiver 才不丢信息。
- 若在 trap 里直接 `t[k]`，getter 的 this 会变成 target 而不是调用方，继承场景直接错乱。
- 典型场景：子类继承 Proxy 化的父类时，父 getter 读子类字段，只有 Reflect.get(t, k, receiver) 才能读到。
- Reflect 的方法与 trap 一一对应、返回值与操作语义一致（如 set 失败返回 false 而非抛错）。

```javascript
const parent = {
  get name() { return this._name ?? 'parent 默认值'; }, // getter 的 this 是关键
};
const child = Object.create(parent);
child._name = 'child 的值';

// 直接调用：getter 的 this 是 parent，读不到 child 的字段
console.log(Reflect.get(parent, 'name'));            // parent 默认值
// 传入 receiver：this 被修正为 child
console.log(Reflect.get(parent, 'name', child));     // child 的值

// 错误的 Proxy 写法：丢 receiver
const broken = new Proxy(parent, {
  get(t, k) { return t[k]; },                        // this 变成 t（parent）
});
const c1 = Object.create(broken);
c1._name = 'ok';
console.log(c1.name); // parent 默认值 — 错了

// 正确写法：Reflect 透传 receiver
const fixed = new Proxy(parent, {
  get(t, k, receiver) { return Reflect.get(t, k, receiver); },
});
const c2 = Object.create(fixed);
c2._name = 'ok';
console.log(c2.name); // ok — this 正确指向 c2
```
