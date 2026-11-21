---
title: "[RD-061] 运维·slowlog（慢查询）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · slowlog（慢查询）

- **事实**：慢查询日志 slowlog-log-slower-than（默认 10ms）与 slowlog-max-len
- **原理**：记录的是命令执行时长（不含网络），只存最近 N 条内存队列，大集合命令与 KEYS 是常客
- **常见误区**：
  1. 慢查询记录网络耗时（错）
  2. 慢查询会持久化到磁盘（错）
  3. 默认阈值 1 秒（错）
- **工程用法**：性能排查入口
- **版本锚点**：官方文档
