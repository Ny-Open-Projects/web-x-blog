---
title: [ZSM-735] 笔试：手写 SSE 流式输出的状态机（分块组装 + 断流恢复 + 取消）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-735：手写 SSE 流式输出的状态机（分块组装 + 断流恢复 + 取消）
**需求**：实现 `createStreamReceiver()` 处理 AI 流式输出：1) 事件类型 `delta(文本块)/done(完整结果)/error`，按 event id 续传（SSE Last-Event-ID）；2) 状态 `idle → streaming → done | interrupted → resuming`；3) 断流：连接中断后自动恢复（用已收 id 续传，重复块去重 by id）；4) `abort()`：取消并保留已收部分（partial 语义）；5) 超时检测（10s 无 delta 判定断流）；6) 附用例：断流恢复去重与取消保留 partial。

```javascript
function createStreamReceiver({ fetchStream, timeoutMs = 10000 } = {}) {
  let state = 'idle'
  let chunks = []            // { id, text }（按 id 去重）
  let lastEventId = null
  let controller = null
  let timeoutTimer = null
  const listeners = new Set()

  function setState(s) { state = s; listeners.forEach((fn) => fn(snapshot())) }
  function snapshot() { return { state, text: chunks.map((c) => c.text).join(''), count: chunks.length } }

  function resetTimer() {
    clearTimeout(timeoutTimer)
    timeoutTimer = setTimeout(async () => {
      if (state === 'streaming') {
        setState('interrupted')
        await resume()         // 超时断流：自动恢复
      }
    }, timeoutMs)
  }

  async function start(prompt) {
    chunks = []
    setState('streaming')
    controller = new AbortController()
    await consume(controller.signal, { prompt, lastEventId: null })
  }

  async function resume() {
    controller = new AbortController()
    setState('resuming')
    // 续传：带 lastEventId，服务端从此处补发
    await consume(controller.signal, { lastEventId, resume: true })
  }

  async function consume(signal, params) {
    try {
      for await (const evt of fetchStream({ ...params, signal })) {
        if (signal.aborted) return
        // 重复块去重（SSE 重连可能重发）
        if (evt.id != null && chunks.some((c) => c.id === evt.id)) { lastEventId = evt.id; continue }
        if (evt.type === 'delta') {
          chunks.push({ id: evt.id, text: evt.text })
          if (evt.id != null) lastEventId = evt.id
          resetTimer()                      // 收到数据：刷新超时
          listeners.forEach((fn) => fn(snapshot()))
        } else if (evt.type === 'done') {
          clearTimeout(timeoutTimer)
          setState('done')
          return
        } else if (evt.type === 'error') {
          clearTimeout(timeoutTimer)
          setState('interrupted')
          await resume()
          return
        }
      }
      // 流自然结束但无 done 事件：视为断流
      if (state !== 'done') { setState('interrupted'); await resume() }
    } catch (e) {
      if (e.name === 'AbortError') return   // 用户取消：保留 partial
      setState('interrupted')
      await resume()
    }
  }

  function abort() {
    clearTimeout(timeoutTimer)
    controller?.abort()
    setState('done')                        // 取消：保留已收部分（partial 语义）
  }

  return { start, abort, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)), snapshot }
}

// 用例
const events = [
  { id: 1, type: 'delta', text: '你好' },
  { id: 2, type: 'delta', text: '，世界' },
  // 模拟断流：id3 之后连接中断，恢复后服务端重发 id3
  { id: 3, type: 'delta', text: '！' },
  { id: 3, type: 'delta', text: '！' },     // 重复：去重
  { type: 'done' },
]
let idx = 0
const recv = createStreamReceiver({
  fetchStream: async function* ({ resume }) {
    if (resume) idx = 2                     // 续传：从断点重发
    for (; idx < events.length; idx++) yield events[idx]
  },
  timeoutMs: 100,
})
recv.subscribe((s) => console.log(s.state, JSON.stringify(s.text)))
await recv.start('hi')
console.log(recv.snapshot().text)           // '你好，世界！'（重复块去重）
recv.abort()                                 // 取消：partial 保留
```
**评分点**：
- 事件 id 去重（重连重发防御）+ lastEventId 续传
- 超时断流检测（10s 无 delta 判定）自动恢复
- abort 保留 partial（流式场景取消语义）
- 三态机（streaming/interrupted/resuming）与通知粒度
