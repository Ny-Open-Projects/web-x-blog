---
title: "[JA-018] Spring AI·PromptTemplate（模板）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · PromptTemplate（模板）

- **事实**：PromptTemplate 用 {占位符} 语法定义模板，add 渲染变量后生成 Prompt 对象
- **原理**：模板与代码分离（资源文件管理），渲染由 StringTemplate 引擎完成，占位符缺失渲染期报错
- **常见误区**：
  1. PromptTemplate 用 ${} 语法（错）
  2. 模板只能写在代码里（错）
  3. 渲染缺失占位符静默跳过（错）
- **工程用法**：提示词资产管理
- **版本锚点**：Spring AI 1.0 GA
