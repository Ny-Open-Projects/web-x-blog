---
title: "[JB-025] ArrayList·subList视图（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## ArrayList · subList视图（误用）

- **事实**：List.subList(from,to) 返回的是原列表的视图，修改原列表结构会使其失效。
- **原理**：视图直接操作底层数组，非拷贝——修改 subList 会同步影响原列表。
- **常见误区**：
  1. subList 返回的是独立的拷贝列表。（错）
  2. subList 修改不影响原列表。（错）
  3. subList 是线程安全的。（错）
- **工程用法**：返回 subList 给调用方存在"泄露内部表示"的封装风险。
- **版本锚点**：List javadoc（视图语义）
