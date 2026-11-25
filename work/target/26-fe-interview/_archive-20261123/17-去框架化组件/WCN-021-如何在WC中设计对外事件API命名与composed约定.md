---
title: [WCN-021] 如何为 WC 组件设计对外事件 API？命名、payload 与 composed 有什么约定？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-021：如何为 WC 组件设计对外事件 API？命名、payload 与 composed 有什么约定？

**答**：
- 命名：对外事件用 kebab-case 且带组件语义（`cart-item-remove`），避免与内置事件重名；一对内置/自定义并行时以内置语义为准（如 `change` 直接触发原生语义）。
- 必须声明 `{ bubbles: true, composed: true }` 才能穿出影子树被宿主外监听；不冒泡的局部交互事件才省略。
- payload：统一放 `event.detail`，保持只读对象；高频事件（input-like）应提供 `event.detail.value` 而非让消费方读内部节点。
- 设计原则：事件是"通知"不是"命令"——组件不依赖消费方响应；需要返回值/异步控制用方法 + Promise，而不是靠事件的 preventDefault（原生 exception：表单控件、`beforetoggle` 等可取消事件需要 expose cancelable）。
- 文档契约：事件名、detail 字段、是否 cancelable、是否 composed 都要写进组件 API 文档，供框架包装层生成 props。

```javascript
class QuantityPicker extends HTMLElement {
  #value = 1;
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML =
      '<button data-d="-1">-</button><output>1</output><button data-d="1">+</button>';
    this.shadowRoot.addEventListener('click', (e) => {
      const d = Number(e.target.dataset.d);
      if (!d) return;
      this.#value = Math.min(999, Math.max(1, this.#value + d));
      this.shadowRoot.querySelector('output').textContent = this.#value;
      this.dispatchEvent(new CustomEvent('quantity-change', {
        bubbles: true, composed: true,
        detail: { value: this.#value, source: 'pointer' },
      }));
    });
  }
  get value() { return this.#value; }
  set value(v) { this.#value = Math.max(1, Number(v) || 1); }
}
customElements.define('quantity-picker', QuantityPicker);
```
