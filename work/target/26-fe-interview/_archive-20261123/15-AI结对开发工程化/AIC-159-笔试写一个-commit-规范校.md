---
title: [AIC-159] 笔试：实现一个 commit 规范校验器（含 AI trailer），校验格式、subject 长度与 AI-Task 引用？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-159：笔试：实现一个 commit 规范校验器（含 AI trailer），校验格式、subject 长度与 AI-Task 引用？
**需求**：实现 `validateCommit(msg, { isAgentBranch, ticketIds })`：
- 首行 `type(scope): subject`：type 白名单、subject ≤ 50 字符且不以句号结尾、非全大写；
- body 非 TODO/占位（防止 AI 混入 "TODO: implement" 提交）；
- agent 分支必须含 `AI-Task:` trailer 且引用的 ticketId 存在于传入列表；
- 返回 `{ok, errors[]}`，错误信息可直接作为 hook 拒绝原因。

```javascript
const TYPES = ['feat', 'fix', 'refactor', 'chore', 'test', 'docs', 'perf', 'style'];
const RE = /^(feat|fix|refactor|chore|test|docs|perf|style)(?:\(([\w/-]+)\))?!?: (.+)$/;

function validateCommit(msg, { isAgentBranch = false, ticketIds = [] } = {}) {
  const errors = [];
  const [first, ...rest] = msg.split('\n');
  const m = first.match(RE);
  if (!m) errors.push('首行不符合 Conventional Commits: <type>(<scope>): <subject>');
  else {
    const [, type, , subject] = m;
    if (subject.length > 50) errors.push(`subject 超长（${subject.length}/50）`);
    if (/。$|\.$/.test(subject)) errors.push('subject 不应以句号结尾');
    if (subject === subject.toUpperCase() && /[A-Z]/.test(subject)) errors.push('subject 禁止全大写');
    if (!TYPES.includes(type)) errors.push(`type "${type}" 不在白名单`);
  }
  const body = rest.join('\n');
  if (/^TODO[: ]/im.test(body)) errors.push('body 含 TODO 占位，禁止空实现提交');

  if (isAgentBranch) {
    const tm = body.match(/AI-Task:\s*(\S+)/);
    if (!tm) errors.push('agent 分支提交必须携带 AI-Task trailer');
    else if (!ticketIds.includes(tm[1])) errors.push(`AI-Task "${tm[1]}" 不在合法任务列表`);
  }
  return { ok: !errors.length, errors };
}

// 测试
console.log(validateCommit(
`feat(goods): 支持批量导出

AI-Task: TICKET-8821`,
  { isAgentBranch: true, ticketIds: ['TICKET-8821'] })); // ok

console.log(validateCommit(
`feat: TODO implement

AI-Task: FAKE-1`,
  { isAgentBranch: true, ticketIds: ['TICKET-1'] })); // 2 errors: TODO + AI-Task 不合法
```

**评分点**：
1. agent 分支的 trailer 强制校验——AI 可追溯性（AIC-117）的执法点在 commit-msg hook；
2. AI-Task 必须对合法任务列表做引用校验，只校验「有 trailer」挡不住编造；
3. TODO 占位检测针对 AI 高频病（提交半成品）；用行首正则避免误伤正文引用；
4. subject 全大写与句号检查体现细节度；
5. 错误信息要能直接作为 git hook 的拒绝理由（可读、可行动）。
