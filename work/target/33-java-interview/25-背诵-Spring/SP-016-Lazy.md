---
title: "[SP-016] IoC·@Lazy（懒加载）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @Lazy（懒加载）

- **事实**：@Lazy 延迟到首次使用时才初始化 Bean
- **原理**：启动提速与打破循环依赖（注入代理占位），@Lazy 加在循环依赖字段上用代理打破死锁
- **常见误区**：
  1. @Lazy 提前初始化（错）
  2. @Lazy 对 singleton 全局生效（只对标注处）（错）
  3. @Lazy 影响 AOP 代理创建（错）
- **工程用法**：启动慢与循环依赖的两个用途
- **版本锚点**：Spring 文档
