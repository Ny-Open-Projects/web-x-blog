---
title: [JS-269] 输出题：async 循环与 for-of await 顺序
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 异步]
type: 笔试题
---

## JS-269：输出题：async 循环的执行顺序

**题目**：对比四种循环写法的输出与耗时差异：for-of await、forEach async、Promise.all(map)、for await-of。

**答**：
```javascript
const delay = (v, ms) => new Promise(r => setTimeout(() => r(v), ms));
const arr = [1, 2, 3];

// ① for-of + await：串行，3 × 100ms = 300ms，输出 1 2 3
async function serial() {
  for (const v of arr) console.log(await delay(v, 100));
}
// ② forEach 里 async：forEach 不等待！三个回调同时跑，输出乱序，~100ms
function broken() {
  arr.forEach(async v => console.log(await delay(v, 100))); // ⚠️ 不算等待
}
// ③ Promise.all(map)：并发，~100ms，输出 1 2 3（顺序保留）
async function parallel() {
  console.log(await Promise.all(arr.map(v => delay(v, 100))));
}
// ④ for await-of：串行消费异步可迭代对象
async function seq() {
  async function* gen() { for (const v of arr) yield delay(v, 100); }
  for await (const v of gen()) console.log(v);
}
```
```
关键结论：forEach 的 async 回调不会被等待（forEach 返回 undefined）——「forEach + async」是最常见的伪并发陷阱。
```

**评分点**：
- ① 串行与总耗时计算
- ② forEach 不等待 async 回调的陷阱识别（本题核心）
- ③ 并发但结果按输入顺序（Promise.all 的顺序保证）
- ④ for await-of 与 ① 的语义区别（迭代器驱动）
