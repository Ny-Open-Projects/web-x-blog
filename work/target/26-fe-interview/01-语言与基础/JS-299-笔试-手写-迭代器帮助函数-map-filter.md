---
title: [JS-299] 笔试：手写迭代器帮助函数（map/filter）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 迭代器]
type: 笔试题
---

## JS-299：笔试：迭代器帮助函数

**题目**：为任意迭代器实现惰性 map/filter/take/toArray：返回新迭代器（生成器），链式调用；不驱动上游迭代直到被消费。

**答**：
```javascript
function* mapIt(it, fn) {
  let i = 0;
  for (const v of it) yield fn(v, i++);
}
function* filterIt(it, fn) {
  let i = 0;
  for (const v of it) if (fn(v, i++)) yield v;
}
function* takeIt(it, n) {
  if (n <= 0) return;
  let i = 0;
  for (const v of it) {
    yield v;
    if (++i >= n) return; // 拿够即停——上游不再被拉取
  }
}
const toArray = (it) => [...it];

function* naturals() { let i = 0; while (true) yield i++; }
// 无限序列安全：惰性链
const r = toArray(takeIt(filterIt(mapIt(naturals(), x => x * 2), x => x % 3 === 0), 5));
// [0, 6, 12, 18, 24]

// 验证惰性：take 后只拉了必要的上游步数
let pulls = 0;
function* spy() { while (true) { pulls++; yield pulls; } }
const s = spy();
[...takeIt(s, 3)]; // pulls === 3，不是无限
```

**评分点**：
- 生成器实现惰性链（每层 for-of 驱动上游）
- take 的提前 return 终止语义（上游不再拉取）——惰性核心
- 验证 pulls === 3 的惰性证明
- 对照 ES2025 原生 Iterator helpers（迁移说明加分）
