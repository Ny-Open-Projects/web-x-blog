---
title: [WCN-187] 笔试：手写跨组件通信总线（命名空间 + once + 通配符 + 生命周期清理）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-187：笔试：手写跨组件通信总线

**题目**：实现 WC 间事件总线 `bus`：① `on(event, fn)` / `once` / `off`；② 通配符订阅 `on('cart.*', fn)`（前缀匹配）；③ `emit(event, payload)` 按注册顺序同步执行，单个 handler 异常不中断其他 handler（错误收集后统一上报）；④ `on` 返回退订函数；⑤ 组件集成约定：`el.bindBus('cart.add')` 自动在 disconnect 时退订；⑥ 内存安全：emit 时快照订阅列表（handler 内 off 不影响本次遍历）。

**答**：

```javascript
const listeners = new Map(); // event -> [{fn, once}]

export const bus = {
  on(event, fn, { once = false } = {}) {
    const list = listeners.get(event) ?? [];
    list.push({ fn, once });
    listeners.set(event, list);
    return () => bus.off(event, fn);
  },
  once(event, fn) { return bus.on(event, fn, { once: true }); },
  off(event, fn) {
    const list = listeners.get(event);
    if (list) listeners.set(event, list.filter((l) => l.fn !== fn));
  },
  emit(event, payload) {
    const errors = [];
    // 精确 + 通配符两类订阅，emit 时快照（避免遍历中修改）
    const matched = [...listeners.get(event) ?? []];
    for (const [pattern, list] of listeners) {
      if (pattern.endsWith('.*') && event.startsWith(pattern.slice(0, -1)))
        matched.push(...list);
    }
    for (const { fn, once } of matched) {
      try { fn(payload, event); }
      catch (e) { errors.push({ event, e }); }     // 单个异常不中断
      if (once) bus.off(event, fn);
    }
    if (errors.length) reportBusErrors(errors);    // 统一上报
  },
};

// 组件集成：bindBus 自动生命周期清理
class WcBase extends HTMLElement {
  #unsubs = [];
  bindBus(event, fn) { this.#unsubs.push(bus.on(event, fn)); }
  disconnectedCallback() { this.#unsubs.forEach((u) => u()); this.#unsubs = []; }
}
// 用法：this.bindBus('cart.add', (p) => console.log(p)); 通配符：bus.on('cart.*', fn)
```

**评分点**：
- 通配符前缀匹配（`cart.*` 匹配 cart.add/cart.remove）。
- emit 快照订阅列表 + once 退订安全（遍历中修改不炸）。
- handler 异常隔离收集后统一上报（不静默吞）。
- bindBus 与 disconnected 自动退订（泄漏防线）。
