---
title: [AIC-403] 笔试：实现 PR diff 的风险评分器，输出风险分与原因清单。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-403：笔试：实现 PR diff 的风险评分器，输出风险分与原因清单。
**题目**：输入 diff 文件列表 `[{path, added, deleted, isTest, isConfig}]`，规则：核心目录（src/core）每文件 +3；配置文件 +4；删测试行数按 2 倍计负向；总新增 > 300 再 +2。输出 `{score, level, reasons[]}`，reasons 每条带依据。

```javascript
function riskOf(files) {
  if (!files.length) return { score: 0, level: 'low', reasons: ['空 diff'] };
  let score = 0; const reasons = [];
  const add = (n, why) => { score += n; reasons.push(why); };
  for (const f of files) {
    if (f.isConfig) add(4, `配置变更: ${f.path}`);
    if (f.path.startsWith('src/core')) add(3, `核心目录变更: ${f.path}`);
    if (f.isTest && f.deleted > 0)
      add(Math.min(6, Math.ceil(f.deleted / 10) * 2), `删除测试 ${f.deleted} 行: ${f.path}`);
  }
  const totalAdd = files.reduce((s, f) => s + f.added, 0);
  if (totalAdd > 300) add(2, `大体积变更 ${totalAdd} 行`);
  const level = score < 3 ? 'low' : score < 7 ? 'mid' : 'high';
  return { score, level, reasons };
}
console.log(riskOf([
  { path: 'src/core/pay.ts', added: 50, deleted: 0, isTest: false, isConfig: false },
  { path: 'ci.yml', added: 5, deleted: 2, isTest: false, isConfig: true },
  { path: 'test/a.test.ts', added: 0, deleted: 40, isTest: true },
])); // score 4+3+6=13 → high

```

**评分点**：
- 评分必须可解释：每个加分项对应一条 reason——只给分数不给原因是主要失分点。
- 删除测试是高危信号（削弱验证），权重设计要体现。
- level 阈值清晰（如 <3 low / <7 mid / else high）且写明。
- 空 diff、纯文档改动应返回 low 并标注「无需深审」。
