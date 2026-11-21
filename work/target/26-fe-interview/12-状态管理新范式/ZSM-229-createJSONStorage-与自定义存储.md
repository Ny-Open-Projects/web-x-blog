---
title: [ZSM-229] persist 怎么换存储介质 createJSONStorage 源码面
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-229：persist 怎么换存储介质，createJSONStorage 的源码面

**答**：
- persist 的 storage 选项接受 `createJSONStorage(() => AsyncStorage | sessionStorage | IndexedDB 封装)`，约定接口为 getItem/setItem/removeItem（返回值可为 Promise）
- createJSONStorage 做两件事：惰性调用 getStorage 工厂（SSR 环境下避免顶层访问 window 报错）+ JSON.stringify/parse 包装
- SSR 关键：storage 工厂返回 undefined/null 时 persist 静默跳过持久化，这正是服务端安全的原因——不要直接 `() => localStorage`
- 大对象用 IndexedDB（idb-keyval）替代 localStorage 的 5MB 上限，接口一致零迁移成本

```javascript
import { persist, createJSONStorage } from 'zustand/middleware'
import { get, set, del } from 'idb-keyval'

create(persist((set) => ({...}), {
  name: 'big-store',
  storage: createJSONStorage(() => typeof window === 'undefined' ? undefined : idbStore), // SSR 安全
}))
```
