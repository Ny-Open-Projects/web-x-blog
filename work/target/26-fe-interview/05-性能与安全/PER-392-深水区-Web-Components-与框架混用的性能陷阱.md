---
title: [PER-392] Web Components 与框架混用的性能陷阱：双重渲染、样式重复与事件桥接成本？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-392：Web Components 与框架混用的性能陷阱？

**答**：
- 陷阱一：双重渲染——框架里用 WC，props 变化走"框架更新 → setAttribute → WC 内部重新渲染"两层管线，比纯框架组件多一次全量渲染。规避：WC 只做"叶子级稳定组件"（图标/富文本渲染器），高频更新组件留在框架内。
- 陷阱二：样式重复与隔离成本——Shadow DOM 每实例一份样式克隆（同一组件 500 个实例 = 500 份样式解析）；constructable stylesheets（adoptedStyleSheets 共享样式表）是正解，老浏览器 fallback CSSStyleSheet 共享文本。
- 陷阱三：事件桥接——WC 内部事件要 re-target 后框架才能监听（composed 事件 + 自定义事件包装），高频事件（input/scroll）桥接产生额外对象分配；节流桥接或让 WC 直接上报给总线。
- 陷阱四：懒加载失配——框架 tree-shaking 不包含 WC 的 customElements.define，chunk 体积管理需单独处理（define 移到按需 chunk，自定义元素升级时机控制）。
- 度量：混用页面的渲染管线耗时对比（纯框架组件 vs WC 包装版本），差异 > 30% 的组件不进 WC。

```javascript
// constructable stylesheets：样式一次构建全实例共享
const sheet = new CSSStyleSheet();
sheet.replaceSync(`.wc-badge { color: var(--badge-color, #09f); }`);

class Badge extends HTMLElement {
  connectedCallback() {
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.adoptedStyleSheets = [sheet];        // 500 实例共享一份样式表
    this.shadowRoot.innerHTML = `<span class="wc-badge"><slot></slot></span>`;
  }
}
customElements.define('x-badge', Badge);
// 高频事件桥接节流：
// this.dispatchEvent(new CustomEvent('x-input', { detail: value, composed: true }))
// → 框架侧 @x-input —— 高频场景在 WC 内部节流后再派发
```
