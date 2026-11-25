---
title: [ZSM-043] Jotai 的 atomFamily 和 atomWithStorage/atomWithReset 分别解决什么问题？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-043：Jotai 的 atomFamily 和 atomWithStorage/atomWithReset 分别解决什么问题？
**答**：
- atomFamily：按参数动态生成 atom 的工厂（`atomFamily(id => atom(0))`），用于列表/会话每行独立状态，内部缓存避免重复创建，等价 Zustand 的 store 工厂。
- atomWithStorage：atom 与 localStorage/AsyncStorage 双向同步（读写走 storage），自带 JSON 序列化与跨标签页监听。
- atomWithReset：提供 `RESET` 哨兵，`useResetAtom` 一键恢复初始值，比手写 reset atom 更不易漏字段。
- 三者体现 Jotai 的「工具函数生态」：状态需求拆成原子工具组合，而不是写一个万能 store。

```javascript
import { atomFamily, atomWithStorage, atomWithReset, useResetAtom, RESET } from 'jotai/utils'

// 每个商品独立 liked atom
const likeFamily = atomFamily(id => atom(false))

// 主题持久化 + 跨标签页
const themeAtom = atomWithStorage('theme', 'light')

// 表单草稿可整体重置
const draftAtom = atomWithReset({ title: '', body: '' })
function Editor() {
  const reset = useResetAtom(draftAtom)
  return <button onClick={() => reset(RESET)}>清空草稿</button>
}
```
