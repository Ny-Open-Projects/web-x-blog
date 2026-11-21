---
title: [JS-313] 笔试：手写 call/apply
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 函数]
type: 笔试题
---

## JS-313：笔试：手写 call 与 apply

**题目**：手写 `myCall` 与 `myApply`：this 绑定（含 null/undefined 回退全局、原始值包装）；参数透传；返回值透传；不使用内置 call（可用简写场景豁免）。

**答**：
```javascript
Function.prototype.myCall = function (ctx, ...args) {
  // 原始值包装成对象；null/undefined → 全局（严格模式例外）
  const thisArg = ctx == null ? globalThis : Object(ctx);
  // 用 Symbol 防止覆盖同名属性
  const key = Symbol('fn');
  thisArg[key] = this;               // 函数挂到目标上成为其方法
  try {
    return thisArg[key](...args);    // 方法调用 → this 指向 thisArg
  } finally {
    delete thisArg[key];             // 清理痕迹
  }
};

Function.prototype.myApply = function (ctx, args = []) {
  const thisArg = ctx == null ? globalThis : Object(ctx);
  const key = Symbol('fn');
  thisArg[key] = this;
  try { return thisArg[key](...args); } finally { delete thisArg[key]; }
};

function greet(a, b) { return `${this.name}:${a}-${b}`; }
greet.myCall({ name: 'A' }, 1, 2);   // 'A:1-2'
greet.myApply({ name: 'B' }, [3, 4]); // 'B:3-4'
greet.myCall(null, 1, 2);            // 'undefined:1-2'（this → globalThis）
```

**评分点**：
- 「挂临时属性 → 方法调用」的实现原理——核心
- Symbol 防覆盖与 finally 清理
- null/undefined → globalThis、原始值 Object() 包装
- 返回值透传；call 与 apply 的参数差异
