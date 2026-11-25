---
title: [AGT-209] RAG 检索失败诊断——"该召回的没召回"怎么排查？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-209：用户明明库里有的知识却没被召回——检索失败怎么诊断？

**答**:
- 先定位失败层：用已知答案做金标测试——文档在库里吗（索引缺失）、在但没召回（检索层问题）、召回但没用上（上下文/生成层问题）——三层分开诊断，不做笼统"RAG 不准"。
- 检索层常见病因：embedding 模型与领域不匹配（专业术语语义漂移）、分块切碎了证据（证据跨块）、query 改写把意思改丢了、过滤条件太严（权限/时间过滤错杀）、ANN 的 top-k 太浅或近似度参数太激进。
- 诊断工具：失败样本集（金标 query→应召回的文档 ID）跑离线评测，看 recall@k 与 MRR；对单条失败做人工回放（看召回列表排名、看块内容、看过滤条件）——把 RAG 当搜索系统调优，有指标有回放。
- 修复优先级：数据层（分块/元数据/embedding 选型）> 检索层（混合检索/rerank/k 调大）> 查询层（改写/澄清）——越往上游修收益越大。

```javascript
// 检索失败诊断脚本
async function diagnose(query, goldDocId) {
  const raw = await vectorSearch(query, { k: 100, noFilter: true });
  const rank = raw.findIndex(d => d.id === goldDocId);
  if (rank === -1) return '索引/分块问题：金标块不在候选';
  if (rank >= 50) return 'embedding 相关性弱：排名靠后，考虑 rerank/换模型';
  const filtered = await vectorSearch(query, { k: 50 });
  if (!filtered.some(d => d.id === goldDocId))
    return '过滤问题：filter 把金标滤掉了';
  return '上下文/生成层问题：召回正常，查 prompt 与答案合成';
}
```
