---
title: "[JV-105] 工具·UsePerfData（容器）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工具 · UsePerfData（容器）

- **事实**：jps/jstat 依赖 hsperfdata 共享内存文件，精简镜像若关闭 UsePerfData 会失效需显式开启
- **原理**：-XX:+UsePerfData 默认开启，部分 distroless 镜像为省开销关闭导致 jstat 连接失败，容器内诊断工具失效的第一排查项
- **常见误区**：
  1. 容器中 jstat 天然失效（错）
  2. UsePerfData 默认关闭（错）
  3. perf 文件在磁盘上持续写入（是内存映射共享文件）（错）
- **工程用法**：容器化 JVM 工具链知识
- **版本锚点**：实战共识
