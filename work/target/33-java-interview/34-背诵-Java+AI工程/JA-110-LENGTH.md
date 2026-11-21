---
title: "[JA-110] 工程·LENGTH（截断）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工程 · LENGTH（截断）

- **事实**：finishReason 为 LENGTH（触达 maxTokens）的业务处理：续写（带已有内容再生成）或截断提示或调大 maxTokens 重试
- **原理**：长文生成被截断是常态，无处理则输出不完整用户可感知，与 JA-077 元数据知识联动
- **常见误区**：
  1. LENGTH 会自动续写（错）
  2. 截断无需处理（错）
  3. LENGTH 是错误状态（错）
- **工程用法**：生成完整性保障
- **版本锚点**：实战共识
