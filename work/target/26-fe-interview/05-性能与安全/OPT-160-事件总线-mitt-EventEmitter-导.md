---
title: [OPT-160] 事件总线（mitt/EventEmitter）导致的组件泄漏如何统一治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-160：事件总线（mitt/EventEmitter）导致的组件泄漏如何统一治理？

**答**：
- 泄漏机理：组件在 mounted 时 `bus.on(evt, handler)`，卸载时忘记 `off`，总线长期持有 handler → handler 闭包持有组件实例 → 组件与整棵 DOM 树无法回收。
- 治理方案①框架层封装：React 用自定义 hook（useEffect 返回 off），Vue 用 `onUnmounted` 钩子自动 off，把"必须 off"从纪律变成默认行为。
- 治理方案②总线增强：给总线加"按 owner 分组订阅"，owner 销毁时一次性解绑全部（`bus.bind(owner)` 返回带销毁的订阅器）。
- 巡检兜底：开发环境在 handler 注册时记录 Error 堆栈（weakref 组件引用），devtools 面板展示"活跃订阅数"，暴露只 on 不 off 的组件。

```javascript
// 一一对应：事件总线防泄漏封装（按 owner 自动解绑 + 双框架 hook）
class SafeEventBus {
  constructor() { this.handlers = new Map(); this.byOwner = new Map(); }
  bind(owner) {   // owner = 组件实例或任意命名空间对象
    if (!this.byOwner.has(owner)) this.byOwner.set(owner, []);
    const self = this;
    return {
      on(evt, fn) {
        self.on(evt, fn);
        self.byOwner.get(owner).push([evt, fn]);  // 记账：便于一次性解绑
      },
    };
  }
  on(evt, fn) { (this.handlers.get(evt) || this.handlers.set(evt, []).get(evt)).push(fn); }
  emit(evt, ...args) { (this.handlers.get(evt) || []).forEach(fn => fn(...args)); }
  destroy(owner) {   // owner 销毁：一次解绑全部订阅，杜绝遗漏
    for (const [evt, fn] of this.byOwner.get(owner) || []) {
      const arr = this.handlers.get(evt);
      const i = arr.indexOf(fn);
      if (i > -1) arr.splice(i, 1);
    }
    this.byOwner.delete(owner);
  }
}

export const bus = new SafeEventBus();

// React hook：useEffect 清理函数天然兜底
export function useBus(evt, handler) {
  useEffect(() => {
    bus.bind('hook').on(evt, handler);          // 简化示例：实际按组件实例分 owner
    return () => bus.destroy('hook');           // 卸载必解绑，无需人肉记忆
  }, [evt, handler]);
}

// Vue 组合式：同样思路
export function useBusOn(evt, handler) {
  const sub = bus.bind(getCurrentInstance());
  sub.on(evt, handler);
  onUnmounted(() => bus.destroy(getCurrentInstance()));
}
```
