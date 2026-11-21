---
title: [WCN-054] WC 与微前端的结合点是什么？哪些场景比 qiankun/wujie 更合适？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, Web Components]
type: 面试题
---

## WCN-054：WC 与微前端的结合点是什么？哪些场景比 qiankun/wujie 更合适？

**答**：
- 结合点一：组件级"微前端"——用 WC 把不同技术栈的模块（React 面板、Vue 表单）以 `<x-xxx>` 形式直接嵌入同一页面，无需容器框架的路由/沙箱编排。
- 结合点二：样式与 DOM 天然隔离（Shadow DOM），等价于 qiankun 的样式隔离诉求；JS 共享全局（信任模型内可控），避免了 iframe 方案的通信成本。
- 结合点三：微前端容器（qiankun/wujie）把子应用"整页"接入，WC 把"积木"接入；粒度不同可组合——容器内子应用再对外暴露 WC 供主应用嵌套。
- 更合适的场景：同域可信团队、组件粒度嵌入（页面局部块）、对加载速度敏感（无沙箱启动开销）、需要 slot 让宿主内容投影进子应用组件。
- 不合适的场景：子应用不可信、需要独立路由与生命周期接管、需要 js 隔离兜底——这时仍应上 qiankun/wujie 或 iframe。

```javascript
// 子应用侧：把核心面板导出为 WC（各框架通用）
// react-panel.js
import React from 'react';
import { createRoot } from 'react-dom/client';

class ReactPanel extends HTMLElement {
  connectedCallback() {
    this.#root = createRoot(this.attachShadow({ mode: 'open' }));
    this.#root.render(React.createElement(Panel, { id: this.getAttribute('panel-id') }));
  }
  disconnectedCallback() { this.#root.unmount(); } // 生命周期映射
  #root;
}
if (!customElements.get('react-panel')) customElements.define('react-panel', ReactPanel);
```

```html
<!-- 主应用（Vue）直接嵌入，无容器框架 -->
<template>
  <react-panel panel-id="sales" />
  <section><slot-comp>宿主内容可投影</slot-comp></section>
</template>
```
