---
title: [ZSM-668] XState 的 meta 与 tags：状态元数据在 UI 层的用法
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-668：XState 的 meta 与 tags：状态元数据在 UI 层的用法

**答**：
- tags 是状态的**语义标签**：`loading: { tags: ['pending'] }`、`ready: { tags: ['success'] }`。消费方式 `state.hasTag('pending')`——UI 层不必知道状态名（`.idle/.loading/.success`），只问「当前有没有这个语义」；tags 可多状态共享（loading/erroring 都有 'busy' 标签），重构状态树（改名/合并状态）UI 不用改。
- meta 是状态的**结构化元数据**：`meta: { analyticsId: 'checkout_step2', trackTiming: true }`，消费 `state.meta` 聚合（嵌套状态逐层合并）。用途：埋点配置、路由标题、测试断言清单——把「伴随状态的配置」声明在状态里而非散在组件。
- 实战模式：1) 全局 UI 状态条（顶部进度条）订阅 `hasTag('busy')`；2) 埋点驱动——transition 时读 `meta.analyticsId` 上报，规则随状态机演进自动同步；3) tags 做样式类名（`className={state.hasTag('error') ? 'text-red' : ''}`）。
- 与 context 的分工：meta/tags 是「静态描述」（同一状态永远一样），context 是「运行数据」（每实例不同）——可枚举的伴随信息放 meta，实例数据放 context。
- 追问钩子：tags 让状态机的「语义面」与「结构面」解耦——产品说「转圈时不能点提交」，实现就是 `hasTag('busy')` 而不是列举所有转圈状态名。

```javascript
import { setup, createActor } from 'xstate'

const machine = setup({}).createMachine({
  id: 'checkout',
  initial: 'idle',
  states: {
    idle: { tags: ['ready'], meta: { analyticsId: 'checkout_idle' } },
    loading: { tags: ['pending', 'busy'], meta: { analyticsId: 'checkout_loading', trackTiming: true } },
    review: { tags: ['ready'], meta: { analyticsId: 'checkout_review' } },
    failed: { tags: ['error', 'busy'], meta: { analyticsId: 'checkout_failed' } },
  },
})

const actor = createActor(machine)
actor.start()

// UI 层只消费语义标签
function StatusBar() {
  const state = useActor(actor)
  return (
    <div className={state.hasTag('error') ? 'bar error' : state.hasTag('pending') ? 'bar pending' : 'bar'}>
      {state.hasTag('busy') && <Spinner />}
    </div>
  )
}

// 埋点：meta 驱动
actor.subscribe((state) => {
  const meta = state.meta    // 嵌套状态 meta 逐层合并
  const id = Object.values(meta).at(-1)?.analyticsId
  if (id) analytics.track(id, { ts: Date.now() })
})

// 重构免疫：状态改名 idle→initial，hasTag('ready') 不变
```
