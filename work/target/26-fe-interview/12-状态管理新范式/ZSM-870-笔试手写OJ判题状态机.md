---
title: [ZSM-870] 笔试：手写 OJ 判题状态机（两阶段流式 + 幂等去重 + 取消）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-870：手写 OJ 判题状态机（两阶段流式 + 幂等去重 + 取消）
**答**：869 落地——实现 `createJudgeService()`：1) `submit(code)`：幂等去重（同代码 hash 短窗口返回上次结果）+ 提交进状态机；2) 两阶段：SSE 逐用例流式（`onCase` 回调）+ 终局 verdict；3) `cancel()`：running 中取消（abort + 服务端终止 + 状态回 idle）；4) 超时判定（TLE）：单用例执行超时由服务端判定，客户端只消费；5) 附用例：去重命中与取消回滚。

```javascript
function createJudgeService({ dedupeWindowMs = 10000 } = {}) {
  const state = { phase: 'idle', submissionId: null, cases: [], verdict: null }
  const hashCache = new Map()   // codeHash -> { verdict, at }
  let controller = null
  const listeners = new Set()

  function hash(code) {
    // 简化 hash（真实用 SHA）
    let h = 0
    for (const c of code) h = (h * 31 + c.charCodeAt(0)) | 0
    return String(h)
  }

  function emit(e) { listeners.forEach((fn) => fn(e)) }
  function setPhase(p) { state.phase = p; emit({ type: 'phase', phase: p }) }

  async function submit(code) {
    const h = hash(code)
    // 幂等去重：相同代码短窗口内返回上次结果
    const cached = hashCache.get(h)
    if (cached && Date.now() - cached.at < dedupeWindowMs) {
      emit({ type: 'dedupe-hit', verdict: cached.verdict })
      return { ok: true, deduped: true, verdict: cached.verdict }
    }

    setPhase('running')
    controller = new AbortController()
    try {
      // SSE 流式判题（735 流式接收语义）
      for await (const evt of api.judgeStream(code, { signal: controller.signal })) {
        if (evt.type === 'case') {
          state.cases.push(evt.result)                 // 逐用例流式
          emit({ type: 'case', index: state.cases.length - 1, result: evt.result })
        } else if (evt.type === 'verdict') {
          state.verdict = evt.verdict                  // 终局
          setPhase(evt.verdict === 'AC' ? 'accepted' : 'failed')
          hashCache.set(h, { verdict: evt.verdict, at: Date.now() })
          emit({ type: 'verdict', verdict: evt.verdict })
          return { ok: true, verdict: evt.verdict, cases: state.cases }
        }
      }
      // 流结束无 verdict：异常
      setPhase('failed')
      throw new Error('stream ended without verdict')
    } catch (e) {
      if (e.name === 'AbortError') {
        setPhase('idle')                               // 取消：状态回 idle
        emit({ type: 'cancelled' })
        return { ok: false, cancelled: true }
      }
      setPhase('failed')
      state.verdict = 'SE'
      emit({ type: 'error', message: e.message })
      return { ok: false, verdict: 'SE' }
    }
  }

  function cancel() {
    if (state.phase === 'running' || state.phase === 'judging') {
      controller?.abort()
    }
  }

  return {
    submit, cancel,
    getState: () => ({ ...state, cases: [...state.cases] }),
    subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)),
  }
}

// 用例
const svc = createJudgeService()
let abortCalled = false
globalThis.api = {
  judgeStream: async function* (code, { signal }) {
    signal.addEventListener('abort', () => { abortCalled = true })
    yield { type: 'case', result: { passed: true, name: 'case1' } }
    yield { type: 'case', result: { passed: true, name: 'case2' } }
    yield { type: 'verdict', verdict: 'AC' }
  },
}

const code = 'function solve() {...}'
const r1 = await svc.submit(code)
console.log(r1.verdict, svc.getState().cases.length)   // 'AC' 2

// 幂等去重：相同代码短窗口
const r2 = await svc.submit(code)
console.log(r2.deduped, r2.verdict)                    // true 'AC'

// 取消：新代码 + running 中取消
const slowCode = 'function slow() {...}'
const p = svc.submit(slowCode)
setTimeout(() => svc.cancel(), 10)
const r3 = await p
console.log(r3.cancelled, svc.getState().phase)        // true 'idle'
```
**评分点**：
- 幂等去重（hash 短窗口返回上次 verdict——防双击重复判题）
- 两阶段消费（逐用例 case 流式 + verdict 终局）
- 取消语义（abort + 状态回 idle + 服务端终止标记）
- hashCache 的 TTL 设计（dedupeWindowMs）
