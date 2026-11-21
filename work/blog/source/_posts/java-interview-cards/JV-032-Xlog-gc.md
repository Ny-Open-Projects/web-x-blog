---
title: "[JV-032] GC 日志·-Xlog:gc*（工具）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC 日志 · -Xlog:gc*（工具）

- **事实**：JDK9+ 开启 GC 日志用 -Xlog:gc* 替代 JDK8 的多个 PrintGC 参数
- **原理**：统一日志框架可输出到文件带时间戳/级别/标签旋转，旧参数 PrintGCDetails 在 JDK9+ 已被映射并废弃提示
- **常见误区**：
  1. PrintGCDetails 在 JDK21 依然推荐（错）
  2. GC 日志默认自动开启（错）
  3. 日志只能输出到控制台（错）
- **工程用法**：生产标配：-Xlog:gc*:file=gc.log:time,uptime
- **版本锚点**：JEP 158
