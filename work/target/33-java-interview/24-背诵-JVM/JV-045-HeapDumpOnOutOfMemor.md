---
title: "[JV-045] OOM·HeapDumpOnOutOfMemoryError（dump）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## OOM · HeapDumpOnOutOfMemoryError（dump）

- **事实**：生产标配 -XX:+HeapDumpOnOutOfMemoryError 事发自动 dump
- **原理**：OOM 瞬间的对象分布是破案关键，事后 dump 无法重现现场，配合 HeapDumpPath 指定位置与 OOM 后重启策略
- **常见误区**：
  1. dump 会自动上传到监控平台（错）
  2. 该参数默认开启（错）
  3. OOM 后 dump 会导致进程挂起一段时间但不影响业务（错）
- **工程用法**：必须上线前就配好不能事后补
- **版本锚点**：实战共识
