---
title: [BAS-121] cookie、session、JWT 一句话速记？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-121：cookie、session、JWT 一句话速记？
**答**：
- cookie：浏览器存储、自动随同源请求携带的小段数据；session：状态存服务端，cookie 里只放 sessionId。
- JWT：状态编码在 token 里（header.payload.signature），服务端无状态、签名防篡改；缺点是无法主动作废、payload 是明文。
- 速记：session 有状态放服务端，JWT 无状态放客户端，cookie 是两者的搬运工。

```http
# session 方案：cookie 只带会话 ID
Cookie: JSESSIONID=abc123

# JWT 方案：token 自带信息与签名
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjF9.xxxx
# payload 是 base64url 明文，别放敏感数据
```
