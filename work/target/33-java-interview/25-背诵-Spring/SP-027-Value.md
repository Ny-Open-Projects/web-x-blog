---
title: "[SP-027] IoC·@Value（配置）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @Value（配置）

- **事实**：@Value 支持 ${} 占位符与 #{} SpEL 表达式
- **原理**：${db.url} 从 Environment 取值，#{systemProperties['x']} 是 SpEL，二者可嵌套，占位符找不到启动即报错（可给默认值 ${a:default}）
- **常见误区**：
  1. @Value 只支持 ${} 语法（错）
  2. SpEL 与占位符互斥（错）
  3. 占位符缺失默认返回空串（错）
- **工程用法**：配置注入推荐 @ConfigurationProperties 优先
- **版本锚点**：Spring 文档
