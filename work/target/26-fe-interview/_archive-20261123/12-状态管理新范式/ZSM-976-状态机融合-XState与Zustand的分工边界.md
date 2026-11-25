---
title: [976] XState 状态机与 Zustand 状态库在应用里怎么分工
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 状态机]
type: 面试题
---

## 976：XState 状态机与 Zustand 状态库在应用里怎么分工

**答**：
- 分工原则：XState 管「有生命周期与合法迁移的状态机」（下单流程/审批流/向导——状态转换有严格规则），Zustand 管「无结构约束的共享数据」（用户偏好/草稿/主题）——状态机管「行为」，状态库管「数据」。
- 衔接模式：状态机的 context 存「过程数据」（当前步骤的表单值），完成时把结果「提交」到 Zustand（状态机是数据的加工流水线，zustand 是仓库）；状态机事件可以读 zustand（setup 里注入输入）。
- 判断标准：状态能否画成有限状态图？能 -> XState（非法转换在编译期杜绝）；只是「一堆相关值」-> Zustand——用状态机建模「值集合」是把机器当垃圾桶（反模式）。
- 追问钩子：为什么「下单流程」特别适合状态机？——下单有明确的合法路径（购物车->填写->支付->完成）与非法跳转（未支付直接完成）——状态机让非法状态不可表示（比 if/else 守卫可靠）。

```ts
// 状态机：管流程；zustand：管数据
const checkoutMachine = setup({
  stores: { cart: getStore } , // 从 zustand 读输入
}).createMachine({
  initial: 'idle',
  states: { idle: { on: { START: 'filling' } },
    filling: { on: { SUBMIT: 'paying' } },        // 非法跳转不可表示
    paying: { on: { PAID: 'done' } }, done: {} },
});
// PAID 事件处理里：zustand.setState({ orders: [...prev, ctx.order] })
```
