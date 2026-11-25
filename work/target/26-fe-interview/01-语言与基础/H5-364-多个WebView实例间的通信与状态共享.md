---
title: [H5-364] 多个 WebView 实例间的通信与状态共享
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, Hybrid]
type: 面试题
---

## H5-364：多个 WebView 实例间的通信与状态共享

**答**：
- iOS WKWebView 多实例独立进程/内存，localStorage 不实时同步（各实例独立写入，读写冲突）——跨实例通信必须走 Native 中转
- Native 中转协议：bridge.registerChannel(name) + bridge.emit(name, payload)，Native 维护实例注册表广播消息；注意实例销毁时注销
- 共享状态的正确姿势：会话级状态放 Native（登录态/主题），页面打开时 bridge 拉取而不是信任本地存储；关键状态变更由 Native 推送广播
- 降级方案（纯浏览器多 tab）：BroadcastChannel/storage 事件（H5-614 已讲）——在 App 内不生效，容器检测分支
- 典型业务：主页面登录后，其他已打开的 tab/WebView 需要同步登录态刷新——没有广播机制就会各页面状态漂移

```javascript
// App 内: Native 中转广播
function emit(channel, payload) {
  if (window.__HYBRID__) return bridge.call('broadcast', { channel, payload });
  if ('BroadcastChannel' in self) return new BroadcastChannel(channel).postMessage(payload);
  localStorage.setItem(`bc:${channel}`, JSON.stringify({ ...payload, _t: Date.now() }));
}
function on(channel, handler) {
  if (window.__HYBRID__) return bridge.on(`broadcast:${channel}`, handler);
  addEventListener('storage', (e) => {
    if (e.key === `bc:${channel}`) handler(JSON.parse(e.newValue));
  });
}
```
