---
title: [ZSM-226] immer 中间件怎么让 set 里直接改草稿（源码级）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-226：immer 中间件怎么让 set 里直接改草稿（源码级）

**答**：
- immer 中间件把 set 包装为 `produce`：业务写的 `(state) => { state.x = 1 }` 是对 Proxy 草稿的修改，produce 返回新不可变对象后再交给底层 set
- 包装后 set 的 replace 语义仍在（第二参数 true 时走原 setState replace），但 `set(() => ({...}), true)` 与 immer 的组合要小心：replace 会绕过 produce
- 典型 bug：在 immer set 里返回新对象又想 replace，或对 Map/Set 用普通方法——要启用 enableMapSet 插件
- 成本：Proxy 创建与最终 freeze 有开销，超大高频 store 慎用；深层嵌套更新场景收益才明显

```javascript
const useStore = create(immer((set) => ({
  tree: { a: { b: [] } },
  addItem: (item) => set((s) => { s.tree.a.b.push(item) }),  // 直接改，无展开
  // replace: set((s) => nextState, true)  // 此时 immer produce 不介入替换语义
})))
```
