---
title: "[JB-065] 语言杂项·char运算（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 语言杂项 · char运算（语法语义）

- **事实**：char 本质是 16 位无符号 UTF-16 代码单元，可参与整数运算（如 'a'+1 得 'b'）。
- **原理**：char 的算术结果自动提升为 int，赋回 char 需强转。
- **常见误区**：
  1. char 参与运算的结果还是 char 类型。（错）
  2. char 只能存储英文字母。（错）
  3. 一个 char 一定能表示一个汉字之外的所有 Unicode 字符。（错）
- **工程用法**：增补平面字符（如 emoji）需要代理对（两个 char），length() 会返回 2。
- **版本锚点**：JLS 4.2.1
