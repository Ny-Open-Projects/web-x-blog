---
title: [V3-401] 笔试：手写轮询 composable（页面不可见暂停 + 失败退避）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-401：笔试：手写轮询 composable（页面不可见暂停 + 失败退避）
**答**：实现 `usePolling(loader, { interval = 5000 })`：可见时按 interval 轮询；隐藏暂停、恢复继续；连续失败按 2^n 退避，成功恢复原间隔；卸载自动停止；返回 start/stop。

```javascript
function usePolling(loader, { interval = 5000, immediate = true } = {}) {
  let timer = null, stopped = false, failCount = 0
  async function tick() {
    try { await loader(); failCount = 0 } catch { failCount++ }
    schedule()
  }
  function schedule() {
    if (stopped) return
    if (document.hidden) return // 等待 visibilitychange 恢复
    const wait = failCount ? Math.min(interval * 2 ** failCount, 60000) : interval
    timer = setTimeout(tick, wait)
  }
  function start() { stopped = false; if (immediate) tick() }
  function stop() { stopped = true; clearTimeout(timer) }
  document.addEventListener('visibilitychange', () => {
    if (!document.hidden && !stopped) { clearTimeout(timer); tick() }
  })
  onScopeDispose(stop)
  start()
  return { start, stop }
}
```
**评分点**：
- visibilitychange 双向处理（隐藏暂停/恢复立即触发）。
- 失败退避有上限（60s），成功重置。
- 卸载 stop 防泄漏。
- 恢复时清旧 timer 防双跑。
