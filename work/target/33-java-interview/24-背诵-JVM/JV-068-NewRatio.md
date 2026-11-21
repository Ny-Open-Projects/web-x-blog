---
title: "[JV-068] 参数·NewRatio（老年代）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · NewRatio（老年代）

- **事实**：NewRatio 默认 2 表示老年代:新生代 = 2:1
- **原理**：新生代过小 Minor GC 频繁且晋升压力增大，过大则 Minor GC 单次停顿变长，权衡取值
- **常见误区**：
  1. NewRatio=2 表示新生代是老年代两倍（错）
  2. 新生代与老年代比例是 1:1（错）
  3. 该参数对 G1 生效（G1 逻辑分代自动调整，不适用）（错）
- **工程用法**：全量理解分代比例参数族
- **版本锚点**：HotSpot
