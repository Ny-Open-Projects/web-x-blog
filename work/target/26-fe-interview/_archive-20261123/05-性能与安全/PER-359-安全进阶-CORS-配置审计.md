---
title: [PER-359] CORS 配置的常见错误与审计方法：宽通配、凭据泄漏与反射 Origin 的危险？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-359：CORS 配置的常见错误与审计方法：宽通配、凭据泄漏与反射 Origin 的危险？

**答**:
- 高危配置一：`Access-Control-Allow-Origin: *` + `Access-Control-Allow-Credentials: true`——浏览器规范禁止此组合生效（凭据请求会被拒），但很多自研网关错误地"反射 Origin"（把请求的 Origin 原样回显到 ACAO 并开凭据）——任何网站都能携带用户 Cookie 读接口，等于 CORS 全开。
- 高危配置二：Origin 前缀/后缀匹配（`startsWith('https://api.example')`）——`api.example-evil.com` 绕过。必须精确匹配白名单。
- 高危配置三：把内部敏感接口加 CORS 允许公共 CDN 域（JSONP 时代遗留），或 `Allow-Headers` 全放行（`*`）暴露内部调试头。
- 审计方法：从外部发起带恶意 Origin 的请求验证反射行为；网关配置扫描（正则匹配反射逻辑）；内部接口清单 × CORS 白名单交叉审计（谁不该被跨域访问）。
- 正确姿势：白名单精确域；凭据接口白名单最小化；`Vary: Origin`（缓存按 Origin 分键，否则 CDN 会把 A 域的响应缓存给 B 域）。

```text
审计用例（对每个接口发三次请求验证）：
curl -H "Origin: https://evil.com" -i https://api.example.com/user/info
  → 反射 Origin + Allow-Credentials: true  ⇒ 高危（任意站可带凭据读取）
curl -H "Origin: https://api.example-evil.com" -i ...
  → 匹配成功 ⇒ 高危（前缀匹配漏洞）
curl -H "Origin: https://partner.com" -i ...
  → 无 ACAO 头 ⇒ 正确（未在白名单）
修复：精确白名单 + 凭据接口最小化 + Vary: Origin
```
