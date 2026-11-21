---
title: [AIC-129] 「Agent 友好的仓库」长什么样？新项目可以从哪些约定开始为 AI 铺路？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-129：「Agent 友好的仓库」长什么样？新项目可以从哪些约定开始为 AI 铺路？
**答**：
- 核心特征：可判定性——agent 能自己验证对错（测试齐全、类型严格、lint 强制）、可导航性（CODEMAP、清晰目录语义）、可约束性（规则文件就位、禁区明确）。
- 起步约定清单：① 严格 TS 配置 ② 测试即文档——测试命名用行为描述 ③ 单一构建/测试命令入口（package.json scripts 规范命名）④ 顶层 README 给出「模块职责一句话表」⑤ 规则文件从第一天就存在（不要等痛了再补）。
- 反 agent 仓库特征：魔法字符串路由、隐式全局状态、非标准目录结构、需要「老人知识」才能构建——这些同样对人类新人不友好，agent 友好 ≈ 新人友好。
- 度量：「agent 一次通过率」按目录统计，低通过率目录通常是结构混乱区——agent 成了代码健康的探测器。
- 追问钩子：「为 AI 铺路」的本质是偿还欠人类的工程债——两者的改善方向高度一致。

```json
// package.json：统一命令入口（agent 与新人都按约定找命令）
{
  "scripts": {
    "dev": "vite",
    "test": "vitest run",
    "test:related": "vitest run --related",
    "lint": "eslint . --max-warnings 0",
    "typecheck": "tsc --noEmit",
    "verify": "npm run typecheck && npm run lint && npm run test"
  }
}
```
