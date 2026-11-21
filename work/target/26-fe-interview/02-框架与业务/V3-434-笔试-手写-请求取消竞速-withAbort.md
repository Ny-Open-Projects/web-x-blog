---
title: [V3-434] 笔试：手写 AbortController 请求取消（组件卸载 + 覆盖旧请求）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-434：笔试：手写 AbortController 请求取消（组件卸载 + 覆盖旧请求）
**题**：实现 `useFetchAbort(loaderFn)`：run() 每次调用前 abort 上一请求（切换参数场景）；组件卸载时 abort 进行中请求；返回 { data, run, cancel }；abort 触发的错误（AbortError）不进 error 状态。

```javascript
function useFetchAbort(loaderFn) {
  const data = ref(null), error = ref(null)
  let controller = null
  async function run(...args) {
    controller?.abort()               // 取消上一个
    controller = new AbortController()
    const cur = controller
    try {
      const res = await loaderFn(...args, { signal: cur.signal })
      data.value = res
      error.value = null
    } catch (e) {
      if (e.name === 'AbortError') return  // 取消不算错误
      if (cur === controller) error.value = e // 只有最新请求的错误才记录
    }
  }
  function cancel() { controller?.abort() }
  onBeforeUnmount(cancel)
  return { data, error, run, cancel }
}
// loaderFn: (q, { signal }) => fetch(`/api?q=${q}`, { signal }).then(r => r.json())
```
**评分点**：
- 新请求覆盖式 abort 旧请求。
- AbortError 识别与忽略（不污染 error）。
- 卸载 abort。
- 错误只由最新请求写入（cur === controller 判断）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-5e1c2417-95a1-4af6-a6ee-719a7b075114-cwd'; fi
exit "$__zcode_status"
