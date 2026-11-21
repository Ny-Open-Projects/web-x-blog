---
title: [WEB-157] 浏览器 0day 时代，前端能做什么自保？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-157：浏览器 0day 时代，前端能做什么自保？
**答**：
- 前端拦不住浏览器自身漏洞，但能收窄利用面：管控第三方脚本（供应链是最大入口），核心页面用 SRI 锁定脚本内容，防 CDN 被劫持后投毒。
- 跨域隔离（COOP/COEP）配合站点隔离，让漏洞利用难以跨站读内存；收敏页面独立域名部署。
- 权限最小化：Permissions-Policy 关闭用不到的摄像头/USB/支付等能力；CSP 去掉 unsafe-inline。
- 运营侧：重大漏洞披露期推动用户升级的横幅与功能降级策略；关键数据服务端再校验，永远假设前端不可信。

```html
<!-- 供应链自保：SRI 确保第三方脚本未被篡改，hash 不匹配直接拒绝执行 -->
<script src="https://cdn.vendor.com/sdk.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>
<!-- 页面同时配合响应头收紧：Permissions-Policy、COOP/COEP、无 unsafe-inline 的 CSP -->
```
