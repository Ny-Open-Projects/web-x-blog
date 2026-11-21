---
title: "[SP-017] 容器·ApplicationContext（对比）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 容器 · ApplicationContext（对比）

- **事实**：ApplicationContext 是 BeanFactory 的超集增强版
- **原理**：BeanFactory 基础容器懒加载，ApplicationContext 增加事件、国际化、资源加载、注解支持且默认预初始化 singleton
- **常见误区**：
  1. ApplicationContext 与 BeanFactory 无关（错）
  2. ApplicationContext 不支持懒加载（错）
  3. BeanFactory 是 ApplicationContext 的子接口（错）
- **工程用法**：回答容器体系对比题
- **版本锚点**：Spring 文档
