---
title: [PER-083] 原型污染的攻防实例是什么？merge 函数为什么会成为漏洞？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-083：原型污染的攻防实例是什么？merge 函数为什么会成为漏洞？

**答**：
- 原型污染：攻击者通过 `{"__proto__": {"isAdmin": true}}` 这类输入，把属性写到 `Object.prototype` 上，**所有对象**凭空获得该属性，可绕过权限判断或触发 RCE（配合模板引擎/命令执行 gadget）。
- 经典漏洞模式：递归 merge/deepClone 不检查 key 名，`__proto__` 与 `constructor.prototype` 被当成普通属性赋值。
- 防御三件套：合并前用 `Object.create(null)` 的目标、**过滤危险键**（`__proto__`、`constructor`、`prototype`）、优先用 `Object.hasOwn` 判断而非 `in`（`in` 会命中原型链）。
- 解析层也要防：`JSON.parse` 本身安全，但解析结果直接进 merge 就出洞；query 解析库（qs）要开启 `allowPrototypes: false`。

```javascript
// 漏洞版 merge：__proto__ 被当普通 key 写入 Object.prototype
function vulnerableMerge(target, source) {
  for (const key in source) {
    if (typeof source[key] === 'object' && source[key] !== null) {
      if (!target[key]) target[key] = {};
      vulnerableMerge(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  }
  return target;
}
vulnerableMerge({}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
console.log(({}).isAdmin); // true —— 全局原型被污染

// 修复版：过滤危险键 + 自有属性判断
const DANGEROUS_KEYS = new Set(['__proto__', 'constructor', 'prototype']);
function safeMerge(target, source) {
  const safeTarget = Object.create(null); // 无原型目标，写不进 Object.prototype
  for (const key of Object.keys(source)) { // Object.keys 只取自有属性，不遍历原型链
    if (DANGEROUS_KEYS.has(key)) continue; // 危险键直接丢弃
    const value = source[key];
    safeTarget[key] = (value && typeof value === 'object') ? safeMerge({}, value) : value;
  }
  return Object.assign(Object.create(Object.getPrototypeOf(target)), safeTarget, target);
}
safeMerge({}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
console.log(({}).isAdmin); // undefined —— 污染被拦截
```
