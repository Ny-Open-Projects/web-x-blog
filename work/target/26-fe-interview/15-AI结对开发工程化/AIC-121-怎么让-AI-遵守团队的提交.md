---
title: [AIC-121] 怎么让 AI 遵守团队的提交规范与分支策略？「AI 不守规矩」的治理层级有哪些？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-121：怎么让 AI 遵守团队的提交规范与分支策略？「AI 不守规矩」的治理层级有哪些？
**答**：
- AI 不守规矩的典型：直接 push 主干、commit 信息乱写、把实验代码混进正式提交、绕过 PR 开权限。
- 治理层级（由强到弱）：① 系统层——CI/分支保护规则直接拒绝（主干禁止 push、commit 格式校验 AIC-039、trailer 校验 AIC-117），这是唯一可靠的层 ② 配置层——agent 权限配置收走 push 权限、锁定分支命名（AIC-096）③ 规则层——规则文件写清流程约定（软约束，会被无视但仍有用）。
- 核心认知：AI 的行为约束必须落「系统层」才真正生效——规则文件是教育，CI 是执法；所有流程类要求先问「CI 能不能拦」。
- 分支策略：agent 固定分支前缀 `agent/*`，便于权限区分（自动合入白名单目录）与统计回滚（AIC-097）。
- 追问钩子：答案的高分点在「不要指望 prompt 解决流程问题」——prompt 治理行为，系统治理结果。

```javascript
// commit-msg hook：AI 产出也必须合规（系统层执法）
const trailerRe = /AI-Task:\s*\S+/;
const msg = read('.git/COMMIT_EDITMSG');
if (git.branch().startsWith('agent/') && !trailerRe.test(msg)) {
  console.error('agent 分支提交必须携带 AI-Task trailer');
  process.exit(1);
}
```
