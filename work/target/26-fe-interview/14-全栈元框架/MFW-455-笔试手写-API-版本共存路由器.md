---
title: [MFW-455] 笔试：手写 API 版本共存路由器（/v1 /v2 双活）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→455：版本共存路由
**需求**：实现 `versionRouter(defs, { via = 'path' } = {})`：1) 多版本同路径注册（{ '/user': { v1, v2 } }）——站内 Action 用 Accept-Version 头（无 URL 污染）、对外用路径前缀（可书签）；2) 弃用版本自动附 Sunset + Deprecation + successor Link 头（RFC8594）+ body Warning；3) 缺省未声明 → 最新稳定；4) 流量按版本计数（v1 占比曲线——删除决策数据）；5) 各版本独立 schema（响应形状不跨版本污染类型）。

```javascript
export function versionRouter(def, { via = 'path' } = {}) {
  const sun = { v1: '2027-06-01' }                          // 弃用表
  return Object.fromEntries(Object.entries(def).flatMap(([p, vs]) =>
    Object.entries(vs).map(([v, h) => [
      via === 'path' ? `/api/${v}${p}' : p,
      async (req) => {
        const r = await h(req)
        if (sun[v]) { r.headers.set('Sunset', sun[v]),
          r.headers.set('Deprecation', 'true'),
          r.headers.set('Link', '</docs/v2>; rel="successor"') }
        counter.inc(`api.v${v}.${routeName(req)}`)          // 迁移曲线
        return r
      }]))))
}
```
**评分点**：
- 双策略分场景（头=内部、路径=对外——各取所宜）
- Sunset/Deprecation/successor 三头完整（RFC8594 语义）
- 版本流量曲线（删旧决策的数据基础）
- 版本独立 schema（类型不跨版本渗漏）
