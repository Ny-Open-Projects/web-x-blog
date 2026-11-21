---
title: "[JB-080] 集合通用·Collection根接口（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 集合通用 · Collection根接口（语法语义）

- **事实**：Collection 根接口下 List/Set/Queue 三大分支；Map 不是 Collection 的子接口。
- **原理**：Map 是独立的键值对抽象，与 Collection 并列。
- **常见误区**：
  1. Map 继承自 Collection 接口。（错）
  2. List 和 Set 都不是 Collection 的子接口。（错）
  3. Queue 不属于 Collection 体系。（错）
- **工程用法**：Collections 是工具类，Collection 是接口——两者常被混淆。
- **版本锚点**：JDK 集合框架文档
