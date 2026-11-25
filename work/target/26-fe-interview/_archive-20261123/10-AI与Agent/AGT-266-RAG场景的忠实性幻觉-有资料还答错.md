---
title: [AGT-266] RAG 的忠实性幻觉——资料明明给了为什么还答错？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-266：资料已提供，模型为什么还产生与资料矛盾的答案？怎么治？

**答**:
- 常见成因：资料内部冲突（两份文档说法不一，模型擅自取舍不声明）、资料与参数知识冲突（模型"更相信自己知道的"）、多资料拼接错误（时间/主体张冠李戴）、指令冲突（用户要求简洁导致模型丢限定条件）。
- 治理手段一（生成对齐）：prompt 明确"答案只基于提供的资料，资料与你的知识冲突时以资料为准并注明"，要求逐句可溯源（AGT-262）——对齐指令配合引用校验形成闭环。
- 治理手段二（冲突显式化）：资料入库时打时效与权威标签，检索结果按权威度排序；生成时把"冲突提示"喂给模型（"以下两份资料在 X 上矛盾"），要求呈现分歧而非擅自合并。
- 治理手段三（事后校验）：忠实性评测（答案与资料的一致性 judge + 数字/实体程序比对）做抽样监控——忠实性幻觉是 RAG 上线后最常见的质量投诉源，必须有持续监控。

```javascript
async function groundedAnswer(query, docs) {
  const conflicts = detectConflicts(docs);      // 资料间冲突
  const out = await llm(`只基于资料作答；资料与
    你的知识冲突时以资料为准；发现资料间矛盾
    时呈现分歧。冲突提示:${conflicts}`, { query, docs });
  const audited = await factAudit(out, docs);   // 数字/实体比对
  return audited.pass ? out : repair(out, audited.diff);
}
```
