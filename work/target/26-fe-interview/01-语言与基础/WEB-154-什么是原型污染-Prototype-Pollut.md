---
title: [WEB-154] 什么是原型污染（Prototype Pollution）攻击？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-154：什么是原型污染（Prototype Pollution）攻击？
**答**：
- 攻击者通过可控对象键 __proto__/constructor.prototype 篡改 Object.prototype，让所有对象"天生"带上恶意属性。
- 常见入口：深拷贝与 merge 工具（早期 lodash.merge 出过 CVE）、qs 类查询串解析、配置合并。
- 危害展开：绕过判断（isAdmin 恒真）、改变 JSON.stringify 行为、配合其他 gadget 实现执行。
- 修复：合并时过滤 __proto__、constructor、prototype 键；用 Object.create(null) 做无原型字典；Node 20+ 可 --disable-proto=throw。

```javascript
// 漏洞版 merge：__proto__ 被当作普通键写入
function unsafeMerge(target, source) {
  for (const k in source) {
    if (typeof source[k] === 'object' && source[k]) unsafeMerge(target[k] ??= {}, source[k]);
    else target[k] = source[k];
  }
  return target;
}
unsafeMerge({}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
console.log({}.isAdmin); // true，全局对象被污染

// 修复版：拦截危险键
function safeMerge(target, source) {
  const blocked = ['__proto__', 'constructor', 'prototype'];
  for (const k of Object.keys(source)) {
    if (blocked.includes(k)) continue;
    target[k] = typeof source[k] === 'object' && source[k] ? safeMerge(target[k] ?? {}, source[k]) : source[k];
  }
  return target;
}
```
