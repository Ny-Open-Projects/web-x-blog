---
title: [ALG-053] 全局埋点需要事件总线：支持 on/off/once/emit，off 一个用 once 注册的监听也要能正确移除。手写 EventBus？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-053：全局埋点需要事件总线：支持 on/off/once/emit，off 一个用 once 注册的监听也要能正确移除。手写 EventBus？
**答**：`Map<type, Set<fn>>` 存监听；once 用包装函数实现"执行前先 self-off"，并把原函数挂到 `wrap.origin`，这样 `off(type, 原函数)` 能通过 origin 反查删除包装函数。emit 时复制一份 Set 防止回调中增删监听导致迭代异常。各操作 O(1)（emit O(k) 为该事件监听数），空间 O(n)。

```javascript
class EventBus {
  constructor() { this.events = new Map(); }
  on(type, fn) {
    if (!this.events.has(type)) this.events.set(type, new Set());
    this.events.get(type).add(fn);
    return () => this.off(type, fn); // 返回取消函数
  }
  once(type, fn) {
    const wrap = (...args) => {
      this.off(type, wrap);
      fn(...args);
    };
    wrap.origin = fn; // 供 off 按原函数反查
    this.on(type, wrap);
  }
  off(type, fn) {
    const set = this.events.get(type);
    if (!set) return;
    for (const item of set) {
      if (item === fn || item.origin === fn) set.delete(item);
    }
  }
  emit(type, ...args) {
    const set = this.events.get(type);
    if (set) [...set].forEach(fn => fn(...args)); // 拷贝防迭代中修改
  }
}
```
