---
title: [AIC-287] CLI 型 Agent（Claude Code/Aider）与 IDE 型（Cursor/Copilot）的能力边界与组合用法？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-287：CLI 型 Agent（Claude Code/Aider）与 IDE 型（Cursor/Copilot）的能力边界与组合用法？
**答**：
- IDE 型强在交互式编辑与即时反馈（补全/局部重构/看 diff），适合日常编码。
- CLI 型强在自治执行长任务（跨文件重构/批量迁移/CI 修复），可无头运行进流水线。
- 组合模式：IDE 做日常开发，CLI 跑批量任务与 CI 中的自动修复，同一套规则文件共享。
- 安全差异：CLI 自治执行需要更严的沙箱与命令白名单。

```javascript
const combo = {
  ide: { use: ['补全', '小重构', 'review 反馈'], guard: '人工逐步确认' },
  cli: { use: ['批量迁移', 'CI 失败修复', '大范围重命名'],
         guard: ['命令白名单', 'git 沙箱分支', 'diff 上限审批'] },
  shared: '.cursor/rules 同时被两家读取（标准 md 格式）',
};
r
```
