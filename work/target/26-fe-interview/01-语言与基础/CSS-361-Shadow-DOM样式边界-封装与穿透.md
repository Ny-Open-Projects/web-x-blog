---
title: [CSS-361] Shadow DOM 样式边界：封装、穿透与继承
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-361：Shadow DOM 样式边界：封装、穿透与继承

**答**：
- 封装边界：shadow 内样式不影响外部、外部样式不影响内部（除继承属性）——shadow 树样式解析独立，组件库的样式隔离正解
- 穿透通道：继承属性（color/font）穿过 shadow 边界；CSS 自定义属性穿过边界（组件主题注入的标准方式）；::part() 与 ::theme() 定向样式化内部件
- @import/@layer 在 shadow 内：light DOM 的 @layer 不直接影响 shadow，但通过变量与 part 可以间接配合；adoptedStyleSheets 支持多组件共享同一 CSSStyleSheet（复用解析结果，避免每实例重复解析）
- 性能含义：每个 shadow root 独立样式树——大量实例（千级列表）会重复解析；adoptedStyleSheets 复用 + constructable stylesheet 是优化关键
- 与 SSR 的矛盾：shadow DOM 内容无法被服务端直接声明式渲染（Declarative Shadow DOM 模板已支持但要额外标注），SSR 框架集成成本高

```javascript
const sheet = new CSSStyleSheet();
sheet.replaceSync(`.btn { color: var(--btn-fg, #1677ff); }`);
class MyBtn extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' }).adoptedStyleSheets = [sheet]; // 复用解析
    this.shadowRoot.innerHTML = `<button class="btn" part="button"><slot></slot></button>`;
  }
}
```

```css
/* 外部穿透 */
my-btn::part(button) { border-radius: 8px; }
my-btn { --btn-fg: #fff; }        /* 变量穿透 */
```
