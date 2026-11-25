---
title: [TST-562] 如何用大模型做失败日志的自动归因
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-562：如何用大模型做失败日志的自动归因

**答**：
- 结论：把「日志 + 上下文（最近提交/环境/测试代码）」喂给 LLM，让它输出「根因分类 + 证据 + 置信度 + 建议」，再用置信度门控决定是否自动采纳。
- 做法：先对日志做清洗/截断/错误指纹聚类降噪；Prompt 中给少样本示例与明确分类标签；输出结构化 JSON；低置信度或新指纹转人工。
- 追问钩子：LLM 归因幻觉怎么办？——要求「引用具体日志行作为证据」，用规则校验证据存在性；并对已知错误指纹走确定性规则，只有未知模式才用 LLM。

```javascript
// 归因结果门控：高置信 + 有证据才自动采纳
function routeAttribution(result) {
  const hasEvidence = result.evidenceLines?.length > 0;
  const auto = result.confidence >= 0.8 && hasEvidence && result.category !== 'unknown';
  return { auto, route: auto ? 'auto-close-suggest' : 'human-review',
    reason: auto ? '高置信且有证据' : !hasEvidence ? '缺证据' : '低置信/未知类' };
}
console.log(routeAttribution({ confidence: 0.9, category: 'timeout', evidenceLines: ['L12'] }));
console.log(routeAttribution({ confidence: 0.5, category: 'timeout', evidenceLines: ['L3'] })); // human-review
// 批量路由后按 route 统计，便于看人工复核队列规模
const routed = [{ confidence: 0.9, category: 'timeout', evidenceLines: ['L1'] }].map(routeAttribution);
console.log(routed.filter(r => r.auto).length); // 1
```
