---
title: [ZSM-058] Jotai 里直接 mutate atom 里的对象（atom.value.xxx = 1）会发生什么？为什么必须不可变更新？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-058：Jotai 里直接 mutate atom 里的对象（atom.value.xxx = 1）会发生什么？为什么必须不可变更新？
**答**：
- 基础 atom 用 useSetAtom 传新引用才触发更新；直接改引用内字段，值对象还是同一个，所有依赖比较（Object.is）都判定「没变」，UI 不更新——数据偷偷变了但视图静止。
- 派生 atom 依赖旧对象算出的缓存也仍然有效，脏读。
- 正确姿势：`set(objAtom, prev => ({ ...prev, xxx: 1 }))` 或用 jotai-immer（atomWithImmer）写 draft。
- 不可变更新让「引用相等 = 内容相等」成立，这是所有原子化/响应式库 Diff 的基石。

```javascript
const userAtom = atom({ name: 'a', tags: ['x'] })

// 错误：静默失效
const u = useAtomValue(userAtom); u.tags.push('y') // UI 不更新

// 正确
const setUser = useSetAtom(userAtom)
setUser(prev => ({ ...prev, tags: [...prev.tags, 'y'] }))

// 或 jotai-immer
const userImmerAtom = atomWithImmer({ name: 'a', tags: ['x'] })
// setUser(draft => { draft.tags.push('y') })
```
