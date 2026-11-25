---
title: [WEB-416] HSTS 是什么，max-age 与 preload 怎么配
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-416：HSTS 是什么，max-age 与 preload 怎么配

**答**：
- HSTS：服务端返回 `Strict-Transport-Security` 头，浏览器在 max-age 内强制用 https 访问该域名，即使用户手输 http
- 三个参数：`max-age`（有效期）、`includeSubDomains`（覆盖子域）、`preload`（申请进浏览器内置名单）
- 解决的问题：SSL 剥离攻击——用户输 example.com，攻击者在中间响应 http；HSTS 让浏览器根本不发 http 请求
- 代价要讲清：进了 preload 名单后所有子域必须长期全 https，包括内网/边缘设备，回退很难
- 上线节奏：先 max-age 短（如 1 天）观察 → 加长子域 → 最后才申请 preload

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
```
