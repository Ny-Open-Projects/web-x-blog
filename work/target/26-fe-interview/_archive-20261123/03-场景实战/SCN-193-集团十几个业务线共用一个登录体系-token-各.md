---
title: [SCN-193] 集团十几个业务线共用一个登录体系，token 各存各的、刷新各刷各的，如何统一治理？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-193：集团十几个业务线共用一个登录体系，token 各存各的、刷新各刷各的，如何统一治理？
**答**：
- 收口到"统一鉴权域 + 短时票据换发"模式：登录、token 存储、刷新全部收敛在 sso.example.com，各业务站不持有长效 token，只持有短时访问票据（15 分钟）+ 一次性 refresh ticket。
- 子站认证流程重定向到统一登录域完成（或静默 iframe 续期），回跳带 code 换票据；刷新动作只在鉴权域发生，业务站零刷新逻辑。
- 登出全端生效：鉴权域维护会话，登出撤销会话并广播（各子站监听 storage 事件 + 服务端会话失效）。
- 迁移兼容：老站 token 过渡期双读（老 token 继续有效但新会话只发新票据），设下线时间表。

```javascript
// 共享登录态治理：鉴权域换发 + 静默续期 + 全端登出
// sso.example.com（鉴权域，唯一持有 refresh token 的地方）
export async function exchangeTicket(code) {           // 子站回跳后到鉴权域换票据
  return api.post('/sso/token', { code });             // { accessToken(15min), expiresAt }
}

// 子站 SDK：只管使用票据，刷新逻辑收敛在鉴权域
export function createAuth() {
  let token = null;
  async function ensureToken() {
    if (token && token.expiresAt > Date.now() + 60_000) return token.accessToken;
    // 静默续期：隐藏 iframe 向鉴权域要新票据（会话仍有效则免登录）
    const code = await silentRenew();                  // iframe postMessage 返回一次性 code
    token = await exchangeTicket(code);
    return token.accessToken;
  }
  return {
    fetch: async (input, init = {}) => {
      const accessToken = await ensureToken();
      return fetch(input, { ...init, headers: { ...init.headers, Authorization: `Bearer ${accessToken}` } });
    },
    logout: async () => {                              // 全端登出：撤销鉴权域会话并广播
      await api.post('/sso/logout');
      localStorage.setItem('sso-logout', String(Date.now())); // 同域子站 storage 事件兜底
      location.href = 'https://sso.example.com/logout';
    },
  };
}

// 多 tab 会话一致性：其他 tab 登出时本 tab 跟随失效
window.addEventListener('storage', e => {
  if (e.key === 'sso-logout') { token = null; redirectToLogin(); }
});

// 静默续期实现：鉴权域会话有效时 iframe 返回一次性 code
function silentRenew() {
  return new Promise((resolve, reject) => {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://sso.example.com/silent-renew?client=shop';
    iframe.style.display = 'none';
    const onMsg = e => {
      if (e.origin !== 'https://sso.example.com') return;
      e.data.code ? resolve(e.data.code) : reject(new Error('SESSION_EXPIRED')); // 会话失效需重登录
      iframe.remove(); window.removeEventListener('message', onMsg);
    };
    window.addEventListener('message', onMsg);
    document.body.appendChild(iframe);
    setTimeout(() => { iframe.remove(); reject(new Error('RENEW_TIMEOUT')); }, 8000);
  });
}

```

## 三十二、新技术融合场景
