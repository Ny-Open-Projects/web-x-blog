---
title: [ENG-059] 如何在团队内规范化使用 Copilot / Cursor 等 AI 编码工具？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-059：如何在团队内规范化使用 Copilot / Cursor 等 AI 编码工具？
**答**：
- 用项目内规则文件约束 AI：GitHub Copilot 用 copilot-instructions.md，Cursor 用 .cursor/rules，内容写清技术栈与禁令。
- 工作流上"先方案后代码"：让 AI 先给出实现思路与影响面，确认后再生成，减少大段返工。
- 生成代码走与人工代码完全相同的门禁：lint、typecheck、test、code review，一个都不能省。
- 约定透明度：AI 参与的改动在 PR 描述中说明，review 时重点关注边界条件与安全。

```yaml
# .cursor/rules/frontend.mdc
---
description: 前端代码生成规范
alwaysApply: true
---
- TypeScript 严格模式，禁止 any 与滥用类型断言
- 组件使用函数组件加 Hooks，遵循项目现有目录结构
- 不引入新依赖，不修改与任务无关的文件，不臆造不存在的 API
- 新增工具函数必须附带 Vitest 单测
- 提交信息遵循 Conventional Commits 规范
```
