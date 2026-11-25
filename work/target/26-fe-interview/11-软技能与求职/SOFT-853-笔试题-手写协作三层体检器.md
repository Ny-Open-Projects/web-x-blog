---
title: [SOFT-853] 手写 collabNineGrid：九宫格逐格自检生成器（每格的自检问题与空白格补齐动作）？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-853：手写 collabNineGrid：九宫格逐格自检生成器（每格的自检问题与空白格补齐动作）

**需求与边界**：
- 实现 collabNineGrid(state)。
- 边界要求：① 九格定义（SOFT-841：任务/关系/机制 × 个人/团队/跨团队），每格含自检问题与补齐动作；② state 每格布尔（有无稳定做法）；③ 空白格按优先级排序输出补齐动作（任务层优先——日常影响最大）；④ 全满输出“进阶建议”（每格的深化方向）；⑤ 输出 markdown 九宫格。

**答**：
```javascript
function collabNineGrid(state = {}) {
  const GRID = {
    '任务×个人': { q: '消息三要素/承诺记账有稳定习惯吗（SOFT-815）?',
      fix: '微习惯五件，绑定既有行为（SOFT-815）' },
    '任务×团队': { q: '同步分级三档在跑吗（SOFT-824）?',
      fix: '同步清单入公约（SOFT-811）' },
    '任务×跨团队': { q: '接口契约书面化了吗（SOFT-544）?',
      fix: '契约进git+CI校验（SOFT-544）' },
    '关系×个人': { q: '横向反馈有习惯吗（SOFT-822）?',
      fix: '请求式开启+季度互评（SOFT-822）' },
    '关系×团队': { q: '心理安全指标健康吗（SOFT-818）?',
      fix: '示范认错+坏消息零惩罚（SOFT-818）' },
    '关系×跨团队': { q: '信任账户在维护吗（SOFT-558）?',
      fix: '季度互助预算+支援记账（SOFT-725/558）' },
    '机制×个人': { q: '口头共识24h书面确认吗（SOFT-544）?',
      fix: '决策留痕入周记（SOFT-616）' },
    '机制×团队': { q: '团队公约存在且被签署吗（SOFT-811）?',
      fix: '四模块公约+全员签署（SOFT-840）' },
    '机制×跨团队': { q: '依赖图谱存在吗（SOFT-823）?',
      fix: '依赖图谱+变更契约+瓶颈保护（SOFT-823）' },
  };
  const rows = Object.entries(GRID).map(([cell, cfg]) => ({
    cell, ok: state[cell] === true, q: cfg.q,
    fix: state[cell] ? `深化：${cfg.fix}` : `补齐：${cfg.fix}` }));
  const blanks = rows.filter(r => !r.ok)
    .sort((a, b) => a.cell.startsWith('任务') ? -1
      : b.cell.startsWith('任务') ? 1 : 0);       // 任务层优先
  const md = rows.map(r =>
    `| ${r.cell} | ${r.ok ? '✅' : '⬜'} | ${r.q} |`).join('\n');
  return { grid: `| 格 | 状态 | 自检 |\n|---|---|---|\n${md}`,
    blanks: blanks.map(b => b.fix),
    allGood: blanks.length === 0 };
}
```

**评分点**:
- 九宫格数据结构完整（三行三列每格自检问题+补齐动作）。
- 空白格任务层优先排序（日常影响最大的先补）。
- 已满格输出深化方向（不只补缺还促精进）。

