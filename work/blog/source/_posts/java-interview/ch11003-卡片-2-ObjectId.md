---
title: "卡片 2：ObjectId"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 2：ObjectId
文档默认主键 `_id`。现代驱动的 ObjectId = **4 字节秒级时间戳 + 5 字节随机（进程级）+ 3 字节递增计数**——时间戳前缀使其**天然趋势递增**，作为 `_id` 写入分布式友好（类似雪花 ID 的效果）。
