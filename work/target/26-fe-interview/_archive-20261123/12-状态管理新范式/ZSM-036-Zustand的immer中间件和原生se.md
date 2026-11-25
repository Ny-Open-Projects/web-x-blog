---
title: [ZSM-036] Zustand 的 immer 中间件什么时候值得用？它改变了 set 的什么行为？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-036：Zustand 的 immer 中间件什么时候值得用？它改变了 set 的什么行为？
**答**：
- immer 中间件让 set 收到「draft 草稿」：可以直接赋值/修改嵌套字段，immer 用 Proxy 记录变更并产出不可变新 state。
- 改变的行为：set 从「返回部分新对象 + 手动逐层展开」变为「修改 draft，自动生成新引用」；浅合并语义不再需要（你改哪就是哪）。
- 值得用的场景：深嵌套结构（树、目录、配置面板）更新频繁，手写展开易漏层；数据结构复杂但心智想「可变」。
- 代价：增加 immer 体积与 Proxy 开销；高性能热点（万级列表单行更新）手写展开往往更快、更可控。

```javascript
import { immer } from 'zustand/middleware/immer'

const useTree = create(immer(set => ({
  tree: { children: [{ id: 1, name: 'a' }] },
  rename: (id, name) => set(state => {
    // 直接改 draft，不用逐层展开
    const node = find(state.tree, id)
    node.name = name
  }),
})))
```
