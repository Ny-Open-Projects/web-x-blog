---
title: [SCN-106] 安全扫描发现某个子域名的旧系统能读到主站会话 Cookie，如何隔离？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-106：安全扫描发现某个子域名的旧系统能读到主站会话 Cookie，如何隔离？
**答**：
- 根因：历史代码把会话 Cookie 设成 `Domain=.example.com`，所有子域名（包括被攻破的旧系统）都能读到。修复是让会话 Cookie 回归 host-only：去掉 Domain 前缀。
- 强约束：用 `__Host-` 前缀，浏览器强制要求 hostOnly + Secure + Path=/，杜绝子域覆写。
- 跨子域确实需要共享的轻量信息（如 uid 偏好），单独发独立低敏感 Cookie，与会话解耦；旧系统本身推动下线或加 WAF 隔离。

```http
# 修复前（危险）：domain 前缀让全部子域名都能读到会话
# Set-Cookie: session=abc; Domain=.example.com; Path=/

# 修复后：仅主站自身可读（无 Domain 属性即 host-only）
Set-Cookie: session=abc; Secure; HttpOnly; SameSite=Lax; Path=/

# 强约束版本：__Host- 前缀，浏览器强制 hostOnly + Secure + Path=/
Set-Cookie: __Host-session=abc; Secure; HttpOnly; SameSite=Lax; Path=/

# 跨子域确实需要的轻量身份（非会话），独立低敏感 Cookie 解耦
Set-Cookie: public_uid=u123; Domain=example.com; Secure; SameSite=Lax
```

## 二十、工程协作
