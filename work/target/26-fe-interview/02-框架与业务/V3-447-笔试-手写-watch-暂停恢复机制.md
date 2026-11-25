---
title: [V3-447] 笔试：手写 watch 的 pause/resume 与暂停期事件合并
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-447：笔试：手写 watch 的 pause/resume 与暂停期事件合并
**答**：实现 `watchWithPause(source, cb)`：返回可写 ref 控制 paused；暂停期间不执行 cb 但记录「最后一次变更值」；resume 时若暂停期内有变更则触发一次（合并而非逐个回放）；返回 stop 仍然有效。

```javascript
function watchWithPause(source, cb, options = {}) {
  const paused = ref(false)
  let pendingChange = false
  const stop = watch(source, () => {
    if (paused.value) { pendingChange = true; return } // 暂停：只记标记
    cb(source.value)
  }, options)
  // resume 时检查合并
  const stopPauseSync = watchEffect(() => {
    if (!paused.value && pendingChange) {
      pendingChange = false
      cb(source.value) // 只触发最后一次
    }
  })
  return {
    paused,          // 读写 paused.value 控制
    stop() { stop(); stopPauseSync() }
  }
}
// 用法：
// const { paused, stop } = watchWithPause(() => form.value, save)
// paused.value = true  // 暂停自动保存（编辑态）
// paused.value = false // 恢复并触发一次合并保存
```
**评分点**：
- 暂停期只置标记不执行（丢弃中间态，语义正确）。
- resume 合并触发一次而非回放全部。
- 两个 watcher 的 stop 都要停（防泄漏）。
- 能说明与 3.5 pause/resume 语义一致。
