---
title: [HW-053] 手写 chunk 分组
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-053：手写 chunk 分组

**答**：
- 评分点：slice 双参版 `[i, i + size)` 一次成型，最后不足 size 的组自动截短；边界：size 必须 ≥ 1（0 或负数会死循环 / 无意义，要抛错）、空数组返回 `[]`、size 大于数组长度返回单组；能给出**生成器版**（大数组流式处理不复制全部）与 `Array.from` + Math.ceil 的一行版是加分；说清与分页的关系——chunk 是纯内存分组，分页通常在服务端。

```javascript
// ===== 5 分钟速写版 =====
function chunk(arr, size = 1) {
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  return result;
}
// chunk([1,2,3,4,5], 2) → [[1,2],[3,4],[5]]

// ===== 标准完整版（含边界处理）=====
function chunkPro(arr, size = 1) {
  if (!Array.isArray(arr)) throw new TypeError('arr must be an array');
  if (!Number.isInteger(size) || size < 1) {
    throw new TypeError('size must be a positive integer'); // 0 会死循环，必须拦截
  }
  if (arr.length === 0) return [];
  const result = [];
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, Math.min(i + size, arr.length)));
  }
  return result;
}
// 生成器版：超大数据集按需产出，不整体驻留内存
function* chunkGen(arr, size) {
  if (!Number.isInteger(size) || size < 1) throw new TypeError('size must be positive');
  for (let i = 0; i < arr.length; i += size) {
    yield arr.slice(i, i + size);
  }
}
// 一行版（面试可展示代码手感）：
const chunkOneLine = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (_, i) => arr.slice(i * size, i * size + size));
// 异步批量场景（高频追问）：分批请求接口
// for (const batch of chunkPro(ids, 50)) {
//   await Promise.all(batch.map(id => fetchDetail(id)));  // 每批 50 个并发
// }
```

---
