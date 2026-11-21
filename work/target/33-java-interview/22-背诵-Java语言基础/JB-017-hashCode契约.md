---
title: "[JB-017] equals体系·hashCode契约（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## equals体系 · hashCode契约（误用）

- **事实**：重写 equals 不重写 hashCode 会导致该对象在 HashMap/HashSet 中"找不到"。
- **原理**：HashMap 先用 hash 定桶再用 equals 精确匹配，缺 hashCode 的对象默认用对象地址。
- **常见误区**：
  1. IDE 自动生成的 equals 不需要同时生成 hashCode。（错）
  2. hashCode 相同则 equals 必须相同。（错）
  3. 重写 hashCode 不影响 HashMap。（错）
- **工程用法**：阿里手册：重写 equals 必须重写 hashCode。
- **版本锚点**：Object.hashCode javadoc
