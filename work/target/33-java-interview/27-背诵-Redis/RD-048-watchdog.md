---
title: "[RD-048] 分布式锁·watchdog（续期）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分布式锁 · watchdog（续期）

- **事实**：锁过期但业务未完成：Redisson watchdog 自动续期（默认 30 秒锁每 10 秒续）
- **原理**：业务时长不可预估时靠看门狗续命，Redisson unlock 后停止续期；手写版需要后台线程续期，忘记解锁的兜底是 EX
- **常见误区**：
  1. watchdog 是自动机制无需配置（错）
  2. watchdog 保证业务永不超时（错）
  3. 续期由客户端线程直接续（Redisson 有专门定时任务）（错）
- **工程用法**：Redisson 分布式锁机制
- **版本锚点**：Redisson 文档
