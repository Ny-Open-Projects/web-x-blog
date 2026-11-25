---
title: [MFW-498] 笔试：手写 Next 版本升级 codemod 计划器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-498：Next 版本升级 codemod 计划器
**答**：实现 `planUpgrade(routes, breaking)`：1) routes = [{ path, features: ['async-params','next/head','getServerSideProps'] }]，breaking = { 'async-params': { fix: 'codemod', effort: 1 }, 'next/head': { fix: 'rewrite', effort: 3 }, 'getServerSideProps': { fix: 'rewrite', effort: 8 } }；2) 输出迁移批次：按 effort 升序分批，每批总量 ≤ 13 点（一批一个 PR，控制 review 与回滚粒度）；3) 依赖排序：`getServerSideProps` 改写批次排在 `async-params` 之后（API 形态先统一再迁移）；4) 输出 [{ batch: n, paths: [...], totalEffort }] 并标注阻塞项（无法 codemod 的功能进度可见）。

```javascript
export function planUpgrade(routes, breaking) {
  const items = []
  for (const r of routes)
    for (const f of r.features)
      if (breaking[f]) items.push({ path: r.path, feature: f, ...breaking[f] })

  // 依赖排序：修复项带 after 字段时先排前置
  const ordered = items.sort((a, b) =>
    (breaking[a.feature].order ?? 0) - (breaking[b.feature].order ?? 0) || a.effort - b.effort)

  const batches = []
  let cur = [], sum = 0
  for (const it of ordered) {
    if (sum + it.effort > 13 && cur.length) { batches.push(cur); cur = []; sum = 0 }
    cur.push(it); sum += it.effort
  }
  if (cur.length) batches.push(cur)

  return batches.map((b, i) => ({
    batch: i + 1,
    paths: [...new Set(b.map(x => x.path))],
    features: [...new Set(b.map(x => x.feature))],
    totalEffort: b.reduce((a, x) => a + x.effort, 0),
    blocked: b.filter(x => x.fix === 'rewrite').length,
  }))
}
```

**评分点**：
- effort 加权装箱（每批 ≤ 13 点——PR 大小约束的量化）
- 依赖序先于成本序（API 形态统一后再迁移，避免返工）
- 批内 paths/features 去重（一条路由多项断点合并进同批）
- blocked 计数（rewrite 项占比高的批次要提前排期——计划器要暴露风险）
