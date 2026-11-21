---
title: "[JV-080] 工具·watch（arthas）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工具 · watch（arthas）

- **事实**：Arthas watch 可观测方法入参、返回值与异常无需改代码
- **原理**：watch 全限定类名 方法名 '{params,returnObj,throwExp}' -x 2，配合条件表达式精准观测，生产排查定位线上问题利器
- **常见误区**：
  1. watch 会修改字节码导致性能大降（动态增强有轻微开销）（错）
  2. watch 只能看返回值（错）
  3. watch 需要预先埋点（错）
- **工程用法**：线上偶现问题抓现场
- **版本锚点**：Arthas 文档
