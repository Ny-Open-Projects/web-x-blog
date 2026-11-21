---
title: "[RD-018] 运维·hotkey（hotkey）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · hotkey（hotkey）

- **事实**：hotkey（热 key）危害：单分片 QPS 极限被打满（单线程）
- **原理**：排查 redis-cli --hotkeys/监控，治理：本地缓存二级化、key 打散（加随机后缀）、读写分离
- **常见误区**：
  1. hotkey 通过加从库彻底解决（错）
  2. 热 key 检测无需工具（错）
  3. 热 key 是内存问题（错）
- **工程用法**：秒杀/热点资讯场景
- **版本锚点**：实战共识
