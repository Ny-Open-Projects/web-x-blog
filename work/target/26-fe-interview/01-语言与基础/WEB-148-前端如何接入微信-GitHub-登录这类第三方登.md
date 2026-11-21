---
title: [WEB-148] 前端如何接入"微信/GitHub 登录"这类第三方登录？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-148：前端如何接入"微信/GitHub 登录"这类第三方登录？
**答**：
- 标准路径就是 OAuth 授权码流程的客户端部分：跳转授权页 → 接回调 code → 后端换 token 拿用户信息 → 映射成自家账号（绑定或静默注册）。
- 两条体验路线：弹窗式（window.open + postMessage）与整页跳转式；弹窗体验好但要处理被拦截与跨窗口通信，整页跳转兼容性最好。
- 内嵌环境差异：微信内打开用网页授权（snsapi_userinfo），微信外用扫码登录，前端要按 UA 分支。
- 安全要点：state 串防伪造回调；回调页不要把 code 转发给第三方；openid/unionid 的映射在后端完成。

```javascript
// 弹窗式第三方登录：open 拉起授权页，回调页 postMessage 通知父窗口
document.getElementById('github-login').addEventListener('click', () => {
  const state = crypto.randomUUID();
  sessionStorage.setItem('oauth_state', state);
  const popup = window.open(
    `https://github.com/login/oauth/authorize?client_id=xxx&redirect_uri=${encodeURIComponent(location.origin + '/oauth/callback')}&state=${state}`,
    'oauth', 'width=600,height=700'
  );
  window.addEventListener('message', function onMsg(e) {
    if (e.origin !== location.origin || e.data.type !== 'oauth:done') return;
    window.removeEventListener('message', onMsg);
    popup?.close();
    if (e.data.ok) location.reload();   // 后端已建立会话
  });
  // 弹窗被拦截时的兜底：整页跳转
  if (!popup) location.assign('/oauth/start?provider=github');
});
```
