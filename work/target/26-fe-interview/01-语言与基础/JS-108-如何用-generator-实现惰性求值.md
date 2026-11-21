---
title: [JS-108] 如何用 generator 实现惰性求值？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-108：如何用 generator 实现惰性求值？

**答**：
- 惰性求值：只在被消费时才计算下一个元素，无穷序列因此可行。
- generator 的 yield 天然是"暂停点"，配合 for-of / 解构只拉动需要的部分。
- 惰性 map/filter/take 链条与数组版 API 同构，但中间结果从不落地。
- 对比：`arr.map().filter()` 会产生中间数组；惰性版本全程只有一个"当前元素"。

```javascript
function* fib() {
  let [a, b] = [0, 1];
  while (true) { yield a; [a, b] = [b, a + b]; } // 无穷序列
}

// 惰性集合操作：只在被拉动时计算
function* lazyMap(iter, fn)        { for (const v of iter) yield fn(v); }
function* lazyFilter(iter, pred)   { for (const v of iter) if (pred(v)) yield v; }
function* take(iter, n) {
  let i = 0;
  for (const v of iter) { if (i++ >= n) return; yield v; }
}

// 链式组合：斐波那契 ×10 后取能被 3 整除的前 3 个
const fibs = fib();
const pipeline = take(
  lazyFilter(lazyMap(fibs, (x) => x * 10), (x) => x % 3 === 0),
  3
);
console.log([...pipeline]); // [0, 30, 210] — 计算到第 11 项即停，不会无限跑

// 与急切求值对比：数组版必须先物化无穷数组，直接栈溢出/死循环
// [...fib()] ← 千万不要这么写

// 惰性分页的另一种用法：需要几页取几页
function* pages(fetchPage) {
  let p = 1;
  while (true) yield fetchPage(p++);
}
// take(pages(fetch), 2) 就只请求两页
```

## 十六、类型系统与运行时
