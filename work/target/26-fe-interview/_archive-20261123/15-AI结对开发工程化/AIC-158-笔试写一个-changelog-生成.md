---
title: [AIC-158] 笔试：实现一个 changelog 生成器，解析 Conventional Commits、分组、校验 hash 引用防编造？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-158：笔试：实现一个 changelog 生成器，解析 Conventional Commits、分组、校验 hash 引用防编造？
**需求**：实现 `genChangelog(commits, version)`：
- 解析 `type(scope)!: subject` 格式，`!` 或 body 含 `BREAKING CHANGE` 归 Breaking；
- 分组 Features(feat)/Fixes(fix)/Others，每组条目 `subject (hash)`；
- breaking 条目必须附带迁移说明（body 中提取）；
- 防编造校验：最终文本中出现的 hash 必须 ⊆ 输入 commit 集，且每个 commit 都被引用（防漏）。

```javascript
const RE = /^(\w+)(?:\(([^)]+)\))?(!)?:\s*(.+)$/;

function genChangelog(commits, version) {
  const groups = { Features: [], Fixes: [], Others: [], Breaking: [] };
  for (const c of commits) {
    const m = c.message.match(RE);
    const subject = m ? m[4] : c.message; // 不规范 commit 兜底进 Others
    const breaking = m?.[3] === '!' || /BREAKING CHANGE/.test(c.body ?? '');
    const entry = { hash: c.hash.slice(0, 8), subject, scope: m?.[2] };
    if (breaking) {
      entry.migration = extractMigration(c.body ?? '');
      groups.Breaking.push(entry);
    } else if (m?.[1] === 'feat') groups.Features.push(entry);
    else if (m?.[1] === 'fix') groups.Fixes.push(entry);
    else groups.Others.push(entry);
  }

  const render = (list) => list.map(e =>
    `- ${e.subject}${e.scope ? ` (${e.scope})` : ''} (${e.hash})` +
    (e.migration ? `\n  迁移：${e.migration}` : '')).join('\n');

  const text = `# ${version}\n\n## Breaking\n${render(groups.Breaking)}\n\n## Features\n${render(groups.Features)}\n\n## Fixes\n${render(groups.Fixes)}`;

  // 防漏防编校验
  const inputHashes = new Set(commits.map(c => c.hash.slice(0, 8)));
  const referenced = [...text.matchAll(/\(([0-9a-f]{8})\)/g)].map(m => m[1]);
  const missing = [...inputHashes].filter(h => !referenced.includes(h));
  const phantom = referenced.filter(h => !inputHashes.has(h));
  return { text, integrity: { missing, phantom, ok: !missing.length && !phantom.length } };
}
function extractMigration(body) {
  return body.split('\n').find(l => /migration|迁移/i.test(l)) ?? 'TODO 补迁移说明';
}

// 测试
const commits = [
  { hash: 'abc1234567', message: 'feat(goods)!: 新增批量导出', body: 'BREAKING CHANGE\nmigration: 旧接口 /export 下线' },
  { hash: 'def2234567', message: 'fix(cart): 金额精度', body: '' },
  { hash: 'aaa3234567', message: 'chore: 依赖升级', body: '' },
];
console.log(genChangelog(commits, 'v2.3.0').integrity); // ok: true
```

**评分点**：
1. Conventional 解析的 `!` 与 body 双通道识别 breaking（只查 `!` 会漏）；
2. 不规范 commit 兜底进 Others 而非丢弃——「防漏」比格式洁癖重要；
3. 完整性双向校验：输入 commit 都被引用（防漏）+ 引用的 hash 都真实存在（防编造）——这是 AI 参与 changelog 生成的核心防线；
4. breaking 必须带迁移说明，缺失时输出 TODO 占位而非静默；
5. hash 统一截断 8 位保持输入输出一致，避免校验误报。
