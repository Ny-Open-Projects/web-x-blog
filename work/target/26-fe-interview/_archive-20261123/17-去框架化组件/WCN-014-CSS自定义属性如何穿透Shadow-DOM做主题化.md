---
title: [WCN-014] CSS 自定义属性为什么能穿透 Shadow DOM？如何设计 WC 组件的主题 token 体系？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-014：CSS 自定义属性为什么能穿透 Shadow DOM？如何设计 WC 组件的主题 token 体系？

**答**：
- 原理：自定义属性沿 DOM 继承链计算，继承不区分 shadow 边界，且取值发生在使用点（影子树内部），所以外部在祖先上设置的 `--token` 影子内可读。
- token 三层设计：全局 token（`--wc-color-primary`）→ 组件 token（`--wc-btn-bg: var(--wc-color-primary)`）→ 影子内使用组件 token 并给默认值。
- 影子内写法：`background: var(--wc-btn-bg, var(--wc-color-primary, #2563eb))`，实现"用户覆盖 → 主题默认 → 兜底"三级回退。
- 动态换肤：只需在 `:root` 或容器上切换全局 token，无需触碰任何组件内部；配合 Constructable Stylesheets 可整包替换主题层。
- 坑：token 名没有作用域校验，跨组件同名会串；规范是统一前缀 + 命名清单（设计系统的 "theming contract"）。

```html
<div class="theme-dark">
  <primary-button>深色主题按钮</primary-button>
</div>
<style>
  .theme-dark { --wc-color-primary: #111827; --wc-color-on-primary: #f9fafb; }
</style>
<script>
class PrimaryButton extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style>
        button {
          /* 组件 token 可被外部逐级覆盖 */
          --btn-bg: var(--wc-btn-bg, var(--wc-color-primary, #2563eb));
          --btn-fg: var(--wc-btn-fg, var(--wc-color-on-primary, #fff));
          background: var(--btn-bg); color: var(--btn-fg);
          border: 0; padding: 8px 16px; border-radius: 8px;
        }
      </style>
      <button part="btn"><slot></slot></button>`;
  }
}
customElements.define('primary-button', PrimaryButton);
</script>
```
