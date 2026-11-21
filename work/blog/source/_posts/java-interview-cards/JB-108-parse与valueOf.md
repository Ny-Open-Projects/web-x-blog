---
title: "[JB-108] 包装类·parse与valueOf（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · parse与valueOf（误用）

- **事实**：Integer.parseInt 返回基本类型 int，Integer.valueOf 返回包装类 Integer——按需求选择。
- **原理**：parse 无装箱开销；valueOf 有缓存。
- **常见误区**：
  1. 两者返回类型相同可混用无影响。（错）
  2. parseInt 返回 Integer。（错）
  3. valueOf 不接受字符串参数。（错）
- **工程用法**：高频解析场景 parseInt 更优（无装箱）。
- **版本锚点**：各包装类 javadoc
