---
title: [MFW-689] 笔试：手写 Suspense 嵌套 fallback 分析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-689：笔试：手写 Suspense 嵌套分析器

**答**：实现 `analyzeSuspenseNesting(tree)`。tree: `{ name, type: 'suspense'|'component', fallback: string|null, children, resolveMs? }[]`. 规则：1) **粗粒度检测**：外层 Suspense 包含内层 Suspense 且外层 fallback 非空 → warn 'coarse-fallback'（外层挂起会覆盖内层——建议平级拆分）；2) **粒度评分**：Suspense 边界的 fallback 有尺寸信息（fallback 含 skeleton 类名）→ 好（RBL-565）；3) **resolveMs 的流序**：内层先 resolve 但外层后 resolve → warn 'nested-blocking'（内层内容被外层骨架遮挡——时间浪费）；4) 返回 `{ findings, suggestions, boundaries }`（boundaries = 检出的 Suspense 边界数）。边界：无 Suspense（空）；纯平级（无嵌套——ok）；fallback=null 的外层（inline——不算 coarse）。

```javascript
function analyzeSuspenseNesting(tree = []) {
  const findings = [], suggestions = [];
  let boundaries = 0;
  function walk(nodes, parentSuspense) {
    for (const n of nodes) {
      if (n.type === 'suspense') {
        boundaries++;
        if (parentSuspense && n.fallback && parentSuspense.fallback)
          findings.push({ node: n.name, issue: 'coarse-fallback',
            detail: '嵌套 Suspense——外层挂起覆盖内层，建议平级拆分' });
        if (n.resolveMs != null && parentSuspense?.resolveMs != null &&
            n.resolveMs < parentSuspense.resolveMs)
          findings.push({ node: n.name, issue: 'nested-blocking',
            detail: `内层 ${n.resolveMs}ms 先完成但外层 ${parentSuspense.resolveMs}ms 阻塞——内容被骨架遮挡` });
        if (n.fallback && /skeleton/i.test(n.fallback))
          suggestions.push(`${n.name} 有尺寸骨架——CLS 防护良好`);
        walk(n.children ?? [], n);
      } else walk(n.children ?? [], parentSuspense);
    }
  }
  walk(tree, null);
  return { findings, suggestions, boundaries };
}

// 自测
const tree = [
  { name: 'outer', type: 'suspense', fallback: 'PageSkeleton', resolveMs: 800, children: [
    { name: 'detail', type: 'component', children: [] },
    { name: 'inner', type: 'suspense', fallback: 'ReviewSkeleton', resolveMs: 100, children: [
      { name: 'reviews', type: 'component', children: [] } ] } ] },
];
let r = analyzeSuspenseNesting(tree);
console.log(r.boundaries === 2);
console.log(r.findings.some(f => f.issue === 'coarse-fallback' && f.node === 'inner'));
console.log(r.findings.some(f => f.issue === 'nested-blocking'));
// inner 100ms < outer 800ms → 内层被遮挡
console.log(r.suggestions.some(s => s.includes('尺寸骨架')));

// 平级拆分（无嵌套）
const flat = [
  { name: 'outer', type: 'suspense', fallback: 'DetailSkeleton', resolveMs: 800, children: [] },
  { name: 'inner', type: 'suspense', fallback: 'ReviewSkeleton', resolveMs: 100, children: [] },
];
r = analyzeSuspenseNesting(flat);
console.log(r.findings.length === 0);                    // 平级无 coarse/blocking
console.log(r.boundaries === 2);

// 无 Suspense
console.log(analyzeSuspenseNesting([{ name: 'static', type: 'component', children: [] }]).boundaries === 0);

// inline fallback 外层
const inlineOuter = [
  { name: 'outer', type: 'suspense', fallback: null, resolveMs: 800, children: [
    { name: 'inner', type: 'suspense', fallback: 'skel', resolveMs: 100, children: [] } ] },
];
r = analyzeSuspenseNesting(inlineOuter);
console.log(!r.findings.some(f => f.issue === 'coarse-fallback'));   // null fallback 不算 coarse
```

**评分点**：
- 粗粒度检测（嵌套 + 双方有 fallback——外层覆盖内层的架构反模式）；nested-blocking（内层快被外层慢遮挡——时间浪费）
- inline fallback（null）不触发 coarse（无占位 = 不遮挡）；骨架尺寸好评
- 边界（无 Suspense/平级/inline）；建议的可执行性（平级拆分）
- 能说清「嵌套 Suspense 的外层 fallback 覆盖内层已完成的树——平级拆分让各边界独立流式」属于加分
