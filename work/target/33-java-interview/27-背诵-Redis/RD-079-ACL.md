---
title: "[RD-079] 安全·ACL（ACL）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 安全 · ACL（ACL）

- **事实**：Redis 6.0 ACL 用户级权限（按命令/key 前缀授权）
- **原理**：替代旧版 requirepass 全局密码，多应用共享实例可分权，生产还需 bind 内网+rename 危险命令（FLUSHALL）
- **常见误区**：
  1. ACL 是 7.0 特性（错）
  2. Redis 默认无密码安全（错）
  3. rename 命令是安全最佳实践（配合 ACL 更好）（错）
- **工程用法**：安全基线
- **版本锚点**：Redis 6.0
