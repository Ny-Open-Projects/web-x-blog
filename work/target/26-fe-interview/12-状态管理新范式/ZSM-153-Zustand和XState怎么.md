---
title: [ZSM-153] 复杂异步流程的状态机语义怎么进 Zustand？什么时候该上 XState 而不是手写 flags？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-153：复杂异步流程的状态机语义怎么进 Zustand？什么时候该上 XState 而不是手写 flags？
**答**：
- 危险信号：store 里出现 `loading + uploading + saving + error` 多个布尔 flags，组合出 2^n 个隐式状态，其中一半是非法态（如 loading && saving）。
- 状态机方案（XState）：显式枚举合法状态与事件迁移（idle → uploading → saving → done | failed），非法迁移直接被框架拒绝；Zustand 负责数据本体，XState actor 持有流程状态，二者组合（store 存 actor 发来的结果）。
- 集成方式：actor.subscribe(state => set({ phase: state.value, result: state.context }))，把机器状态镜像进 Zustand 或直接用 useMachine 局部持有。
- 判断标准：状态数少（≤4）且线性用 flags 够了；有并发子流程、可取消、可重入的用状态机——面试官想听的是「你对复杂度阈值有感知」。

```javascript
import { setup, assign, fromPromise } from 'xstate'

export const uploadMachine = setup({
  actors: { doUpload: fromPromise(({ input }) => api.upload(input)) },
}).createMachine({
  id: 'upload',
  initial: 'idle',
  context: { progress: 0, result: null },
  states: {
    idle:     { on: { START: 'uploading' } },
    uploading:{ invoke: { src: 'doUpload', input: ({ event }) => event.file,
      onDone: { target: 'saving', action: assign({ result: ({ event }) => event.output }) },
      onError: 'failed' } },
    saving:   { on: { DONE: 'done', RETRY: 'uploading' } },
    failed:   { on: { START: 'uploading' } },
    done:     { type: 'final' },
  },
})

// Zustand 侧只存结果数据
const useUploadStore = create((set) => ({
  files: {}, setFile: (id, f) => set(s => ({ files: { ...s.files, [id]: f } })),
}))
```
