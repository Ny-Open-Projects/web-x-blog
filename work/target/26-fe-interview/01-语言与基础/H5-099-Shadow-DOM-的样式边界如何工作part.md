---
title: [H5-099] Shadow DOM 的样式边界如何工作？::part 解决什么问题？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-099：Shadow DOM 的样式边界如何工作？::part 解决什么问题？
**答**：
- 默认完全隔离：外部 CSS 选择器进不来，内部样式漏不出去；可穿透的只有**继承属性**（color、font 等）与 CSS 自定义属性（变量）。
- 对外暴露定制点的三个层级：CSS 变量（粒度粗、最常用）→ `::part(name)`（按部件定向，样式可完全重写）→ `<slot>` 内容区域样式。
- `::part` 用法：shadow 内元素标 `part="btn"`，外部 `my-dialog::part(btn) { color: red }`；支持 `::part(btn):hover` 与复合 `::part(a b)`。
- `::part` 边界：不能选中 part 内部的子元素（需 `part` 层级命名或配合 `::slotted`）；`exportparts` 可跨多层 shadow 转发。
- `:host` 控制宿主自身样式（优先级低于外部对宿主的规则），`:host-context()` 按祖先条件匹配。

```html
<my-dialog>
  <span slot="title">删除确认</span>
</my-dialog>

<script>
  customElements.define('my-dialog', class extends HTMLElement {
    connectedCallback() {
      if (!this.shadowRoot) {
        this.attachShadow({ mode: 'open' }).innerHTML = `
          <style>
            :host { display: block; font: inherit; }      /* 宿主外观 */
            .panel { border: 1px solid var(--dlg-border, #ddd); }
            .actions button { padding: var(--dlg-pad, 6px 16px); }
          </style>
          <div class="panel">
            <p><slot name="title"></slot></p>
            <div class="actions">
              <button part="cancel-btn">取消</button>
              <button part="ok-btn" class="primary">确定</button>
            </div>
          </div>`;
      }
    }
  });
</script>

<style>
  /* 层级 1：CSS 变量定制 */
  my-dialog { --dlg-border: #1677ff33; --dlg-pad: 8px 20px; }

  /* 层级 2：::part 精确定向，含伪类 */
  my-dialog::part(ok-btn) { background: #d33; color: #fff; border: none; }
  my-dialog::part(ok-btn):hover { background: #b22; }
  my-dialog::part(cancel-btn) { background: #eee; }
</style>
```
