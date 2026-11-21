---
title: "[JV-067] 参数·SurvivorRatio（Survivor）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · SurvivorRatio（Survivor）

- **事实**：SurvivorRatio=8 表示 Eden 占新生代 8/10 两个 Survivor 各 1/10
- **原理**：Survivor 过小加剧动态年龄提前晋升，对象中期存活率高时应加大 Survivor 或新生代
- **常见误区**：
  1. SurvivorRatio=8 表示 Survivor 占 8 成（错）
  2. 两个 Survivor 大小可以不同（错）
  3. 该参数对 ZGC 生效（ZGC 无分代 JDK21 前无意义，分代 ZGC 有）（错）
- **工程用法**：调新生代布局的标准参数
- **版本锚点**：HotSpot
