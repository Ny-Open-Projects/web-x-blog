---
title: [ZSM-594] 跨端登录态与 Token 的同步策略：哪端是权威
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-594：跨端登录态与 Token 的同步策略：哪端是权威

**答**：
- 归属判断：**token 是服务端事实**——客户端只做持有与携带，不做权威判断。多端同步登录态的语义是「服务端会话状态在各端的镜像」：A 端登出/被踢，服务端会话失效，B 端下次请求 401 后自然感知。
- 同步策略分两层：1) **被动感知**（必须）：任何 API 401 → 清理本地凭证 → 广播其他 tab（BroadcastChannel `logout` 事件）→ 跳登录页。这是兜底，保证最终一致。2) **主动推送**（体验优化）：服务端在会话变化时通过 WS/长轮询推 `session-changed`，各端立即响应，不用等下一次 401。
- 安全边界：token 不进 BroadcastChannel/localStorage 明文广播（XSS 面）；多 tab 共享 token 用「SharedWorker 持有 + 主 tab 转发」或至少 HttpOnly cookie（web 端最优，tab 天然共享且 JS 不可读）。RN/小程序端用安全存储（Keychain/KeyStore），通过安全桥接给 WebView。
- 刷新竞态：多 tab 同时 refresh token 会互相失效（旧 refresh token 被用后作废）——解法是 refresh 也走 leader 选举或服务端 refresh token 允许一次宽限（同 family 重放）。
- 追问钩子：登出后「状态清理清单」要显式化（store 重置、缓存清空、订阅退订、WS 断开），遗漏任何一项都是数据泄漏风险。

```javascript
// 401 感知 + 广播登出
const ch = new BroadcastChannel('auth')

async function fetchWithAuth(input, init) {
  const res = await fetch(input, init)
  if (res.status === 401) {
    await logout('expired')      // 服务端会话已失效
    throw new Error('unauthorized')
  }
  return res
}

async function logout(reason) {
  // 清理清单（显式列出）
  useUser.getState().reset()                 // store 重置
  queryClient.clear()                        // 服务端缓存清空
  ws.close()                                 // 长连接断开
  await api.revokeToken().catch(() => {})    // 尽力撤销
  ch.postMessage({ type: 'logout', reason }) // 通知其他 tab
  location.href = '/login'
}

ch.onmessage = (e) => {
  if (e.data.type === 'logout') {
    useUser.getState().reset()
    queryClient.clear()
    toast.info('已在其他设备退出登录')
    location.href = '/login'
  }
}

// refresh 竞态：tab 间单飞
let refreshing = null
async function refreshToken() {
  if (refreshing) return refreshing          // 其他 tab/调用已在刷：复用
  refreshing = api.refresh().finally(() => { refreshing = null })
  return refreshing
}
```
