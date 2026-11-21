---
title: [ZSM-062] Jotai + TanStack Query 混合架构里，Query 的数据怎么进入派生 atom 参与计算？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-062：Jotai + TanStack Query 混合架构里，Query 的数据怎么进入派生 atom 参与计算？
**答**：
- 原则：Query 是服务端状态唯一事实源；atom 只做「视图派生」，不复制数据本体。
- 方式一：组件里 `const { data } = useQuery(...)` 再把 data 写进 UI 派生 atom（如选中行、过滤后列表），写的是派生结果不是源数据。
- 方式二：选中态双向 atom（选中集合）+ 组件里用 useMemo 把 data × selected 求交，atom 不感知 data。
- 反例：把 data 全量 setState 进 atom，Query invalidate 后 atom 与缓存脱节出现旧数据。
- 关键判据：数据刷新后派生 atom 必须自动跟着变——只要 atom 不持有源数据，这个性质天然成立。

```javascript
const selectedIdsAtom = atom(new Set()) // 纯客户端选择态

function GoodsTable({ data }) {         // data 来自 useQuery
  const selected = useAtomValue(selectedIdsAtom)
  const rows = useMemo(
    () => data.filter(g => selected.has(g.id)), // 派生留在渲染层
    [data, selected],
  )
}
```
