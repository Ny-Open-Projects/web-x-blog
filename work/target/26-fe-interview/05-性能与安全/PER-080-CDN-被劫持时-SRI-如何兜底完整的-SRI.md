---
title: [PER-080] CDN 被劫持时 SRI 如何兜底？完整的 SRI 方案包含哪些环节？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-080：CDN 被劫持时 SRI 如何兜底？完整的 SRI 方案包含哪些环节？

**答**：
- SRI（Subresource Integrity）让浏览器校验**资源内容哈希**：被劫持返回的脚本与 `integrity` 不符即拒绝执行，是 CDN/运营商劫持的最后防线。
- 完整环节：构建时计算文件哈希写入 HTML、`crossorigin="anonymous"` 必须配套（否则 CORS 失败回退加载）、静态资源带 `Cache-Control` 与正确 CORS 头。
- 限制认知：SRI 只保护**静态资源**，不覆盖同源动态接口；资源经常更新的页面每次发版都要重新生成哈希（构建工具自动化）。
- 配套监控：`error` 事件区分 SRI 失败类型上报，劫持发生时能告警而不是静默白屏。

```html
<!-- SRI 完整方案：第三方 CDN 资源带内容哈希 -->
<!-- crossorigin=anonymous 必须：SRI 校验走 CORS 模式 -->
<script
  src="https://cdn.example.com/vue@3.4.21/dist/vue.global.prod.js"
  integrity="sha384-o7/8XSPe0PW3fXdX8ZFLKGZxLnJmOa1vUq8IQ0OVCKMPeVBVwB4XAVBTwCmRB4jW"
  crossorigin="anonymous"></script>
<link
  rel="stylesheet"
  href="https://cdn.example.com/antd@5.16.0/reset.css"
  integrity="sha384-kQ9XyYABCDWQjKH7s9yZQE/0FRhR7u+uTGxOLmS0PX1PQpTcV1lJ0K3zV3Gk3Eim"
  crossorigin="anonymous" />
```

```bash
# 构建时自动生成 integrity 属性（Node 脚本，配合 html 处理插件使用）
openssl dgst -sha384 -binary vue.global.prod.js | openssl base64 -A
# 输出即 integrity 的值，前面拼上 sha384- 写入 <script integrity>
```

```javascript
// 监控 SRI 失败：区分加载错误与完整性错误并告警
window.addEventListener('error', (e) => {
  const el = e.target;
  if (!(el instanceof HTMLScriptElement || el instanceof HTMLLinkElement)) return;
  navigator.sendBeacon('/api/asset-fail', JSON.stringify({
    src: el.src || el.href,
    // 含 integrity 属性的加载失败大概率是哈希不匹配（内容被篡改）
    sriProtected: Boolean(el.integrity),
    page: location.pathname,
  }));
}, true); // 资源错误不冒泡，必须用捕获阶段
```
