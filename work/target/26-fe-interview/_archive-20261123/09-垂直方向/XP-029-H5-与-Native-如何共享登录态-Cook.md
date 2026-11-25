---
title: [XP-029] H5 与 Native 如何共享登录态（Cookie/Token 注入）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-029：H5 与 Native 如何共享登录态（Cookie/Token 注入）？
**答**：
- 两种主流方案：**Cookie 共享**（Native 把 session 写入 WebView CookieManager，H5 请求自动携带，服务端无感知）与 **Token 注入**（桥下发 token，H5 自行放 header，适合纯接口型 H5）。
- Cookie 注入时机必须在**首次请求发出前**（WKWebView 需在 `WKHTTPCookieStore.setCookie` 完成后 loadUrl，Android 在 loadUrl 前写 CookieManager 并 flush）。
- 一致性难题：Native 登录/登出后要**同步刷新**所有 WebView Cookie；多容器实例（WKWebView 各自 store）需遍历同步。
- 安全红线：token 不落 localStorage（XSS 可读）；敏感域 Cookie 用 HttpOnly+Secure；JSBridge 下发凭据必须白名单域。
- SSO 场景：共享 Cookie 域（父域）+ 桥通知刷新，双保险。

```javascript
// Native Shell 侧：登录态同步到 WebView（两端关键时序）
// Android：
// CookieManager.getInstance().setAcceptCookie(true);
// CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);
// for (const c of buildAuthCookies(token)) {
//   CookieManager.getInstance().setCookie('https://m.example.com',
//     `session=${c.value}; Domain=.example.com; Path=/; Secure; HttpOnly`);
// }
// CookieManager.getInstance().flush();           // 关键：立刻落盘，否则首个请求丢 Cookie

// iOS（WKWebView 必须等 setCookie 完成再 loadUrl）：
async function syncCookieToWK(webView, cookies) {
  const store = webView.configuration.websiteDataStore.httpCookieStore;
  await Promise.all(cookies.map((c) =>
    new Promise((res) => store.setCookie(
      new NSHTTPCookie({ name: c.name, value: c.value, domain: '.example.com', path: '/', secure: true }),
      res,
    )),
  ));
}
// H5 侧（Token 方案）：桥获取 token 后由统一请求库注入 header，绝不写 localStorage
// const token = await bridge.call('getAccessToken');
// http.interceptors.request.use((cfg) => ({ ...cfg, headers: { Authorization: `Bearer ${token}` } }));
```
