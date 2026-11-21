---
title: "[JA-109] Spring AI·media（多模态）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · media（多模态）

- **事实**：Spring AI 多模态输入：user 消息可附 Media（图片等），模型侧需多模态能力支持
- **原理**：Java 侧组装多模态消息（AI-041 联动），图像按分辨率折算 token（AI-080 计费联动），文本与图像同请求发送
- **常见误区**：
  1. 多模态只能发文本（错）
  2. 图片必须先 OCR 成文字（错）
  3. media 参数不存在（错）
- **工程用法**：图文理解接入
- **版本锚点**：Spring AI 1.0 GA
