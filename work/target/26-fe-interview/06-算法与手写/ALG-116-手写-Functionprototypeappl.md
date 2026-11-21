---
title: [ALG-116] 手写 Function.prototype.apply：SDK 要把 arguments 类参数透传给目标方法，参数可能是 null 或数组类对象？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-116：手写 Function.prototype.apply：SDK 要把 arguments 类参数透传给目标方法，参数可能是 null 或数组类对象？
**答**：与 call 同源，区别只在参数是数组/类数组。要点：args 为 null/undefined 视为空参；类数组用 `Array.from` 或展开前校验 length。直接复用 myCall 展开即可，复杂度 O(n)。

```javascript
Function.prototype.myApply = function (ctx, args) {
  // args 为 null/undefined => 无参调用；类数组 => 转真数组后展开
  const list = args == null ? [] : Array.from(args);
  return this.myCall(ctx, ...list);
};
// 场景：桥接旧模块——把 arguments 原样转发给适配器
function legacyAdapter() {
  return api.invoke.myApply(adapter, arguments); // 类数组也能透传
}
// myApply({ name: 'x' }, null) 与 myApply({ name: 'x' }, []) 等价
```
