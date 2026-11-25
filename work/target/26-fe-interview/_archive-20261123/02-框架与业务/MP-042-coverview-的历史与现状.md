---
title: [MP-042] cover-view 的历史与现状？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-042：cover-view 的历史与现状？
**答**：
- 历史：同层渲染普及前，原生组件之上只能覆盖 cover-view/cover-image（由 native 渲染的"原生层兄弟"），样式支持极有限（不支持大部分 wxss）。
- 现状：input/video/map/canvas 等已同层，普通 view 可直接覆盖，官方建议新代码直接用普通组件，cover-view 仅用于兼容老基础库/未同层组件。
- 仍可能遇到：部分端（如小程序 PC 端、低版本抖音宿主）组件未同层时需要 cover-view 兜底。

```xml
<!-- 旧写法：非同层年代必须 cover-view 覆盖 video -->
<video src="{{src}}">
  <cover-view class="btn-legacy">旧写法按钮</cover-view>
</video>

<!-- 新写法：同层渲染后普通 view 直接覆盖 -->
<view class="video-box">
  <video src="{{src}}"></video>
  <view class="btn-modern">新写法按钮</view>
</view>
```
