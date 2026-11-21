---
title: [JS-270] 输出题：微任务嵌套与 then 链返回值
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-270：输出题：微任务嵌套与 then 链返回值

**题目**：写出输出顺序，说明「then 内再注册微任务」与「then 返回值进入下一个 then」的交织逻辑。

**答**：
```javascript
Promise.resolve()
  .then(() => {
    console.log('t1');
    Promise.resolve().then(() => console.log('t1-inner'));
  })
  .then(() => console.log('t2'))
  .then(() => console.log('t3'));

Promise.resolve().then(() => console.log('t0'));
```
```
输出：t1 t0 t1-inner t2 t3
解释：
1. 链A的 t1 与 链B的 t0 先后入队
2. 执行 t1：打印 t1；其内部注册的 t1-inner 入队尾
3. 此时队列：[t0, t1-inner] → 执行 t0
4. t1-inner 执行
5. 链A的第一段完成，第二段 then('t2') 在「第一段 resolve 后」才入队（在 t1 执行完时入队）——但它在 t1-inner 之后
6. t2、t3 依次
关键：then 链的下一段是在上一段回调执行完毕时才注册微任务；嵌套注册的微任务插在当前队列尾。
```

**评分点**：
- t1 → t0 → t1-inner 的顺序（嵌套注册排在队列尾）
- then 链下一段的注册时机（上一段执行完才注册）——本题核心
- t2/t3 最后的完整解释
- 能用队列图示推演（加分）
