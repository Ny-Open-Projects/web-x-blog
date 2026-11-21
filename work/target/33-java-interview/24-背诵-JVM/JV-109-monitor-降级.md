---
title: "[JV-109] 锁·monitor 降级（降级）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 锁 · monitor 降级（降级）

- **事实**：HotSpot 自 JDK15 起支持空闲 monitor 降级（deflation）膨胀不再是永久性的
- **原理**：周期任务检测无竞争空闲 monitor 降级回无锁，JDK18+ 批量降级增强，"锁一旦膨胀永久不降"的说法已过时（JC-014 误认知的依据）
- **常见误区**：
  1. monitor 降级不存在（JDK15+ 已支持）（错）
  2. 降级需要重启（错）
  3. 所有 monitor 每轮都被降级（错）
- **工程用法**：锁升级描述必须带版本限定
- **版本锚点**：JDK15+
