---
title: [ZSM-663] 笔试：手写 Redux 的 listenerMiddleware（副作用订阅器）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-663：手写 Redux 的 listenerMiddleware（副作用订阅器）
**答**：实现 `createListenerMiddleware()`：1) `addListener(actionMatcher, { effect, condition })`：匹配 action 时执行 effect（可 dispatch、可访问 getState）；2) **防抖 effect**（`debounce: ms`）——同 matcher 连续触发只跑最后一次（超时清除）；3) `condition(fn, timeout)`：effect 内可等待「状态谓词为真」（轮询 getState，超时 reject）——RTK 的 take 语义；4) middleware 装配 `(store) => (next) => (action)` 标准形态；5) 附用例：防抖保存 + condition 等待加载数据。

```javascript
function createListenerMiddleware() {
  const listeners = []
  let storeRef = null

  function addListener(matcher, { effect, debounce = 0, onCleanup } = {}) {
    const entry = { matcher, effect, debounce, timer: null, onCleanup }
    listeners.push(entry)
    return () => {
      clearTimeout(entry.timer)
      listeners.splice(listeners.indexOf(entry), 1)
    }
  }

  // condition：等待状态谓词（take 语义）
  function condition(predicate, { timeout = 5000, interval = 50 } = {}) {
    return new Promise((resolve, reject) => {
      const start = Date.now()
      const timer = setInterval(() => {
        const state = storeRef.getState()
        if (predicate(state)) { clearInterval(timer); resolve(state) }
        else if (Date.now() - start > timeout) { clearInterval(timer); reject(new Error('condition timeout')) }
      }, interval)
    })
  }

  function middleware(store) {
    storeRef = store
    return (next) => (action) => {
      const result = next(action)              // 先入 reducer 再跑 effect（action 已生效）
      for (const l of listeners) {
        if (!l.matcher(action)) continue
        const run = () => {
          Promise.resolve(l.effect(action, store)).catch((e) => console.error('[listener]', e))
        }
        if (l.debounce > 0) {
          clearTimeout(l.timer)                // 防抖：只跑最后一次
          l.timer = setTimeout(run, l.debounce)
        } else run()
      }
      return result
    }
  }

  return { middleware, addListener, condition }
}

// 用例：文档编辑器自动保存 + 数据等待
const store = createStore(reducer)   // dispatch 时 effect 会被调用
const lm = createListenerMiddleware()

// 1) 防抖自动保存：连续 EDIT 只保存最后一次
lm.addListener(
  (a) => a.type === 'doc/EDIT',
  {
    debounce: 800,
    effect: (action, store) => {
      const doc = store.getState().doc
      return api.save(doc.id, doc.content)
    },
  },
)

// 2) condition：提交前等待资料加载完成
async function submit() {
  store.dispatch({ type: 'submit/start' })
  await lm.condition((s) => s.profile.status === 'loaded', { timeout: 3000 })
  store.dispatch({ type: 'submit/do', payload: collect() })
}

// 装配
const enhancer = applyMiddleware(lm.middleware)
```
**评分点**：
- matcher 匹配 + effect 先入 reducer 后执行（状态已生效）
- 防抖计时器清除（同 matcher 连续触发合并）
- condition 的轮询谓词等待 + 超时（take 语义）
- 中间件标准三参装配（可替换原生 dispatch）
