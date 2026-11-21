---
title: [JS-154] 如何用对象和 Map 实现高频缓存与计数场景？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-154：如何用对象和 Map 实现高频缓存与计数场景？

**答**：
- 计数：`map.set(k, (map.get(k) || 0) + 1)` 是词频统计的标准套路，一次遍历 O(n)。
- Top-K：计数完成后按值排序取前 N，数据量大时可用桶排序把复杂度降到 O(n)。
- 分组：reduce + Map 按任意键聚合，比对象分组更安全（键不会被原型属性污染）。
- Map 键可以是对象/NaN/任意类型，普通对象键只能是字符串——缓存「组件实例 → 数据」必须用 Map。
- 去重用 Set，保序去重 `[...new Set(arr)]` 是最简洁写法。

```javascript
// 1. 词频统计：Map 计数
const words = ['a', 'b', 'a', 'c', 'b', 'a'];
const freq = words.reduce((m, w) => m.set(w, (m.get(w) || 0) + 1), new Map());
console.log(Object.fromEntries(freq));   // { a: 3, b: 2, c: 1 }

// 2. Top-K：计数后按值排序
const top2 = [...freq.entries()].sort((x, y) => y[1] - x[1]).slice(0, 2);
console.log(top2);                        // [['a', 3], ['b', 2]]

// 3. 分组：Map 聚合
const users = [
  { name: 'A', dept: 'dev' }, { name: 'B', dept: 'ops' }, { name: 'C', dept: 'dev' },
];
const byDept = users.reduce((m, u) => {
  const list = m.get(u.dept) || [];
  list.push(u);
  m.set(u.dept, list);
  return m;
}, new Map());
console.log(byDept.get('dev').length);    // 2

// 4. 保序去重
console.log([...new Set(words)]);         // ['a', 'b', 'c']

// 5. memoize：Map 做结果缓存（键可以是任意类型）
function memoize(fn) {
  const cache = new Map();
  return (arg) => {
    if (!cache.has(arg)) cache.set(arg, fn(arg));
    return cache.get(arg);
  };
}
const slowSquare = memoize((n) => { console.log('计算了', n); return n * n; });
slowSquare(4);   // 计算了 4
slowSquare(4);   // 命中缓存，不再打印
```
