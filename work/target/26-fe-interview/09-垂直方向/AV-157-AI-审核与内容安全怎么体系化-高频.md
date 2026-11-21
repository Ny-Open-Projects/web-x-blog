---
title: [AV-157] AI 审核与内容安全怎么体系化？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-157：AI 审核与内容安全怎么体系化？（高频）
**答**：
- 多模态审核：视频帧（色情/暴力/违禁物）、音频 ASR（涉政/辱骂）、文本（弹幕/标题）、封面，各自模型 + 融合仲裁。
- 三级处置：机审高置信直接处置、中置信限流降权（不给推荐）、低置信人工复审队列。
- 直播特性：抽帧频率与成本平衡（1-2s/帧 + 关键帧），音频流式送审；直播与回放分开策略。
- 前端配合：审核状态实时下发（流内提示）、违规片段时间戳回传给主播端警示。
- 度量：机审准确率/召回率、人工复审率（复审比例是成本核心）、误杀申诉成功率。

```json
{
  "moderation-pipeline": {
    "video": { "sample-rate": "1fps加关键帧", "model": "nsfw加violence", "threshold": { "block": 0.9, "review": 0.6 } },
    "audio": { "pipeline": "asr流式转写后文本审核", "latency-target": "<3s" },
    "text": { "scope": ["弹幕", "标题", "评论"], "strategy": "词库加语义模型双通道" }
  },
  "disposal": [
    { "confidence": ">=0.9", "action": "切断流加封禁", "notify": "immediate" },
    { "confidence": "0.6-0.9", "action": "限流且不给推荐", "notify": "async" },
    { "confidence": "<0.6", "action": "人工复审队列", "sla": "10min" }
  ],
  "metrics": { "review-rate-target": "<5%", "appeal-success-rate": "监控误杀" }
}
```

## 二十、综合大题与体系（AV-158 ~ AV-200）
