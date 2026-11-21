---
title: [ZSM-006] Zustand 的 persist 版本迁移（version/migrate）怎么做？老用户数据结构变了怎么办？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-006：Zustand 的 persist 版本迁移（version/migrate）怎么做？老用户数据结构变了怎么办？
**答**：
- persist 会在存入时写一个 `version` 字段；读回时若版本与当前 `version` 不一致，把旧数据交给 `migrate(persistedState, oldVersion)` 处理后再合并。
- migrate 按旧版本号逐级升级（写 if/switch 链），返回新结构；不提供 migrate 时版本不匹配会丢弃存储并警告。
- 迁移要防御性处理：字段缺失、类型错误、JSON 损坏都要兜底，迁移失败抛错会导致本次水合失败。
- 场景包装：购物车从「数组」升级为「对象 map」结构，老用户刷新后购物车不能清空。

```javascript
persist((set) => ({ /* v2: items 由数组改为 map */ }), {
  name: 'cart', version: 2,
  migrate: (old, version) => {
    if (version === 0) return { items: {} }            // v0 没有结构化数据，直接重置
    if (version === 1) {
      // v1: [{id, qty}] → v2: { [id]: {qty} }，防御字段缺失
      const items = {}
      for (const it of (old.items ?? [])) {
        if (it?.id) items[it.id] = { qty: it.qty ?? 1 }
      }
      return { items }
    }
    return old
  },
})
```
