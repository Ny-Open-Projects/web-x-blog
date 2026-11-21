---
title: "[JB-026] ArrayList·Arrays.asList（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ArrayList · Arrays.asList（误用）

- **事实**：Arrays.asList 返回定长列表，add/remove 会抛 UnsupportedOperationException。
- **原理**：其内部是同类型数组包装，不支持结构修改。
- **常见误区**：
  1. Arrays.asList 返回普通 ArrayList 可自由增删。（错）
  2. Arrays.asList 的修改会同步到原数组——事实上会，但结构修改不支持。（错）
  3. Arrays.asList(null 参数) 会返回空列表。（错）
- **工程用法**：返回值如果要可变需 new ArrayList<>(Arrays.asList(...)) 包装。
- **版本锚点**：JDK 文档（定长列表）
