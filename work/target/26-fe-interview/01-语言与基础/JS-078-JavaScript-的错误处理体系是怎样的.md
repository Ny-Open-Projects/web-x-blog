---
title: [JS-078] JavaScript 的错误处理体系是怎样的？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-078：JavaScript 的错误处理体系是怎样的？

**答**：
- 内置错误类型：Error、TypeError、RangeError、ReferenceError、SyntaxError、URIError。
- `throw` 可抛任意值，但规范只抛 Error 实例（保留 stack 与 cause）。
- try/catch/finally：finally 总是执行，且其 return 会覆盖 try 的返回。
- 异步错误要分场景：Promise 用 catch，async/await 用 try/catch，回调式错误约定 error-first 参数。

```javascript
function parseJSON(json) {
  try {
    return JSON.parse(json);
  } catch (err) {
    throw new Error(`invalid json: ${err.message}`, { cause: err });
  }
}

try {
  parseJSON('{bad}');
} catch (e) {
  console.log(e instanceof Error, e.cause instanceof SyntaxError); // true true
} finally {
  console.log('cleanup always runs');
}

// finally 覆盖 return（了解即可）
function finallyReturn() {
  try { return 'try'; } finally { return 'finally'; }
}
console.log(finallyReturn()); // finally

// Node 进程级兜底
// process.on('uncaughtException', ...)
// 浏览器：window.addEventListener('error', handler)
```
