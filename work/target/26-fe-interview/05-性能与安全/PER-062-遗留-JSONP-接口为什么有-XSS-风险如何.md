---
title: [PER-062] 遗留 JSONP 接口为什么有 XSS 风险？如何安全下线或加固？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-062：遗留 JSONP 接口为什么有 XSS 风险？如何安全下线或加固？

**答**：
- JSONP 的本质是**用 `<script>` 加载远端代码**：回调名拼进 JS 执行，攻击者若能控制回调名（`?callback=<script>...`）或劫持返回内容，就是反射/存储 XSS。
- 次生风险：JSONP 不受同源策略约束，任何页面都能带着用户 Cookie 调用接口，等于把**已登录态数据**暴露给任意第三方（登录态泄露）。
- 加固存量：回调名只允许 `[A-Za-z0-9_.]` 白名单、响应加 `Content-Type: application/javascript` 与 CSP、Cookie 改 SameSite 限制跨站携带。
- 正确方向是**下线**：接口套 CORS + 凭据方案替代，前端埋点统计 JSONP 调用量，归零后关闭路由。

```javascript
// 前端：存量 JSONP 调用的加固封装 + 用量统计为下线做准备
function jsonp(url, callbackName) {
  // 回调名白名单：只允许字母数字下划线点，杜绝注入
  if (!/^[A-Za-z_$][\w$.]{0,30}$/.test(callbackName)) {
    return Promise.reject(new Error('invalid callback name'));
  }
  return new Promise((resolve, reject) => {
    window[callbackName] = (data) => resolve(data);
    const s = document.createElement('script');
    s.src = `${url}?callback=${encodeURIComponent(callbackName)}`;
    s.onerror = () => reject(new Error('jsonp failed'));
    s.onload = () => { delete window[callbackName]; s.remove(); };
    document.head.appendChild(s);
    // 上报 JSONP 调用点，用于推动业务方迁移到 CORS 接口
    navigator.sendBeacon('/api/legacy-tracking', JSON.stringify({ url, path: location.pathname }));
  });
}

jsonp('https://api.example.com/v1/user', 'legacyUserCb');
```
