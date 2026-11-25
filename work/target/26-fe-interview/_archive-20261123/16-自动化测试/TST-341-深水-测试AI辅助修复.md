---
title: [TST-341] AI 辅助测试修复（失败自动归因+建议修法）如何设计？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-341：AI 辅助测试修复（失败自动归因+建议修法）如何设计？
**答**：
- 输入三件套：失败用例、trace/日志、最近相关变更——AI 归因（产品 bug/环境/测试问题）。
- 归因输出置信度与证据链，低置信直接转人（不瞎建议）。
- 测试问题类：AI 给修复 patch 建议（如等待不足→加稳定等待），人审后应用。
- 闭环统计：AI 归因准确率追踪，低的场景补充上下文模板。

```javascript
async function aiDiagnose(failure) {
  const r = await llm(`用例：${failure.title}\n错误：${failure.error}
trace 摘要：${failure.traceDigest}\n近期变更：${failure.diffDigest}
归因：impl-bug / env / test-issue，给证据与（若 test-issue）修复建议`);
  return r.confidence > 0.7 ? r : { escalate: true };
}
r
```
