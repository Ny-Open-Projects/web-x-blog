---
title: [ENG-307] 笔试题——实现 changelog 生成器（conventional commits → 分组文档）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-307：手写 changelog 生成器

**需求与边界**：
- 需求：解析 conventional commits（自上次 tag），生成分组 changelog（feat/fix/perf/breaking）；breaking 提取 MIGRATION 块输出迁移指引；生成包级与应用级两种视角。
- 边界：① scope 归组（feat(ui): xxx 归 UI 组）；② squash merge 提交取 PR 标题与描述；③ breaking 缺 MIGRATION 的提交生成 TODO 标记；④ 版本头带日期与对比链接。

**答**：
```javascript
function generateChangelog(commits, { lastTag, version, repo }) {
  const groups = { breaking: [], feat: [], fix: [], perf: [], other: [] };
  for (const c of commits) {
    const m = c.message.match(/^(\w+)(?:\(([^)]+)\))?!?:\s(.*)/);
    if (!m) { groups.other.push(c.message); continue; }
    const [, type, scope, subject] = m;
    const entry = { scope, subject, sha: c.sha };
    if (c.body?.includes('BREAKING CHANGE')) {
      entry.migration = c.body.split('BREAKING CHANGE')[1]?.match(/MIGRATION:([\s\S]*)/)?.[1]?.trim();
      groups.breaking.push(entry);
    } else if (groups[type]) groups[type].push(entry);
    else groups.other.push(c.message);
  }
  const compare = `${repo}/compare/${lastTag}...v${version}`;
  const md = [`## v${version} (${new Date().toISOString().slice(0, 10)})`, `[对比](${compare})`];
  if (groups.breaking.length) {
    md.push('### ⚠️ Breaking');
    for (const b of groups.breaking)
      md.push(`- ${b.subject}${b.migration ? `\n  迁移: ${b.migration}` : '\n  TODO: 补充迁移说明'}`);
  }
  for (const [t, list] of Object.entries(groups))
    if (t !== 'breaking' && list.length)
      md.push(`### ${t}`, ...list.map(e => `- ${e.scope ? `**${e.scope}**: ` : ''}${e.subject}`));
  return md.join('\n');
}
```

**评分点**:
- conventional 解析容错（不合规范的进 other 不丢）。
- BREAKING 提取 MIGRATION 块 + 缺失 TODO（发布质量门禁 ENG-249）。
- breaking 置顶 + 对比链接（可导航）。
- scope 归组输出（包级视角可筛选）。
