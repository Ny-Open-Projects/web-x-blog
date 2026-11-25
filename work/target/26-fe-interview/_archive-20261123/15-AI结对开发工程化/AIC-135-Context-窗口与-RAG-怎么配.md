---
title: [AIC-135] 编码场景里「上下文窗口」和「RAG 检索」怎么配合？什么时候该建向量库？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-135：编码场景里「上下文窗口」和「RAG 检索」怎么配合？什么时候该建向量库？
**答**：
- 优先级判断：代码任务的上下文供给首选**确定性检索**（import 图、grep、依赖闭包——AIC-028/113），因为代码结构是精确的；RAG（语义检索）用在「非结构化知识」——文档、issue、历史决策、聊天记录。
- 什么时候建向量库：知识规模超过「贴得下」的范围（数千文档）、查询是语义化的（「上次支付超时怎么解决的」）、且知识更新频率可控。代码本身不建议向量化检索——结构化手段更准。
- 配合模式：规则文件/代码地图先给「骨架」，确定性检索给「代码事实」，RAG 给「经验与文档」，三者按窗口预算分层注入（AIC-099）。
- RAG 质量坑：切片过碎丢上下文、检索召回但模型不用、知识过期仍在库里（要配失效机制，AIC-082 的记忆遗忘问题）。
- 追问钩子：面试答「先穷尽简单手段再上 RAG」是成熟信号——多数团队的问题是直接上向量库而没做好 grep 和依赖图。

```javascript
// 三层上下文供给策略
async function gatherContext(task) {
  const skeleton = read('ai/CODEMAP.md');                    // 骨架层
  const code = dependencyClosure(task.files, { sigOnly: true }); // 确定性层
  const knowledge = task.needsExperience
    ? await rag.search(task.query, { topK: 3, filter: { fresh: true } }) // 语义层
    : '';
  return [skeleton, code, knowledge].filter(Boolean).join('\n');
}
```
