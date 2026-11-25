---
title: [RBL-649] 笔试：手写构建器升级语义 diff 判定器（预期/意外变化分类）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-649：笔试：手写构建器升级语义 diff 判定器（预期/意外变化分类）

**答**：实现 `classifyDiff(oldOut, newOut, declared)`。oldOut/newOut: `{ exports: string[], chunks: string[][] (chunk 内模块 id), assets: string[] }`；declared: `{ kind, detail? }[]`（changelog 声明）。输出 `Array<{ kind, detail, unexpected }>`，kind ∈ 'exports-added'|'exports-removed'|'chunk-move'|'asset-changed'。判定规则：1) exports 差集；2) chunk-move：模块在新旧版本的 chunk 归属变化（记录 from→to）；3) asset-changed：资产名集合变化；4) 每条变化检查是否被 declared 覆盖（declared.detail 若提供则做子串匹配 kind+detail，否则按 kind 匹配）——覆盖则 unexpected=false。返回完整列表 + `unexpectedCount`。边界：两版本完全一致返回空数组。

```javascript
function classifyDiff(oldOut, newOut, declared = []) {
  const changes = [];
  const covered = (kind, detail) => declared.some(d =>
    d.kind === kind && (!d.detail || (detail && String(detail).includes(d.detail))));

  const oldExp = new Set(oldOut.exports), newExp = new Set(newOut.exports);
  for (const e of newExp) if (!oldExp.has(e))
    changes.push({ kind: 'exports-added', detail: e, unexpected: !covered('exports-added', e) });
  for (const e of oldExp) if (!newExp.has(e))
    changes.push({ kind: 'exports-removed', detail: e, unexpected: !covered('exports-removed', e) });

  const locate = (chunks) => {                           // module -> chunkIdx
    const m = new Map();
    chunks.forEach((c, i) => c.forEach(mod => m.set(mod, i)));
    return m;
  };
  const lo = locate(oldOut.chunks), ln = locate(newOut.chunks);
  for (const [mod, from] of lo) {
    const to = ln.get(mod);
    if (to !== undefined && to !== from)
      changes.push({ kind: 'chunk-move', detail: `${mod}:${from}->${to}`,
                     unexpected: !covered('chunk-move', mod) });
  }
  const oa = new Set(oldOut.assets), na = new Set(newOut.assets);
  for (const a of na) if (!oa.has(a))
    changes.push({ kind: 'asset-changed', detail: a, unexpected: !covered('asset-changed', a) });

  return { changes, unexpectedCount: changes.filter(c => c.unexpected).length };
}

// 自测
const oldOut = {
  exports: ['main', 'legacy'],
  chunks: [['main.ts', 'util.ts'], ['legacy.ts']],
  assets: ['logo.png', 'font.woff2'],
};
const newOut = {
  exports: ['main'],
  chunks: [['main.ts'], ['util.ts'], ['legacy.ts']],
  assets: ['logo.png'],
};
// 无声明：全部意外
let r = classifyDiff(oldOut, newOut, []);
console.log(r.unexpectedCount === 4);                    // exports-removed + chunk-move + asset-changed
console.log(r.changes.some(c => c.kind === 'exports-removed' && c.detail === 'legacy'));

// 声明覆盖
r = classifyDiff(oldOut, newOut, [
  { kind: 'exports-removed' },
  { kind: 'chunk-move', detail: 'util.ts' },
  { kind: 'asset-changed', detail: 'font.woff2' },
]);
console.log(r.unexpectedCount === 0);

// detail 子串不匹配仍意外
r = classifyDiff(oldOut, newOut, [{ kind: 'chunk-move', detail: 'other.ts' }]);
console.log(r.unexpectedCount === 1);                    // util.ts 移动未被声明

// 完全一致
r = classifyDiff(oldOut, oldOut, []);
console.log(r.changes.length === 0);
```

**评分点**：
- 三类语义 diff 正确（exports 差集双向、chunk 归属变化 from→to、资产集合变化）
- declared 覆盖判定正确：无 detail 按 kind 全覆盖、有 detail 做子串校验（精确到模块级）
- unexpectedCount 汇总准确；完全一致返回空
- 能说清「升级评审的对象是意外变化，预期变化对照 changelog」属于加分
