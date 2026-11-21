---
title: [AIC-226] 一个 PR 改了 80 个文件，AI 评审如何处理大 diff 才不会丢细节？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-226：一个 PR 改了 80 个文件，AI 评审如何处理大 diff 才不会丢细节？
**答**：
- 分块策略：按模块/目录切分 diff，逐块评审后汇总，避免单次上下文塞不下。
- 两级评审：先全局摘要级（影响面、模块拓扑变化），再局部细节级（每块的具体问题）。
- 摘要级结果指导细节级优先级：高风险模块深审，机械改动浅审。
- 汇总时去重与合并，输出统一报告并标注每条发现的文件定位。

```javascript
async function reviewBigDiff(files: string[]) {
  const chunks = groupByModule(files, { maxLines: 1500 });
  const global = await llm(`输出本次变更的全局拓扑摘要与高风险模块：${files}`);
  const findings = [];
  for (const c of chunks.sort(byRisk(global))) {
    findings.push(...await llm(`仅评审本块：${c.diff}，上下文摘要：${global}`));
  }
  return dedupe(findings);
}
r
```
