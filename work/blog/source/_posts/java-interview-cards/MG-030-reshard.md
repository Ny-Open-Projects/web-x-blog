---
title: "[MG-030] 分片·reshard（演进）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分片 · reshard（演进）

- **事实**：分片键选错的补救：4.4 refineCollectionShardKey 追加后缀字段、5.0 reshardCollection 在线重分片
- **原理**：重分片代价大（全量数据重写），所以分片键决策前置评审，4.2 前只能在导出重导入
- **常见误区**：
  1. 分片键随时可改（错）
  2. refine 与 reshard 是同一功能（错）
  3. 5.0 前也能在线改分片键（错）
- **工程用法**：分片键演进知识
- **版本锚点**：官方文档
