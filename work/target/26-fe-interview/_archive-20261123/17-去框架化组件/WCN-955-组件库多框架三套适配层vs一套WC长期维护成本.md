---
title: [WCN-955] 组件库同时支持 React / Vue / 原生：维护三套适配层 vs 一套 WC 的长期成本
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-955：组件库同时支持 React / Vue / 原生：维护三套适配层 vs 一套 WC 的长期成本

**答**：
- 结论先行：三套适配层的显性成本是 3× 开发维护，隐性成本是「行为不一致」——同一个组件在 React 与 Vue 下事件/props 语义漂移，测试矩阵爆炸。
- 一套 WC 的成本前置在「协议设计」：属性/事件/slot 协议要一次设计对，后期各框架只用薄适配（甚至框架原生支持 WC 后接近零适配）。
- 现实收益点：WC 的 bug 修一次全端生效；适配层的 bug 要三端各修一遍且要协调发版节奏（大促前多端版本对齐是高频痛点）。
- 但 WC 不是银弹：复杂交互组件（如数据表格）在 WC 里重实现成本高，这类通常保留框架原生 + 各自优化。
- 追问钩子：面试官问「React 对 WC 支持不好怎么办」——答：React 19 已大幅改善自定义元素支持，过渡期用 @lit/react 等包装器生成薄适配，仍是「一套 WC + 薄壳」而非三套重实现。

```javascript
// 一套 WC + 各框架薄包装（@lit/react 风格）
import { createComponent } from '@lit/react';
import { DsButton } from './ds-button.js'; // 唯一的真实实现
export const ReactDsButton = createComponent({
  tagName: 'ds-button', elementClass: DsButton, react: React,
  events: { onChange: 'ds-change' }, // 薄适配：事件名映射
});
// Vue 几乎零适配：直接在模板用 <ds-button @ds-change="...">
// 原生：document.createElement('ds-button')
// bug 只需改 ds-button.js 一处
```
