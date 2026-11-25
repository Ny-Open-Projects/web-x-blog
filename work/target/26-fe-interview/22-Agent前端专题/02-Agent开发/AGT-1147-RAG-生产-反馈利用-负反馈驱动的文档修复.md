---
title: [1147] 用户负反馈怎么驱动「文档本身」的修复
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 反馈]
type: 面试题
---

## 1147：用户负反馈怎么驱动「文档本身」的修复

**答**：
- 负反馈的根因常是「文档写得不适合被检索/被引用」：关键信息埋在长段落深处、术语与用户用词不一致、一页讲多件事。修复文档比调检索参数更治本。
- 修复管道：负反馈 → 归因（知识缺口/表述问题/结构问题）→ 生成修复建议（LLM 起草「本段应补充…」「术语应统一为…」）→ 文档 owner 确认修改 → 变更进评估回归。
- 闭环指标：「修复后该类 query 的负反馈率下降幅度」——文档修复的 ROI 用这个度量，防止修了一堆没人问的文档。
- 追问钩子：文档 owner 不响应怎么办？——负反馈率超阈值的文档自动升级（抄送 owner 上级/进技术债清单），且该文档检索降权（宁可不命中也不给用户坏答案）。

```ts
async function docFeedbackLoop(fb) {
  const root = await triage(fb);            // 缺口/表述/结构
  if (root.kind !== 'knowledge_gap') {
    const suggestion = await llm(fixPrompt(root.doc, fb));
    await ticket(owner(root.doc), { suggestion, priority: fbRate(root.doc) });
    if (fbRate(root.doc) > 0.3) demote(root.doc);   // 高负反馈降权
  } else {
    await kbGapQueue.push(fb);                       // 缺口走补文档
  }
}
```
