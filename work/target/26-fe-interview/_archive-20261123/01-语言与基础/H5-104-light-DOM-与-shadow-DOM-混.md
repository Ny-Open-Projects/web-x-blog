---
title: [H5-104] light DOM 与 shadow DOM 混合渲染策略怎么选？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-104：light DOM 与 shadow DOM 混合渲染策略怎么选？
**答**：
- 决策轴：内容是否需要 SEO/服务端渲染、是否需要外部样式覆盖、是否需要全局事件委托命中。
- **shadow-only**：UI 原子组件（开关、日历）——完全封装最省心；**light-only**：内容型组件（文章卡片、列表）——利于 SEO 与站点统一样式。
- 混合模式 A"shadow 外壳 + light 内容"：逻辑壳在 shadow（样式封装），内容 slot 全部投影（SEO 可抓、可被全局委托命中）。
- 混合模式 B"关键结构进 light + 交互浮层进 shadow"：表格数据在 light（表格样式复用），弹层/日历浮窗进 shadow（防样式污染）。
- 反模式警告：把整页内容塞进 shadow 后再 wondering 为什么全局 CSS 框架失效；`display: contents` 滥用导致无障碍树结构混乱。

```html
<!-- 混合模式 A：数据行在 light DOM（SEO + 全局委托可命中），控件壳在 shadow -->
<user-row data-id="42">
  <td>张三</td>
  <td>zhangsan@example.com</td>
</user-row>

<table id="users"><tbody></tbody></table>

<script>
  customElements.define('user-row', class extends HTMLElement {
    connectedCallback() {
      // shadow 只承载"行为壳"：行首操作按钮，样式完全封装
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>
          :host { display: contents; }              /* 融入表格行布局 */
          .ops button { margin-right: 4px; }
        </style>
        <td class="ops">
          <button data-act="edit">编辑</button>
          <button data-act="del">删除</button>
        </td>
        <slot></slot>                                <!-- light 内容原位投影 -->`;

      this.shadowRoot.addEventListener('click', (e) => {
        this.dispatchEvent(new CustomEvent('row-action', {
          detail: { id: this.dataset.id, act: e.target.dataset.act },
          bubbles: true, composed: true,
        }));
      });
    }
  });
</script>

<script>
  // 全局委托依然命中 light DOM 内容（若内容也在 shadow 里就抓不到了）
  document.getElementById('users').addEventListener('click', (e) => {
    if (e.target.matches('td')) console.log('点击单元格：', e.target.textContent);
  });
  document.addEventListener('row-action', (e) =>
    console.log('行操作：', e.detail));
</script>
```
