---
title: [WCN-022] WC 组件如何做无障碍？delegatesFocus、aria 关联与 role 透传怎么处理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-022：WC 组件如何做无障碍？delegatesFocus、aria 关联与 role 透传怎么处理？

**答**：
- `attachShadow({ delegatesFocus: true })`：宿主元素聚焦时自动委托给影子树第一个可聚焦节点，解决"焦点在容器而非内部控件"的问题。
- ARIA 关系不能跨 shadow 边界用 `id` 引用：`aria-labelledby="外部id"` 在影子树内不可见，需要把引用的节点也放进影子树，或用 `ariaDetailId`（ARIA reflection + ElementInternals 的 `ariaActiveDescendantElement` 等元素型属性，较新）。
- role 约定：用户在宿主上写的 role 优先，组件用 ElementInternals 设置默认 role 作为兜底；`role="presentation"` 时应清空内部语义。
- 键盘导航：影子树内自行管理 roving tabindex，焦点事件用 `focusin/focusout`（composed）对外通知。
- `:focus-visible` 在影子树内正常工作；`:host(:focus)` 与 `:host:focus-within` 区分组件自身聚焦与内部聚焦。

```javascript
class MenuButton extends HTMLElement {
  connectedCallback() {
    const root = this.attachShadow({ mode: 'open', delegatesFocus: true });
    root.innerHTML = `
      <style>
        :host(:focus-visible) button { outline: 2px solid #2563eb; } /* 外部聚焦透传视觉 */
        ul { margin: 0; padding: 0; list-style: none; }
        li[tabindex="-1"]:focus { background: #eff6ff; }
      </style>
      <button part="trigger" aria-haspopup="menu" aria-expanded="false"><slot name="label">菜单</slot></button>
      <ul role="menu" hidden></ul>`;
    const [btn, menu] = [root.querySelector('button'), root.querySelector('ul')];
    btn.addEventListener('click', () => {
      menu.hidden = !menu.hidden;
      btn.setAttribute('aria-expanded', String(!menu.hidden));
      if (!menu.hidden) menu.querySelector('li')?.focus(); // delegatesFocus 配合键盘
    });
    menu.addEventListener('keydown', (e) => {
      const items = [...menu.querySelectorAll('li')];
      const i = items.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') items[(i + 1) % items.length].focus();
      if (e.key === 'ArrowUp') items[(i - 1 + items.length) % items.length].focus();
    });
  }
}
customElements.define('menu-button', MenuButton);
```
