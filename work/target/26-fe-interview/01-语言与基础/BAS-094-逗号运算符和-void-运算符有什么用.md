---
title: [BAS-094] 逗号运算符和 void 运算符有什么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-094：逗号运算符和 void 运算符有什么用？
**答**：
- 逗号运算符依次求值、返回最后一个：常用于 for 循环多变量更新和压缩代码；箭头函数里 `(侧效果(), 返回值())` 是惯用技巧。
- void 后跟任意表达式都返回 undefined，经典用途 `href="javascript:void(0)"` 和获取纯 undefined（void 0）。
- 两者优先级都极低，容易出歧义，业务代码应克制使用。

```javascript
const log = [];
const step = (x) => (log.push(x), x);   // 先执行 push，再返回 x
console.log(step(1) + step(2), log);    // 3 [1, 2]
console.log(void 0 === undefined);      // true
console.log((1, 2, 3));                 // 3，取最后一个
```

## 十一、DOM 与事件补充
