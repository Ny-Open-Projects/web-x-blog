---
title: "[JV-104] 引用·softly-reachable（降级）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 引用 · softly-reachable（降级）

- **事实**：软引用对象在内存不足时才降级回收，且 JVM 会根据历史 GC 频率动态调整保留时长（-XX:SoftRefLRUPolicyMSPerMB）
- **原理**：软引用缓存"快满才回收"的行为由该策略控制（默认 1000ms/MB 空闲堆），堆越大软引用缓存存活越久，软引用缓存泛滥的机制解释
- **常见误区**：
  1. 软引用在每次 GC 必回收（错）
  2. 保留时长固定不变（错）
  3. 策略参数无实际影响（错）
- **工程用法**：软引用缓存调优
- **版本锚点**：HotSpot 文档
