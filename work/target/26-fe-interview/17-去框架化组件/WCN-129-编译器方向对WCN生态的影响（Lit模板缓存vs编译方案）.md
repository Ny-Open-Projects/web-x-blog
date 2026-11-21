---
title: [WCN-129] 编译器趋势对 WCN 生态的影响？Lit 模板缓存与编译式 WC 的路线对比？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-129：编译器趋势对 WCN 生态的影响？Lit 模板缓存与编译式 WC 的路线对比？

**答**：
- Lit 路线：运行时 `html` 标签模板 + 首次解析缓存（static template），每次 update 只填动态槽——"运行时缓存"近似编译产物，兼容所有构建环境。
- 编译式 WC：Solid Element（solid 自定义元素）、Vue defineCustomElement（编译期优化 + VDOM）、Stencil（AOT 生成 WC）——构建期生成更优代码但绑定工具链。
- 趋势影响一：编译器让"WC 运行时成本"进一步下降（Lit 的 lit-html 静态模板已接近手写 DOM 操作）；影响二：跨框架分发更依赖构建产物标准化（DSD、manifest）。
- 选型：纯分发型库（给任意宿主用）→ Lit/Stencil（运行时自足）；自家 Monorepo 全链路 → 可用编译式（Vue Vapor/Solid）获得更小体积。
- 风险：编译式 WC 绑定框架版本，跨宿主升级要协调；Lit 的无编译依赖使其成为库分发的事实默认。

```javascript
// Lit 运行时模板缓存（伪码示意）
// 第一次 render：解析 html`<div>${x}</div>` → 缓存 Part 位置
// 第二次 render：跳过解析，直接 commit 到既有 Part
render() {
  return html`<div class=${cls}>${this.text}</div>`;
  // cls/text 变化 → 只调用 setAttribute/textContent，不重建 DOM
}
```
