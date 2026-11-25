---
title: [MP-027] 多具名 slot 与抽象节点 generics 分别解决什么问题？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-027：多具名 slot 与抽象节点 generics 分别解决什么问题？
**答**：
- 具名 slot：组件 json 开 `"componentGenerics"`? 不对——开启 `"styleIsolation"`? 准确说需在组件 json 中声明 `"component": true` 且页面开启多 slot：**组件 json 配 `"multipleSlots": true`（options 里也有）**，模板 `<slot name="header"/>`，使用方 `<view slot="header">`。
- 抽象节点 generics：组件内写 `<generic-node/>` 占位，由**使用方指定具体实现组件**，解决"通用容器组件不知道要用哪个子组件"的依赖倒置问题。
- 配置：组件侧 `componentGenerics: { "list-item": true }`，使用侧在 usingComponents 里注册同名节点。

```javascript
// —— components/list/index.json：声明抽象节点 ——
{ "componentGenerics": { "list-item": true } }

// —— components/list/index.wxml：占位 ——
// <view><generic-node wx:for="{{list}}" item="{{item}}" /></view>

// —— pages/index/index.json：使用方指定实现 ——
{
  "usingComponents": {
    "list": "/components/list/index",
    "list-item": "/components/item/index"
  }
}
```
