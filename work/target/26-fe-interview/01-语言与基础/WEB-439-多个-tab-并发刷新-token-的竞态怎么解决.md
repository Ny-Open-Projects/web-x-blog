---
title: [WEB-439] 多个 tab 并发刷新 token 的竞态怎么解决
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 鉴权]
type: 面试题
---

## WEB-439：多个 tab 并发刷新 token 的竞态怎么解决

**答**：
- 现象：三个 tab 同时发现 token 过期，同时发起 refresh，旧 refresh token 用一次就作废时，后两个请求 401，全被登出
- 方案一：Web Locks API——`navigator.locks` 保证同一时刻只有一个 tab 在刷新，其他 tab 等锁
- 方案二：storage 事件协调——约定 localStorage 里的 token 版本号，抢写成功者刷新，其余 tab 监听变更后读新 token
- 方案三（服务端）：refresh token 支持宽限期内多次使用（旋转宽限），或直接允许多会话
- 兜底：刷新失败若是「token 已被使用」而非过期，静默重拉登录态而不是粗暴踢出

```javascript
async function refreshWithLock() {
  return navigator.locks.request('auth-refresh', async () => {
    const cur = localStorage.getItem('access_token');
    const res = await fetch('/api/refresh', { method: 'POST', body: currentRefreshToken });
    const { access_token } = await res.json();
    localStorage.setItem('access_token', access_token); // 其他 tab 靠 storage 事件感知
    return access_token;
  });
}
```
