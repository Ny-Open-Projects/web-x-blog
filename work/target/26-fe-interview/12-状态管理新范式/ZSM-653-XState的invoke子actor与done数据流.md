---
title: [ZSM-653] XState 的 invoke 生命周期：子 actor 的 spawn、stop 与数据回流
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-653：XState 的 invoke 生命周期：子 actor 的 spawn、stop 与数据回流

**答**：
- `invoke` 把子 actor 的生命周期绑定到状态：进入状态时创建/启动子 actor（`src` 解析为 actor 定义：fromPromise/fromCallback/嵌套 machine/observable），**离开状态时自动 stop**（连取消逻辑都免了）——异步任务与状态的绑定是 XState 相对手写 useEffect 管理异步的核心优势。
- 数据回流三通道：1) `onDone`/`onError` 事件（子 actor 完成时自动发给父机，output 带数据）；2) `fromCallback(({ sendBack, receive }) => ...)` 双向通道——子 actor 可以 sendBack 任意事件给父机（长连接监听场景），父机 `on: {...}` 直接消费；3) 父机 `sendTo(childRef, event)` 向子 actor 发指令。
- spawn（动态子 actor）：`spawnChild` action 或 context 里 `enqueueActions` 动态创建，引用存 context——「N 个并发任务」建模（批量上传每个文件一个子 actor），完成时 sendTo 父级汇总。
- cancel 语义：fromPromise 的 stop 会调用其 abort（v5 传 signal）；fromCallback 的 stop 触发 cleanup 返回值——资源释放完整闭环。
- 追问钩子：invoke 的 retry 不是内置的——用 `error` 事件迁移回同一状态实现重试（重新 invoke），配合 after 延迟做退避。

```javascript
import { setup, createActor, fromCallback, fromPromise } from 'xstate'

// 批量上传：每文件一个子 actor
const uploadMachine = setup({
  actors: {
    uploadOne: fromPromise(({ input, signal }) =>
      fetch('/api/upload', { method: 'POST', body: input.file, signal }).then((r) => r.json())),
  },
}).createMachine({
  context: ({ input }) => ({ files: input.files, results: [] }),
  initial: 'uploading',
  states: {
    uploading: {
      entry: ({ context, enqueueActions }) => {
        context.files.forEach((file) => {
          enqueueActions(({ spawn }) => {   // 动态 spawn：并发任务
            spawn('uploadOne', { input: { file }, onDone: { actions: 'collect' } })
          })
        })
      },
      actions: {
        collect: ({ context, event }) => ({ context: { results: [...context.results, event.output] } }),
      },
      on: { ALL_DONE: 'finished' },   // results.length === files.length 时由逻辑发
      exit: 'cancelAll',              // 离开状态：所有子 actor 自动 stop（abort 上传）
    },
    finished: {},
  },
})

// fromCallback 双向通道：长连接监听
const wsActor = fromCallback(({ sendBack, receive }) => {
  const ws = new WebSocket('wss://example.com')
  ws.onmessage = (e) => sendBack({ type: 'WS_MSG', payload: JSON.parse(e.data) })
  receive((evt) => { if (evt.type === 'SUBSCRIBE') ws.send(JSON.stringify(evt)) })
  return () => ws.close()   // 父机离开状态自动调：资源释放
})
```
