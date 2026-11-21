---
title: [V3-392] 笔试：手写 nextTick 批量调度队列
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-392：笔试：手写 nextTick 批量调度队列
**题**：实现 `queueJob(job)` 与 `nextTick(fn)`：同一 job 在一个 flush 周期内去重；flush 按加入顺序执行；nextTick 回调在本轮 flush 后执行；支持嵌套（job 内再入队则进入下一轮）。

```javascript
const queue = new Set()
let flushing = false
let currentFlushPromise = null
function nextTick(fn) {
  return (currentFlushPromise ||= Promise.resolve()).then(fn)
}
function queueJob(job) {
  if (flushing) { nextTick(() => queueJob(job)); return } // 嵌套进下一轮
  queue.add(job)
  if (!currentFlushPromise) {
    currentFlushPromise = Promise.resolve().then(flushJobs)
  }
}
function flushJobs() {
  flushing = true
  try {
    for (const job of [...queue]) { queue.delete(job); job() }
  } finally {
    flushing = false
    currentFlushPromise = null
  }
}
// 用法：多次 queueJob(render) 只执行一次；nextTick 里能读到更新后的 DOM
```
**评分点**：
- Set 去重；flushing 标记防重入。
- 嵌套入队时排到下一轮（微任务）。
- flush 完成后清空 currentFlushPromise。
- 能解释这与 Vue 的「pre/post 队列、按 id 排序」差异。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-10f4c758-f1e4-4a70-8e36-415bb628bcf1-cwd'; fi
exit "$__zcode_status"
