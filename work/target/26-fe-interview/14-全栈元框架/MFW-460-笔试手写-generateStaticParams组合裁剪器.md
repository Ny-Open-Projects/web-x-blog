---
title: [MFW-460] 笔试：手写 generateStaticParams 组合爆炸裁剪器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-460：generateStaticParams 组合爆炸裁剪器
**答**：实现 `pruneStaticParams(segments, { max = 10000 })`：1) segments = [{ name, values: [] }]（如 [{ name:'category', values:[...] }, { name:'slug', values:[...] }]）；2) 笛卡尔积展开预览总路径数，超 `max` 时按段优先级裁剪：从最后一段起截断到 `max / 前面已展开数` 个（高频前缀优先静态化，长尾走 fallback）；3) 返回 { combos: [[...]], truncated: true, dropped: n }；4) 空段（values 空）视为动态段，不参与展开。

```javascript
export function pruneStaticParams(segments, { max = 10000 } = {}) {
  const live = segments.filter(s => s.values.length > 0)
  let total = live.reduce((acc, s) => acc * s.values.length, 1)
  const plan = live.map(s => [...s.values])
  let truncated = false, dropped = 0
  if (total > max) {
    truncated = true
    // 从最后一段往前裁，保住高优先级（靠前）段的全部组合
    for (let i = plan.length - 1; i >= 0 && total > max; i--) {
      const prefix = plan.slice(0, i).reduce((a, s) => a * s.length, 1)
      const keep = Math.max(1, Math.floor(max / prefix))
      dropped += plan[i].length - Math.min(plan[i].length, keep)
      plan[i] = plan[i].slice(0, keep)
      total = plan.reduce((a, s) => a * s.length, 1)
    }
  }
  // 展开笛卡尔积（含空段占位）
  const combos = plan.length
    ? plan.reduce((acc, cur) =>
        acc.flatMap(p => cur.map(v => [...p, v])), [[]])
    : []
  return { combos, truncated, dropped, total: combos.length }
}
```

**评分点**：
- 笛卡尔积先算总数再决定裁剪（不盲目展开爆内存）
- 从尾段裁、保头段（业务上首段类目页优先全静态）
- 空段跳过（动态段不进 SSG 矩阵）
- dropped/truncated 可审计（构建日志能解释为什么少了页面）
