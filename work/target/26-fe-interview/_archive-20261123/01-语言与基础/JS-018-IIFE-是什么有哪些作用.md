---
title: [JS-018] IIFE 是什么？有哪些作用？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-018：IIFE 是什么？有哪些作用？

**答**：
- 立即执行函数：`(function () { ... })()`，定义即执行，常见写法还有 `!function(){}()`。
- 作用一：创建独立作用域，避免污染全局（ES5 时代的模块雏形）。
- 作用二：解决循环中闭包捕获问题（把循环变量按值固化）。
- 作用三：配合返回对象暴露接口，实现 reveal module 模式。

```javascript
// 模块模式
const counterModule = (function () {
  let count = 0; // 私有
  function increment() { count += 1; }
  function getCount() { return count; }
  return { increment, getCount }; // 只暴露接口
})();
counterModule.increment();
console.log(counterModule.getCount()); // 1

// 异步环境隔离 await
(async () => {
  const res = await fetch('/api/user');
  console.log(await res.json());
})();
```

## 三、this 与 call/apply/bind
