---
title: [RBL-868] 迁移复盘：AI 辅助迁移的新范式——LLM 在配置翻译与语义判断中的位置
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-868：迁移复盘：AI 辅助迁移的新范式——LLM 在配置翻译中的位置

**答**:
- LLM 在迁移管线中的合理位置：1) **规则库写不出来时的兜底翻译**（规则引擎覆盖 80%，LLM 对剩余 20% 给候选翻译 + 置信度——低置信进人工清单 RBL-666）；2) **语义解释器**（把 diff 报告翻译成业务语言给 owner 签核 RBL-802）；3) 考古助手（解释老配置的历史意图，辅助 git blame 归因 RBL-861）。不合理的位置：确定性路径（正则/AST 能做的用 LLM 是把确定问题随机化）。
- LLM 输出的验证纪律：LLM 翻译的配置必须过「语义 diff 验证」（构建对比 RBL-649）——LLM 会自信地写错；验证基建是 AI 参与的前提（没有 diff 验证 = LLM 翻译不可用）。
- 上下文工程：给 LLM 的材料是「结构化上下文」（配置片段 + 工具文档摘录 + 规则库相似案例 RBL-781 的 AI 上下文裁剪）——上下文质量决定输出质量，不是 prompt 技巧。
- 成本与一致性的权衡：LLM 翻译有随机性（同输入不同输出）——迁移要「确定性优先」：规则引擎确定性、LLM 兜底且输出要缓存（同配置片段只问一次）。
- 追问钩子：为什么「LLM 兜底」比「LLM 主力」的架构更可靠？——规则引擎覆盖的 80% 是确定性的（可测试可复现），LLM 的 20% 每条都有验证闸门（语义 diff）；反过来 LLM 主力意味着 80% 的翻译质量依赖模型稳定性（版本升级行为漂移）；架构上「确定性优先 + AI 兜底 + 验证闸门」三层防线让 AI 参与不降低系统可靠性——这也是 AIC/AI 工程化的通用模式在构建迁移的应用。

```javascript
// LLM 兜底翻译管线
async function translateConfig(config, { rules, llm, verifier }) {
  const report = { rules: [], llm: [], manual: [] };
  const { config: out, unmatched } = ruleTranslate(config, rules);   // RBL-666 规则先行
  for (const item of unmatched) {
    const ctx = buildContext(item, { docs: TOOL_DOCS, similar: ruleLibrary.similar(item) });
    const cand = await llm.translate(ctx);             // LLM 兜底
    const verified = await verifier.verify(cand);      // 语义 diff 验证闸门
    if (verified.confidence > 0.9) report.llm.push({ ...cand, verified: true });
    else report.manual.push({ item, candidate: cand, reason: verified.reason });
  }
  return report;                                       // 规则确定性 + AI 兜底 + 人工闸门
}
// 输出缓存（确定性优先）
const llmCache = new Map();
const cachedTranslate = (ctx) => llmCache.get(ctx) ?? llm.translate(ctx).then(v => (llmCache.set(ctx, v), v));
```
