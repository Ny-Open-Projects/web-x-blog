---
title: [DP-282] 笔试题：手写 EventBus（once/通配/命名空间解绑）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-282：笔试题：手写 EventBus（once/通配/命名空间解绑）？
**题目**：实现 EventBus：1) on/off/emit/once；2) 通配符 `*` 监听所有事件（收到 {event, payload}）；3) offNamespace('cart') 批量解绑前缀事件；4) emit 时 handler 抛错不阻断其他 handler。
**评分点**：
- once 自解绑在 emit 遍历前快照（防遍历中修改集合）。
- 通配事件签名正确。
- 错误隔离 try/catch 每个 handler。
- 命名空间解绑覆盖 `*` 监听（需记录注册命名空间）。
```javascript
class EventBus {
  handlers = new Map();
  wildcard = new Set();
  on(event, fn) {
    const target = event === '*' ? this.wildcard : (this.handlers.get(event) ?? this.handlers.set(event, new Set()).get(event));
    target.add(fn);
    return () => this.off(event, fn);
  }
  once(event, fn) {
    const wrap = (...args) => { this.off(event, wrap); fn(...args); };
    return this.on(event, wrap);                            // wrap 记录 ns 由 event 决定
  }
  off(event, fn) { (event === '*' ? this.wildcard : this.handlers.get(event))?.delete(fn); }
  offNamespace(ns) {                                        // 3)
    for (const [event, set] of this.handlers) if (event.startsWith(ns + ':')) set.clear();
    for (const w of [...this.wildcard]) if (w.__ns === ns) this.wildcard.delete(w);
  }
  emit(event, payload) {
    [...this.handlers.get(event) ?? []].forEach(fn => {     // 快照遍历
      try { fn(payload); } catch (e) { report(e); }         // 4) 错误隔离
    });
    [...this.wildcard].forEach(fn => { try { fn({ event, payload }); } catch (e) { report(e); } });  // 2)
  }
}
```
