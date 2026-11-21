---
title: "[JB-090] String·replace与replaceAll（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · replace与replaceAll（误用）

- **事实**：replace 接收字面量（char/CharSequence），replaceAll 接收正则表达式——replaceAll(".") 会替换所有字符。
- **原理**：replaceAll 是正则语义，点号匹配任意字符。
- **常见误区**：
  1. replace 与 replaceAll 完全等价只是名字不同。（错）
  2. replace 不支持替换所有出现次数。（错）
  3. replaceAll 的性能一定比 replace 好。（错）
- **工程用法**：分割 IP 前缀等场景 replaceAll("\\.","-") 需双反斜杠转义。
- **版本锚点**：String javadoc
