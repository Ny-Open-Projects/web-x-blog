---
title: [MP-299] 笔试：手写小程序错误监控 SDK
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-299：笔试：手写错误监控 SDK
**答**：实现 monitor.init(app)：捕获 App.onError / onUnhandledRejection / wx.onMemoryWarning；错误去重指纹（消息前 100 字符，10 分钟窗口）；自动附带上下文（route/页面栈深度/系统信息/内存水位）；关键流程 try-catch 包装 helper；上报失败本地暂存重试。

```javascript
const monitor = {
  seen: new Map(), pending: []
}
function fingerprint(msg) { return String(msg).slice(0, 100) }
function report(err, extra = {}) {
  const fp = fingerprint(err)
  const now = Date.now()
  if (now - (monitor.seen.get(fp) || 0) < 600000) return // 去重窗口
  monitor.seen.set(fp, now)
  monitor.pending.push({
    msg: String(err).slice(0, 2000), stack: err?.stack?.slice(0, 2000),
    route: getCurrentPages().at(-1)?.route, depth: getCurrentPages().length,
    memLevel: monitor.memLevel, sys: monitor.sysInfo, ...extra, ts: now
  })
  monitor.flush()
}
function flush() {
  const list = monitor.pending.splice(0)
  if (!list.length) return
  wx.request({ url: '/api/monitor', method: 'POST', data: list, fail: () => monitor.pending.unshift(...list) })
}
function init(app) {
  monitor.sysInfo = wx.getSystemInfoSync()
  wx.onMemoryWarning?.(level => { monitor.memLevel = level; report('memory-warning', { level }) })
  const originError = app.onError
  app.onError = (msg) => { report(msg); originError?.call(app, msg) }
  wx.onUnhandledRejection?.(({ reason }) => report(reason))
}
function tryGuard(name, fn) {
  return (...args) => { try { return fn(...args) } catch (e) { report(e, { guard: name }); throw e } }
}
```
**评分点**：
- 三通道捕获（error/unhandledrejection/memory）。
- 指纹去重 + 时间窗口。
- 上下文丰富（路由/栈深/内存）。
- 上报失败暂存重试；tryGuard 不吞错（report 后 rethrow）。
