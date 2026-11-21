---
title: [ALG-003] 报表页拿到一批订单数据 `[{city, amount}]`，需要按城市分组展示，并进一步求每组的金额总和。如何实现通用分组与聚合？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-003：报表页拿到一批订单数据 `[{city, amount}]`，需要按城市分组展示，并进一步求每组的金额总和。如何实现通用分组与聚合？
**答**：分组本质是用 `reduce` 以 `keyFn(item)` 为 key 把元素收集进桶，单次遍历完成，O(n)。聚合可在分组结果上再遍历求和。注意用 `Object.create(null)` 或 `Map` 避免 `__proto__` 等 key 污染。时间 O(n)，空间 O(n)。

```javascript
function groupBy(list, keyFn) {
  return list.reduce((acc, item) => {
    const k = keyFn(item);
    (acc[k] || (acc[k] = [])).push(item);
    return acc;
  }, Object.create(null)); // 无原型对象：city 叫 __proto__ 也不会污染
}
// 报表聚合：分组后再求和
function sumBy(list, keyFn, valFn) {
  const grouped = groupBy(list, keyFn);
  return Object.fromEntries(
    Object.entries(grouped).map(([k, items]) => [
      k,
      items.reduce((s, it) => s + valFn(it), 0),
    ])
  );
}
// sumBy(orders, o => o.city, o => o.amount) => { 北京: 300, 上海: 200 }
```
