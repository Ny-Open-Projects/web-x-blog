---
title: [1091] 攻击者向知识库塞投毒文档，怎么检测
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, RAG投毒]
type: 面试题
---

## 1091：攻击者向知识库塞投毒文档，怎么检测

**答**：
- 攻击面：能写入知识库的通道（用户上传、爬虫、第三方同步）都是投毒入口；投毒文档特征：内容看似正常但埋「针对性指令」或「误导性事实」，命中后污染所有相关回答。
- 检测三层：入库审查（新文档过「指令特征扫描 + 与既有知识冲突检测」——新文档断言与高置信既有文档矛盾即为可疑）、行为监控（某文档被召回后答案偏离基线的比例突升）、溯源审计（答案引用链回溯到可疑文档）。
- 防御根基：写入通道权限收敛（只有可信来源可直写，用户内容进「待审区」）——比检测更根本。
- 追问钩子：为什么「冲突检测」对事实类投毒有效？——投毒要影响回答必须提供「替代事实」，而替代事实几乎必然与既有可信内容矛盾，矛盾是投毒的影子。

```ts
async function ingestGuard(doc) {
  if (hasInjectionPatterns(doc.text)) return quarantine(doc, 'instruction');
  const conflicts = await conflictCheck(doc, highConfidenceCorpus);
  if (conflicts.length > 3) return quarantine(doc, 'fact_conflict'); // 多处矛盾
  return promote(doc);
}
// 行为监控：召回该文档的回答与基线 diff
monitor.on('answer', a => { if (a.cites.has(suspectId)) diffAgainstBaseline(a); });
```
