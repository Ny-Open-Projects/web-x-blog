---
title: [ZSM-005] Zustand 的 persist 怎么只持久化部分字段？函数和临时态为什么要排除？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-005：Zustand 的 persist 怎么只持久化部分字段？函数和临时态为什么要排除？
**答**：
- persist 默认会把整个 state JSON 序列化写入 storage，用 `partialize` 挑选需要持久化的切片，函数字段和临时态必须排除。
- 排除函数：JSON.stringify 会静默丢弃函数，但读回合并时多余字段会污染 state，显式排除更安全。
- 排除临时态：如表单输入中、弹窗开关、loading 标记，刷新后恢复反而造成「页面卡在加载」的 bug。
- 水合时机：默认同步读回（localStorage）；SSR 场景要 `skipHydration: true`，在客户端手动 `persist.rehydrate()`，避免服务端与客户端内容不一致。
- 追问钩子：跨标签页同步可监听 storage 事件或用 persist 的 onRehydrateStorage。

```javascript
const useCart = create(persist(
  (set) => ({
    items: [], isOpen: false, loading: false,   // isOpen/loading 是临时态
    add: item => set(s => ({ items: [...s.items, item] })),
  }),
  {
    name: 'cart',
    partialize: ({ items }) => ({ items }),  // 只存 items
    onRehydrateStorage: () => (state, err) => {
      // err 非空说明 JSON 损坏或版本迁移失败，可回退默认值
      console.log('rehydrated', err)
    },
  }
))
```
