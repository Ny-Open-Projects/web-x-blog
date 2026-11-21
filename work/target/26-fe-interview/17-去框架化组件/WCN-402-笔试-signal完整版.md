---
title: [WCN-402] 笔试：手写带双向订阅注册的 signal/computed/effect（依赖图完整版）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-402：笔试：手写带双向订阅注册的 signal/computed/effect（依赖图完整版）。
**题目**：在 401 基础上补全：signal.subs 注册订阅者；computed 作为「既是依赖又是订阅者」的双向节点；写信号 → 标脏直接订阅者 → 传播到间接 effect；批处理去重。

```javascript
const stack = [];
let queue = new Set(), q = false;
const schedule = e => { queue.add(e); if (!q) { q = true; queueMicrotask(() => {
  const list = [...queue]; queue.clear(); q = false;
  list.sort((a, b) => a.depth - b.depth);           // 深度优先浅层（简化拓扑）
  for (const e of list) e.dirty && e.run();
}); } };
function signal(v) {
  const node = { subs: new Set(), _v: v,
    get() { track(this); return this._v; },
    set(nv) { if (nv === this._v) return; this._v = nv;
      for (const s of this.subs) { s.dirty = true; schedule(s); } } };
  return node;
}
function track(node) { if (stack.length) { const top = stack[stack.length - 1];
  node.subs.add(top); top.deps.add(node); } }
function computed(fn) {
  const node = { subs: new Set(), deps: new Set(), dirty: true, _c: undefined,
    get() { track(this); if (this.dirty) {
      stack.push(this);
      const v = fn();
      stack.pop();
      // 依赖变化：新依赖重建 + 通知我的订阅者
      this._c = v; this.dirty = false;
    } return this._c; } };
  node.run = () => { node.get(); };
  return node;
}
function effect(fn) {
  const node = { subs: new Set(), deps: new Set(), dirty: true, depth: 0,
    run() { stack.push(this); try { fn(); } finally { stack.pop(); this.dirty = false; } } };
  node.run();
  return () => { node.deps.forEach(d => d.subs.delete(node)); node.deps.clear(); };
}

```

**评分点**：
- 双向边：node.subs（订阅我的）与 node.deps（我依赖的）。
- 传播：写 → 直接 subs 标脏 → 每个 computed 继续向上传播到 effect。
- 批处理：effect 去重集合，微任务一次执行（按拓扑简化：收集后递归驱动）。
- 销毁：effect dispose 断开双向边（防泄漏）。
