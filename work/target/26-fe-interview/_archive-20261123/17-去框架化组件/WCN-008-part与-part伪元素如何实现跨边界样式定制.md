---
title: [WCN-008] ::part 与 ::theme 如何实现跨 Shadow 边界的样式定制？与 CSS 变量方案怎么选？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-008：::part 与 ::theme 如何实现跨 Shadow 边界的样式定制？与 CSS 变量方案怎么选？

**答**：
- `::part(name)`：外部文档通过元素上 `part="name"` 导出的"部件"直接选择器定制，如 `fancy-card::part(title) { color: red }`，一条规则可多级穿透到子组件的导出部件。
- 部件可以映射转发：子组件 `part="header header-title"`，父组件再导出为 `exportparts="header: outer-header"`，实现设计系统层级透传。
- `::theme()`（Chrome 实验性）：对同名 part 做全局主题匹配，无视嵌套层级，适合整站主题覆盖，兼容性差需渐进使用。
- 对比 CSS 变量方案：变量只能"传值"（颜色/尺寸等 token），part 能"传结构选择器"（可改 padding、flex、伪元素）；变量兼容性最好。
- 选型：设计 token 走 CSS 变量，结构性定制走 `::part`，两者组合是 WC 设计系统的标准姿势。

```html
<style>
  /* 外部定制导出的部件 */
  stat-card::part(value) { font-size: 28px; }
  stat-card::part(trend)[data-up] { color: #16a34a; }
</style>

<stat-card value="1280" trend="up">今日访问</stat-card>

<script>
class StatCard extends HTMLElement {
  static observedAttributes = ['value', 'trend'];
  connectedCallback() {
    this.attachShadow({ mode: 'open' }).innerHTML = `
      <style> #value { font-weight: 700; } </style>
      <div id="value" part="value">0</div>
      <div part="trend" data-up>↑</div>
      <slot></slot>`;
    this.render();
  }
  attributeChangedCallback() { if (this.shadowRoot) this.render(); }
  render() {
    this.shadowRoot.getElementById('value').textContent = this.getAttribute('value') ?? '';
    this.shadowRoot.querySelector('[part=trend]').dataset.up = this.getAttribute('trend') === 'up';
  }
}
customElements.define('stat-card', StatCard);
</script>
```
