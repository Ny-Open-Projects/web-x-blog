---
title: [XP-375] 跨端页面间通信（事件总线 vs 路由参数）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-375：跨端页面间通信（事件总线 vs 路由参数）

**答**：
- 方式：路由参数（一次性）、全局 store（共享状态）、事件总线（跨页面通知）。
- 选择：数据流单向优先（store），页面级通知用事件（带清理防泄漏）。
- 坑：事件总线监听器未清理导致内存泄漏与重复触发。

```javascript
// 事件总线防泄漏
class EventBus {
  constructor() { this.map = new Map(); }
  on(event, fn) {
    if (!this.map.has(event)) this.map.set(event, new Set());
    this.map.get(event).add(fn);
    return () => this.map.get(event).delete(fn);      // 返回取消函数
  }
  emit(event, payload) {
    this.map.get(event)?.forEach(fn => fn(payload));
  }
}
// 页面卸载必须调用取消函数（组件 unmount 清理）
```
