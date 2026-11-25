---
title: [AIC-412] 笔试：解析 git commit trailers，构建 AI 产出溯源查询。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-412：笔试：解析 git commit trailers，构建 AI 产出溯源查询。
**题目**：commit message 尾部格式 `Co-authored-by: cursor-agent <a@x>` 与 `Ai-Task-Id: T-123`。实现 `parseTrailers(msg)` 与 `findByTask(commits, taskId)`，后者返回该任务全部 commit 的 `{sha, model}`。

```javascript
function parseTrailers(msg) {
  const blocks = msg.trim().split(/\n\s*\n/);
  const tail = blocks[blocks.length - 1];
  const out = { model: 'human', taskId: null };
  for (const line of tail.split('\n')) {
    const co = line.match(/^Co-authored-by:\s*([\w-]+)/);
    if (co && /agent|cursor|copilot/i.test(co[1])) out.model = co[1];
    const t = line.match(/^Ai-Task-Id:\s*(\S+)/);
    if (t) out.taskId = t[1];
  }
  return out;
}
function findByTask(commits, taskId) {
  return commits
    .map(c => ({ sha: c.sha, ...parseTrailers(c.message) }))
    .filter(x => x.taskId === taskId)
    .map(({ sha, model }) => ({ sha, model }));
}
console.log(findByTask([
  { sha: 'abc', message: 'feat: x\n\nCo-authored-by: cursor-agent <a@x>\nAi-Task-Id: T-1' },
  { sha: 'def', message: 'fix: y' },
], 'T-1')); // [{ sha: 'abc', model: 'cursor-agent' }]

```

**评分点**：
- trailer 只解析 message 最后一段（空行分隔后的尾部块）。
- model 从 co-author 邮箱/名字映射，未标记视为 human。
- 非法/缺失 trailer 容错不抛错。
- 支持多 co-author 行。
