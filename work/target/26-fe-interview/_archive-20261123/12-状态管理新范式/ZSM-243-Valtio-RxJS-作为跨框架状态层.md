---
title: [ZSM-243] RxJS Observable 怎么当跨框架状态层用
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-243：RxJS Observable 怎么当跨框架状态层用

**答**：
- Observable 天然框架无关：React 用 useSyncExternalStore + subscribe/getValue 桥，Vue 用 rxjs 库转 ref，Angular 原生 async pipe
- BehaviorSubject 当 store：有当前值（getValue 供 getSnapshot 用），subscribe 供订阅，next 供写入——正好满足 useSyncExternalStore 三件套
- 适合事件流丰富（合并/节流/重试操作符）的场景；纯 CRUD 状态用它过重
- 陷阱：getSnapshot 必须稳定——BehaviorSubject.getValue 返回引用值即可；subscribe 里要即时退订防泄漏

```javascript
import { BehaviorSubject } from 'rxjs'
const theme$ = new BehaviorSubject('dark')

// React 桥
function useTheme() {
  return useSyncExternalStore(
    (cb) => { const s = theme$.subscribe(cb); return () => s.unsubscribe() },
    () => theme$.getValue(),
  )
}
theme$.next('light')   // Vue/Angular/React 同时收到
```
