---
title: "[RD-028] 事务·pipeline（对比）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · pipeline（对比）

- **事实**：pipeline 是批量发送减 RTT 不保证原子，事务/Lua 保证原子
- **原理**：pipeline 一次发 N 条命令收 N 个结果省网络往返，大量写入场景吞吐倍增，事务额外保证串行
- **常见误区**：
  1. pipeline 与事务等价（错）
  2. pipeline 原子执行（错）
  3. Lua 不能批量（错）
- **工程用法**：批量操作选型三件套
- **版本锚点**：实战共识
