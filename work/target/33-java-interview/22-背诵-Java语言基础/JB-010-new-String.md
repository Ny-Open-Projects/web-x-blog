---
title: "[JB-010] String·new String（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · new String（误用）

- **事实**：new String("abc") 在字面量已入池时额外创建 1 个堆对象，未入池时创建 2 个。
- **原理**：字面量入池 + new 强制堆上新建副本，两者独立。
- **常见误区**：
  1. new String("abc") 只创建 1 个对象。（错）
  2. new String("abc") 创建 3 个对象。（错）
  3. new String 不涉及常量池。（错）
- **工程用法**：代码里出现 new String(字面量) 基本都是误用，review 直接标记。
- **版本锚点**：Java 语言通用语义
