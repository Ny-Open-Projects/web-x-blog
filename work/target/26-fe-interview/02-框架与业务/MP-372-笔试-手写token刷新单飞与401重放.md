---
title: [MP-372] 笔试：手写 token 刷新单飞与 401 重放
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## MP-372：笔试：手写 token 刷新

**答**：实现 `authFetch`：① token 失效（401）→ 静默重新登录（wx.login + code2session）→ 重放原请求（仅幂等方法）；② 刷新单飞（并发 401 只触发一次登录，其余等待复用）；③ 写操作 401 不自动重放（返回明确错误，防重复下单）；④ 重放次数上限（1 次——防死循环）；⑤ checkSession 主动校验（启动时静默续期）。写出实现。

```javascript
let refreshing = null;   // 单飞 promise

async function refreshToken() {
  refreshing ??= (async () => {
    const { code } = await wx.login();
    const { token } = await api.code2session(code);
    wx.setStorageSync('token', token);
    return token;
  })().finally(() => { refreshing = null; });
  return refreshing;
}

async function authFetch(opts, replayed = false) {
  const token = wx.getStorageSync('token');
  const res = await new Promise((resolve) =>
    wx.request({ ...opts, header: { ...opts.header, Authorization: `Bearer ${token}` }, success: resolve, fail: (e) => resolve({ statusCode: 0, errMsg: e.errMsg }) }));
  if (res.statusCode === 401) {
    if (replayed || !isIdempotent(opts.method)) {
      throw new AuthError('登录过期, 请重试');        // 写操作不自动重放
    }
    await refreshToken();                             // 单飞: 并发 401 共享一次登录
    return authFetch(opts, true);                     // 重放一次
  }
  return res;
}
function isIdempotent(m = 'GET') { return ['GET', 'HEAD'].includes(m.toUpperCase()); }
// 启动静默续期
App({
  onLaunch() { wx.checkSession({ fail: () => refreshToken() }); },
});
```

**评分点**：
- 单飞 promise（并发 401 共享一次登录）
- 幂等方法才重放（写操作防重复下单——核心安全点）
- 重放上限 1 次防死循环
- checkSession 启动静默续期（无感登录）
