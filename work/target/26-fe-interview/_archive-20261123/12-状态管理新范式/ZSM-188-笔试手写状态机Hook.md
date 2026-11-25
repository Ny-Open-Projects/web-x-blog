---
title: [ZSM-188] 笔试：手写 useAsyncAction 状态机 Hook（idle/pending/success/error 四态 + 防重入）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-188：手写 useAsyncAction 状态机 Hook（idle/pending/success/error 四态 + 防重入）
**需求**：实现 `useAsyncAction(fn)`，返回 `{ run, status, error, reset }`：1) status ∈ idle|pending|success|error，迁移合法：idle→pending→success/error，error→pending 允许重试；2) pending 期间重复 run 被拒绝（返回同一个 Promise）；3) 卸载后 run 完成不 setState；4) 手动 reset 回 idle 并清 error；5) fn 参数透传，成功保存 result 供 UI 使用。核心考点：非法迁移拒绝 + 竞态（连续两次 run 只保留最后结果）。

```javascript
export function useAsyncAction(fn) {
  const [st, setSt] = useState({ status: 'idle', error: null, result: null })
  const alive = useRef(true)
  const inFlight = useRef(null)
  const seq = useRef(0)                    // 竞态序号：只接受最后一次
  const fnRef = useRef(fn); fnRef.current = fn
  useEffect(() => () => { alive.current = false }, [])

  const run = useCallback((...args) => {
    if (st.status === 'pending') return inFlight.current   // 防重入：复用
    const mySeq = ++seq.current
    setSt({ status: 'pending', error: null, result: null })
    const p = Promise.resolve().then(() => fnRef.current(...args))
      .then(result => {
        if (!alive.current || mySeq !== seq.current) return  // 卸载/被更新覆盖
        setSt({ status: 'success', error: null, result })
        return result
      })
      .catch(error => {
        if (!alive.current || mySeq !== seq.current) return
        setSt({ status: 'error', error, result: null })
        throw error
      })
    inFlight.current = p
    p.finally(() => { if (inFlight.current === p) inFlight.current = null })
    return p
  }, [st.status])

  const reset = useCallback(() =>
    setSt({ status: 'idle', error: null, result: null }), [])

  return { ...st, run, reset }
}

// 评分点：
// 1. 四态机迁移图明确，pending 拒绝重入并返回在途 Promise
// 2. 卸载守卫 alive 防止 setState on unmounted
// 3. seq 竞态序号：连续 run 只采纳最后一次的结果
// 4. reset 显式回 idle（允许从任意合法态迁移）
// 5. fn 用 ref 透传最新闭包，回调不因依赖变化重建
```
