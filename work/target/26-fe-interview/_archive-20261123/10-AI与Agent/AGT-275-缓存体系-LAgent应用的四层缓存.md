---
title: [AGT-275] 缓存体系——LLM 应用的四层缓存怎么设计？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-275：LLM 应用的缓存有哪些层——各自的 key 与失效策略？

**答**:
- 四层缓存：精确缓存（相同 prompt+参数 → 相同答案，key=请求 hash，适合确定性任务如分类/改写）、语义缓存（query embedding 相似度超阈值 → 复用答案，适合 FAQ/搜索类，需防"相似但不同意图"误命中）、前缀缓存（AGT-224，模型侧 KV 复用，降输入费）、工具/检索缓存（相同检索 query → 相同召回，工具结果缓存——RAG 与 Agent 都高频命中）。
- 语义缓存的坑：相似度阈值难调（0.92 相似但语义相反的问句会误命中）——缓解：命中后带"缓存答案"提示重新生成校验，或对数值/时间敏感问题禁用语义缓存；失效策略：知识更新时按文档版本联动清缓存。
- 一致性设计：缓存 key 必须包含所有影响输出的因子（prompt 版本/模型版本/检索版本/用户权限）——缺一个因子就是错答事故（不同权限用户共享答案=越权泄露）。
- 收益度量：各层命中率与节省金额分开统计——命中率低的层及时下线，别留着一个维护成本高于收益的缓存。

```javascript
async function cachedLLM(req) {
  const key = hash(req.prompt, req.model, req.promptVer,
                   req.user.acl);              // 全因子入 key
  if (exact.has(key)) return exact.get(key);
  const sem = await semanticHit(req.prompt, { acl: req.user.acl });
  if (sem && sem.score > 0.95 && !req.numericSensitive)
    return sem.answer;                          // 语义命中
  const ans = await llm(req);
  exact.set(key, ans, { ttl: 3600 });
  return ans;
}
```
