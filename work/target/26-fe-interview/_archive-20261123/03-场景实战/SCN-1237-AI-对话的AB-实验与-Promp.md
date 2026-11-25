---
title: [SCN-1237] AI 对话的A/B 实验与 Prompt 版本管理
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1237：AI 对话的A/B 实验与 Prompt 版本管理

**答**：
- 实验：Prompt 版本 A/B（分流 uid），指标（满意度/负反馈率/成本）对比。
- 管理：Prompt 版本库（变更记录/回滚），灰度发布。
- 监控：新版本上线后负反馈率监控（劣化自动回滚）。

```javascript
// Prompt A/B
function promptExperiment(uid, versions) {
  const bucket = hash(uid) % versions.length;
  const v = versions[bucket];
  return { prompt: v.text, version: v.id,
    monitor: { metric: 'negative-rate', baseline: versions[0].metrics },
    rollback: () => switchPrompt(versions[0].id) };
}
function hash(s) { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; }
```
