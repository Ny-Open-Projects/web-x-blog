---
title: [ZSM-344] 缓存 key 体系怎么设计才能「改哪失效哪」
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-344：缓存 key 体系怎么设计才能「改哪失效哪」

**答**:
- key 是失效的坐标系：结构约定 `['资源', 参数..., '视图']`——资源在前保证前缀失效命中，参数居中区分实例，视图在后（如 ['order', id, 'detail']）
- key 工厂函数：`orderKeys.detail(id)` 单点定义，禁止手写数组字面量散落各处——写错一个字段就是永不失效的缓存
- 参数规范化：进入 key 的参数必须稳定序列化（排序后 JSON、时间戳而非 Date、null 而非 undefined），否则同语义不同 key
- 失效映射表：维护「写操作 → 影响的 key 前缀」清单（代码化或文档化），新增接口必须登记——失效正确性靠这张表而不是记忆

```javascript
// key 工厂
export const orderKeys = {
  all: ['order'],
  list: (filters) => [...orderKeys.all, 'list', stableStringify(filters)],
  detail: (id) => [...orderKeys.all, 'detail', String(id)],
}
// 失效映射
const invalidations = {
  'POST /order': [orderKeys.all, ['stats']],
  'PATCH /order/:id': [(id) => [orderKeys.detail(id), ...orderKeys.list({})]],
}
```
