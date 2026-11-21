---
title: [ALG-122] 数据清洗管道：原始文案要依次经过 trim、小写化、空白转连字符三步，后续可能还要插步骤。如何用函数组合优雅实现？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-122：数据清洗管道：原始文案要依次经过 trim、小写化、空白转连字符三步，后续可能还要插步骤。如何用函数组合优雅实现？
**答**：compose 从右往左执行（数学定义 f(g(x))），pipe 从左往右（数据流更直观），两者都是 `reduce` 一次遍历，O(步数)。组合的价值：每个函数单一职责、可独立测试、可自由插拔。进阶版可在每步包 try/catch 或加日志中间件。

```javascript
function compose(...fns) {
  return x => fns.reduceRight((acc, fn) => fn(acc), x); // 从右往左 f(g(x))
}
function pipe(...fns) {
  return x => fns.reduce((acc, fn) => fn(acc), x);      // 从左往右，数据流方向
}
// 场景：slug 生成管道
const toSlug = pipe(
  s => s.trim(),
  s => s.toLowerCase(),
  s => s.replace(/\s+/g, '-')
);
// toSlug('  Hello  World ') => 'hello-world'
// 新需求加步骤：pipe(toSlugSteps..., s => s.slice(0, 50)) 直接插入即可
```
