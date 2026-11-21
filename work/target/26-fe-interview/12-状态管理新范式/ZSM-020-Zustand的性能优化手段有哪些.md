---
title: [ZSM-020] 用 Zustand 做大列表（万级商品）页面，有哪些性能优化手段？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-020：用 Zustand 做大列表（万级商品）页面，有哪些性能优化手段？
**答**：
- 数据结构归一化：state 存 `{ byId, ids }`，selector 按 id 取单条，勾选/置顶只更新一条，避免整列表新数组。
- selector 拆到原子：每个 item 组件 `useStore(s => s.byId[id])`，id 是稳定引用，其他行更新不会触发本行。
- 高频更新（滚动位置、hover）单独拆 store 或用 subscribeWithSelector 监听，不入 React 渲染流。
- 列表组件配合虚拟滚动；选中项这类派生值用 useMemo 在 render 层算，别进 store。
- actions 保持引用稳定：定义在 create 闭包里天然稳定，别在组件里每次 set 新函数。

```javascript
const useGoods = create(set => ({
  byId: {}, ids: [],
  toggleLike: id => set(s => ({
    // 只新建受影响的那个对象，其余行引用不变
    byId: { ...s.byId, [id]: { ...s.byId[id], liked: !s.byId[id].liked } },
  })),
}))
function Row({ id }) {
  const item = useGoods(s => s.byId[id])  // 单行订阅
  return <li onClick={() => useGoods.getState().toggleLike(id)}>{item.title}</li>
}
```
