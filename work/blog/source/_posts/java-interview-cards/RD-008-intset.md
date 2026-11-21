---
title: "[RD-008] Set·intset（编码）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Set · intset（编码）

- **事实**：Set 全整数且数量少时用 intset（紧凑整数数组）编码
- **原理**：整数数组二分查找省内存，加入字符串元素自动转 hashtable，编码自动升级不可逆
- **常见误区**：
  1. intset 可存字符串（错）
  2. intset 有序但查找 O(n)（错）
  3. 编码转换会丢数据（错）
- **工程用法**：纯数字集合（用户 ID 集合）的内存优化
- **版本锚点**：源码实现
