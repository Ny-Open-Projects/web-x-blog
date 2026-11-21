---
title: "[MG-072] 副本集·initial sync（同步）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · initial sync（同步）

- **事实**：新成员 initial sync（全量同步）：选源→拷贝集合→建索引→追 oplog
- **原理**：拷贝期间源负载高（选低峰），索引重建耗时（集合大时小时级），完成后进入 oplog 增量追平
- **常见误区**：
  1. 新成员自动增量同步（错）
  2. initial sync 很快（错）
  3. 不建索引直接服务（错）
- **工程用法**：扩容操作细节
- **版本锚点**：官方文档
