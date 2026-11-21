---
title: [SCN-019] 用户在 A 标签页退出登录，B 标签页仍是登录态，如何同步多标签页状态？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-019：用户在 A 标签页退出登录，B 标签页仍是登录态，如何同步多标签页状态？
**答**：
- 同源标签页通信两条路：BroadcastChannel（现代浏览器首选，语义清晰）和 storage 事件（localStorage 的写操作会广播给其他页面）。
- 登录/退出时广播一条带时间戳的 auth-change 消息，其他页面收到后清理内存态并跳登录页或刷新用户信息。
- 注意 storage 事件只在"其他页面"触发，本页面不会收到；老浏览器用 storage 方案兜底。

```javascript
// 封装跨标签页广播：优先 BroadcastChannel，降级 storage 事件
const channel = 'BroadcastChannel' in window
  ? new BroadcastChannel('auth')
  : null;

function broadcastAuthChange(action) {
  const msg = { action, time: Date.now() };
  if (channel) channel.postMessage(msg);
  else localStorage.setItem('auth-change', JSON.stringify(msg)); // 触发其他页 storage 事件
}

function onAuthChange(handler) {
  if (channel) {
    channel.onmessage = (e) => handler(e.data);
  } else {
    window.addEventListener('storage', (e) => {
      if (e.key === 'auth-change') handler(JSON.parse(e.newValue));
    });
  }
}

onAuthChange(({ action }) => {
  if (action === 'logout') {
    userStore.clearUser();      // 清理内存态，防止返回键看到脏数据
    router.push('/login');
  }
});
// 退出登录的动作里调用：broadcastAuthChange('logout')
```
