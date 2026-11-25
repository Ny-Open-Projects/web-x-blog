---
title: [ZSM-586] iframe / 微前端间的状态同步通道与安全边界
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-586：iframe / 微前端间的状态同步通道与安全边界

**答**：
- 通道选型：同源 iframe 可以直接 `iframe.contentWindow` 访问（快但耦合）；跨域 iframe 必须走 `postMessage`（异步、可校验）；微前端（qiankun 等）通常用共享 store（主应用下发）+ 自定义事件。
- postMessage 协议要点：1) 消息带 `type + namespace`（避免多 iframe 串台）；2) **发送时用 `targetOrigin` 明确限制**（'*' 是安全漏洞——消息可能被恶意 iframe 收到）；3) 接收方校验 `event.origin` 白名单 + 消息结构，不可信消息直接丢弃。
- 状态语义：iframe 间同步的是「摘要事件」而非共享可变状态——父页面改了用户信息 → 广播 `user-changed` 摘要；iframe 收到后更新自己的 store。直接跨边界引用/写对方 store 对象会造成双向耦合与内存泄漏（iframe 卸载时引用悬挂）。
- 生命周期：iframe 的 load/unload 与主页面独立——主页面要在 iframe `beforeunload` 时清理订阅；iframe 内部监听器在 `pagehide` 主动移除，否则 message 监听泄漏。
- 追问钩子：微前端状态隔离（ZSM-251~260 已覆盖隔离）与同步是两个问题——隔离靠沙箱（Proxy/window 隔离），同步靠显式协议，两者正交。

```javascript
// 父页面：状态广播器
class IFrameSyncHub {
  constructor(namespace) {
    this.ns = namespace
    this.frames = new Map()     // iframe -> { origin, alive }
  }
  register(iframe, expectedOrigin) {
    this.frames.set(iframe, { origin: expectedOrigin, alive: true })
    iframe.addEventListener('load', () => { this.frames.get(iframe).alive = true })
  }
  broadcast(type, payload) {
    for (const [iframe, info] of this.frames) {
      if (!info.alive) continue
      // targetOrigin 明确指定：不用 '*'
      iframe.contentWindow?.postMessage({ ns: this.ns, type, payload }, info.origin)
    }
  }
}

// iframe 内：受控接收
const ALLOWED = new Set(['https://parent.example.com'])
window.addEventListener('message', (e) => {
  if (!ALLOWED.has(e.origin)) return                    // origin 白名单
  if (e.data?.ns !== 'app') return                      // namespace 匹配
  if (!isTrustedPayload(e.data)) return                 // 结构校验
  switch (e.data.type) {
    case 'user-changed':
      useUser.getState().hydrate(e.data.payload)        // 更新自己的 store
      break
  }
})

// iframe → 父：只回摘要事件
useUser.subscribe((s) => {
  parent.postMessage({ ns: 'app', type: 'web-view-ready', payload: { version: APP_V } },
    'https://parent.example.com')
})

window.addEventListener('pagehide', () => {             // 卸载清理
  window.removeEventListener('message', arguments.callee)
})
```
