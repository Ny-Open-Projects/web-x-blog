---
title: "[JB-006] String·hashCode算法（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## String · hashCode算法（语法语义）

- **事实**：String 的 hashCode 算法为 s[0]*31^(n-1)+...+s[n-1]，乘数是 31。
- **原理**：31 是奇素数且 31*i 可优化为 (i<<5)-i 位运算；散列分布经大量字符串验证。
- **常见误区**：
  1. String 的 hashCode 乘数是 131。（错）
  2. String 的 hashCode 与内容顺序无关。（错）
  3. 空字符串的 hashCode 是 -1。（错）
- **工程用法**：面试可现场推 "abc"=97*31*31+98*31+99=96354。
- **版本锚点**：JDK 8+ 源码（31 乘子）
