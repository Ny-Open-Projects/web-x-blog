---
title: [AIC-955] 让 AI 重构时它「顺手」把 React 17 升到 19 并改了一堆 API，如何给 AI 的重构设边界防止越界？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-955：让 AI 重构时它「顺手」把 React 17 升到 19 并改了一堆 API，如何给 AI 的重构设边界防止越界？
**答**：
- 先「圈定变更范围」：任务明确声明本次是「纯结构重构，不改依赖、不改对外 API、不改行为」，并把 lockfile、package.json 列为 AI 不可写文件。
- 用「变更白名单/黑名单」配合 pre-commit 校验：提交时若发现超出声明范围的文件（如 package.json 被改）直接拒绝，让越界无法落地。
- 依赖升级等「高风险独立变更」必须单独成任务、单独评审、单独灰度——结论：一次只做一件事，重构与升级解耦。
- 追问钩子：能提出「AI 越界往往源于任务描述模糊，明确的边界声明 + 自动化校验比事后 review 更可靠」的候选人懂预防优于检查。

```typescript
// 变更范围守卫：pre-commit 校验
const taskScope = { allowed:['src/components/**'], forbidden:['package.json','**/lockfile','src/api/**'] };
function guardChanges(changedFiles, scope = taskScope) {
  const violations = changedFiles.filter(f =>
    scope.forbidden.some(g => globMatch(f,g)) || !scope.allowed.some(g => globMatch(f,g)));
  return { ok: violations.length===0, violations };
}
function globMatch(p,g){ return new RegExp('^'+g.replace(/\*\*/g,'.*').replace(/\*/g,'[^/]*').replace(/\./g,'\.')+'$').test(p); }
// 接入 pre-commit：有越界即非零退出，阻止提交
function preCommitHook(changedFiles) {
  const result = guardChanges(changedFiles);
  if (!result.ok) {
    console.error('变更越界，禁止提交:', result.violations);
    process.exitCode = 1; // CI/本地提交均拦截
  }
  return result;
}
console.log(preCommitHook(['src/components/List.tsx','package.json'])); // 越界: package.json
```
