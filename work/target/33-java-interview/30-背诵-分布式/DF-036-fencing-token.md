---
title: "[DF-036] 锁·fencing token（fencing）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 锁 · fencing token（fencing）

- **事实**：fencing token：锁服务发放单调递增令牌，下游校验拒绝旧令牌写入
- **原理**：GC 停顿/时钟偏差下持锁者可能"复活"过期写入，令牌单调递增让下游识别过期持有者（Martin Kleppmann 方案），彻底解决需下游支持
- **常见误区**：
  1. fencing 由锁服务自动完成（错）
  2. 令牌不需要单调（错）
  3. 下游无需配合（错）
- **工程用法**：锁正确性的终极方案
- **版本锚点**：学术共识
