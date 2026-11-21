---
title: "[SP-079] 缓存·@Cacheable（抽象）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 缓存 · @Cacheable（抽象）

- **事实**：Spring Cache 抽象：@Cacheable/@CachePut/@CacheEvict/@Caching 组合
- **原理**：基于 AOP 代理，缓存管理器可切 Redis/Caffeine，@Cacheable 先查缓存 miss 才执行方法，@CachePut 总是执行（写穿）
- **常见误区**：
  1. @CachePut 也先查缓存（错）
  2. 缓存注解在类内部自调用生效（错）
  3. 缓存 key 默认是方法所有参数（错）
- **工程用法**：声明式缓存落地
- **版本锚点**：Spring 文档
