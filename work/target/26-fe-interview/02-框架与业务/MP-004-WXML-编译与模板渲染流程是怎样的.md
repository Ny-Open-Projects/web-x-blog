---
title: [MP-004] WXML 编译与模板渲染流程是怎样的？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-004：WXML 编译与模板渲染流程是怎样的？
**答**：
- 上传/构建时，WXML 被编译成一段 **JS 函数（generateFunc）**，它接收 data 返回一棵虚拟节点树描述；WXSS 编译为 JS 注入的样式；二者打进代码包。
- 页面首次渲染：渲染层 WebView 拿到初始 data → 执行 generateFunc 生成虚拟树 → 挂载真实 DOM。
- 后续 setData：只传变化数据 → 渲染层在既有虚拟树上 diff → 增量更新 DOM，避免整页重渲。
- `wx:if` 与 `hidden` 的差异也发生在这层：前者控制节点树是否生成，后者只改样式显隐。

```xml
<!-- pages/list/list.wxml -->
<view wx:for="{{items}}" wx:key="id" wx:if="{{items.length > 0}}">
  {{item.name}}
</view>
<view hidden="{{!visible}}">仅隐藏，节点树仍存在</view>
```
