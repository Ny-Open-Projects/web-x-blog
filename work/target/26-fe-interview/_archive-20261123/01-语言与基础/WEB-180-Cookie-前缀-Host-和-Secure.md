---
title: [WEB-180] Cookie 前缀 __Host- 和 __Secure- 是干什么的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-180：Cookie 前缀 __Host- 和 __Secure- 是干什么的？
**答**：
- 浏览器对前缀有硬性约束：__Secure- 必须带 Secure；__Host- 必须 Secure 且 Path=/ 且不能有 Domain 属性。
- 收益：__Host- 从协议层保证"这个 Cookie 一定属于当前精确域名、全站路径、仅 HTTPS"，子域与路径注入都写不出来。
- 前缀必须从名字第一个字符开始；设置时不满足约束浏览器直接拒收——比事后校验可靠。
- 实践：会话 Cookie 用 __Host-session；确实需要子域共享的才退回普通 Cookie 加 Domain。

```http
# 会话 Cookie 用 __Host- 前缀：浏览器强制校验以下条件全部满足才接受
Set-Cookie: __Host-session=abc123; Secure; HttpOnly; SameSite=Lax; Path=/

# 反例：带 Domain 属性或 Path 非 /，浏览器直接拒收（静默失败，排查时注意）
# Set-Cookie: __Host-session=abc123; Secure; Domain=example.com; Path=/

# 需要子域共享时退回普通 Cookie，至少保证 Secure
Set-Cookie: theme=dark; Secure; Domain=example.com; Path=/; SameSite=Lax
```
