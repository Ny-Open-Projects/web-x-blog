---
title: "[JV-020] 收集器·CMS（版本）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 收集器 · CMS（版本）

- **事实**：CMS 以最短停顿为目标采用标记-清除并已在 JDK9 被移除
- **原理**：并发标记与并发清除减少 STW，但标记-清除产生碎片且并发失败会退化 Serial Full GC，G1 全面接棒
- **常见误区**：
  1. CMS 是 JDK9 的默认收集器（错）
  2. CMS 用标记-整理无碎片（错）
  3. JDK21 还能使用 CMS（错）
- **工程用法**：老项目升级先替换 CMS 配置
- **版本锚点**：JEP 291
