---
title: "[RD-046] 缓存·binlog 订阅（一致性）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 缓存 · binlog 订阅（一致性）

- **事实**：强一致诉求的终极方案：Canal/Flink CDC 订阅 binlog 删除缓存+TTL 兜底
- **原理**：业务代码只写库，缓存失效由 CDC 异步驱动（解耦+防漏删），TTL 是最后防线，本项目总结的一致性框架
- **常见误区**：
  1. 业务代码里写缓存删除最可靠（错）
  2. CDC 删除不需要 TTL（错）
  3. binlog 订阅是同步的（错）
- **工程用法**：大型系统缓存一致性架构
- **版本锚点**：实战方法论
