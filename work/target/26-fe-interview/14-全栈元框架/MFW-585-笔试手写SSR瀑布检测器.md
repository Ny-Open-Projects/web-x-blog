---
title: [MFW-585] 笔试：手写 SSR 瀑布检测器（span 树 → 串行化机会）
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-585：笔试：手写 SSR 瀑布检测器

**答**：实现 `detectWaterfalls(spanTree)`。span: `{ name, start, end, children }`（ms 时间戳）。规则：1) 找「兄弟串行」：同一父节点下、时间区间不重叠但顺序相连的兄弟 span（前一个 end ≤ 后一个 start）且无依赖声明 → 瀑布嫌疑；2) 计算并行化收益：若完全并行，总时长 = max(兄弟) 而非 sum——收益 = sum − max（父 span 内这些兄弟的总耗时差）；3) 只报告「收益 ≥ 100ms」的瀑布；4) 嵌套检测：递归子树。返回 `[{ parent, siblings: string[], gainMs }]`（gain 降序）。边界：单子节点；重叠兄弟（真依赖——不报）；全并行。

```javascript
function detectWaterfalls(root, { minGain = 100 } = {}) {
  const results = [];
  function walk(node) {
    const kids = node.children ?? [];
    if (kids.length >= 2) {
      // 按时间排序
      const sorted = [...kids].sort((a, b) => a.start - b.start);
      const serial = [];
      for (let i = 1; i < sorted.length; i++) {
        if (sorted[i].start >= sorted[i - 1].end) serial.push(sorted[i]);
        else if (serial.length) { /* 中断：之前的连续段结算 */ }
      }
      // 连续串行段（含第一个）
      const runs = [];
      let run = [sorted[0]];
      for (let i = 1; i < sorted.length; i++) {
        if (sorted[i].start >= sorted[i - 1].end) run.push(sorted[i]);
        else { if (run.length >= 2) runs.push(run); run = [sorted[i]]; }
      }
      if (run.length >= 2) runs.push(run);
      for (const seg of runs) {
        const sum = seg.reduce((s, x) => s + (x.end - x.start), 0);
        const max = Math.max(...seg.map(x => x.end - x.start));
        const gain = sum - max;
        if (gain >= minGain)
          results.push({ parent: node.name,
            siblings: seg.map(x => x.name), gainMs: gain });
      }
    }
    kids.forEach(walk);
  }
  walk(root);
  return results.sort((a, b) => b.gainMs - a.gainMs);
}

// 自测
const tree = { name: 'page', start: 0, end: 900, children: [
  { name: 'Header', start: 0, end: 5, children: [] },
  { name: 'ProductView', start: 5, end: 895, children: [
    { name: 'getProduct', start: 5, end: 605, children: [] },     // 600ms
    { name: 'getReviews', start: 605, end: 1005, children: [] },  // 串行！400ms
  ] },
  { name: 'Footer', start: 895, end: 898, children: [] },
] };
let r = detectWaterfalls(tree);
console.log(r.length === 1);
console.log(r[0].parent === 'ProductView');
console.log(r[0].siblings.join(',') === 'getProduct,getReviews');
console.log(r[0].gainMs === 400);                        // sum 1000 - max 600

// 重叠（真依赖）不报
const dep = { name: 'p', start: 0, end: 200, children: [
  { name: 'first', start: 0, end: 100, children: [] },
  { name: 'second', start: 50, end: 150, children: [] },  // 重叠：并行中
] };
console.log(detectWaterfalls(dep).length === 0);

// 嵌套检测 + 排序
const nested = { name: 'root', start: 0, end: 1500, children: [
  { name: 'a', start: 0, end: 200, children: [] },
  { name: 'b', start: 200, end: 400, children: [] },     // a→b 串行 200ms 收益
  { name: 'c', start: 400, end: 600, children: [] },     // b→c 又串行 → 三连
  { name: 'big', start: 600, end: 1400, children: [
    { name: 'x', start: 600, end: 1000, children: [] },
    { name: 'y', start: 1000, end: 1400, children: [] },
  ] },
] };
r = detectWaterfalls(nested);
console.log(r[0].parent === 'root' && r[0].gainMs === 400);   // 三连 sum 600 max 200 → 400
console.log(r[1].gainMs === 200);
```

**评分点**：
- 串行段识别（时间不重叠的连续兄弟）；重叠兄弟视为真依赖不误报
- 收益公式（sum − max——并行化的理论收益）；minGain 阈值过滤噪声
- 递归嵌套 + 收益降序；边界
- 能说清「SSR 火焰图的头号问题是 IO 串行阶梯——并行化零风险高收益优先于索引优化」属于加分
