---
title: [FRP-291] 笔试：手写迷你 Vapor createFor（key 复用 DOM 块）
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-291：笔试：手写迷你 Vapor createFor
**题**：实现 `createFor(container, renderItem, getKey, source)`：source 为响应式数组（watch 驱动）；key→block 映射复用 DOM；新增 renderItem、删除移除并调用 cleanup；顺序变化按新序 insertBefore；无 diff 算法但保证正确与最少重排。

```javascript
function createFor(container, renderItem, getKey, source) {
  const blocks = new Map() // key -> { el, cleanups: [] }
  function sync(list) {
    const seen = new Set()
    list.forEach((item, i) => {
      const key = getKey(item)
      seen.add(key)
      let block = blocks.get(key)
      if (!block) {
        const cleanups = []
        const el = renderItem(item, (fn) => cleanups.push(fn))
        blocks.set(key, block = { el, cleanups })
        container.appendChild(el)
      } else {
        container.appendChild(block.el) // 挪到正确顺序（简单全量 append 重排）
      }
    })
    blocks.forEach((block, key) => {
      if (!seen.has(key)) {
        block.cleanups.forEach(fn => fn()) // 项级清理（订阅/事件）
        container.removeChild(block.el)
        blocks.delete(key)
      }
    })
  }
  watch(source, sync, { immediate: true })
  return { dispose: () => blocks.forEach(b => b.cleanups.forEach(f => f())) }
}
```
**评分点**：
- key→block Map 复用（核心：无 vnode 的 reconcile）。
- 项级 cleanups（Vapor 块作用域语义）。
- 删除时先清理再移除。
- 能指出「全量 append 重排」可优化为 LIS/标记位重排（说出即可）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-3fc17b4c-20de-4a01-9250-05192eb8a843-cwd'; fi
exit "$__zcode_status"
