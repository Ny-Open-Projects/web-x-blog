---
title: [977] 用状态机替代 Zustand 的 action 逻辑（防非法状态）
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 状态机]
type: 面试题
---

## 977：用状态机替代 Zustand 的 action 逻辑（防非法状态）

**答**：
- 反模式识别：Zustand store 里长满 if/else（action 里判断「当前能不能做这个操作」）——这些判断就是隐式状态机；显式化为 XState 后「非法操作」直接不可触发（事件在当前状态没有定义就不响应）。
- 混合模式实现：XState 管状态转换 + Zustand 管数据快照——状态机 transition 回调里同步数据到 zustand（单向：机器 -> 数据库），组件从两边各取所需（状态用机器、数据用 store）。
- 收益量化：非法状态 bug（点了不该点的按钮/重复提交/状态错乱）在状态机化后归零——「非法状态不可表示」是类型系统之外的另一道结构防线。
- 追问钩子：什么时候不要状态机化？——状态少于 4 个且转换无条件分支的（两个布尔值的状态），状态机的建模成本超过收益——避免「状态机教条主义」。

```ts
// 状态机驱动 zustand 数据写入
const machine = createMachine({
  states: {
    editing: { on: { SAVE: { target: 'saving',
      actions: assign(({ event }) => saveToStore(event.draft)) } } },
    saving: { on: { SAVED: 'idle', FAILED: 'editing' } },
    idle: { on: { EDIT: 'editing' } },
  },
});
// 组件：const state = useSelector(actor, s => s.value);  // 状态来自机器
//        const draft = useStore(s => s.draft);           // 数据来自 store
```
