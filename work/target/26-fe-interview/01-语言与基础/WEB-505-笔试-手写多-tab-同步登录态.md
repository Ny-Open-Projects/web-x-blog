---
title: [WEB-505] 笔试：手写多 tab 同步登录态
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 鉴权]
type: 笔试题
---

## WEB-505：笔试：手写多 tab 同步登录态

**题目**：实现 `authSync()`：任一 tab 登录/登出后，其他 tab 实时感知；优先 BroadcastChannel，降级 storage 事件；提供 `login(token)`/`logout()` 与 `onChange(cb)`。

**答**：
```javascript
function authSync() {
  const KEY = 'auth_token';
  const listeners = new Set();
  let bc = null;
  try {
    bc = new BroadcastChannel('auth');
    bc.onmessage = (e) => notify(e.data.type); // 同源 tab 即时通知
  } catch (e) { /* 旧浏览器降级 */ }

  window.addEventListener('storage', (e) => {
    if (e.key === KEY) notify(e.newValue ? 'LOGIN' : 'LOGOUT'); // 跨 tab 兜底
  });

  function notify(type) {
    listeners.forEach(cb => cb({ type, token: localStorage.getItem(KEY) }));
  }
  return {
    login(token) { localStorage.setItem(KEY, token); bc?.postMessage({ type: 'LOGIN' }); notify('LOGIN'); },
    logout() { localStorage.removeItem(KEY); bc?.postMessage({ type: 'LOGOUT' }); notify('LOGOUT'); },
    onChange(cb) { listeners.add(cb); return () => listeners.delete(cb); },
  };
}
```

**评分点**：
- BroadcastChannel 主通道 + storage 事件降级通道，双通道兼容
- 本 tab 也要 notify（storage 事件只触发其他 tab）——补发本地通知是易漏点
- login/logout 同时写本地与广播，且两通道触发时 UI 不能收到双份（去重或幂等处理）
- onChange 返回退订函数
