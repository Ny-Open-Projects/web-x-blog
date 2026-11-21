---
title: [WEB-103] CSP 的核心指令有哪些？分别限制什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-103：CSP 的核心指令有哪些？分别限制什么？
**答**：
- `default-src` 是兜底策略，未单独声明的 fetch 类指令全部回退到它；`script-src/style-src/img-src/connect-src/font-src` 等按资源类型细分。
- 导航与嵌入类独立于 default-src：`frame-ancestors`（谁能嵌入我，替代 X-Frame-Options）、`frame-src`（我能嵌谁）、`form-action`（表单提交目标）、`navigate-to`。
- `report-uri`/`report-to` 把违规上报到服务端，配合 `Content-Security-Policy-Report-Only` 先观察不拦截，是灰度上线标准流程。
- 注意：frame-ancestors 只能走响应头，`<meta>` 里写无效；unsafe-inline/unsafe-eval 是豁免口子，能不开就不开。

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.example.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://img.example.com; connect-src 'self' https://api.example.com wss://push.example.com; font-src 'self' https://fonts.gstatic.com; frame-ancestors 'none'; form-action 'self'; base-uri 'self'; object-src 'none'; report-uri /csp-report

# 逐条解读：
# default-src 'self'        兜底只允许同源
# script-src                JS 只能来自同源与指定 CDN，内联脚本直接不执行
# frame-ancestors 'none'    禁止被任何页面 iframe，等价 X-Frame-Options: DENY
# object-src 'none'         封死 Flash 时代的 object/embed 注入
# report-uri                违规 JSON 上报到 /csp-report 供审计
```
