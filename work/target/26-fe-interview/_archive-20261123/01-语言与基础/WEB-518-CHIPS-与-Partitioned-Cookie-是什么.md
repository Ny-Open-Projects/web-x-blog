---
title: [WEB-518] CHIPS 与 Partitioned Cookie 是什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 隐私]
type: 面试题
---

## WEB-518：CHIPS 与 Partitioned Cookie 是什么

**答**：
- CHIPS（Cookies Having Independent Partitioned State）：第三方 Cookie 的「分区替代方案」，加 `Partitioned` 属性
- 语义：iframe 内的 Cookie 按顶级站点分桶——同一服务在 A 站、B 站各存各的，无法跨站串联用户
- 必备约束：Partitioned 必须搭配 Secure，且要 SameSite=None（它是跨站上下文使用的 Cookie）
- 适用场景：客服组件会话、支付 iframe 状态、第三方嵌入页的登录态——正是第三方 Cookie 退场后还能合法工作的少数方案
- 前端自查：嵌入第三方 iframe 后「Cookie 不见了」，先查有没有 Partitioned 支持与设置是否完整

```http
Set-Cookie: helpdesk_session=xyz; SameSite=None; Secure; Partitioned; Max-Age=3600
```
