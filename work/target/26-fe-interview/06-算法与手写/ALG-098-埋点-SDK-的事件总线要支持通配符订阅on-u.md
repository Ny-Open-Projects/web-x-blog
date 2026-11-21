---
title: [ALG-098] 埋点 SDK 的事件总线要支持通配符订阅：`on('user.*')` 能收到 `user.login`、`user.logout` 等所有 user 开头的事件。如何实现带通配符的 EventEmitter？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-098：埋点 SDK 的事件总线要支持通配符订阅：`on('user.*')` 能收到 `user.login`、`user.logout` 等所有 user 开头的事件。如何实现带通配符的 EventEmitter？
**答**：订阅按注册顺序存数组，emit 时遍历：事件名完全相等直接命中；否则若 pattern 以 `*` 结尾，检查事件名是否以去掉 `*` 的前缀开头。emit 中遍历副本防止回调里 off 导致跳项。emit O(k)，on/off O(1) / O(k)，空间 O(n)。

```javascript
class WildcardEmitter {
  constructor() { this.handlers = []; }
  on(pattern, fn) { this.handlers.push({ pattern, fn }); }
  off(pattern, fn) {
    this.handlers = this.handlers.filter(
      h => !(h.pattern === pattern && h.fn === fn)
    );
  }
  emit(event, ...args) {
    for (const { pattern, fn } of [...this.handlers]) { // 遍历副本
      if (pattern === event || this._match(pattern, event)) fn(...args);
    }
  }
  _match(pattern, event) {
    if (!pattern.endsWith('*')) return false;
    return event.startsWith(pattern.slice(0, -1)); // user.* 匹配 user.login
  }
}
```
