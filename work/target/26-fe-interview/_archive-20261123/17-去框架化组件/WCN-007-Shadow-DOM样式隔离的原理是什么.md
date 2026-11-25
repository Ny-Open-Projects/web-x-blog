---
title: [WCN-007] Shadow DOM 样式隔离的原理是什么？哪些东西依然会"漏"进去？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-007：Shadow DOM 样式隔离的原理是什么？哪些东西依然会"漏"进去？

**答**：
- 隔离原理：选择器匹配在影子树边界处被拦截——文档样式无法匹配影子树内部，影子树样式（shadowRoot 内 `<style>`/`<link>`）也无法影响外部；两者在样式计算时属于不同的树作用域。
- 继承会漏：`color`、`font`、`direction` 等可继承属性会从宿主元素继承进影子树，所以组件常在 `:host` 里显式重置关键可继承属性。
- CSS 自定义属性会漏：`--x` 沿继承链穿透边界，这是刻意设计的"样式输入通道"。
- `:host` 规则、`::slotted()`、`::part()` 是三条受控的跨界通道；`:host` 优先级低于外部对宿主元素的规则，外部样式可覆盖。
- `!important` 与 `all` 简写：外部 `!important` 作用于宿主元素时会影响其继承值；影子内 `:host { all: initial }` 可做样式重启。
- 追问钩子：@keyframes 名在影子树内是作用域化的，但全局 keyframes 可被继承动画引用。

```html
<div class="page" style="--accent: red; color: blue;">
  <fancy-tag>隔离测试</fancy-tag>
</div>
<script>
  class FancyTag extends HTMLElement {
    connectedCallback() {
      this.attachShadow({ mode: 'open' }).innerHTML = `
        <style>
          /* 继承漏进来的 color:blue 被显式重置；--accent 穿透进来生效 */
          :host { color: #333; background: var(--accent, gray); all: initial; /* 可选样式重启 */ }
          span { font: inherit; }
        </style>
        <span><slot></slot></span>`;
    }
  }
  customElements.define('fancy-tag', FancyTag);
</script>
```
