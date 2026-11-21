---
title: "[DF-021] 可靠性·jitter（退避）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 可靠性 · jitter（退避）

- **事实**：指数退避+jitter：delay=base×2^n 加随机抖动，避免重试同步扎堆
- **原理**：无抖动的退避让所有客户端同一时刻重试（thundering herd），AWS SDK 默认 full jitter，jitter 是退避算法的标配
- **常见误区**：
  1. 指数退避本身足够（需要 jitter）（错）
  2. 退避时间越长越好（错）
  3. 线性退避与指数等价（错）
- **工程用法**：重试策略实现细节
- **版本锚点**：AWS 架构博客
