---
title: [JS-242] Iterator helpers：迭代器的 map/filter/toArray
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-242：Iterator helpers（ES2025）

**答**：
- 迭代器原生获得 map/filter/take/drop/flatMap/reduce/toArray 等——惰性链式处理，不用先转数组
- 与数组方法的区别：数组立即全量执行建中间数组；迭代器逐条流动，内存 O(1)
- 无限序列可用：`fib().map(x => x * 2).take(10).toArray()`——数组方法会死循环
- 惰性陷阱：不消费就不执行（toArray/for-of 才驱动）；take 后必须消费
- 兼容：Chrome 122+/Firefox 131+；Node 22+

```javascript
function* naturals() { let i = 0; while (true) yield i++; }
// 无限序列取前 10 个偶数的平方
const r = naturals().map(n => n * n).filter(x => x % 2 === 0).take(10).toArray();
// 大文件流式处理：不再中间建数组
const rows = fileLines().map(l => l.split(',')).filter(c => c[1] === 'A');
```
