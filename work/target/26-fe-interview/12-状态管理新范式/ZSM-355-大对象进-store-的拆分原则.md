---
title: [ZSM-355] 一个 10MB 的 JSON 响应怎么进 store
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-355：一个 10MB 的 JSON 响应怎么进 store

**答**:
- 先问要不要全进内存：多数字段消费面窄——裁剪进 store（只取渲染需要的列），全量留在 IndexedDB/服务器按需查
- 进 store 时的结构改造：数组归一化（Map<id, row> + 顺序数组）、嵌套拍平、大字符串（base64 图/富文本）挪出主 store
- 订阅隔离：10MB 对象任何一处变更触发全订阅者比较——归一化后按 id 切片订阅，变更通知粒度降到行级
- 兜底：必须全存时用「冷热分离」（ZSM-324）+ 结构共享更新，避免每次 set 全量复制

```javascript
// 10MB 响应的进仓改造
const { rows, order } = await api.export()
const index = new Map(rows.map((r) => [r.id, pickColumns(r, RENDER_COLS)]))   // 裁剪 + 归一化
useStore.setState({ rowIndex: index, rowOrder: rows.map((r) => r.id), meta: order })
rowsBigStore = idbPut('export', rows)                                        // 全量落盘
```
