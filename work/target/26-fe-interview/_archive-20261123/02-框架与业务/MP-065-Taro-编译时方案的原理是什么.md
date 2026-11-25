---
title: [MP-065] Taro 编译时方案的原理是什么？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-065：Taro 编译时方案的原理是什么？
**答**：
- Taro 1/2 是纯**编译时**方案：用 Babel 把 React/JSX 源码解析成 AST，再按目标端模板生成小程序原生代码（JS→js、JSX→wxml、样式→wxss）。
- 优点：产物是纯原生代码，运行时开销小。
- 缺点：受**语法静态分析限制**——JSX 必须可静态转换（不能随意用变量标签、复杂表达式），写法约束多，React 特性支持不全。

```bash
# Taro 编译时方案：源码经 AST 转换输出各端原生代码
npx @tarojs/cli init myApp        # 初始化项目
npm run build:weapp               # React 源码 → 微信小程序原生代码
# src/pages/index/index.jsx  →  dist/pages/index/index.js + index.wxml + index.wxss
```
