---
title: [MP-026] include 与 import 的作用域差异？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-026：include 与 import 的作用域差异？
**答**：
- `import`：只引入目标文件中**定义的 template**，且**不传递**——目标文件里 import 进来的 template 不会被带过来（作用域不传递是常考点）。
- `include`：把目标文件**除 template/wxs 外的全部内容**原样拷贝到当前位置，用于整块结构复用，不能传数据。
- `template`：用 `is` 引用、`data` 传参，模板内只能访问传入的数据，无独立逻辑。

```xml
<!-- import：只拿到 item.wxml 中定义的 template（不含其再 import 的） -->
<import src="../item/item.wxml" />
<template is="item" data="{{ item: list[0] }}" />

<!-- include：整体拷贝 header.wxml，不含其中 template -->
<include src="../header/header.wxml" />
```
