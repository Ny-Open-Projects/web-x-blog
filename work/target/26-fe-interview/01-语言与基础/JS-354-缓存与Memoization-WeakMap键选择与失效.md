---
title: [JS-354] 缓存与 Memoization：WeakMap 键选择与失效策略
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## JS-354：缓存与 Memoization：WeakMap 键选择与失效策略

**答**：
- 键选择决定泄漏与否：Map 以对象为键持有强引用（对象不被回收）；WeakMap 键为弱引用（对象回收条目自动消失）——「按 DOM 元素/组件实例缓存计算结果」必须 WeakMap
- 参数做键：原始值直接用 Map；复合参数序列化（JSON.stringify 排序键）或嵌套 Map（逐参数分级）；引用类型参数做键要「归一化标识」（如 id）而不是对象本身
- 失效策略：TTL（时间）、容量 LRU（最近最少使用淘汰）、依赖失效（依赖数据变更时清除）——React 的 useMemo 依赖数组就是手动依赖失效；手写 memoize 要暴露 invalidate
- 大小控制：无界缓存是慢性泄漏（长会话累计）——LRU 容量上限是底线；缓存命中收益与键计算成本要平衡（键计算比原计算贵就别缓存）
- 纯度前提：memoize 只对纯函数有效（副作用函数缓存会改变行为）

```javascript
function memoize(fn, { max = 100, ttl = Infinity } = {}) {
  const cache = new Map();
  const memo = (...args) => {
    const k = args.length === 1 && typeof args[0] !== 'object' ? args[0] : JSON.stringify(args);
    const hit = cache.get(k);
    if (hit && Date.now() - hit.t < ttl) return hit.v;
    const v = fn(...args);
    cache.set(k, { v, t: Date.now() });
    if (cache.size > max) cache.delete(cache.keys().next().value); // FIFO/LRU 近似
    return v;
  };
  memo.invalidate = () => cache.clear();
  return memo;
}
const byEl = new WeakMap();          // DOM 元素缓存: WeakMap 防泄漏
function layoutInfo(el) { if (!byEl.has(el)) byEl.set(el, compute(el)); return byEl.get(el); }
```
