---
title: [AIC-104] AI 时代 CODEOWNERS 机制有什么新含义？「AI 产出的归属路径」怎么设计？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-104：AI 时代 CODEOWNERS 机制有什么新含义？「AI 产出的归属路径」怎么设计？
**答**：
- 新含义：CODEOWNERS 原本解决「人改了谁的地盘谁来审」，AI 时代追加一层——「AI 生成的代码进入谁的目录，谁的 review 标准就生效」，owner 需要知道本目录的 AI 使用强度。
- 归属路径设计：AI 产出的代码必须落在有明确 owner 的目录（禁止 AI 往 orphan 目录塞代码）；agent 目录（自动化产出）独立标记，owner 可对其设置更严格的门禁（AIC-050 的意见阈值）。
- 责任绑定：merge 权限始终在 owner 手里，AI 只能开 PR——保证「每个目录都有人对其 AI 产出负责」，避免责任稀释。
- 实践：CODEOWNERS 增加注释字段标注「本目录 AI 允许范围」（如 ui/ 允许生成组件骨架，payment/ 仅允许生成测试）。
- 追问钩子：这题考的是「组织设计如何回应技术变化」——答案核心是把 AI 视为「无编制的实习生」，每个 owner 都要带教。

```gitignore
# CODEOWNERS（AI 时代扩展版）
/packages/ui/            @fe-core    # AI: 允许生成组件+测试
/packages/payment/       @pay-team   # AI: 仅允许生成测试，实现必须人工
/ai-generated/           @fe-core    # AI: 自动产出暂存区，转正需人工迁出
```
