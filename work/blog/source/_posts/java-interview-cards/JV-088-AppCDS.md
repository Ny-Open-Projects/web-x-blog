---
title: "[JV-088] 启动·AppCDS（优化）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 启动 · AppCDS（优化）

- **事实**：AppCDS 把类加载产物缓存为文件加速启动
- **原理**：-XX:SharedArchiveFile 预生成存档，微服务与 Serverless 冷启动场景收益明显（启动时间可降 30-50%），JDK10 起 AppCDS 开源
- **常见误区**：
  1. AppCDS 是商业特性（错）
  2. AppCDS 缓存堆内对象（错）
  3. AppCDS 对启动时间无影响（错）
- **工程用法**：Serverless/弹性扩容场景
- **版本锚点**：JEP 310
