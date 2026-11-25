---
title: [AIC-258] AI 评审与 ESLint/类型检查/安全扫描如何在 CI 里分工与串联？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-258：AI 评审与 ESLint/类型检查/安全扫描如何在 CI 里分工与串联？
**答**：
- 顺序串联：先跑确定性工具（快、准、便宜），失败直接打回——AI 只看确定性工具通过的 diff。
- 结果互证：静态工具告警项让 AI 复核降误报（如 deprecated API 是否有降级路径）。
- AI 负责静态工具做不到的：业务逻辑漏洞、跨文件影响、测试缺失判断。
- 报告合并去重：同一位置多来源告警合并为一条，标注来源与置信度。

```javascript
const pipeline = async (pr: PR) => {
  const det = await runDetectors(pr);   // eslint/tsc/semgrep：先跑且必须过
  if (det.length) return reject(det);
  const aiFindings = await aiReview(pr.diff);          // 语义层
  const merged = mergeFindings(det.warns, aiFindings); // 去重合并输出
  return verdict(merged);
};
r
```
