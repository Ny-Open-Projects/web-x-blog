---
title: "[MG-087] 备份·--oplog（一致性）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 备份 · --oplog（一致性）

- **事实**：mongodump 加 --oplog 捕获备份期间变更，恢复时重放保证一致性快照
- **原理**：备份耗时段内新写入若不捕获，恢复后数据不一致（引用关系断裂），--oplog 让 dump 与恢复点一致，大库备份标配
- **常见误区**：
  1. mongodump 天然一致（备份耗时有写入就不一致）（错）
  2. --oplog 是可选可不加（错）
  3. 恢复不需要重放 oplog（错）
- **工程用法**：备份一致性方法论
- **版本锚点**：实战共识
