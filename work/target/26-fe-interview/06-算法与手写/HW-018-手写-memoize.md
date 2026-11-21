---
title: [HW-018] 手写 memoize
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-018：手写 memoize

**答**：
- 评分点：用 Map/WeakMap 闭包缓存「入参 → 结果」；默认取第一个参数做 key，支持自定义 resolver（如多参数 join 序列化）；结果缓存前函数内部的 this 要保留（`fn.apply(this, args)`）；缓存要暴露出来（`memoized.cache`）便于测试与手动失效；能讨论缓存对象作为 key 时用 WeakMap 防内存泄漏是加分项。

```javascript
// ===== 5 分钟速写版 =====
function memoize(fn, resolver) {
  const cache = new Map();
  function memoized(...args) {
    const key = resolver ? resolver(...args) : args[0];
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  }
  memoized.cache = cache; // 暴露缓存，便于测试与清理
  return memoized;
}

// ===== 标准完整版（含边界处理）=====
function memoizePro(fn, resolver) {
  if (typeof fn !== 'function') throw new TypeError('fn must be a function');
  if (resolver !== undefined && typeof resolver !== 'function') {
    throw new TypeError('resolver must be a function');
  }
  const cache = new Map();
  function memoized(...args) {
    const key = resolver ? resolver.apply(this, args) : args[0];
    if (cache.has(key)) return cache.get(key);
    const result = fn.apply(this, args);
    // Promise 语义：失败结果不该缓存，下次重试
    if (result && typeof result.then === 'function') {
      return result.catch(e => {
        cache.delete(key); // 失败即淘汰，成功保留
        throw e;
      }).then(v => (cache.set(key, result), v));
    }
    cache.set(key, result);
    return result;
  }
  memoized.cache = cache;
  return memoized;
}
// 多参数缓存示例：
// memoizePro(fetchUser, (id, type) => `${id}:${type}`)
// 追问：WeakMap 版 key 只能是对象，无法缓存原始值入参，两者取舍要能说清。
```

---
