---
title: [WCN-030] 用 WC 实现可复用的防抖搜索输入组件要注意什么？（对外 API、事件与清理）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-030：用 WC 实现可复用的防抖搜索输入组件要注意什么？（对外 API、事件与清理）

**答**：
- 对外 API：`debounce`（attribute，毫秒数字符串）、`value`（property 反射）、`search-input` 事件（composed + detail.value）、`valueMissing` 场景下不发事件（空值只清状态）。
- 防抖实现要点：连续输入重置计时器；disconnected 必须 clearTimeout；debounce 属性变化时重建节流逻辑。
- 竞态处理：组件只负责派发，请求竞态由调用方管理；但如果组件内置 loading 态，要用递增 requestId 丢弃过期响应。
- 输入法兼容：中文输入 composite 期间（compositionstart/end）不派发，避免拼音中间态触发请求。
- 追问钩子：`debounce` 属性是字符串，要 `Number() | 0` 并校验非法值回落默认 300。

```javascript
class DebounceSearch extends HTMLElement {
  static observedAttributes = ['debounce', 'placeholder'];
  #timer = 0; #seq = 0;
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open' });
    root.innerHTML = `<input placeholder="${this.getAttribute('placeholder') ?? '搜索'}">`;
    const input = root.querySelector('input');
    let composing = false;
    input.addEventListener('compositionstart', () => composing = true);
    input.addEventListener('compositionend', () => { composing = false; this.#emit(input.value); });
    input.addEventListener('input', () => { if (!composing) this.#emit(input.value); });
    this.#input = input;
  }
  disconnectedCallback() { clearTimeout(this.#timer); this.#input = null; }
  #emit(v) {
    clearTimeout(this.#timer);
    const wait = Number(this.getAttribute('debounce')) | 0 || 300;
    this.#timer = setTimeout(() => {
      this.dispatchEvent(new CustomEvent('search-input', {
        bubbles: true, composed: true, detail: { value: v, seq: ++this.#seq },
      }));
    }, wait);
  }
  get value() { return this.#input?.value ?? ''; }
  set value(v) { if (this.#input) this.#input.value = String(v ?? ''); }
}
customElements.define('debounce-search', DebounceSearch);
```
