---
title: [ZSM-045] Jotai 和 Zustand 怎么选？什么状态适合 atom 化？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-045：Jotai 和 Zustand 怎么选？什么状态适合 atom 化？
**答**：
- 同作者出品、可共存。经验法则：状态间有派生关系、需要细粒度组合（表单联动、可视化配置、权限矩阵）→ Jotai；命令式全局单例（用户态、购物车）、组件外读写、IM/WS 推送 → Zustand。
- Jotai 的 atom 树自动最小化重渲染，无 selector 心智负担；代价是 atom 数量多、需要组织文件结构，异步状态管理弱于 Query。
- Zustand 一个 store 一份心智，适合「状态少而集中」；Jotai 适合「状态多而互联」。
- 混用模式：Zustand 放会话级全局态，Jotai 放页面内派生态，两者互不依赖是常见生产组合。

```javascript
// Jotai 擅长的：三个字段互相派生，UI 自动只重算受影响 atom
const baseAtom = atom(100)
const rateAtom = atom(0.1)
const withTaxAtom = atom(get => get(baseAtom) * (1 + get(rateAtom)))
const formattedAtom = atom(get => `¥${get(withTaxAtom).toFixed(2)}`)

// Zustand 擅长的：WS 推送全局消息
const useIm = create(set => ({ msgs: [], onPush: m => set(s => ({ msgs: [...s.msgs, m] })) }))
```
