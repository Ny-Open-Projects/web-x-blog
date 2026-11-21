---
title: [JS-262] 笔试：手写生成器 Fibonacci 无限序列
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 生成器]
type: 笔试题
---

## JS-262：笔试：手写生成器 Fibonacci

**题目**：实现无限 Fibonacci 生成器；写 `take(iter, n)` 取前 n 个；证明惰性（take(5) 后生成器仍可继续 next）。

**答**：
```javascript
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b]; // 解构交换，无需临时变量
  }
}
function* take(iter, n) {
  let i = 0;
  for (const v of iter) {
    if (i++ >= n) return; // return 终止并让外层 done: true
    yield v;
  }
}
const fib = fibonacci();
console.log([...take(fib, 8)]); // [0,1,1,2,3,5,8,13]
console.log(fib.next().value);  // 21 —— 生成器状态还在，惰性可续
// 大数警告：Number 超过 2^53 后失真，工程中应换 BigInt
```

**评分点**：
- 双变量解构交换的写法
- while(true) 无限序列 + take 惰性截取的组合
- 惰性验证：take 后 next 继续有效（不是每次重建）
- 能主动提 BigInt/精度边界（加分）
