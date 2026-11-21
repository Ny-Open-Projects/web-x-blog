---
title: [ZSM-073] TanStack Query 的失效策略怎么设计？invalidateQueries 与 setQueryData/ resetQueries 的取舍
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-073：TanStack Query 的失效策略怎么设计？invalidateQueries 与 setQueryData/resetQueries 的取舍
**答**：
- 默认姿势 invalidateQueries：标记 stale + 触发活跃订阅重取，服务端数据是权威，写操作后用它最稳。
- setQueryData：用 mutation 响应直接写缓存（服务端返回了完整新对象时），省一次请求；前提是响应可信且结构同缓存。
- resetQueries：回到 initialData 并重取，用于「重置到服务端初始视图」（退出筛选、测试清态）。
- 精度选择：invalidate(['goods']) 全失效 vs invalidate(['goods', 'detail', id]) 点失效；列表分页场景精确失效避免全列表闪动。
- 取舍口诀：能精确就精确，拿不准就粗失效（数据正确性优先于少一次请求）。

```javascript
onSuccess: (updated) => {
  // A. 服务端回了完整对象 → 直接写
  qc.setQueryData(['goods', 'detail', updated.id], updated)
  // B. 列表只失效对应页，避免全列表 loading
  qc.invalidateQueries({ queryKey: ['goods', { page: updated.page }] })
}
// 退出登录清全部
qc.resetQueries()
qc.removeQueries() // 彻底删除
```
