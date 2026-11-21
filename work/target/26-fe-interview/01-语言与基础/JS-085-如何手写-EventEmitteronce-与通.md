---
title: [JS-085] 如何手写 EventEmitter？once 与通配符监听怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-085：如何手写 EventEmitter？once 与通配符监听怎么实现？

**答**：
- 数据结构：`Map<event, Set<callback>>`，Set 天然去重，emit 时拷贝一份遍历防止“边遍历边删除”丢事件。
- once：包装一层，触发后自动 off；用 `_origin` 记录原回调，使 `off(event, 原回调)` 也能解绑。
- 通配符：注册 `user:*`，emit('user:created') 时前缀匹配即触发。
- emit 应返回是否有监听者（node 语义），方便调试未消费的事件。

```javascript
class EventEmitter {
  constructor() { this._events = new Map(); }

  on(event, cb) {
    if (!this._events.has(event)) this._events.set(event, new Set());
    this._events.get(event).add(cb);
    return this;
  }

  once(event, cb) {
    const wrap = (...args) => {
      this.off(event, wrap); // 触发一次后自动移除
      cb(...args);
    };
    wrap._origin = cb; // 记录原回调，让 off 能按原回调解绑
    return this.on(event, wrap);
  }

  off(event, cb) {
    const set = this._events.get(event);
    if (!set) return this;
    for (const item of set) if (item === cb || item._origin === cb) set.delete(item);
    if (set.size === 0) this._events.delete(event);
    return this;
  }

  emit(event, ...args) {
    let fired = false;
    for (const [key, set] of this._events) {
      const hit = key === event || (key.endsWith('*') && event.startsWith(key.slice(0, -1)));
      if (!hit) continue;
      for (const cb of [...set]) { cb(...args); fired = true; } // 拷贝防遍历中修改
    }
    return fired;
  }
}

const em = new EventEmitter();
em.on('user:*', (data) => console.log('通配符收到', data.type));
em.once('user:created', () => console.log('once 只执行一次'));
em.emit('user:created', { type: 'signup' }); // 两条都触发
em.emit('user:created', { type: 'signup' }); // 只剩通配符触发
console.log(em.emit('user:deleted', {}));    // true
console.log(em.emit('nothing', {}));         // false
```
