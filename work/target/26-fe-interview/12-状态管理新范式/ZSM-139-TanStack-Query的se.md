---
title: [ZSM-139] TanStack Query 的 select 选项有什么用？怎么用它减少无效重渲染？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-139：TanStack Query 的 select 选项有什么用？怎么用它减少无效重渲染？
**答**：
- select 是「缓存到组件之间」的派生管道：缓存里存全量数据，组件只订阅 select 的输出，结果引用不变（结构共享作用于 select 结果）就不重渲染。
- 典型场景：缓存整份用户对象，组件只取 userName——缓存里其他字段变化不再波及该组件，相当于内建 selector。
- 注意 select 必须是稳定引用（组件外定义或 useMemo/useCallback 包裹），内联箭头函数每次渲染都是新引用会导致 memo 失效、每次都重算。
- 复杂派生（过滤+排序大列表）放 select 里还能借到 TanStack 的缓存比较，比在 render 里每次算便宜。

```javascript
// 组件外稳定引用
const selectName = (user) => user?.name
const selectHotGoods = (data) =>
  (data?.list ?? []).filter(g => g.heat > 1000).sort((a, b) => b.heat - a.heat)

function UserName() {
  // 缓存是全量 user，本组件只订阅 name
  const { data: name } = useQuery({ queryKey: ['me'], queryFn: api.me,
                                    select: selectName })
  return <span>{name}</span>
}

function HotList() {
  const { data: hot } = useQuery({ queryKey: ['goods-list'], queryFn: api.goodsList,
                                   select: selectHotGoods })
  return <List items={hot ?? []}/>
}
```
