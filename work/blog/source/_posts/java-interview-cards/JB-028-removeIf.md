---
title: "[JB-028] ArrayList·removeIf（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ArrayList · removeIf（语法语义）

- **事实**：JDK8+ 用 removeIf(lambda) 安全地按条件删除元素，内部处理了移位与 modCount。
- **原理**：手写循环删除会因索引移动漏删元素。
- **常见误区**：
  1. 循环中 list.remove(i) 删除元素是完全安全的。（错）
  2. removeIf 是第三方工具类的方法。（错）
  3. removeIf 不支持条件删除。（错）
- **工程用法**：漏删是"遍历中删除"的最高频 bug——验证过 index 前移导致跳元素。
- **版本锚点**：JDK 8
