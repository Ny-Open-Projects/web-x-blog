---
title: "卡片 3：跳表为什么替换了 ziplist/平衡树？"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 3：跳表为什么替换了 ziplist/平衡树？
- vs 平衡树：实现简单，范围查询同样高效，且按概率分层无需旋转；
- vs B+ 树：内存型，无需页对齐，层数期望 O(log n)；
- 关键点：ZSet 用**跳表（排序范围查询）+ 字典（O(1) 按 member 查 score）**双结构，空间换时间。
