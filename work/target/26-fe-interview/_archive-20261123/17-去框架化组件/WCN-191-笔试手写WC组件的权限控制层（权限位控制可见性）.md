---
title: [WCN-191] 笔试：手写 WC 组件的权限控制层（权限位决定可见性/可交互）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-191：笔试：手写 WC 组件的权限控制层

**题目**：实现 `<wc-perm need="order:export,order:delete" mode="any">`：① 权限来源：全局 `window.__PERMS__` 集合或 context 注入；② mode=any/all 判定；③ 通过：显示 slot 内容；不通过：隐藏并派发 `perm-denied`（detail: {missing}）；④ 权限变化（登录/切换角色）实时重判定（订阅权限 signal）；⑤ 防闪烁：未加载权限前渲染骨架或隐藏。

**答**：

```javascript
import { createSignal, effect, untrack } from './mini.js';

// 权限中心（模块级 signal，登录/切角色时更新）
export const perms = createSignal(new Set(window.__PERMS__ ?? []));

class WcPerm extends HTMLElement {
  static observedAttributes = ['need', 'mode'];
  connectedCallback() {
    if (!this.shadowRoot) {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>:host{display:contents}</style>
        <slot id="body" hidden></slot><div class="sk" hidden></div>`;
      this.#body = this.shadowRoot.getElementById('body');
    }
    this.#stop = effect(() => {
      const set = perms()[0] ?? perms();    // signal getter
      this.#evaluate(set);
    });
  }
  #body; #stop;
  disconnectedCallback() { this.#stop?.(); }
  #evaluate(set) {
    const need = (this.getAttribute('need') ?? '').split(',').map((s) => s.trim()).filter(Boolean);
    if (!need.length) return this.#grant();
    const missing = need.filter((p) => !set.has(p));
    const mode = this.getAttribute('mode') ?? 'all';
    const ok = mode === 'any' ? missing.length < need.length : missing.length === 0;
    ok ? this.#grant() : this.#deny(missing);
  }
  #grant() {
    this.#body.hidden = false;
    this.#toggleLoading(false);
  }
  #deny(missing) {
    this.#body.hidden = true;
    this.#toggleLoading(false);
    this.dispatchEvent(new CustomEvent('perm-denied', {
      bubbles: true, composed: true, detail: { missing },
    }));
  }
  #toggleLoading(on) {
    // 权限未就绪时防闪烁：perms 初始为空且 need 非空 → 显示骨架
    const sk = this.shadowRoot.querySelector('.sk');
    const notReady = !window.__PERMS_READY__;
    sk.hidden = !on && !notReady;
    if (notReady) this.#body.hidden = true;
  }
  attributeChangedCallback() {
    if (this.shadowRoot) this.#evaluate(untrack(() => perms()[0] ?? perms()));
  }
}
customElements.define('wc-perm', WcPerm);
// 用法：<wc-perm need="order:export" mode="any"><export-btn></export-btn></wc-perm>
```

**评分点**：
- any/all 两种判定语义正确，missing 计算用于 deny 事件 detail。
- 权限是 signal → 切角色实时重判定（细粒度订阅）。
- 防闪烁处理（权限未就绪先骨架/隐藏）。
- disconnected 释放订阅。
