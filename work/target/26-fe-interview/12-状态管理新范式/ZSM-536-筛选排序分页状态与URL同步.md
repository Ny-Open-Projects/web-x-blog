---
title: [ZSM-536] 列表页筛选/排序/分页状态为什么要以 URL 为单一事实源
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-536：列表页筛选/排序/分页状态为什么要以 URL 为单一事实源

**答**：
- URL 作为事实源（SSOT）的价值：刷新/分享/回退不丢筛选状态；浏览器前进后退天然成为「筛选历史」的 undo 栈；埋点和服务端日志能直接看到状态——全都是白得的。
- 实现方向：**URL → 状态**：解析 `searchParams` 到 store 初始值；**状态 → URL**：交互变更时 `history.replaceState`（或框架 router 的 replace）写回。避免用 push 导致每次改筛选都多一条历史。
- 校验与归一化：URL 参数是不可信输入，解析层要白名单校验 + 默认值兜底（`page` 必须正整数、`sort` 必须在允许集合里），脏参数静默修正，别让 `?page=999999` 崩掉列表。
- 状态分层：URL 存「可共享视图状态」（筛选/排序/页码），store 存「会话态」（滚动位置、多选集合、乐观变更）——不是所有状态都该进 URL。
- 追问钩子：防抖写回（输入类筛选 300ms）避免历史污染；表单类筛选点「查询」才 replace 一次。

```javascript
// 解析层：白名单 + 默认值
const DEFAULTS = { page: 1, pageSize: 20, sort: 'time_desc', q: '', status: 'all' }
const SORTS = new Set(['time_desc', 'price_asc', 'price_desc'])

function parseQuery(search) {
  const sp = new URLSearchParams(search)
  const page = Math.max(1, parseInt(sp.get('page') ?? '1', 10) || 1)
  const sort = SORTS.has(sp.get('sort')) ? sp.get('sort') : DEFAULTS.sort
  return {
    page,
    pageSize: Math.min(100, parseInt(sp.get('pageSize') ?? '20', 10) || 20),
    sort,
    q: (sp.get('q') ?? '').slice(0, 100),          // 长度防注入
    status: ['all', 'paid', 'refunded'].includes(sp.get('status')) ? sp.get('status') : 'all',
  }
}

function writeQuery(q) {
  const sp = new URLSearchParams()
  Object.entries(q).forEach(([k, v]) => { if (String(v) !== String(DEFAULTS[k])) sp.set(k, v) })
  history.replaceState(null, '', `?${sp}`)         // replace：不污染历史
}

const useListQuery = create((set) => ({
  ...parseQuery(location.search),
  update(patch) {
    const next = { ...useListQuery.getState(), ...patch, page: patch.page ?? 1 }
    // 改筛选回到第 1 页（改页码除外）
    set(next)
    writeQuery(next)
  },
}))
```
