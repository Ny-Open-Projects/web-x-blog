---
title: "[JV-043] 类加载·Class.forName（API）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 类加载 · Class.forName（API）

- **事实**：Class.forName 触发初始化而 ClassLoader.loadClass 不触发
- **原理**：forName(name) 默认 initialize=true 执行静态块，loadClass 只加载不初始化（延迟到首次使用），驱动注册等场景用 forName 的历史原因
- **常见误区**：
  1. 两者完全等价（错）
  2. loadClass 也会执行静态块（错）
  3. forName 不执行静态块（错）
- **工程用法**：面试高频对比题
- **版本锚点**：JDK 文档
