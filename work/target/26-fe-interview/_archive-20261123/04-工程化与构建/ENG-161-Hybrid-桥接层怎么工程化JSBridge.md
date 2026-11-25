---
title: [ENG-161] Hybrid 桥接层怎么工程化？JSBridge 协议 版本兼容与调试？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-161：Hybrid 桥接层怎么工程化？JSBridge 协议 版本兼容与调试？
**答**：
- 双向通道：H5 到 Native 用注入对象 postMessage 或 scheme 拦截；Native 到 H5 用 evaluateJavascript 触发回调。
- 协议设计：请求 {bridge action callbackId params} 响应 {callbackId code data}，callbackId 注册表管理回调与超时。
- 版本兼容：Native 声明能力位（getAvailableActions），H5 未支持能力走 H5 兜底实现；协议版本写进 UA 供识别。
- 调试手段：真机注入 vConsole + 桥接日志开关（全部调用落 console），是排查桥接问题的标配。

```typescript
// src/bridge/index.ts —— JSBridge 核心实现
type Callback = (res: { code: number; data?: unknown; msg?: string }) => void
const callbacks = new Map<string, Callback>()
let seq = 0

export function call(action: string, params: object, cb: Callback) {
  const callbackId = `cb_${Date.now()}_${seq++}`
  callbacks.set(callbackId, cb)
  const payload = JSON.stringify({ bridge: 'corp', action, callbackId, params })
  const native = (window as any).CorpBridge
  if (native?.postMessage) native.postMessage(payload)
  else location.href = `corpscheme://bridge?payload=${encodeURIComponent(payload)}`
  setTimeout(() => {          // 超时保护 防 Native 无响应悬挂
    if (callbacks.has(callbackId)) { callbacks.delete(callbackId); cb({ code: -1, msg: 'timeout' }) }
  }, 10000)
}

export function dispatchFromNative(res: { callbackId: string; code: number; data?: unknown; msg?: string }) {
  callbacks.get(res.callbackId)?.(res)
  callbacks.delete(res.callbackId)
}
;(window as any).CorpBridge_dispatch = dispatchFromNative   // Native 回调入口
```
