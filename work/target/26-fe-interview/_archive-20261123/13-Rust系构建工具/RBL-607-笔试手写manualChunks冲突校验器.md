---
title: [RBL-607] 笔试：手写 manualChunks 冲突校验器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-607：笔试：手写 manualChunks 冲突校验器

**需求**：实现 `validateManual(manual, graph)`。manual: `Map<chunkName, string[]>`；graph: `{ entries: Set, dynamicEntries: Set, sccs: string[][] }`。检测三类冲突并返回 warnings 数组 `{ chunk, issue, detail }`：1) `contains-entry`：chunk 含 entry 模块；2) `eats-dynamic`：chunk 含 dynamic import 入口模块；3) `splits-scc`：某长度 >1 的 SCC 被该配置拆散（部分在内部分在外，或 SCC 成员分属不同手动 chunk）。另要求：模块重复出现在多个 chunk（`duplicate-module`）也要报告。无冲突返回空数组；manual 中模块不存在于 graph（`unknown-module`）同样报告。

```javascript
function validateManual(manual, graph) {
  const warnings = [];
  const owner = new Map();                               // module -> [chunkNames]

  for (const [chunk, mods] of manual) {
    for (const m of mods) {
      if (!graph.hasModule(m)) { warnings.push({ chunk, issue: 'unknown-module', detail: m }); continue; }
      (owner.get(m) || owner.set(m, []).get(m)).push(chunk);
      if (graph.entries.has(m)) warnings.push({ chunk, issue: 'contains-entry', detail: m });
      if (graph.dynamicEntries.has(m)) warnings.push({ chunk, issue: 'eats-dynamic', detail: m });
    }
  }
  for (const [m, cs] of owner)
    if (cs.length > 1) warnings.push({ chunk: cs.join(','), issue: 'duplicate-module', detail: m });

  for (const scc of graph.sccs) {
    if (scc.length <= 1) continue;
    const chunksInvolved = new Set(scc.flatMap(m => owner.get(m) || []));
    const covered = scc.filter(m => (owner.get(m) || []).length);
    if (chunksInvolved.size > 1 || (covered.length && covered.length !== scc.length))
      warnings.push({ chunk: [...chunksInvolved].join(','), issue: 'splits-scc', detail: scc.join('->') });
  }
  return warnings;
}

// 自测
const graph = {
  entries: new Set(['main']),
  dynamicEntries: new Set(['lazyWidget']),
  sccs: [['a', 'b']],                                    // a<->b 环
  hasModule: (m) => ['main', 'lazyWidget', 'a', 'b', 'vendor1'].includes(m),
};
let w = validateManual(new Map([
  ['entry', ['main']],                                  // contains-entry
  ['lazy', ['lazyWidget']],                             // eats-dynamic
  ['cycle', ['a']],                                     // splits-scc（b 不在内）
]), graph);
console.log(w.map(x => x.issue).sort());                 // ['contains-entry','eats-dynamic','splits-scc']

w = validateManual(new Map([
  ['v1', ['vendor1']],
  ['v2', ['vendor1']],                                  // duplicate-module
]), graph);
console.log(w.some(x => x.issue === 'duplicate-module'));

w = validateManual(new Map([['ok', ['a', 'b']]]), graph);  // SCC 完整保留：无冲突
console.log(w.length === 0);

w = validateManual(new Map([['x', ['ghost']]]), graph);
console.log(w[0].issue === 'unknown-module');
```

**评分点**：
- 四类冲突检测齐全（entry/动态边界/SCC 拆散/重复模块），unknown-module 也有报告
- SCC 拆散判定正确：部分覆盖或跨多 chunk 都算；完整保留不误报
- 重复模块的 owner 收集逻辑正确（含 unknown-module 不进 owner 的防御）
- 能说清「循环依赖不可分割是硬约束，手动配置也不豁免」属于加分
