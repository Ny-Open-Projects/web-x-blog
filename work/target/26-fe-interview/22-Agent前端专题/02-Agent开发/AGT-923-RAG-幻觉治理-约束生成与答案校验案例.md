---
title: [923] RAG 幻觉率从 12% 降到 3% 的完整案例怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 幻觉]
type: 面试题
---

## 923：RAG 幻觉率从 12% 降到 3% 的完整案例怎么做

**答**：
- 先归因再动手：badcase 复盘发现 70% 幻觉来自「检索不足时模型硬答」，20% 来自「多源冲突时模型自己挑」，10% 才是纯生成失控——治理重点不在 prompt 措辞。
- 约束生成三件套：system prompt 显式规定「仅基于给定材料」「材料冲突时列出各方说法」；生成时 top_p 收紧；拒答模板固定。
- 答案校验层：抽取答案中的事实句与来源做蕴含校验（小模型打分），不蕴含的句子替换为「未在材料中找到」或整条降级。
- 数字双盲：对时间、金额、百分比做正则抽取后与来源比对，数字类幻觉零容忍。
- 追问钩子：校验层误杀怎么办？——同义改写导致蕴含分偏低，允许「来源同义改写」白名单通道，误杀率控制后再收紧阈值。

```ts
async function guardedAnswer(q, hits) {
  const ans = await llm(genPrompt(q, hits), { temperature: 0.2 });
  const facts = extractFactSentences(ans);        // 含数字/结论的句子
  for (const f of facts) {
    const ok = await entail(f, hits.map(h => h.text));  // 蕴含校验
    if (!ok && !isParaphrase(f, hits)) {          // 同义改写豁免
      return degrade(ans, f);                     // 替换/降级，并计入幻觉率
    }
  }
  return ans;
}
```

