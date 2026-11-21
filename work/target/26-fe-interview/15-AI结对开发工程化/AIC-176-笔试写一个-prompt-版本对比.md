---
title: [AIC-176] 笔试：实现一个 Prompt 版本对比器：语义 diff（约束增删/变量变更）、风险标记与回归建议？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-176：笔试：实现一个 Prompt 版本对比器：语义 diff（约束增删/变量变更）、风险标记与回归建议？
**需求**：实现 `diffPrompt(oldP, newP)`：
- 按「约束行」级别 diff（以 `-` 开头的行视为约束，规则文件约定）；普通文本行做普通 diff；
- 识别三类语义变更：约束新增（低风险）、约束删除（高风险——模型行为可能失控）、变量槽位增删（需检查调用方）；
- 约束删除时给出回归建议（跑哪些基准用例）；
- 输出 `{changes, risk, suggestRegression}`。

```javascript
function diffLines(a, b) {
  const aSet = new Map(a.map(l => [l, a.filter(x => x === l).length]));
  const changes = [];
  const bCount = new Map(b.map(l => [l, b.filter(x => x === l).length]));
  for (const [l, n] of aSet) {
    const m = bCount.get(l) ?? 0;
    for (let i = m; i < n; i++) changes.push({ line: l, kind: 'removed' });
  }
  for (const [l, n] of bCount) {
    const m = aSet.get(l) ?? 0;
    for (let i = m; i < n; i++) changes.push({ line: l, kind: 'added' });
  }
  return changes;
}
const isConstraint = (l) => /^[-*]\s*/.test(l) || /^禁止/.test(l);

function diffPrompt(oldP, newP) {
  const changes = diffLines(oldP.split('\n'), newP.split('\n'));
  const oldVars = varsOf(oldP), newVars = varsOf(newP);
  const varChanges = [
    ...[...oldVars].filter(v => !newVars.has(v)).map(v => ({ var: v, kind: 'removed' })),
    ...[...newVars].filter(v => !oldVars.has(v)).map(v => ({ var: v, kind: 'added' })),
  ];
  const constraintRemoved = changes.filter(c => c.kind === 'removed' && isConstraint(c.line));
  const risk = constraintRemoved.length ? 'high'
    : varChanges.some(v => v.kind === 'removed') ? 'medium' : 'low';
  return {
    changes: changes.map(c => ({ ...c, semantic: isConstraint(c.line) ? 'constraint' : 'text' })),
    varChanges,
    risk,
    suggestRegression: risk === 'high'
      ? ['rules-cases 全量回归', '重点跑与被删约束相关的用例：' + constraintRemoved.map(c => c.line).join(' / ')]
      : risk === 'medium' ? ['检查模板调用方传参'] : [],
  };
}
const varsOf = (p) => new Set([...p.matchAll(/\{\{(\w+)\}\}/g)].map(m => m[1]));

// 测试
const oldP = '- 禁止使用 any\n- 函数 ≤ 40 行\n使用 {{lang}}';
const newP = '- 函数 ≤ 50 行\n使用 {{lang}}\n- 新增：禁止 console.log';
const d = diffPrompt(oldP, newP);
console.log(d.risk, d.suggestRegression);
// high：删除了「禁止使用 any」约束 → 建议全量回归
```

**评分点**：
1. 约束行与普通行区分对待——约束删除是高风险语义，普通文本改写是低风险；
2. 变量槽位增删独立检测（删除变量意味着调用方会炸，呼应 AIC-145 槽位校验）；
3. 风险分级与回归建议联动（high → rules-cases 全量）；
4. 多行重复计数 diff（同一约束出现两次删一次的边界）；
5. 追问：更精细的语义 diff 可按约束主题聚类（安全类/风格类），删除安全类约束直接 block。
