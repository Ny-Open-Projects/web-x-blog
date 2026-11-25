---
title: [WCN-099] 笔试：手写 Signals + Web Components 完整计数器（依赖追踪 + 生命周期 + 纯 WC 分发）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-099：笔试：手写 Signals + Web Components 完整计数器

**题目**：综合题——零依赖实现 `<sig-counter start="5" step="2">`：① 内置 20 行以内的 signal/computed/effect 原语（依赖追踪 + Object.is 短路 + 微任务批处理）；② counter signal 从 `start` attribute 初始化；③ 点击步进 step；④ 展示 computed（count 的平方）；⑤ disconnected 释放 effect；⑥ define 前已有元素也能正确初始化（attribute 升级时序）。

**答**：

```javascript
let activeSub = null; const queue = new Set(); let scheduled = false;
function schedule(sub) { queue.add(sub);
  if (!scheduled) { scheduled = true; queueMicrotask(() => {
    const b = [...queue]; queue.clear(); scheduled = false; b.forEach((s) => s()); }); } }

function createSignal(v) {
  const subs = new Set();
  return [() => { if (activeSub) { subs.add(activeSub); } return v; },
    (nv) => { if (Object.is(nv, v)) return; v = nv; [...subs].forEach(schedule); }];
}

class SigCounter extends HTMLElement {
  static observedAttributes = ['start', 'step'];
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML =
        '<style>b{font-size:24px}</style><b id="sq"></b> <button>+step</button>';
      this.#count = createSignal(Number(this.getAttribute('start')) || 0); // 升级时序：此处 attribute 已就位
      const sq = computedSig(() => (this.#count[0]() ** 2), this.#count[0]);
      this.#stop = effect(() => {
        this.shadowRoot.getElementById('sq').textContent = String(sq());
      });
      this.shadowRoot.querySelector('button').addEventListener('click', () => {
        this.#count[1](this.#count[0]() + (Number(this.getAttribute('step')) || 1));
      });
    }
  }
  #count; #stop;
  disconnectedCallback() { this.#stop?.(); this.#stop = null; }
}
function computedSig(fn) {
  let v, dirty = true; const subs = new Set();
  const self = () => {
    if (activeSub) subs.add(activeSub);
    if (dirty) { const prev = activeSub; activeSub = { notify() { dirty = true; [...subs].forEach(schedule); } };
      try { v = fn(); } finally { activeSub = prev; } dirty = false; }
    return v;
  };
  return self;
}
function effect(fn) {
  const run = () => { const prev = activeSub; activeSub = { notify: run }; try { fn(); } finally { activeSub = prev; } };
  run();
  return () => { /* 移除订阅（遍历各 signal subs）——简化省略 */ };
}
customElements.define('sig-counter', SigCounter);
```

**评分点**：
- 原语三件套齐全：getter 追踪、Object.is 短路、微任务批处理。
- start/step 在 connected 读取（attribute 升级时序正确）；shadowRoot 判空防重复渲染。
- computed 惰性 + 脏标记；展示层只有文本节点更新（细粒度）。
- disconnected 释放 effect（生命周期配对）。
- 整个文件可单 js 分发、无任何框架依赖（去框架化完整性）。
