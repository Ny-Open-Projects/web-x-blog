---
title: [MP-288] 笔试：手写小程序埋点 SDK（自动 PV + 点击 + 批量上报）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-288：笔试：手写小程序埋点 SDK
**题**：实现 track.js：track(event, props)（批量：10 条或 5s flush）；自动 PV：重写 Page/Component 构造器，onShow 上报 PV 带 route 与来源（referrer）；页面隐藏/小程序切后台 flush；失败重试队列（最多 3 次）。

```javascript
const buffer = []
let timer = null
function track(event, props = {}) {
  buffer.push({ event, props, ts: Date.now(), route: getCurrentPages().at(-1)?.route })
  if (buffer.length >= 10) flush()
  else timer ||= setTimeout(flush, 5000)
}
function flush() {
  clearTimeout(timer); timer = null
  const list = buffer.splice(0)
  if (!list.length) return
  wx.request({ url: '/api/track', method: 'POST', data: list,
    fail: () => { // 重试 ≤3 次
      list.retry = (list.retry || 0) + 1
      if (list.retry <= 3) buffer.push(...list)
    }
  })
}
// 自动 PV：包装 Page
const OriginPage = Page
function Page(config) {
  const originShow = config.onShow
  config.onShow = function (...args) {
    track('pv', { route: this.route, referrer: this.__route__ })
    originShow?.apply(this, args)
  }
  return OriginPage(config)
}
wx.onAppHide?.(flush) // 切后台兜底（生命周期内 sendBeacon 不可用，尽快 flush）
```
**评分点**：
- Page 包装自动 PV（来源字段）。
- 批量双阈值 + hide flush。
- 重试上限。
- 小程序无 sendBeacon——切后台时机的兜底思路（说出局限加分）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-cc7bbb62-104c-46fb-89f6-5e5154e67c9b-cwd'; fi
exit "$__zcode_status"
