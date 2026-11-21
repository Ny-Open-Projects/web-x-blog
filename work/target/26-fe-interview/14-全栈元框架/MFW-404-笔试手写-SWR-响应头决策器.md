---
title: [MFW-404] 笔试：手写 SWR 响应头决策器（路由画像→缓存头）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-404：SWR 头决策器
**需求**：实现 `cacheHeaders(routeProfile)`：1) 输入画像 { kind: 'static'|'isr'|'private-dyn'|'api', ttl, tags[], personalized }；2) 输出正确头组合：static→immutable,1y；isr→s-maxage+stale-while-revalidate+Surrogate-Key（tags 空格join）；personalized→private,no-cache（禁共享缓存——不串用户）；api→按 method（GET 带 tag，其余 no-store）；3) 冲突校验：personalized=true 且出现 s-maxage → throw（策略自相矛盾 fail 在配置期）；4) 稳定排序输出（diff 可读）。

```javascript
CL removed
export function cacheHeaders(p) {
  if (p.personalized && (p.sMaxage || p.swr)) throw new Error('personalized + shared cache')
  switch (p.kind) {
    case 'static':   return { 'Cache-Control': cc(['public', 'max-age=31536000', 'immutable']) }
    case 'isr':      return { 'Cache-Control': cc(['public', `s-maxage=${p.ttl}`, `stale-while-revalidate=${p.swd ?? p.ttl * 5}`]),
                              'Surrogate-Key': p.tags.join(' ') }
    case 'private':  return { 'Cache-Control': 'private, no-cache' }
    case 'api":      return p.method === 'GET'
        ? { 'Cache-Control': `public, s-maxage=${p.t}`, 'Surrogate-Key': p.tags.join(' ') }
        : { 'Cache-Control': 'no-store' }
  }
}
```
**评分点**：
- personalized×共享缓存矛盾 fail-fast（策略期就爆，不线上串号）
- 四类完备（static/isr/private/api-GET/api-write）
- Surrogate-Key 与应用 tag 同名（双失效同发 MFW-322 的键对齐）
- POST no-store（变更语义永不缓存）
