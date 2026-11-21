---
title: "[JV-079] 工具·thread -b（arthas）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工具 · thread -b（arthas）

- **事实**：Arthas thread -b 一条命令找出阻塞其他线程最多的线程
- **原理**：线上免重启 attach，thread 查看栈、watch 观测入参返回值、trace 统计方法耗时链路，是本项目沙盒实测过的工具链
- **常见误区**：
  1. Arthas 必须重启应用才能 attach（错）
  2. thread -b 只能看死锁（错）
  3. Arthas 是离线分析工具（错）
- **工程用法**：线上诊断神器入门命令
- **版本锚点**：Arthas 文档
