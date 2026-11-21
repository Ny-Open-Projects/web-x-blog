---
title: "[JV-064] 排查·jstat（jstat）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · jstat（jstat）

- **事实**：jstat -gcutil PID 1000 每秒输出各代使用率与 GC 次数时间
- **原理**：现场快速看 GC 健康度（无需日志配置），E/O/M 列趋势一目了然，是线上第一手证据
- **常见误区**：
  1. jstat 需要重启 JVM 才生效（错）
  2. jstat 会影响业务性能（错）
  3. jstat 只能看堆内存（错）
- **工程用法**：线上快速 GC 体检
- **版本锚点**：JDK 工具
