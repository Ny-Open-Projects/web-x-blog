---
title: [JS-271] 输出题：setTimeout(0) 与 await 的先后
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 事件循环]
type: 笔试题
---

## JS-271：输出题：setTimeout(0) 与 await 的先后

**题目**：判断 setTimeout(fn, 0) 与 await 后代码的执行顺序，并解释「setTimeout 0 至少 4ms」与微任务排空的规则。

**答**：
```javascript
setTimeout(() => console.log('macro'), 0);
(async () => {
  console.log('sync-in-async');        // 同步执行
  await Promise.resolve();             // 让出，后续进微任务
  console.log('micro-after-await');
})();
Promise.resolve().then(() => console.log('micro-plain'));
console.log('sync-last');
```
```
输出：sync-in-async sync-last micro-plain micro-after-await macro
解释：
- async 函数体内 await 前的代码同步执行
- await 后的代码是微任务；setTimeout(0) 是宏任务
- 微任务永远在当前宏任务结束前全部排空 → micro 两行先于 macro
- 规范：setTimeout 的 0 会被钳制为最小 4ms（嵌套超过 5 层后钳制更狠）；
  所以「setTimeout 0 立即执行」是错误认知
```

**评分点**：
- 完整顺序：同步 → 微任务（plain 与 await 后的顺序按注册序）→ 宏任务
- await 后代码进入微任务的机制
- setTimeout 0 的 4ms 钳制知识
- 「微任务排空优先于宏任务」的一句话总结
