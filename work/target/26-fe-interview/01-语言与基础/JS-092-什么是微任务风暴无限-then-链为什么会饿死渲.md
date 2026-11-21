---
title: [JS-092] 什么是微任务风暴？无限 then 链为什么会饿死渲染？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-092：什么是微任务风暴？无限 then 链为什么会饿死渲染？

**答**：
- 事件循环要先把整个微任务队列清空才可能进入渲染与宏任务。
- 无限自我续接的 then 链会不停地向队首插入新微任务，队列永远不清空。
- 结果：页面冻结、点击无响应、rAF 与 setTimeout 全部无法执行。
- 解法：在分片处理中插入 `setTimeout`/`requestIdleCallback` 等宏任务，主动让出渲染机会。

```javascript
// 反面示例：微任务风暴 —— 页面会完全冻结
function microtaskStorm() {
  Promise.resolve().then(function loop() {
    return Promise.resolve().then(loop); // 每个 tick 又排入新微任务
  });
}
// microtaskStorm(); // 打开即冻结：同步 → 微任务 → 微任务 → ... 永远到不了渲染

// 同理：async 里的 await Promise.resolve() 也是微任务
async function storm2() {
  while (true) await Promise.resolve(); // 同样饿死渲染
}

// 正确做法：大计算分片，每片之间让出主线程
async function processInChunks(list, handler, size = 1000) {
  for (let i = 0; i < list.length; i += size) {
    list.slice(i, i + size).forEach(handler);
    // setTimeout 让出事件循环：渲染与输入事件得以处理
    await new Promise((r) => setTimeout(r, 0));
  }
}
processInChunks(Array(1e6).keys(), (i) => { /* 重计算 */ }, 10000);
```
