---
title: "[JV-022] 收集器·RSet（G1）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 收集器 · RSet（G1）

- **事实**：G1 用 RSet（记忆集）记录其他 Region 指向本 Region 的引用
- **原理**：每个 Region 维护自己的 RSet，回收时无需扫描全堆找引用者，空间换停顿，RSet 维护成本是 G1 主要开销之一
- **常见误区**：
  1. RSet 记录的是本 Region 指向别人的引用（错）
  2. RSet 免费无维护成本（错）
  3. RSet 让 G1 回收需要全堆扫描（错）
- **工程用法**：G1 吞吐低于 Parallel 的主要原因之一
- **版本锚点**：G1 论文
