---
title: [WEB-181] SameSite=None 的约束是什么？第三方 Cookie 为什么在消亡？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-181：SameSite=None 的约束是什么？第三方 Cookie 为什么在消亡？
**答**：
- SameSite=None 必须搭配 Secure，否则浏览器拒收；它是"允许跨站发送 Cookie"的唯一开关，第三方 iframe/广告/支付都依赖它。
- 消亡进程：Safari ITP 与 Firefox 已默认分区或禁用第三方 Cookie，Chrome 逐步限制并推进隐私沙盒替代。
- 技术替代方向：CHIPS（Partitioned 属性，Cookie 按顶级站点分区存储）、Storage Access API、Topics/Fenced Frame 等沙盒 API。
- 前端影响：嵌入第三方登录/支付/统计的 iframe 若依赖跨站 Cookie，需要迁移到分区 Cookie 或 Storage Access。

```http
# 跨站场景（iframe 内业务）：分区 Cookie，按顶级站点隔离存储
Set-Cookie: __Host-widget_state=t1; Secure; HttpOnly; SameSite=None; Partitioned; Path=/

# 传统跨站 Cookie（未来将被限制，仅过渡期）
Set-Cookie: tracker=u42; Secure; SameSite=None; Path=/

# 配套 API：被嵌入方主动向用户申请访问其第一方 Cookie
# await document.requestStorageAccess();  // 需要用户手势与浏览器授予
```
