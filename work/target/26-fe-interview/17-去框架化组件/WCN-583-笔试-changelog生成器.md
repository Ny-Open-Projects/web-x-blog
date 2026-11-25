---
title: [WCN-583] 笔试：实现「conventional commit → changelog + 影响面」生成器。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-583：笔试：实现「conventional commit → changelog + 影响面」生成器。

**答**：
- 结论：解析 commit 列表，判定 semver 等级，按类型分组生成 changelog，并汇总 break 变更的影响面。
- 解析格式：type(scope)!: desc，可选 BREAKING CHANGE 段落。
- 影响面：break commit 可声明 affected（元素清单），汇总为迁移清单。
- 追问：如何生成迁移指南链接？（答：每个 break commit 带 migration doc URL，自动拼装）

```javascript
function parseCommit(msg) {
  const m = msg.match(/^(\w+)(?:\(([^)]+)\))?(!)?:\s*(.+)$/);
  if (!m) return null;
  return { type: m[1], scope: m[2], breaking: !!m[3] || /BREAKING CHANGE/.test(msg), desc: m[4],
           affected: [...msg.matchAll(/affected:\s*([\w-]+)/g)].map(x => x[1]),
           migration: (msg.match(/migration:\s*(\S+)/) || [])[1] };
}
function generate(msgs) {
  const commits = msgs.map(parseCommit).filter(Boolean);
  const level = commits.some(c => c.breaking) ? 'major' : commits.some(c => c.type === 'feat') ? 'minor' : 'patch';
  const groups = {};
  for (const c of commits) (groups[c.type] ||= []).push(`- ${c.scope ? '**'+c.scope+'**: ' : ''}${c.desc}`);
  const affected = [...new Set(commits.flatMap(c => c.affected))];
  const guides = commits.filter(c => c.migration).map(c => c.migration);
  return { level, changelog: Object.entries(groups).map(([k,v]) => `### ${k}\n${v.join('\n')}`).join('\n'), affected, guides };
}
```

**评分点**：
- Conventional Commit 解析
- semver 等级自动判定
- 分组 changelog
- break 影响面与迁移链接
