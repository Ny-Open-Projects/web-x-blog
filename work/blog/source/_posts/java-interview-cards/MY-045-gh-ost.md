---
title: "[MY-045] DDL·gh-ost（大表）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## DDL · gh-ost（大表）

- **事实**：大表 DDL 变更用 gh-ost/pt-online-schema-change：影子表+增量同步+原子改名
- **原理**：直接 DDL 主从延迟与 MDL 风险大，工具建影子表拷数据、捕获增量（binlog/触发器）、锁表窗口极短，是行业标准做法
- **常见误区**：
  1. 大表 DDL 用 ALTER 直接执行即可（错）
  2. gh-ost 使用触发器同步（其卖点恰是免触发器）（错）
  3. 影子表方案会长时间锁表（错）
- **工程用法**：生产 DDL 变更流程
- **版本锚点**：gh-ost 文档
