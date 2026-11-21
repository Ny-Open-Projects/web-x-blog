---
title: "[DF-023] 可靠性·Sentinel（对比）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可靠性 · Sentinel（对比）

- **事实**：Sentinel vs Hystrix：Sentinel（阿里，流控规则丰富+控制台+滑动窗口实时统计，Hystrix 已停更）
- **原理**：Sentinel 支持 QPS/线程数/关联/链路限流与热点参数限流，Hystrix 线程池隔离重（开销大）已进维护模式，国内新项目默认 Sentinel
- **常见误区**：
  1. Hystrix 是当前主流（错）
  2. Sentinel 无熔断能力（错）
  3. 两者功能完全相同（错）
- **工程用法**：组件选型
- **版本锚点**：实战共识
