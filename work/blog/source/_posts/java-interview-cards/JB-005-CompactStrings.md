---
title: "[JB-005] String·CompactStrings（版本）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · CompactStrings（版本）

- **事实**：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
- **原理**：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。
- **常见误区**：
  1. JDK9 后 String 内部仍是 char 数组。（错）
  2. Compact Strings 改变了 String 不可变的语义。（错）
  3. Compact Strings 会改变 String 的 hashCode 值。（错）
- **工程用法**：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。
- **版本锚点**：JDK9+
