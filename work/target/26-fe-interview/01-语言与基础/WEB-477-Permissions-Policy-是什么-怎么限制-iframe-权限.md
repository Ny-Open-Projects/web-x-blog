---
title: [WEB-477] Permissions Policy 是什么，怎么限制 iframe 权限
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-477：Permissions Policy 是什么，怎么限制 iframe 权限

**答**：
- Permissions Policy（原 Feature Policy）：HTTP 头声明站点允许哪些能力（摄像头、地理位置、全屏、支付等）给谁用
- 两个作用面：自己页面关闭不需要的能力（缩攻击面）；嵌入第三方 iframe 时用 allow 列表白名单授权
- 语法：`Permissions-Policy: camera=(), geolocation=(self "https://map.partner.com")`——空括号=全员禁用
- iframe 授权联动：外层 policy + iframe 的 `allow` 属性双重门禁，缺一不可
- 实战价值：广告位/富媒体 iframe 只给 fullscreen 和 autoplay，不给摄像头麦克风，是低成本高收益的加固

```http
Permissions-Policy: camera=(), microphone=(), payment=(self), fullscreen=*
```
```html
<iframe src="https://ad.partner.com" allow="fullscreen; autoplay"></iframe>
```
