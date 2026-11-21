---
title: "[JB-071] Object·finalize废弃（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Object · finalize废弃（语法语义）

- **事实**：finalize 在 JDK9 标记废弃、JDK18 进一步降级，资源清理应使用 try-with-resources 或 Cleaner。
- **原理**：finalize 执行时机不定、可能永不执行、且影响 GC 性能。
- **常见误区**：
  1. finalize 是可靠的资源清理手段。（错）
  2. finalize 会在对象不可达后立即执行。（错）
  3. finalize 被 GC 最多调用两次。（错）
- **工程用法**：Cleaner 也是"尽力而为"，显式关闭（AutoCloseable）才是正解。
- **版本锚点**：JDK9+/JDK18+
