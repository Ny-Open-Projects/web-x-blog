---
title: [JS-042] async 函数的返回值与 await 包装规则？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-042：async 函数的返回值与 await 包装规则？

**答**：
- async 函数 return 的值会被 `Promise.resolve` 包装；抛出的错误变成 rejected Promise。
- await 非 Promise 值时按该值处理，不会真的等一帧（规范上有一层 thenable 适配）。
- await thenable（带 then 方法的对象）会调用其 then。
- async 函数内部 return 另一个 Promise，最终结果以那个 Promise 的结果为准。

```javascript
async function num() { return 42; }
console.log(num() instanceof Promise); // true
num().then(console.log);               // 42

async function fail() { throw new Error('x'); }
fail().catch((e) => console.log(e.message)); // x

async function thenable() {
  return await {
    then(resolve) { setTimeout(() => resolve('thenable done'), 100); },
  };
}
thenable().then(console.log); // thenable done

async function chain() { return num(); }
chain().then(console.log); // 42，内层 Promise 被展开
```

## 六、事件循环与宏微任务
