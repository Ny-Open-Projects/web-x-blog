---
title: "[JV-053] 排查·JFR（JFR）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · JFR（JFR）

- **事实**：JDK11 起 JFR（Flight Recorder）免费且持续低开销采集
- **原理**：记录 GC、锁、IO、分配等事件，jcmd JFR.start 采集后 JMC 分析，是比日志更深一层的证据链
- **常见误区**：
  1. JFR 是商业收费特性（错）
  2. JFR 开销在 30% 以上（错）
  3. JFR 只能记录启动阶段（错）
- **工程用法**：生产长期开启 JFR（开销 <1%）
- **版本锚点**：JEP 328
