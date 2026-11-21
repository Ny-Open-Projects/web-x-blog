---
title: [DP-256] 源码识别：跨应用 EventBus 源码中的命名空间观察者？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-256：源码识别：跨应用 EventBus 源码中的命名空间观察者？
**答**:
- 命名空间观察者：事件名带应用前缀（'cart:updated'），注册表 Map<event, Set<handler>>，卸载时 offNamespace('cart') 批量解绑（微前端防泄漏关键，ARC-216）。
- 通配与优先级：'*' 通配订阅（调试面板用）；once/优先级是注册项元数据。
- 备忘录（sticky 事件）：最后一条事件缓存（lastValue），新订阅者立即拿到——"黏性广播"用于主子应用状态初始化。
- 识别要点：能说清命名空间是"解绑单位"——没有它，子应用卸载后监听器残留就是内存泄漏与幽灵回调。

```javascript
// 命名空间 EventBus（源码级简化）
class NsEventBus {
  handlers = new Map(); lastValue = new Map();
  on(event, handler, { sticky = false } = {}) {
    const [ns] = event.split(':');
    this.handlers.get(event) ?? this.handlers.set(event, new Set());
    this.handlers.get(event).add(handler);
    if (sticky && this.lastValue.has(event)) handler(this.lastValue.get(event));  // 黏性：立即回放
    return () => this.off(event, handler);
  }
  emit(event, payload) {
    if (this.lastValue.has(event) || true) this.lastValue.set(event, payload);    // 记录最近值
    this.handlers.get(event)?.forEach(h => h(payload));
    this.handlers.get('*')?.forEach(h => h({ event, payload }));                  // 通配（调试）
  }
  offNamespace(ns) {                               // 子应用卸载：批量解绑
    for (const [event, set] of this.handlers)
      if (event.split(':')[0] === ns || event === '*') set.clear();
  }
}
// 主应用 emit('cart:updated', {...})；子应用 cart on('cart:updated')，unmount 时 offNamespace('cart')
```
