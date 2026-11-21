---
title: "[SP-008] 循环依赖·getEarlyBeanReference（原理）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 循环依赖 · getEarlyBeanReference（原理）

- **事实**：三级缓存存在的意义是让 AOP 场景能提前拿到代理引用
- **原理**：如果只有二级缓存，AOP 代理只能等初始化后创建，循环依赖时另一方拿到的是原始对象导致不一致；三级工厂通过 getEarlyBeanReference 提前生成代理
- **常见误区**：
  1. AOP 循环依赖靠二级缓存就够（错）
  2. 三级缓存是为了性能优化（错）
  3. 只有构造器注入才需要三级缓存（错）
- **工程用法**：解释"为什么是三级不是二级"的标准答案
- **版本锚点**：Spring 源码
