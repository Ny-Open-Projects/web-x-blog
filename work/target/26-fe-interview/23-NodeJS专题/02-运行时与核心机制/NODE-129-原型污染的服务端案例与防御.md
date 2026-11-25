---
title: [NODE-129] 原型污染的服务端案例与防御？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-129：原型污染的服务端案例与防御？
**答**：
- 案例链路：请求体 `{"__proto__": {"isAdmin": true}}` → 被递归 merge 进对象 → `Object.prototype.isAdmin = true` → 全局所有对象 `obj.isAdmin === true` → 鉴权绕过甚至 RCE。
- 关键认知：`JSON.parse('{"__proto__":{}}')` 会产生名为 `__proto__` 的**自有属性**；递归 merge 时 `target[key]` 取到的是继承原型而非自有属性，写穿就发生在这一步。
- 防御：merge 前拦截黑名单键（`__proto__`/`constructor`/`prototype`）、只合并 plain object、用 `Map` 或 `Object.create(null)` 存动态配置。
- 纵深：升级 lodash 等已修 CVE 的版本、服务启动 `Object.freeze(Object.prototype)`、qs/query 解析库开安全选项。

```javascript
const isPlain = (v) => v !== null && typeof v === 'object'
  && !Array.isArray(v) && Object.getPrototypeOf(v) === Object.prototype;

function safeMerge(target, src) {
  for (const key of Object.keys(src)) {
    if (key === '__proto__' || key === 'constructor' || key === 'prototype') continue; // 黑名单拦截
    if (isPlain(src[key]) && isPlain(target[key])) safeMerge(target[key], src[key]);
    else target[key] = src[key];
  }
  return target;
}

// 漏洞复现（仅演示，勿用于生产）：
// merge({}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
// ({ }).isAdmin === true  → 全局污染

// 兜底加固：
Object.freeze(Object.prototype);
Object.freeze(Array.prototype);
// 动态键配置容器用无原型对象，污染原型也无济于事：
const config = Object.create(null);
```
