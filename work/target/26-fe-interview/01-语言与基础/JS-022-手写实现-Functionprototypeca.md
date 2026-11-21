---
title: [JS-022] 手写实现 Function.prototype.call？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-022：手写实现 Function.prototype.call？

**答**：
- 核心思路：把函数临时挂到目标对象上，借助隐式绑定调用后再删除。
- context 为 null/undefined 时指向全局对象（严格模式则传什么用什么）。
- 用 `Symbol` 避免属性名冲突，展开 rest 参数逐个传入。
- 返回值需要透传函数的执行结果。

```javascript
Function.prototype.myCall = function (context, ...args) {
  context = context ?? globalThis;            // 处理 null/undefined
  context = Object(context) ?? globalThis;    // 原始值包装为对象
  const key = Symbol('fn');
  context[key] = this;                        // this 是被调用的函数
  const result = context[key](...args);       // 隐式绑定
  delete context[key];
  return result;
};

function intro(city, job) {
  return `${this.name} - ${city} - ${job}`;
}
console.log(intro.myCall({ name: 'Tom' }, 'BJ', 'FE')); // Tom - BJ - FE
```
