---
title: [AIC-127] 怎么防止 Agent 的破坏性输出（误删文件、误提交、污染共享分支）？多层防线怎么排布？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-127：怎么防止 Agent 的破坏性输出（误删文件、误提交、污染共享分支）？多层防线怎么排布？
**答**：
- 防线排布（外层最可靠）：① Git 层——agent 只能推 agent/* 前缀分支，主干与共享分支 push 保护 ② 文件系统层——工作区快照（任务前 git stash/commit），破坏性命令（rm、reset --hard）白名单外一律拒绝（AIC-009）③ 权限层——agent 运行账号无共享资源写权限 ④ 提示层——规则文件写禁区（最弱，只作教育）。
- 误删恢复前提：任务开始前必做快照点（AIC-083 的绿色基线），任何时刻可 `git reset` 回去；工作区外的文件（如配置）挂只读。
- 误提交检测：CI 扫 agent 分支的 commit 是否混入非白名单文件（如 .env、CI 配置）——超范围即自动打回。
- 关键认知：防线的有效性递减于「离 agent 越近」——prompt 禁令最弱，系统权限最强；配置防线时按「最坏意图」假设 agent 行为。
- 追问钩子：加分点是指出「破坏性输出」的主要来源不是恶意而是「实现冲动」——agent 为达成目标会尝试激进手段，防线要假设它会试。

```javascript
// 破坏性命令拦截 + 超范围文件检测
const destructive = [/^rm\s+-rf?\s/, /git\s+(push|reset)\s+--?hard/, />\/dev\/sda/];
function guardCommand(cmd) {
  if (destructive.some(r => r.test(cmd))) return { allow: false, reason: '破坏性命令，需人工确认' };
  return { allow: true };
}
function checkCommitScope(commit, whitelist) {
  const out = commit.files.filter(f => !whitelist.some(w => f.startsWith(w)));
  return out.length ? { ok: false, out } : { ok: true };  // 超范围自动打回
}
```
