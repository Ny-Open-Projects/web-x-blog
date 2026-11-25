---
title: [922] 新知识库上线没有评估集，冷启动怎么做
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 冷启动]
type: 面试题
---

## 922：新知识库上线没有评估集，冷启动怎么做

**答**：
- 三步走：文档结构反推（目录/FAQ 天然成题）→ LLM 按章节生成候选问题（每节 2~3 问，覆盖事实与流程两类）→ 人工快速过一遍剔除「文档里根本没答案」的坏题。
- 生成的题要带「答案出处 chunk 引用」，否则后续没法算检索指标；人工抽检比例不低于 20%。
- 冷启动指标红线：上线前评估集准确率不低于 0.75、拒答场景不产生幻觉即可放量，别追求完美，真实验证靠灰度流量观察。
- 追问钩子：上线后怎么发现评估集没覆盖的问题类型？——线上 query 聚类，簇大小超过阈值且簇内负反馈率高，就是新的出题方向。

```ts
async function seedQuestions(doc) {
  const cases = [];
  for (const chunk of chunkDoc(doc)) {
    for (const q of await llm('基于以下内容出2个用户可能问的问题，附答案与原文引用：\n' + chunk.text)) {
      cases.push({ query: q.question, goldAnswer: q.answer,
        evidence: [chunk.id], intent: q.kind, source: 'synthetic' }); // 标记为合成题
    }
  }
  return humanReview(cases, { sampleRate: 0.2 });
}
```

