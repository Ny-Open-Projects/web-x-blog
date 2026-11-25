---
title: [WCN-582] 设计系统「语义化版本 + 变更日志自动化」：如何从 commit 自动生成 changelog 与迁移指南？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-582：设计系统「语义化版本 + 变更日志自动化」：如何从 commit 自动生成 changelog 与迁移指南？

**答**：
- 结论：用 Conventional Commits 规范（feat/fix/break），CI 解析 commit 自动判定 semver 并生成 changelog。
- break 标记（! 或 BREAKING CHANGE）触发 major，feat 触发 minor，fix 触发 patch。
- 迁移指南从 break commit 的模板段落自动拼装，关联受影响元素与 codemod。
- 追问：如何避免「改了但没写规范 commit」漏记？（答：CI 校验 commit 格式，非规范拒绝合并）

```javascript
function releaseFromCommits(commits) {
  let level = 'patch';
  const sections = { feat: [], fix: [], break: [] };
  for (const c of commits) {
    if (c.breaking) { level = 'major'; sections.break.push(c.desc); }
    else if (c.type === 'feat') { if (level !== 'major') level = 'minor'; sections.feat.push(c.desc); }
    else if (c.type === 'fix') sections.fix.push(c.desc);
  }
  return { level, changelog: `## ${level}\n` + Object.entries(sections).filter(([,v])=>v.length).map(([k,v])=>`### ${k}\n- ${v.join('\n- ')}`).join('\n') };
}
```
