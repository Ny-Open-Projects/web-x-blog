---
title: [ZSM-040] 排查题：页面刷新后 Zustand 里部分字段变回默认值，怎么定位？可能原因有哪些？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-040：排查题：页面刷新后 Zustand 里部分字段变回默认值，怎么定位？可能原因有哪些？
**答**：
- 先确认是否走了 persist：storage 里有没有该 key；有 key 但字段丢了多半是 partialize 没包含该字段，或字段被函数类型过滤掉。
- 版本迁移：persist 的 version 变了但没写 migrate，旧数据整体被丢弃——查 version 与 migrate 链。
- 水合竞态：初始化代码在 rehydrate 完成后执行 `setState(默认值)` 把恢复值覆盖；用 onRehydrateStorage 回调里再初始化，或调整执行顺序。
- 多入口/多 store：同 key 写入互相覆盖（两个 store 共用 name），或 SSR 串数据（模块级单例）。
- 定位手段：devtools 看动作时间线 + onRehydrateStorage 的 error 参数 + localStorage 快照比对。

```javascript
persist((set) => ({ /* ... */ }), {
  name: 'app',
  partialize: s => ({ theme: s.theme }), // ← 若漏了 lang，刷新后 lang 回默认
  onRehydrateStorage: () => (state, error) => {
    if (error) console.error('hydrate fail', error) // 第一步先看这里
  },
})
```
