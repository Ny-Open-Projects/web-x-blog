---
title: [R19-383] React19 与 Web Components 集成
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## R19-383：React19 与 Web Components 集成

**答**：
- React19 原生支持自定义元素：属性/事件/children 的自动映射——event handlers 按事件名（on-x / addEventListener）绑定，slot children 传递
- 属性传递策略：基本类型设 property（首选）、复杂对象引用赋 property、字符串回退 attribute——React19 统一了「attribute vs property」的混乱（18 需要 ref 手工桥接）
- Shadow DOM 与 React 的边界：事件冒泡穿过 shadow（composed events）、样式隔离（全局 CSS 进不去）——组件库用 WC 时 React 侧的样式注入策略
- 用例定位：跨框架组件分发（设计系统同时服务 Vue/React 页面）、微前端边缘层——React 应用内部不推荐 WC（失去 React 生态优化）
- 已知边界：受控语义（value prop 双向）需要自己桥、Context 不跨 WC 边界——设计系统接口要「自包含」

```jsx
// React19 直接用自定义元素
<my-datepicker
  value={date}
  on-date-change={(e) => setDate(e.detail)}    // 事件自动绑定
>
  <span slot="header">{label}</span>            // slot children
</my-datepicker>
```
