---
title: [WCN-425] 笔试：实现 transition 双缓冲（低优先级更新不闪烁）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-425：笔试：实现 transition 双缓冲（低优先级更新不闪烁）。
**题目**：`startTransition(fn)`：fn 内信号写入进「pending 层」；读取时 transition 进行中返回旧值；transition 结束合并进主层一次 flush。

```javascript
let transacting = false; const pendingLayer = new Map();
function startTransition(fn) {
  transacting = true;
  try { fn(); } finally { transacting = false;
    for (const [s, v] of pendingLayer) s._v = v;   // 合并进主层
    pendingLayer.clear(); flushNow(); }
}
function signalWithTransition(v) {
  return {
    get() { return transacting && pendingLayer.has(this) ? this._v : (pendingLayer.get(this) ?? this._v); },
    set(nv) { if (transacting) pendingLayer.set(this, nv); else this._v = nv, this._propagate(); },
  };
}

```

**评分点**：
- 双缓冲：主值 + pending 值两层。
- 读取语义：transition 中读 → 旧值（视觉稳定）。
- 结束：pending → 主层单次传播。
- 非 transition 写仍即时（无影响）。
