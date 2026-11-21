---
title: "[JV-086] OOM·GC overhead（类型）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## OOM · GC overhead（类型）

- **事实**：GC overhead limit exceeded：JVM 花超 98% 时间做 GC 但回收不足 2% 堆
- **原理**：本质是堆接近死满，参数 -XX:-UseGCOverheadLimit 只是关闭该报错不解决问题，根因仍是泄漏或堆不足
- **常见误区**：
  1. 该错误关闭后问题消失（错）
  2. 它是独立于堆满的另一种故障（错）
  3. 它只在 ZGC 下出现（错）
- **工程用法**：OOM 分诊知识
- **版本锚点**：HotSpot
