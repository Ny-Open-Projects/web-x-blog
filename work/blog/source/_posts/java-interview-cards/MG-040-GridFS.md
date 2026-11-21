---
title: "[MG-040] 大文档·GridFS（GridFS）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 大文档 · GridFS（GridFS）

- **事实**：超 16MB 大文件用 GridFS 或对象存储存 URL
- **原理**：GridFS 分块存集合（chunks 255KB/块），代价是查询与管理复杂，现代方案倾向对象存储（OSS/S3）+文档存 URL
- **常见误区**：
  1. GridFS 是唯一方案（错）
  2. GridFS 自动压缩（错）
  3. 16MB 限制包含索引（错）
- **工程用法**：大文件架构选型
- **版本锚点**：官方文档
