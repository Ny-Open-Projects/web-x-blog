---
title: [JS-346] async/await 编译后的形态：执行顺序的本质
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-346：async/await 编译后的形态：执行顺序的本质

**答**：
- await 的本质：挂起当前 async 函数，把「函数剩余部分」注册为该 Promise 的 then 回调（微任务）——async 函数是「状态机 + 协程」的语法糖，每 await 一个暂停点
- 输出顺序题的关键：await 右侧表达式先同步求值，其 then 回调进微任务；await 恢复还要再过一层（规范内建的额外微任务跳转）——「await Promise.resolve() 之后为何还有一次额外微任务」是深水考点
- 并行写法差异：`await a(); await b();` 串行；`const [x,y] = await Promise.all([a(), b()])` 并行；`const p = a(); const y = await b(); await p;` 手动并发——知道「启动即执行，await 只是等结果」
- 错误传播：try/catch 包 await 即可捕获异步 reject；多 await 并行时 Promise.all 的聚合错误 vs allSettled 的逐个处理
- 与 generator 的关系：async/await ≈ 自动执行的 generator + Promise 化——老面试题「用 generator 实现 async」仍是理解深度的试金石

```javascript
async function demo() {
  console.log('A');                  // 同步
  const p = Promise.resolve().then(() => console.log('C')); // C 排微任务
  await p;                           // A 后挂起
  console.log('D');                  // D 在 C 之后(微任务内恢复)
}
// 顺序: A → C → D
// 手动并发: 
// const p1 = fetchA(); const a = await fetchB(); const x = await p1; // 并行
```
