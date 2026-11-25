---
title: [AIC-885] 大家用 AI 总结的经验散落在各自聊天记录里，怎么沉淀成组织资产？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-885：大家用 AI 总结的经验散落在各自聊天记录里，怎么沉淀成组织资产？
**答**：
- 散落的根因是**沉淀成本高于复用收益**：把一段有用的 AI 对话整理成文档要花时间，而「下次再用 AI 重新问一遍」似乎更省事——于是知识反复产生又反复丢失。
- 降低沉淀成本：提供**一键沉淀**——把优质 AI 会话/提示词一键发布到团队知识库，自动生成摘要、标签、适用场景；工具要嵌入工作流（在 IDE/聊天工具里就能发布），而不是「另开一个系统填表」。
- 知识要有**结构与归属**：每条沉淀含「问题场景 + 可复用 prompt/方法 + 效果证据（评测数据）+ owner + 有效期」；按场景标签组织，可被搜索；owner 负责更新，过期归档。
- 闭环激励：让沉淀可度量价值（被复用次数、节省的时间），复用时自动标注来源——贡献者获得可见的回馈（呼应能力市场 AIC-869）。**沉淀进规则文件/模板**是最有效的形式，因为它会在下次 AI 协作时自动生效。
- 追问钩子：能说出「沉淀的最佳载体是规则文件与模板（自动生效），而非需要人主动查阅的文档库」的候选人，理解了知识要进入工作流才有生命力。

```typescript
type Artifact = { id: string; scene: string; prompt: string; evidence?: string;
  owner: string; createdAt: number; reused: number };

function publishArtifact(session: any): Artifact {
  return {
    id: crypto.randomUUID(),
    scene: session.tags?.[0] ?? 'general',
    prompt: session.bestPrompt,                  // 一键提取优质 prompt
    evidence: session.evalScore ? `评测 ${session.evalScore}` : undefined,
    owner: session.author, createdAt: Date.now(), reused: 0,
  };
}
function reuse(a: Artifact) {
  a.reused++; // 复用计数 → 衡量沉淀价值，回馈贡献者
  return a.prompt;
}
// 高价值沉淀进一步写入团队规则文件，使下次 AI 协作自动加载
const art = publishArtifact({ bestPrompt:'长文档先分段再汇总', tags:['doc'], author:'li', evalScore:0.9 });
console.log(reuse(art)); // 被复用，owner 获得可见贡献
```
