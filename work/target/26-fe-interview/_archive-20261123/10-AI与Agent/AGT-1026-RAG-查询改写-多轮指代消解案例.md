---
title: [1026] 多轮对话里「它」「上面说的」检索失败，查询改写怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 查询改写]
type: 面试题
---

## 1026：多轮对话里「它」「上面说的」检索失败，查询改写怎么做

**答**：
- 根因：检索器拿到的 query 是「它支持灰度吗」，缺少指代对象——改写模块用小模型把「当前 query + 最近对话」融合成自足 query（「Next.js 中间件支持灰度发布吗」），检索命中率立刻回升。
- 改写策略分级：指代消解（必须）→ 意图补全（补隐含约束）→ 分解（复合问题拆多路检索）；逐级开，按评估数据决定开到哪级。
- 改写失败的兜底：改写后与原 query 语义距离过大（漂移）时双路检索（原 query + 改写 query）取融合结果，防改写跑偏。
- 追问钩子：改写用大模型还是小模型？——小模型 + 精简 prompt 足够（指代消解不需要推理深度），改写是延迟敏感环节，控制在 300ms 内。

```ts
async function rewrite(query, history) {
  const rw = await llm(rewritePrompt(query, history.slice(-3)), { model: 'small' });
  if (await similarity(rw, query) < 0.4) {          // 漂移检测
    return rrfFuse([search(query), search(rw)], [1, 1], 10); // 双路兜底
  }
  return search(rw);
}
```
