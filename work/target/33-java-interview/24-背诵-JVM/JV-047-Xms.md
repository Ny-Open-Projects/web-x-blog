---
title: "[JV-047] 参数·-Xms（堆）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · -Xms（堆）

- **事实**：-Xms 与 -Xmx 设为相同值避免堆动态伸缩抖动
- **原理**：堆动态扩容触发 Full GC 或影响延迟稳定性，服务器固定负载场景等值是标配，容器环境用 MaxRAMPercentage 更优
- **常见误区**：
  1. 堆越小性能越好（错）
  2. -Xms 必须小于 -Xmx（错）
  3. 堆自动扩容没有成本（错）
- **工程用法**：G1 等低延迟场景尤其要等值
- **版本锚点**：实战共识
