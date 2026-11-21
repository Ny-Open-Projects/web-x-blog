---
title: [V3-433] 笔试：手写埋点 SDK 的 Vue 插件（指令 + 路由自动埋点 + 批量上报）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-433：笔试：手写埋点 SDK 的 Vue 插件（指令 + 路由自动埋点 + 批量上报）
**题**：实现 `createTracker({ endpoint })`：v-track 指令（点击上报 + 额外参数）；router.afterEach 自动 PV 上报；事件批量上报（攒 10 条或 5s flush）；页面卸载用 sendBeacon 兜底。

```javascript
export function createTracker({ endpoint, app, router }) {
  const buffer = []
  let timer = null
  function send(list = buffer.splice(0)) {
    if (!list.length) return
    if (navigator.sendBeacon && !document.visibilityState) {
      navigator.sendBeacon(endpoint, JSON.stringify(list))
    } else {
      fetch(endpoint, { method: 'POST', body: JSON.stringify(list), keepalive: true }).catch(() => {})
    }
  }
  function track(event, props = {}) {
    buffer.push({ event, props, ts: Date.now(), url: location.href })
    if (buffer.length >= 10) send()
    else { clearTimeout(timer); timer = setTimeout(() => send(), 5000) }
  }
  window.addEventListener('pagehide', () => send()) // 卸载兜底
  router.afterEach((to) => track('pv', { path: to.path }))
  const vTrack = {
    mounted(el, binding) {
      el.addEventListener('click', () => track(binding.arg || 'click', binding.value))
    }
  }
  app.directive('track', vTrack)
  app.provide('track', track)
  return { track }
}
```
**评分点**：
- 批量策略双阈值（条数 + 时间）。
- pagehide/sendBeacon/keepalive 兜底（数据不丢是核心）。
- 指令绑定 click + 参数透传。
- afterEach 自动 PV。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-b30cb7fb-ffc9-41c1-a6fa-583b72cfc742-cwd'; fi
exit "$__zcode_status"
