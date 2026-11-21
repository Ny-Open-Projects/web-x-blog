---
title: "[MG-062] 运维·profiler（profiler）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · profiler（profiler）

- **事实**：profiler（慢查询记录）slowms 默认 100ms 写入 system.profile
- **原理**：三级级别（0 关/1 慢/2 全量，2 代价大临时用），与 explain 组合定位慢查询，生产常开级别 1
- **常见误区**：
  1. profiler 默认全量记录（错）
  2. profiler 不影响性能（级别 2 有明显开销）（错）
  3. slowms 是秒为单位（错）
- **工程用法**：慢查询监控
- **版本锚点**：官方文档
