---
title: [R19-328] 笔试：手写 MessageChannel 时间切片执行器
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-328：笔试：手写 MessageChannel 时间切片执行器
**题**：实现 `timeSlice(tasks, deadline = 5)`：任务数组逐个执行，累计超过 deadline 停止，用 MessageChannel 宏任务续跑剩余，全部完成调用 onDone；支持 cancel。

```javascript
function timeSlice(tasks, { deadline = 5, onDone, onTick } = {}) {
  const channel = new MessageChannel()
  let i = 0, cancelled = false
  channel.port1.onmessage = () => {
    if (cancelled) return
    const start = performance.now()
    while (i < tasks.length && performance.now() - start < deadline) {
      tasks[i++]() // 同步任务
    }
    onTick?.(i, tasks.length)
    if (i < tasks.length) channel.port2.postMessage(null) // 让出后续跑
    else { channel.port1.close(); onDone?.() }
  }
  channel.port2.postMessage(null) // 启动
  return { cancel: () => { cancelled = true; channel.port1.close() } }
}
```
**评分点**：
- MessageChannel 代替 setTimeout（无最低延迟、独立于绘制循环）。
- deadline 判断在 while 条件内（先执行再判断，避免死循环）。
- cancel 关闭端口防泄漏。
- 能对比 rAF/setTimeout/微任务三种让出方式差异。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-cb22169e-442b-4969-a9f5-46644cb63fe0-cwd'; fi
exit "$__zcode_status"
