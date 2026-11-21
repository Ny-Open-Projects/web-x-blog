---
title: [JS-087] 如何手写 mergePromise？把多个返回 Promise 的任务串行执行
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-087：如何手写 mergePromise？把多个返回 Promise 的任务串行执行

**答**：
- 目标：任务数组按顺序逐个执行，前一个 resolve 后才跑下一个，最终按序收集全部结果。
- 核心技巧：用 `chain = chain.then(task).then(collect)` 把 then 链当作“执行队列”，天然保证串行。
- 不能用 `for + await` 直接放进 Promise 构造器里，否则任务在构建时就并行启动了。
- 结果顺序与任务顺序一致（因为是依次 push，而不是按下标写入）。

```javascript
function mergePromise(tasks) {
  const results = [];
  let chain = Promise.resolve(); // 空链头
  tasks.forEach((task) => {
    chain = chain
      .then(task)                            // 等上一个完成才执行 task
      .then((data) => { results.push(data); });
  });
  return chain.then(() => results);          // 全部完成后统一返回
}

const t = (ms, val) => () =>
  new Promise((r) => setTimeout(() => { console.log('执行', val); r(val); }, ms));

mergePromise([t(100, 'a'), t(50, 'b'), t(30, 'c')]).then((all) => {
  console.log('结果', all); // 依次打印 a b c，结果 ['a','b','c']
});

// 带错误中断语义的变体：任一失败立即整体 reject
function mergePromiseStrict(tasks) {
  return tasks.reduce(
    (chain, task) => chain.then(task),
    Promise.resolve()
  );
}
```
