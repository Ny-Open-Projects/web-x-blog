---
title: [PER-033] 如何捕获页面上的所有错误？JS 错误与资源错误的捕获有什么不同？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-033：如何捕获页面上的所有错误？JS 错误与资源错误的捕获有什么不同？

**答**：
- JS 运行时错误：`window.onerror` 能拿到 message、文件、行列号和 error 对象（含堆栈）。
- 资源加载错误（img/script/css 失败）：不冒泡，`window.onerror` 收不到，必须用 `addEventListener('error', fn, true)` 在**捕获阶段**监听。
- 两者都在时注意区分 `event.target`：目标是元素（非 window）即资源错误。
- 跨域脚本报错只有 `Script error.`，需要给 script 标签加 `crossorigin` 且响应头带 `Access-Control-Allow-Origin`。

```javascript
// 1. JS 运行时错误：window.onerror 能拿到完整堆栈信息
window.onerror = function (message, source, lineno, colno, error) {
  report('js-error', { // report 为上报函数
    message,
    source,
    lineno,
    colno,
    stack: error?.stack
  });
};

// 2. 资源加载错误不冒泡，必须用捕获阶段监听
window.addEventListener('error', (e) => {
  const target = e.target;
  if (target && target !== window) {
    report('resource-error', {
      tag: target.tagName,
      url: target.src || target.href
    });
  }
}, true);
```
