---
title: [RBL-658] 笔试：手写 ddmin 崩溃最小化（行块删除 + 自适应粒度）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-658：笔试：手写 ddmin 崩溃最小化（行块删除 + 自适应粒度）

**答**：实现 `ddmin(lines, test, { maxRuns })`。lines 为字符串数组（crash 样本）；test(candidateLines) -> boolean（true = 仍 crash）。目标：找最小仍 crash 的子集。算法（简化 ddmin）：1) 从 n=2 开始按块删除：移除一个块后仍 crash 则保留删除（样本变小，n 重置 2）；2) 一轮所有块都不可删 → n 翻倍（粒度更细）；3) n ≥ 行数或单行 → 停止；4) 每次删除尝试算一次 run，超过 maxRuns 停止并返回当前最优；5) 边界：初始不 crash 返回 null；全删空仍 crash 返回 []。

```javascript
function ddmin(lines, test, { maxRuns = 200 } = {}) {
  if (!test(lines)) return null;
  let current = [...lines];
  let n = 2, runs = 0;

  const tryRemove = (idxList) => {
    if (runs >= maxRuns) return false;
    runs++;
    const candidate = current.filter((_, i) => !idxList.includes(i));
    if (candidate.length === current.length) return false;
    if (test(candidate)) { current = candidate; return true; }
    return false;
  };

  while (n <= current.length && current.length > 1 && runs < maxRuns) {
    const size = Math.max(1, Math.floor(current.length / n));
    let removed = false;
    outer:
    for (let start = 0; start < current.length; start += size) {
      const idxList = [];
      for (let i = start; i < Math.min(start + size, current.length); i++) idxList.push(i);
      if (tryRemove(idxList)) { removed = true; n = 2; break outer; }  // 成功 -> 粒度重置
    }
    if (!removed) n = Math.min(n * 2, current.length);   // 全不可删 -> 细化
    if (current.length <= 1) break;
  }
  return current;
}

// 自测：干扰行 + 一行关键代码
const lines = [
  'const a = 1;', 'const b = 2;', 'foo(a);', 'foo(b);',
  'crashTrigger();',                                     // 关键行
  'const c = 3;', 'bar();',
];
const test = (ls) => ls.includes('crashTrigger();');
const result = ddmin(lines, test);
console.log(result.length === 1 && result[0] === 'crashTrigger();');

// 依赖组合的最小集（两行共同触发）
const lines2 = ['a();', 'b();', 'c();', 'noise();'];
const test2 = (ls) => ls.includes('a();') && ls.includes('b();');
const r2 = ddmin(lines2, test2);
console.log(r2.length === 2 && r2.includes('a();') && r2.includes('b();'));

// 初始不 crash
console.log(ddmin(lines, () => false) === null);
// run 上限
const expensive = ddmin(Array.from({ length: 50 }, (_, i) => `l${i};`)
  .concat(['crash();']), test, { maxRuns: 5 });
console.log(expensive.includes('crash();'));             // 超限返回当前最优仍 crash
```

**评分点**：
- ddmin 主循环正确：块删除成功重置 n=2，失败翻倍细化；终止条件（n≥len 或单行）
- run 预算控制（超限返回当前最优而非死循环）；初始不 crash 返回 null
- 多行共同触发的最小集保留（不是贪心单行删除）；空候选不误删全空
- 能说清「最小化让 crash 样本可提交为回归 fixture」属于加分
