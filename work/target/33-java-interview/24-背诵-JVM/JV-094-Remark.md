---
title: "[JV-094] GC·Remark（标记）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · Remark（标记）

- **事实**：G1 的 Remark（重新标记）阶段需要 STW 且耗时与写屏障脏队列长度相关
- **原理**：SATB 模式下 Remark 主要处理标记期遗留缓冲，通常几十毫秒，若日志显示 Remark 很长查应用是否大量改引用（如大集合并发修改）
- **常见误区**：
  1. Remark 是并发的（错）
  2. Remark 耗时与应用写行为无关（错）
  3. Remark 在标记开始阶段（错）
- **工程用法**：G1 停顿细项分析
- **版本锚点**：G1 实战
