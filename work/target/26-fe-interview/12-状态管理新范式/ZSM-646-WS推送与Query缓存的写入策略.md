---
title: [ZSM-646] WebSocket 推送与 Query 缓存的写入策略：直接写还是失效拉
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-646：WebSocket 推送与 Query 缓存的写入策略：直接写还是失效拉

**答**：
- WS 推送更新缓存的两条路：**直接写**（setQueryData/setQueriesData，推送里带完整最新数据，写完立即生效零延迟）和**失效拉**（invalidateQueries，推送只作为「信号」，数据靠 refetch 拿）。决策标准：推送载荷是否完整、缓存条目是否可定位、写入是否需要合并逻辑。
- 直接写适用：单实体精确推送（`todo.updated` 带 id 和完整对象）——`setQueryData(['todo', id], payload)`，确定性写入；列表推送要合并时用 setQueriesData 的 updater（如 `insert if not exists`）。
- 失效拉适用：1) 推送只带变更信号（`counters.changed`）不带数据；2) 影响聚合/排序（直接写会把「新数据」插进按旧规则排序的列表，出现排序错乱——失效重拉保序）；3) 影响多个缓存条目且写入逻辑复杂。**带 debounce**——推送风暴（1 秒 50 条）时失效要节流，比如 500ms 合并一轮。
- 混合策略（生产主流）：**关键数据直接写 + 兜底失效**——先 setQueryData 保证即时性，同时 debounce invalidate 做终局对账（推拉结合，两端一致）。
- 追问钩子：WS 重连后的「状态追平」——重连成功时先 invalidate 全部活跃缓存（lastSeq 只能靠服务端增量接口补齐时才用增量）。

```javascript
// WS → 缓存桥（生产骨架）
const pendingInvalidations = new Set()
let flushTimer = null

ws.on('message', (msg) => {
  switch (msg.type) {
    case 'todo.updated':
      // 精确推送：直接写
      queryClient.setQueryData(['todo', msg.id], msg.payload)
      break
    case 'todo.created':
      queryClient.setQueriesData({ queryKey: ['todos', 'list'] }, (old) =>
        old?.items.some((i) => i.id === msg.payload.id) ? old
          : { ...old, items: [msg.payload, ...old.items] })
      // 聚合字段不确定 → 兜底失效
      scheduleInvalidate(['todos', 'stats'])
      break
    case 'list.reordered':          // 只带信号：失效拉（保排序正确）
      scheduleInvalidate(['todos', 'list'])
      break
  }
})

// 失效去抖：推送风暴合并
function scheduleInvalidate(keyPrefix) {
  pendingInvalidations.add(keyPrefix.join('|'))
  clearTimeout(flushTimer)
  flushTimer = setTimeout(() => {
    pendingInvalidations.forEach((p) => queryClient.invalidateQueries({ queryKey: p.split('|') }))
    pendingInvalidations.clear()
  }, 500)
}

// 重连追平
ws.on('reconnected', () => {
  queryClient.invalidateQueries({ refetchType: 'active' })   // 全量活跃缓存对账
})
```
