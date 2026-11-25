---
title: [MP-029] isolated 组件的样式如何穿透定制？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-029：isolated 组件的样式如何穿透定制？
**答**：
- 方案一 `externalClasses`：组件声明外部样式类名，使用方传入自己的类，权重高于组件内部样式。
- 方案二 CSS 变量：组件内写 `color: var(--comp-color, #333)`，使用方在父级注入变量。
- 方案三 styleIsolation 设为 apply-shared/shared（放宽隔离，影响面大）。
- slot 内容的样式由**使用方**的 wxss 控制，本身就是一条穿透通道。

```xml
<!-- 组件：components/badge/index -->
<!-- index.js: Component({ externalClasses: ['badge-class'] }) -->
<view class="badge badge-class">NEW</view>

<!-- 使用方页面 -->
<badge badge-class="my-red-badge" />
<!-- page.wxss: .my-red-badge { color: red; font-weight: bold } -->
```
