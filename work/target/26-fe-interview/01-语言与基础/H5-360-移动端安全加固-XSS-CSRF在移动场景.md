---
title: [H5-360] 移动端安全加固：XSS/CSRF 在移动场景的变形
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## H5-360：移动端安全加固：XSS/CSRF 在移动场景的变形

**答**：
- XSS 在移动的变形：URL scheme 注入（`javascript:` 协议被桥拦截器执行）、WebView cookie 共享放大危害（App 全局登录态）、老内核无 CSP 支持——防御要输出编码 + 桥白名单双管
- CSRF 在移动的特点：App 内 WebView cookie 自动携带 + 部分接口无 token；防御靠自定义 header + SameSite + 桥签名，Native 侧对敏感接口二次校验
- 深链安全：scheme/deeplink 参数直接进页面逻辑（如 redirect 参数）→ 开放重定向/任意跳转漏洞，深链参数必须白名单校验
- WebView 配置加固：关闭 file 域访问（allowFileAccess=false）、关闭 JS 与本地文件互访（allowFileAccessFromFileURLs）、仅 HTTPS、禁用不受信第三方 cookie
- 混合内容与证书：强制 HTTPS 并处理证书校验失败（Native 侧 onReceivedSslError 不可默认放行——这是高频安全审计点）

```javascript
// 深链参数白名单
function safeRedirect(target) {
  const allowed = ['^https://m\\.example\\.com/'];
  if (!allowed.some(re => re.test(target)) || target.startsWith('javascript:')) return '/home';
  return target;
}
location.href = safeRedirect(params.get('redirect') || '/home');
// CSP 兜底(新内核生效):
// <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'nonce-xxx'">
```
