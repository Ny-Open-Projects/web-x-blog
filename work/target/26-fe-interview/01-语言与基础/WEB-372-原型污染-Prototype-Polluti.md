---
title: [WEB-372] 原型污染（Prototype Pollution）是什么？前端有什么风险？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 笔试题
---

## WEB-372：原型污染（Prototype Pollution）是什么？前端有什么风险？
**答**：
- 合并/深拷贝/qs 解析用户输入时，__proto__/constructor.prototype 作为 key 写入，污染 Object.prototype → 全局属性被改。
- 前端风险：qs 库解析 ?__proto__[x]=1 类参数、路由参数合并、localStorage 配置反序列化都可能触发；污染可导致 XSS（改 innerHTML 相关逻辑）或逻辑绕过。
- 防御：合并时跳过 __proto__/constructor 键；用 Object.create(null) 字典；现代 qs/lodash 已修，但仍要警惕自写 merge。

```javascript
const badMerge = (dst, src) => {
  for (const k in src) {
    if (typeof src[k] === 'object') badMerge(dst[k] ??= {}, src[k]);
    else dst[k] = src[k];
  }
  return dst;
};
// 攻击: badMerge({}, JSON.parse('{"__proto__":{"isAdmin":true}}'))
const safeMerge = (dst, src) => {
  for (const k of Object.keys(src)) {
    if (['__proto__', 'constructor', 'prototype'].includes(k)) continue;
    dst[k] = src[k];
  }
  return dst;
};
console.log(({}).isAdmin, safeMerge({}, JSON.parse('{"__proto__":{"x":1}}')));
```

**评分点**：
- 结论先行，机制一句话讲透
- 覆盖攻击面/异常分支与边界条件
- 代码可运行、命名清晰、有防御性处理
- 主动给出工程取舍与常见坑
