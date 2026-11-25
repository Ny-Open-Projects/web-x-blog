---
title: [BAS-105] 什么情况下会触发 OPTIONS 预检请求？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-105：什么情况下会触发 OPTIONS 预检请求？
**答**：
- 非简单请求先发 OPTIONS 探路：方法为 PUT/DELETE/PATCH 等，或 Content-Type 不是三种简单值，或携带自定义头（如 X-Token、Authorization）。
- 简单请求判定：GET/HEAD/POST 之一，Content-Type 限于 text/plain、multipart/form-data、application/x-www-form-urlencoded，且无自定义头。
- 预检由浏览器自动发出，服务端对 OPTIONS 返回 2xx 并带 Access-Control-Allow-Methods/Headers；Access-Control-Max-Age 可缓存预检结果减少次数。

```http
# 前端带自定义头的请求，浏览器先自动发预检
OPTIONS /api/user HTTP/1.1
Access-Control-Request-Method: POST
Access-Control-Request-Headers: x-token

# 服务端响应
HTTP/1.1 204 No Content
Access-Control-Allow-Methods: POST, DELETE
Access-Control-Allow-Headers: x-token
Access-Control-Max-Age: 86400
```

```mermaid
flowchart TD
    A[发起跨域请求] --> B{方法是 GET HEAD POST 之一}
    B -- 否 --> F[先发 OPTIONS 预检]
    B -- 是 --> C{Content-Type 为三种简单值之一}
    C -- 否 --> F
    C -- 是 --> D{是否携带自定义头}
    D -- 是 --> F
    D -- 否 --> E[简单请求直接发送]
    F --> G[服务端返回允许的方法与头]
    G --> H[浏览器再发真实请求]
```
