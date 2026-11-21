---
title: [AIC-117] 「AI 产出的可追溯性」具体指什么？怎么在 Git/CI 里落地标记方案？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-117：「AI 产出的可追溯性」具体指什么？怎么在 Git/CI 里落地标记方案？
**答**：
- 定义：任何一段代码都能回答「是不是 AI 生成的、用什么工具、基于什么任务、谁验收的」——这是合规（AIC-056）、事故复盘（AIC-080）、度量（AIC-074）的共同前提。
- Git 落地：commit message 尾部带结构化 trailer——`Co-authored-by: cursor-agent <agent@corp>` + `AI-Task: AIC-1234`；业界通用 trailer 可被工具链识别。
- CI 落地：CI 脚本解析 trailer 生成「AI 产出索引」（文件 × 提交 × 任务），供统计与回溯查询；PR 模板加「AI 生成范围」段让提交人自我声明。
- 粒度权衡：commit 级标记便宜但粗（人机混合提交），行级标记（IDE 插件记录）最准但维护成本高——务实选择 commit 级 + 高风险模块人工标注。
- 追问钩子：标记不是为了「监控人」，是为了事故归因与效果度量——表达这点能避免制度被抵触。

```text
commit 示例（可追溯标记规范）：
feat(goods): 支持批量导出

Co-authored-by: cursor-agent <agent@corp>
AI-Task: TICKET-8821
AI-Scope: packages/goods/export.ts (生成), 手写: index.ts
```
