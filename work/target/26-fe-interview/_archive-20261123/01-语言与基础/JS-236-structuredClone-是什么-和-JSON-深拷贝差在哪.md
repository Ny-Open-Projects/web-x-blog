---
title: [JS-236] structuredClone 是什么：和 JSON 深拷贝差在哪
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-236：structuredClone 与 JSON 深拷贝的差异

**答**：
- structuredClone（ES2022 引入浏览器/Node 17+）：结构化克隆算法——Date/RegExp/Map/Set/ArrayBuffer/循环引用都正确处理
- JSON.parse(JSON.stringify()) 的失败清单：丢失函数/undefined/Symbol、Date 变字符串、NaN→null、循环引用直接报错、丢失原型
- structuredClone 仍不支持的：函数、DOM 节点、Symbol 属性、Error 的自定义消息部分保留但栈不复制
- 性能：structuredClone 走引擎内置快路径；JSON 方案两趟序列化解析更慢
- 需要拷贝函数/类实例行为时：仍需手写深拷贝（保留原型与函数）

```javascript
const src = { t: new Date(), m: new Map([['a', 1]]), self: null };
src.self = src;                                  // 循环引用
const c = structuredClone(src);                  // ✅ 全部正确
const bad = JSON.parse(JSON.stringify(src));     // ❌ Date 变字符串、Map 变 {}、循环报错
```
