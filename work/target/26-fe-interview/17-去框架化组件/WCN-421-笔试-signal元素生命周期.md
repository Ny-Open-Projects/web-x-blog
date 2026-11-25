---
title: [WCN-421] 笔试：元素内信号 effect 的生命周期绑定（自动随元素销毁）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-421：笔试：元素内信号 effect 的生命周期绑定（自动随元素销毁）。
**答**：`bindEffect(el, fn)`：effect 创建时关联元素；元素 disconnectedCallback 自动 dispose 全部绑定 effect。实现注册表（WeakRef 元素 → effect 集合）。

```javascript
const reg = new WeakMap();
function bindEffect(el, fn) {
  const dispose = effect(fn);
  const set = reg.get(el) ?? new Set();
  set.add(dispose); reg.set(el, set);
  return () => { dispose(); set.delete(dispose); };
}
class X extends HTMLElement {
  connectedCallback() { bindEffect(this, () => this._render(sig.get())); }
  disconnectedCallback() { reg.get(this)?.forEach(d => d()); reg.delete(this); }
}

```

**评分点**：
- WeakRef 持元素（防元素泄漏）。
- disconnectedCallback：遍历注册表 dispose。
- 防重入（同元素重复注册幂等）。
- 开发告警：元素销毁仍有活跃 effect（审计）。
