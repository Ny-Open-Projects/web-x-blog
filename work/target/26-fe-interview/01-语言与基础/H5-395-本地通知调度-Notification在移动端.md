---
title: [H5-395] 本地通知调度：Notification 在移动端的正确用法
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 设备能力]
type: 面试题
---

## H5-395：本地通知调度：Notification 在移动端的正确用法

**答**：
- 页面存活期通知：new Notification(title, { body, tag, icon })，tag 去重防堆叠；前台轮询/长连接收到消息时提醒
- 授权率策略：价值时刻申请（关注主播/设置提醒后），从未授权状态直接弹的转化 <20%；denied 后不可再弹系统授权，只能引导去设置
- 离开页面后通知：必须 Web Push（SW showNotification），纯本地 setTimeout 不可靠（页面冻结）——「倒计时提醒」类需求要 Push 服务端定时下发
- iOS 边界：16.4 前无 Web Push，16.4+ 需「添加到主屏幕」的 PWA；App 内 WebView 不显示系统通知——统一走桥让 Native 发本地通知
- 数据闭环：通知送达/点击率统计，点击深链回页面并携带来源参数

```javascript
async function remindAt(ts, payload) {
  // 用户可感知提醒: 优先服务端 Push(可靠), 前台轮询兜底
  const reg = await navigator.serviceWorker.getRegistration();
  if (reg && Notification.permission === 'granted') {
    await api.post('/push/schedule', { at: ts, payload });  // 服务端定时 Web Push
    return;
  }
  if (window.__HYBRID__) return bridge.call('notify', { at: ts, ...payload }); // App 内桥
  // 页面存活期兜底: setTimeout(不可靠, 仅辅助)
  const delay = ts - Date.now();
  if (delay > 0 && delay < 60_000) setTimeout(() => new Notification(payload.title), delay);
}
```
