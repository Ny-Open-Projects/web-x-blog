---
title: "[JV-056] String·Compact Strings（布局）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · Compact Strings（布局）

- **事实**：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）
- **原理**：纯 Latin-1 字符串内存减半，含中文等多字节字符时退回 UTF-16 存储，是 JDK9 升级的隐形收益之一（本项目有实测断言）
- **常见误区**：
  1. JDK9 的 String 变慢了（错）
  2. Compact Strings 对中文也减半（错）
  3. String 仍是 char[]（错）
- **工程用法**：估算字符串内存必须分 JDK8/9+
- **版本锚点**：JEP 254 实测
