---
title: [WEB-231] CSP 内容安全策略怎么配置？怎么兜底 XSS？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-231：CSP 内容安全策略怎么配置？怎么兜底 XSS？

**答**：
- CSP 是浏览器执行的脚本/资源来源白名单，即使 XSS 注入成功，脚本不在白名单内也不执行——纵深防御最后一道。
- 核心指令：default-src 兜底、script-src 脚本、style-src 样式、img-src、connect-src（fetch/XHR 目标）、frame-ancestors（防点击劫持，替代 X-Frame-Options）。
- 消除内联脚本：`script-src` 不加 'unsafe-inline' 时，`<script>alert(1)</script>` 直接被浏览器拒执行；需要内联用 nonce（每响应随机）或 SRI hash。
- 灰度方法：先用 `Content-Security-Policy-Report-Only` + report-uri 收集违规上报，不拦只报，确认无误后切正式头。

```http
# 生产级 CSP 示例
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'nonce-N6hMzF' https://cdn.example.com;
  style-src 'self' 'unsafe-inline';   # 样式内联风险低，常放行
  img-src 'self' data: https://img.example.com;
  connect-src 'self' https://api.example.com;
  frame-ancestors 'none';
  report-uri /csp-report;

# 灰度期只上报不拦截
Content-Security-Policy-Report-Only: default-src 'self'; report-uri /csp-report;
```
