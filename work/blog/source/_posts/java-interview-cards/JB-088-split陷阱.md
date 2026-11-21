---
title: "[JB-088] String·split陷阱（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · split陷阱（误用）

- **事实**：String.split 的参数是正则表达式，且默认省略尾部空串——特殊字符（点号与星号）必须转义。
- **原理**：正则语义导致 "." 会匹配任意字符；limit 参数传负数保留尾部空串。
- **常见误区**：
  1. split(".") 会按字面量点分割。（错）
  2. split 永远保留尾部空字符串。（错）
  3. split 的参数就是普通字符串。（错）
- **工程用法**：常见事故：按 "." 分割 IP 地址得到空数组。
- **版本锚点**：Java 正则语义
