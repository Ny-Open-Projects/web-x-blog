---
title: [JS-289] 笔试：手写 WeakMap 缓存 DOM 计算结果
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 内存]
type: 笔试题
---

## JS-289：笔试：WeakMap 缓存 DOM 计算结果

**题目**：实现元素级缓存：`measure(el)` 返回元素尺寸并缓存；元素从文档移除并失去引用后缓存自动失效；提供 `invalidate(el)` 手动失效；对比 Map 实现说明泄漏差异。

**答**：
```javascript
const cache = new WeakMap();

function measure(el) {
  if (!cache.has(el)) {
    cache.set(el, { w: el.offsetWidth, h: el.offsetHeight, t: Date.now() });
  }
  return cache.get(el);
}
function invalidate(el) { cache.delete(el); }

// Map 版的泄漏对比
const badCache = new Map();
function measureBad(el) {
  if (!badCache.has(el)) badCache.set(el, el.offsetWidth);
  return badCache.get(el);
}
// el 移除后 badCache 仍强引用节点 → 整棵 DOM 子树无法回收（detached DOM）
// WeakMap：无其他引用时条目随节点一起被 GC——零手动清理

// 组合使用：弱引用为主 + LRU 提示（WeakMap 不可遍历，统计需独立结构）
const hits = new WeakMap();
function measureWithStats(el) {
  hits.set(el, (hits.get(el) ?? 0) + 1);
  return measure(el);
}
```

**评分点**：
- WeakMap 键的弱引用语义（条目随键回收）
- Map 版 detached DOM 泄漏的机制说明——对比是本题核心
- invalidate 手动失效接口
- WeakMap 不可遍历/无 size 的限制认知（加分：stats 用独立 WeakMap）
