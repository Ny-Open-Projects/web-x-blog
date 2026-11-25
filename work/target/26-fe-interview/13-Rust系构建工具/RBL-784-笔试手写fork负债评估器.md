---
title: [RBL-784] 笔试：手写 fork 负债评估器（补丁分类 + 落后版本 + 退出建议）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-784：笔试：手写 fork 负债评估器（补丁分类 + 落后度 + 建议）

**答**：实现 `assessFork(fork)`。fork: `{ patches: Array<{ file, lines, generic?: boolean, upstreamPR?: string }>, upstreamLatest: string, forkBase: string, behindMinor?: number }`。评估：1) 负债分 = Σpatches.lines ×（generic ? 1 : 2.5）（不可上上游的补丁更贵）+ behindMinor × 10；2) 状态：负债 < 50 'healthy'、< 200 'watch'、≥ 200 'high-debt'；3) 建议：有 upstreamPR 且 generic → '等待合并后删除补丁'；非 generic 大补丁 → '评估以插件替代'；behindMinor ≥ 3 → '先 rebase 到最新再谈'。返回 `{ score, status, suggestions: string[] }`。边界：无补丁；behindMinor 缺省 0。

```javascript
function assessFork(fork) {
  const patches = fork.patches ?? [];
  const behind = fork.behindMinor ?? 0;
  const score = Math.round(
    patches.reduce((s, p) => s + p.lines * (p.generic ? 1 : 2.5), 0) + behind * 10);
  const status = score < 50 ? 'healthy' : score < 200 ? 'watch' : 'high-debt';

  const suggestions = [];
  if (behind >= 3) suggestions.push('先 rebase 到 upstream 最新，再评估补丁存活');
  for (const p of patches) {
    if (p.generic && p.upstreamPR) suggestions.push(`等待 PR 合并后删除补丁: ${p.file}`);
    else if (!p.generic && p.lines > 50) suggestions.push(`评估以插件替代补丁: ${p.file}`);
  }
  if (!patches.length) suggestions.push('无补丁——考虑回归社区版');
  return { score, status, suggestions };
}

// 自测
let r = assessFork({
  patches: [
    { file: 'resolve.rs', lines: 20, generic: true, upstreamPR: '#1234' },
    { file: 'chunk.rs', lines: 80, generic: false },
  ],
  behindMinor: 2,
});
console.log(r.score === 20 + 200 + 20);                  // 240
console.log(r.status === 'high-debt');
console.log(r.suggestions.some(s => s.includes('插件替代')));
console.log(r.suggestions.some(s => s.includes('#1234')));

r = assessFork({ patches: [{ file: 'a.rs', lines: 10, generic: true }], behindMinor: 0 });
console.log(r.score === 10 && r.status === 'healthy');

r = assessFork({ patches: [], behindMinor: 1 });
console.log(r.score === 10 && r.status === 'healthy' && r.suggestions[0].includes('回归社区版'));

r = assessFork({ patches: [{ file: 'x.rs', lines: 5, generic: false }], behindMinor: 4 });
console.log(r.suggestions[0].includes('rebase'));
console.log(assessFork({ patches: [] }).status === 'healthy');
```

**评分点**：
- 负债公式正确（generic 权重 1、非 generic 2.5、落后版本 ×10）；状态三档阈值
- 建议生成有依据（PR 等待/插件替代/rebase 优先）；无补丁建议回归社区版
- 边界：缺省 behindMinor=0、空补丁
- 能说清「fork 是负债需定期偿还、插件优先是组织成本判断」属于加分
