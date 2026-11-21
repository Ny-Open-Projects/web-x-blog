---
title: [BAS-139] 属性描述符有哪几个字段？defineProperty 怎么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-139：属性描述符有哪几个字段？defineProperty 怎么用？
**答**：
- 数据描述符四件套：value、writable（能否改值）、enumerable（能否被枚举）、configurable（能否删除或改描述符）。
- 访问器描述符是 get/set，与 value/writable 互斥，不能同时出现。
- 默认全为 false/undefined，所以 defineProperty 创建的属性默认不可枚举不可写——Vue2 响应式、JSON 序列化丢字段都与此有关。

```javascript
const o = {};
Object.defineProperty(o, 'id', {
  value: 1, writable: false, enumerable: false, configurable: false,
});
o.id = 2;                            // 静默失败（严格模式下报错）
console.log(Object.keys(o), o.id);   // [] 1 —— 不可枚举但可访问
console.log(JSON.stringify(o));      // {} —— JSON 序列化只看可枚举属性
```
