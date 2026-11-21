---
title: "[SP-109] IoC·ApplicationContext（API）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · ApplicationContext（API）

- **事实**：获取容器内 Bean 的正道是注入而非 ApplicationContextAware 手动 getBean
- **原理**：手动 getBean 隐藏依赖关系与静态耦合（ServiceLocator 反模式），例外：工具类/无法注入的场景
- **常见误区**：
  1. 手动 getBean 是推荐做法（错）
  2. ApplicationContextAware 已废弃（错）
  3. 静态获取 Bean 与注入等价（错）
- **工程用法**：代码 review 识别 ServiceLocator
- **版本锚点**：Spring 官方建议
