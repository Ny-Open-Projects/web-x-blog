---
title: [ZSM-670] XState 的机器测试模式：纯迁移测试与状态模拟（model-based）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-670：XState 的机器测试模式：纯迁移测试与状态模拟（model-based）

**答**：
- 状态机是「纯迁移图」，这带来两种测试形态：1) **迁移单元测试**——只测 `(state, event) => nextState` 的正确性，不渲染组件：`createActor` 后按事件序列 send，断言 `snapshot.value` 与 context；2) **模型测试（model-based testing）**——用 model 库（@xstate/test + model-viewer）从状态机自动生成测试路径（每条边至少走一次），路径应用到真实 UI 断言 DOM。
- 纯迁移测试的价值：状态逻辑 bug（守卫漏分支、非法迁移）在渲染前就被抓住；用例组织成「路径表」——`[['idle', 'LOAD', 'loading'], ['loading', 'FAIL', 'error'], ...]` 每行一个 it。
- actor 的可注入性：测试用假 actor 替换 invoke 的 src（`machine.provide({ actors: { fetchUser: fakePromiseActor } } )`）——异步行为确定性化；延迟迁移用 `actor.send` + fake timers 或 v5 的 `clock` 注入。
- context 断言：迁移后不仅要断 state.value，还要断 `snapshot.context`（assign 是否正确）与 `snapshot.status`（done/error）。
- 追问钩子：迁移表可以直接生成「状态图文档」供 review——测试与文档同源，改机器时表过期即测试红。

```javascript
import { createActor, fromPromise } from 'xstate'
import { expect, test } from 'vitest'
import { checkoutMachine } from './machine'

// 1) 迁移路径表测试
const paths = [
  ['idle', [{ type: 'LOAD' }], 'loading'],
  ['loading', [{ type: 'FAIL' }], 'error'],
  ['error', [{ type: 'RETRY' }], 'loading'],
  ['loading', [{ type: 'DONE', data: 1 }], 'ready'],
]
for (const [initial, events, expected] of paths) {
  test(`${initial} → ${events[0].type} → ${expected}`, () => {
    const actor = createActor(checkoutMachine.provide({
      actors: { loadData: fromPromise(async () => ({ ok: true })) },   // 假 actor 注入
    }))
    actor.start()
    // 状态直设：先迁移到 initial（测试用）
    events.forEach((e) => actor.send(e))
    expect(actor.getSnapshot().value).toBe(expected)
  })
}

// 2) context 断言
test('SUBMIT 通过守卫后 retries 递增', () => {
  const actor = createActor(checkoutMachine, { input: { retries: 0 } })
  actor.start()
  actor.send({ type: 'INPUT', value: 'hi' })
  actor.send({ type: 'SUBMIT' })
  const s = actor.getSnapshot()
  expect(s.context.retries).toBe(0)   // submit 成功不增
})

// 3) model-based（概念）
// const testModel = createTestModel(checkoutMachine)
// testModel.getShortestPaths().forEach((path) => test(path.description, async () => {...}))
```
