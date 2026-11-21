---
title: "[DF-102] 稳定性·MTTD（度量）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 稳定性 · MTTD（度量）

- **事实**：故障度量四件套：MTTD（发现时长）/MTTA（响应时长）/MTTR（恢复时长）/MTBF（间隔）
- **原理**：MTTD 靠监控覆盖（未发现的故障最贵），MTTA 靠 oncall 机制，MTTR 靠预案与自动化，只看 MTTR 会掩盖发现慢的问题
- **常见误区**：
  1. MTTD 与 MTTR 是一回事（错）
  2. 度量只看恢复时间（错）
  3. MTTD 无法度量（错）
- **工程用法**：故障复盘的量化框架
- **版本锚点**：Google SRE
