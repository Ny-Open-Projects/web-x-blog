---
title: [ZSM-234] atomFamily 的参数化缓存怎么清理防泄漏
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-234：atomFamily 的参数化缓存怎么清理防泄漏

**答**：
- atomFamily(参数 => atom) 内部是 Map 缓存，同参数返回同一 atom 实例——是「动态数量原子」的标配（列表每行一个、每个商品一个）
- 泄漏面：参数空间无限增长（每条消息一个 atom）时 Map 永不清除；需要业务侧调用 `family.remove(param)` 主动回收
- 参数必须是原始值或稳定可比较的结构，`shouldRemove` 选项可做条件清理（如基于过期时间）
- 与 atomWithStorage/atomWithQuery 组合时，remove 前要确认没有活跃订阅，否则组件下次挂载重建成本高

```javascript
const messageAtom = atomFamily(
  (id) => atom(undefined, { unstable_timeoutMs: 60_000 }),  // 实验性超时清理
  { shouldRemove: (created, id) => Date.now() - created > 3600_000 }  // 条件回收
)
messageAtom.remove('msg_123')   // 明确不需要时主动删
```
