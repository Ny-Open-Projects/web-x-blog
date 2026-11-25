---
title: [WCN-412] 笔试：实现 keyed 列表信号结构（顺序 + 内容分离）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-412：笔试：实现 keyed 列表信号结构（顺序 + 内容分离）。
**答**：`keyedList(initial)` 返回 `{keys: signal, item(id): signal, push, remove, update}`：内容更新只触发对应 item 订阅；顺序变更触发 keys 订阅。

```javascript
function keyedList(initial) {
  const keys = signal(initial.map((_, i) => `k${i}`));
  const items = new Map();
  let seq = initial.length;
  const ensure = (id, v) => { if (!items.has(id)) items.set(id, signal(v)); return items.get(id); };
  initial.forEach((v, i) => ensure(`k${i}`, v));
  return {
    keys, item: id => ensure(id),
    push(v) { const id = `k${seq++}`; ensure(id, v); keys.set([...keys.get(), id]); },
    remove(id) { keys.set(keys.get().filter(k => k !== id)); items.delete(id); },
    update(id, patch) { const s = ensure(id); s.set({ ...s.get(), ...patch }); },
  };
}

```

**评分点**：
- keys 信号存顺序数组；items Map 存 per-key 信号。
- update 只写对应 item 信号；push/remove 写 keys + 增删 item。
- 内容订阅不因顺序变化触发（keys 与 item 分离的关键）。
- GC：remove 时删除 item 信号（防泄漏）。
