---
title: [R19-330] 笔试：手写 useLatestRequest（AbortController + 过期丢弃）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-330：笔试：手写 useLatestRequest
**题**：实现 `useLatestRequest(fetcher)`：run(args) 取消上一个请求并发起新的；卸载取消；结果只接受最新请求；返回 { data, error, run, cancel }。

```javascript
function useLatestRequest(fetcher) {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)
  const ctrlRef = useRef(null)
  const run = (...args) => {
    ctrlRef.current?.abort()
    const ctrl = ctrlRef.current = new AbortController()
    fetcher(...args, { signal: ctrl.signal })
      .then(res => { if (!ctrl.signal.aborted) { setData(res); setError(null) } })
      .catch(e => { if (e.name !== 'AbortError') setError(e) })
  }
  const cancel = () => ctrlRef.current?.abort()
  useEffect(() => cancel, []) // 卸载取消
  return { data, error, run, cancel }
}
```
**评分点**：
- abort 旧请求 + aborted 检查双重防护。
- AbortError 不进 error 状态。
- 卸载取消（useEffect 返回 cancel）。
- ctrlRef 用 ref 而非 state（避免触发渲染）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-52592bd4-306a-4ce9-8690-e99613aa1e66-cwd'; fi
exit "$__zcode_status"
