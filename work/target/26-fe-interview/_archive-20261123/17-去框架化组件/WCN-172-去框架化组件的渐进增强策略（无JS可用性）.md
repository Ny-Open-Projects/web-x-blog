---
title: [WCN-172] 去框架化组件的渐进增强策略：无 JS 时组件应退化到什么形态？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-172：去框架化组件的渐进增强策略：无 JS 时组件应退化到什么形态？

**答**：
- 原则：内容先行——无 JS 时至少内容可读、链接可点；交互降级为服务端表单提交或原生控件。
- 手段一：light DOM 承载内容 + DSD 承载样式（WCN-162），JS 缺失时 slot 内容依旧渲染且可被样式化（DSD 无需 JS）。
- 手段二：组件功能分层——展示态纯 CSS（DSD），交互态 JS define；`<noscript>` 提示或切换到原生表单路径（如搜索框退化为 form GET）。
- 手段三：原生控件兜底——`<acme-menu>` 无 JS 时渲染为 `<details>/<summary>` 等价物（组件模板内放 noscript 分支或服务端按能力输出）。
- 验证：CI 加"no-JS 渲染快照"（Playwright javaScriptEnabled: false），内容可达性断言（标题/正文/主链接存在）。

```html
<!-- 渐进增强示例：搜索组件 -->
<acme-search action="/search" method="get">
  <template shadowrootmode="open">
    <style>/* 展示态样式，无需 JS */</style>
    <form part="form" action="/" method="get">  <!-- 无 JS 时原生提交 -->
      <input name="q" placeholder="搜索">
      <slot name="button"></slot>
    </form>
  </template>
  <button slot="button">搜索</button>
</acme-search>
<!-- JS define 后：接管 input 事件防抖、派发 search-input；无 JS：原生 GET 提交仍然可用 -->
```
