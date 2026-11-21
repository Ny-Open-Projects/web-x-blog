---
title: [AIC-188] 笔试：实现一个 PR 描述生成器：从 commit 群组聚合改动、生成结构化描述与风险段？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-188：笔试：实现一个 PR 描述生成器：从 commit 群组聚合改动、生成结构化描述与风险段？
**需求**：实现 `genPrDesc(commits, diffStat, meta)`：
- 输入 commit 列表（含 type/scope/subject）与 diffStat（每文件 ±行数）；
- 生成结构：概述（一句）→ 按模块分组的改动表 → 测试说明 → 风险与回滚 → AI 标记段；
- 风险段规则：删除公共 API / 依赖变更 / 改动核心目录（payment 等）自动列出；
- 概述去重：同 type+scope 的多条 commit 合并为一条描述。

```javascript
const RISK_DIRS = ['payment', 'auth'];

function genPrDesc(commits, diffStat, meta = {}) {
  // 按模块（scope 或目录前缀）分组
  const groups = new Map();
  for (const c of commits) {
    const k = c.scope ?? c.files?.[0]?.split('/')[0] ?? 'other';
    const g = groups.get(k) ?? [];
    g.push(c.subject);
    groups.set(k, g);
  }
  const table = [...groups.entries()].map(([mod, subs]) =>
    `| ${mod} | ${[...new Set(subs)].join('；')} |`).join('\n');

  const risky = Object.entries(diffStat)
    .filter(([f]) => RISK_DIRS.some(d => f.includes(d)))
    .map(([f, s]) => `${f} (+${s.added}/-${s.deleted})`);
  const depChanged = commits.some(c => c.files?.includes('package.json'));
  const apiRemoved = commits.some(c => /remov|删除|deprecat/i.test(c.subject));

  const riskLines = [
    risky.length && `核心目录改动：${risky.join(', ')}`,
    depChanged && '依赖变更：确认 semver 兼容与 lockfile 审查',
    apiRemoved && '疑似删除公共 API：确认调用方已同步',
  ].filter(Boolean);

  return `## 概述
${commits[0]?.subject ?? meta.title ?? '改动'}${commits.length > 1 ? ` 等 ${commits.length} 项提交` : ''}

## 改动
| 模块 | 内容 |
|---|---|
${table}

## 测试
${meta.tests ? `已运行：${meta.tests}` : 'TODO: 列出验证方式'}

## 风险与回滚
${riskLines.length ? riskLines.map(l => `- ${l}`).join('\n') : '- 低风险改动，revert PR 即可回滚'}

<!-- AI-Scope: 生成段落为模板聚合，语义请人工确认 -->
`;
}

// 测试
console.log(genPrDesc(
  [{ type: 'feat', scope: 'goods', subject: '批量导出', files: ['packages/goods/export.ts'] },
   { type: 'fix', scope: 'payment', subject: '金额精度', files: ['packages/payment/calc.ts'] }],
  { 'packages/payment/calc.ts': { added: 40, deleted: 10 }, 'packages/goods/export.ts': { added: 5, deleted: 0 } },
  { tests: 'vitest 24 passed' }));
```

**评分点**：
1. 结构化固定段落（概述/改动表/测试/风险回滚）——reviewer 阅读顺序稳定；
2. 风险段是自动规则推导（核心目录/依赖/API 删除）而非 AI 自由发挥；
3. 分组去重（同模块多条 commit 合并）避免流水账；
4. AI 标记段保留（可追溯性，AIC-117）；
5. 测试段无数据时输出 TODO 而非静默省略。
