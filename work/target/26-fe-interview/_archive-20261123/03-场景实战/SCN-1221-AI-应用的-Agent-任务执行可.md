---
title: [SCN-1221] AI 应用的 Agent 任务执行可视化
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1221：AI 应用的 Agent 任务执行可视化

**答**：
- 可视化：Agent 多步任务（规划→执行→反思循环）步骤时间线实时展示。
- 透明：每步展示（工具调用/中间结果），失败步骤展开错误详情。
- 控制：执行中可暂停/取消（任务级），完成后总结报告。

```javascript
// Agent 可视化
class AgentRunner {
  renderStep(step) {                                  // step: { type, name, status }
    return { timeline: [...this.timeline, step],
      active: step.status === 'running',
      detail: step.status === 'failed' ? step.error : summarize(step.result) };
  }
  pause() { return api('/agent/pause', { runId: this.runId }); }
  cancel() { return api('/agent/cancel', { runId: this.runId }); }
}
function summarize(r) { return JSON.stringify(r).slice(0, 100); }
```
