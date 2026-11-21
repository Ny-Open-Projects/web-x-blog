---
title: "[JB-087] String·equals方向（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · equals方向（误用）

- **事实**：常量在前调用 equals（"CONST".equals(variable)）可避免 variable 为 null 时抛 NPE。
- **原理**：null.equals 抛 NPE，常量.equals(null) 返回 false。
- **常见误区**：
  1. variable.equals("CONST") 与常量在前等价且同样安全。（错）
  2. null.equals("x") 返回 false。（错）
  3. Objects.equals(a,b) 不存在。（错）
- **工程用法**：JDK7+ 的 java.util.Objects.equals(a,b) 是 null 安全的标准替代。
- **版本锚点**：JDK7+
