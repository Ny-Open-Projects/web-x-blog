---
title: [ZSM-745] Web Push 与后台同步：页面关闭时的状态更新通道
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-745：Web Push 与后台同步：页面关闭时的状态更新通道

**答**：
- 页面全关后仍要「收到消息/补发数据」的两条 SW 通道：**Web Push**（服务端经 Push Service 投递，SW 的 push 事件唤醒处理——即时消息、审批提醒）与 **Background Sync**（`sync` 事件，浏览器在恢复联网时触发——离线队列补发，ZSM-598）。两者互补：Push 是「别人推给我」，Sync 是「我欠服务端的」。
- Push 的状态处理链：SW 收到 push → 解析 payload → ① 有活跃页面：MessageChannel 转发（页面更新 store）；② 无页面：显示 Notification（tag 去重）+ 把数据写入 IndexedDB（下次页面打开时追平）。**SW 与页面状态的双写**是关键——SW 无法直接改页面内存 store，只能写持久层让页面读取。
- 订阅状态管理：`pushManager.subscribe` 的授权链（权限询问需用户手势）+ 订阅过期/服务端清理——「订阅有效」本身是状态（订阅 token 上报服务端），失效检测靠服务端推送 410 Gone（重新订阅）。
- Sync 的限制：`periodicSync`（周期性后台同步）需要 PWA 安装 + 用户参与度门槛；一次性 `sync` 是「联网时触发一次」——队列补发的正确姿势，不能当定时器用。
- 追问钩子：Push payload 加密（VAPID + aes128gcm）与体积限制（~4KB）——推大 payload 是反模式，Push 只带「信号」（有新消息），内容由页面/SW 拉取。

```javascript
// SW：push 事件处理（双写：页面转发 + 持久层）
self.addEventListener('push', (event) => {
  const payload = event.data?.json() ?? {}
  event.waitUntil((async () => {
    const clients = await self.clients.matchAll({ type: 'window' })
    if (clients.length) {
      // 有页面：转发，页面自己更新 store
      clients.forEach((c) => c.postMessage({ type: 'push', payload }))
    } else {
      // 无页面：写 IndexedDB（下次打开追平）+ 系统通知
      const db = await openDB()
      await put(db, 'inbox', { id: payload.id, ...payload, receivedAt: Date.now() })
      await self.registration.showNotification(payload.title, {
        body: payload.body,
        tag: payload.dedupeKey,        // 同 tag 折叠防重复弹
        data: { url: payload.url },    // 点击跳转
      })
    }
  })())
})

// 页面：收 SW 转发 + 打开时追平 inbox
navigator.serviceWorker.addEventListener('message', (e) => {
  if (e.data.type === 'push') notificationHub.receive(e.data.payload)
})
// 页面启动：读 SW 写的 inbox 追平
const missed = await getAll(db, 'inbox')
missed.forEach((n) => notificationHub.receive(n))
await clear(db, 'inbox')

// Push 订阅状态管理
async function ensurePushSubscription() {
  const perm = await Notification.requestPermission()   // 需用户手势
  if (perm !== 'granted') return { subscribed: false, reason: perm }
  const reg = await navigator.serviceWorker.ready
  const sub = await reg.pushManager.getSubscription()
    ?? await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: VAPID_PUBLIC })
  await api.reportSubscription(sub)                     // 上报服务端
  return { subscribed: true, endpoint: sub.endpoint }
}
// 服务端推送返回 410 Gone → 重新订阅流程
```
