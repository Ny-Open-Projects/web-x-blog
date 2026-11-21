---
title: [JS-208] Symbol.iterator 与 Symbol.asyncIterator 的差别
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 迭代器]
type: 面试题
---

## JS-208：Symbol.iterator 与 Symbol.asyncIterator 的差别

**答**：
- 同步迭代：next() 返回 { value, done }；消费方式 for-of / 展开
- 异步迭代：next() 返回 Promise<{ value, done }>；消费方式 for await-of——每步之间可 await
- 生成器对应：function* 配同步；async function* 配异步（分页拉取/流处理的标配）
- 互操作：异步可迭代对象不能被 [...展开]（会报不可迭代），同步与异步协议不可混用

```javascript
async function* ticker(interval) {
  for (let i = 0; ; i++) {
    yield await new Promise(r => setTimeout(() => r(Date.now()), interval));
  }
}
(async () => {
  for await (const t of ticker(1000)) {
    console.log(t);
    if (t % 10 < 1000) break; // for await-of 支持 break
  }
})();
```
