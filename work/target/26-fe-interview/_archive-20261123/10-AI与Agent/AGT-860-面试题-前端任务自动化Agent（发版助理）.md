---
title: [AGT-860] 把发版流程交给 Agent（changelog/版本号/tag/通知），边界与安全网怎么定？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-860：把发版流程交给 Agent（changelog/版本号/tag/通知），边界与安全网怎么定

**答**：
- 可交给 Agent 的：检查 CI 绿、生成 changelog、semver 版本号推断、打 tag、发通知、更新文档；不可交的：正式发布按钮（生产发布保持人工一键确认）、热修复决策。
- 安全网：发布前的 dry-run 输出（将发布的版本号/变更清单/影响面）供人工确认；Agent 的一切动作可撤销（tag 可删/通知可撤回）且全程留痕。
- 失败中断：流程中任一步验证失败（tag 已存在/CI 红了）立即停止并报告，不做"尽力而为"的半截发版。

```javascript
async function releaseAssistant(branch) {
  const plan = await planRelease(branch);          // dry-run
  await human.confirm(plan);                       // 生产发布人工确认
  const steps = [ciGreen, changelog, bumpVersion, tag, notes, notify];
  for (const s of steps) {
    const r = await s(plan);
    if (!r.ok) { await rollbackTo(steps.indexOf(s)); // 失败即停
      return { aborted: s.name, done: steps.indexOf(s) }; }
  }
  return { released: plan.version };
}
```

