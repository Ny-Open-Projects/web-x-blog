---
title: [AGT-534] AI 对话页的体验度量体系怎么搭（技术指标+产品指标+质量指标）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-534：AI 对话页的体验度量体系怎么搭（技术指标+产品指标+质量指标）

**答**：
- 技术层：首 token 时间、生成速率（token/s）、流中断率、错误率按错误码分布、页面性能（INP/内存）。
- 产品层：采纳信号（复制/点赞/继续追问/重新生成率）、任务完成率（Agent 场景：目标达成而非满意度）、留存与频次。
- 质量层：抽检评分、负反馈率与标签分布、引用准确率；三层指标用同一 traceId 打通，能从"用户点踩"下钻到"哪个环节耗时/什么模型版本"。

```javascript
// 统一轮次上报：三层指标共享 traceId
function reportTurn(turn, signals) {
  track('turn_summary', {
    traceId: turn.traceId,
    tech: { ttft: turn.ttft, tps: turn.tokensPerSec,
      aborted: turn.aborted, errCode: turn.errCode },
    product: signals,                     // copy/like/regen/followUp
    quality: { cited: turn.sourcesCount, feedback: turn.feedbackTags },
  });
}
```

