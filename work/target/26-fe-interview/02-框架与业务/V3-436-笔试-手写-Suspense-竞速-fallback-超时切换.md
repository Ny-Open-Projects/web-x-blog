---
title: [V3-436] 笔试：手写「300ms 内不出数据先显示骨架」的竞速逻辑
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-436：笔试：手写「300ms 内不出数据先显示骨架」的竞速逻辑
**题**：实现 `delayFallback(promise, ms = 300)`：数据在 ms 内返回 → 直接渲染（不闪骨架）；超时 → 标记进入 fallback 态（显示骨架），数据到达后切换；提供 onFallback/onDone 回调；防内存泄漏（clearTimeout）。

```javascript
function delayFallback(promise, ms = 300, { onFallback, onDone } = {}) {
  let timer = null
  let fallbackShown = false
  return new Promise((resolve, reject) => {
    timer = setTimeout(() => {
      fallbackShown = true
      onFallback?.()   // 进入骨架态
    }, ms)
    promise.then(
      (data) => {
        clearTimeout(timer)
        onDone?.(fallbackShown) // 告知是否经过骨架
        resolve(data)
      },
      (err) => { clearTimeout(timer); reject(err) }
    )
  })
}
// 组件层：
// const showSkeleton = ref(false)
// const data = await delayFallback(load(), 300, { onFallback: () => showSkeleton.value = true, onDone: () => showSkeleton.value = false })
```
**评分点**：
- 竞速语义正确：超时只触发 UI 标记，不取消请求。
- onDone 传「是否经过骨架」便于埋点。
- 成功/失败都 clearTimeout。
- 300ms 是公认阈值（能说出研究依据加分）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-eea6858a-47b4-4f7d-b518-a1cefd660770-cwd'; fi
exit "$__zcode_status"
