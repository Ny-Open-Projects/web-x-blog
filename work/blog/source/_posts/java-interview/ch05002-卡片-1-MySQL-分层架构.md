---
title: "卡片 1：MySQL 分层架构"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 1：MySQL 分层架构
连接器（认证/连接池）→ 分析器（词法/语法）→ 优化器（选索引/join 顺序）→ 执行器（调存储引擎接口）→ **InnoDB 存储引擎**。
记忆：Server 层管"语法与计划"，引擎层管"数据怎么存"。
