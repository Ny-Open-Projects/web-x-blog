---
title: "卡片 2：Temperature / Top-p / System Prompt"
date: 2026-11-18
categories: [Java面试, AI与Agent]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 2：Temperature / Top-p / System Prompt
- Temperature：采样随机性。0~0.3 抽取/分类/结构化输出；0.7+ 创意生成。**生产结构化任务建议 0 或低温**。
- System Prompt：全局人设与规则约束；用户消息只放业务输入——**分层管理，规则不混入业务数据**。
- 结构化输出：JSON Mode / Function Calling（严格 schema），别用正则从自由文本里抠 JSON。
