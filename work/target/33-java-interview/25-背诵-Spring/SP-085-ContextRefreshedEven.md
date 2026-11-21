---
title: "[SP-085] 容器·ContextRefreshedEvent（扩展）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 容器 · ContextRefreshedEvent（扩展）

- **事实**：ContextRefreshedEvent 在容器刷新完成后发布适合做启动后初始化
- **原理**：此时所有 Bean 就绪（含非懒加载），对比 @PostConstruct（自身就绪）与 ApplicationRunner（Boot 专属）的时机差异
- **常见误区**：
  1. 该事件在每个 Bean 初始化时发布（错）
  2. @PostConstruct 时所有 Bean 已就绪（错）
  3. ApplicationRunner 与该事件同时触发（错）
- **工程用法**：全量就绪后的预热/校验任务
- **版本锚点**：Spring 文档
