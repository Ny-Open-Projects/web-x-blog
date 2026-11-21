---
title: [JS-095] 异步迭代器与 for await...of 如何用于流处理？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-095：异步迭代器与 for await...of 如何用于流处理？

**答**：
- 异步迭代器协议：对象实现 `[Symbol.asyncIterator]()`，返回 `{ next(): Promise<{value, done}> }`。
- `for await...of` 逐个 await 每一次 next，直到 done 为 true，天然匹配“数据逐步到达”的流。
- async generator（`async function*` + yield）是构造异步序列最简洁的方式。
- 中途 return/break 会自动调用 `iterator.return()`，适合做资源清理；Node 流、分页拉取都靠它。

```javascript
// async generator：模拟逐条到达的数据流
async function* numberStream(n) {
  for (let i = 1; i <= n; i++) {
    await new Promise((r) => setTimeout(r, 50)); // 模拟网络/IO 延迟
    yield i;
  }
}

(async () => {
  for await (const v of numberStream(3)) console.log('到达', v); // 1 2 3 逐个输出
})();

// 等价的手动消费
const it = numberStream(2);
it.next().then(({ value, done }) => console.log(value, done)); // 1 false

// 分页拉取的典型模式：一直取到没有下一页
async function* pagedFetch(path) {
  let page = 1;
  while (true) {
    const data = await Promise.resolve({ items: [page], hasMore: page < 3 }); // 模拟
    yield* data.items;
    if (!data.hasMore) return;
    page++;
  }
}
(async () => {
  const all = [];
  for await (const item of pagedFetch('/api/list')) all.push(item);
  console.log(all); // [1, 2, 3]
})();

// Node 流处理：for await (const chunk of readable) { ... }
// 中断时会自动调用 iterator.return 释放资源
```

## 十四、对象与元编程
