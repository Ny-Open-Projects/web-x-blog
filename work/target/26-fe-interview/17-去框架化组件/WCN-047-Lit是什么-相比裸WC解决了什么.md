---
title: [WCN-047] Lit 库相比裸写 WC 解决了哪些痛点？reactive properties 与模板缓存是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-047：Lit 库相比裸写 WC 解决了哪些痛点？reactive properties 与模板缓存是什么？

**答**：
- 裸 WC 痛点：attribute/property 手写映射、innerHTML 每次全量解析、事件与子节点管理繁琐。
- reactive properties：`static properties = { value: { type: Number, reflect: true } }` 声明式定义属性——类型转换、attribute 反射、变化触发 `requestUpdate` 全部自动。
- `html` 模板标签函数：模板字符串只解析一次并缓存为静态模板（每个表达式位置留动态槽），更新时只改动态部分，性能接近编译期方案。
- `updateComplete` Promise：一帧内多次 setState 合并为一次 render，且测试里可 `await el.updateComplete` 断言。
- 生态：`@lit/context`（context 注入）、`@lit-labs/ssr`（DSD 渲染）、`@lit/react`（React 包装器）补齐工程化。
- 追问钩子：Lit 本质是"运行时模板缓存"路线，与 Solid 的"编译期"路线是响应式 WC 的两个流派。

```javascript
import { LitElement, html, css } from 'lit';

class GaugeLit extends LitElement {
  static properties = { value: { type: Number, reflect: true } };
  static styles = css`:host { display:block } .bar { background:#2563eb; height:8px }`;
  constructor() { super(); this.value = 0; }         // 默认值必写（upgrade 搬运）
  render() {
    const pct = Math.min(100, Math.max(0, this.value));
    return html`<div class="bar" style="width:${pct}%"></div>
      <span>${pct}%</span>`; // 模板结构静态，只有 ${} 位置是动态槽
  }
}
customElements.define('gauge-lit', GaugeLit);
```
