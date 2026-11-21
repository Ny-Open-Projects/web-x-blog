---
title: "[RD-108] 运维·memory doctor（内存）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · memory doctor（内存）

- **事实**：MEMORY DOCTOR 输出内存健康诊断结论（碎片/峰值/分配器问题）
- **原理**：与 MEMORY STATS/USAGE 组成内存诊断族：doctor 给结论性建议（碎片高/peer 分配问题），大 key 定位用 USAGE 逐 key 采样，免费自带工具链
- **常见误区**：
  1. MEMORY DOCTOR 自动修复内存（错）
  2. 该命令无性能影响（大 key USAGE 采样有开销）（错）
  3. 内存诊断只能靠外部工具（错）
- **工程用法**：内存问题排查入口
- **版本锚点**：官方文档
