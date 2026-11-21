---
title: [CSS-210] CSS Parser API 现状与前景
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-210：CSS Parser API：现状与前景

**答**：
- 设想：让开发者参与 CSS 的解析——自定义规则、自定义 at-rule、把新语法 polyfill 成浏览器可懂的样式
- 愿景价值：新的 CSS 特性不用等浏览器支持，社区可以「解析器级 polyfill」（如 grid polyfill 曾是它的动机）
- 现状：提案多年未进入任何浏览器实现（被 @property/Typed OM 等小步快跑取代），基本停滞
- 面试正确姿势：能说出「Houdini 六大模块里 Parser API 是唯一没有实现的」体现对规范地图的熟悉
- 工程替代：PostCSS 在构建期做语法扩展（嵌套、自定义函数），是 Parser API 愿望的现实版本

```javascript
// 设想中的 API（未实现）——面试说清现状即可
CSS.parseRule('.a { color: red }'); // 提案中的 AST 操作
// 现实替代：PostCSS 插件在构建期扩展 CSS
```
