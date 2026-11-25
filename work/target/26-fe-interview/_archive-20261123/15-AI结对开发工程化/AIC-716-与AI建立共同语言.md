---
title: [AIC-716] 结对开发中如何与 AI 建立团队共同语言（术语对齐）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-716：结对开发中如何与 AI 建立团队共同语言（术语对齐）

**答**：
- 结论先行：AI 不理解你们团队的「黑话」（如「中台」「灰度开关」「大促链路」），若不先对齐术语，生成代码会用错概念；解决方式是在规则文件里维护一份「领域术语表」并要求 AI 严格沿用。
- 做法：1) 术语表写明「中文名 ↔ 代码标识符 ↔ 含义 ↔ 反例」；2) 在 prompt 中引用术语表条目而非复述；3) 发现 AI 误用立即纠正并回写术语表。
- 进阶：把术语表做成可被检索的上下文片段，按任务相关度注入，避免整表塞满 token。
- 追问钩子：为什么「纠正后回写术语表」比「每次重新解释」更重要？——回写让一次纠正惠及全团队和后续所有会话，是知识复利。

```javascript
// 术语表：团队黑话到代码标识符的映射
const GLOSSARY = {
  灰度开关: { id: 'featureFlag', meaning: '按比例放量的运行时开关', forbid: ['release', 'debug'] },
  大促链路: { id: 'promoPath', meaning: '大促专属下单流程', forbid: ['normalOrder'] },
};
function alignTerm(text) {
  for (const [term, def] of Object.entries(GLOSSARY)) {
    if (text.includes(term)) return { term, id: def.id, hint: `请使用 ${def.id}，勿用 ${def.forbid.join('/')}` };
  }
  return { term: null };
}
console.log(alignTerm('给灰度开关加个配置')); // 请使用 featureFlag，勿用 release/debug
```
