---
title: [FRP-015] keep-alive 的实现原理是什么？LRU 缓存如何工作？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-015：keep-alive 的实现原理是什么？LRU 缓存如何工作？

**答**：
- keep-alive 是一个抽象组件：它**不渲染自己的容器 DOM**，而是缓存子组件的 vnode；切换回来时不重新 mount，直接把缓存 vnode 恢复，所以实例状态、滚动位置都在。
- 缓存结构：`Map<key, vnode>` + `keys` 数组（记录访问顺序）。命中时把 key 移到数组末尾（最新使用）；超过 `max` 时删数组**头部**（最久未用）——这就是 LRU。
- `include/exclude` 用组件 name 正则匹配决定缓存谁；被"逐出"或被 exclude 的组件才真正走 unmounted。
- 命中/失活时触发 `activated/deactivated` 而不是 `mounted/unmounted`。

```javascript
// 简化实现，帮助理解 keep-alive 的 LRU 缓存
class KeepAliveCache {
  constructor(max = 10) {
    this.cache = new Map(); // key -> vnode（缓存 vnode，恢复时不重渲染）
    this.keys = [];         // 访问顺序：尾部最新，头部最久未用
    this.max = max;
  }

  get(key) {
    if (!this.cache.has(key)) return null;
    // LRU 命中：移到数组末尾，表示"刚刚被使用"
    const idx = this.keys.indexOf(key);
    this.keys.splice(idx, 1);
    this.keys.push(key);
    return this.cache.get(key);
  }

  put(key, vnode, onEvict) {
    if (this.cache.has(key)) return;
    this.cache.set(key, vnode);
    this.keys.push(key);
    if (this.keys.length > this.max) {
      // 超出 max：驱逐头部（最久未使用），并真正 unmount 该组件
      const evicted = this.keys.shift();
      this.cache.delete(evicted);
      onEvict?.(evicted); // 触发被驱逐组件的 unmounted
    }
  }
}

const cache = new KeepAliveCache(2);
cache.put('a', { name: 'A' });
cache.put('b', { name: 'B' });
cache.get('a');             // a 变为"最新"，keys = [b, a]
cache.put('c', { name: 'C' }); // 超出 max=2，驱逐 b —— 最久未使用
console.log(cache.get('b')); // null，b 已被 LRU 驱逐
console.log(cache.get('a')); // { name: 'A' }，a 仍存活
```
