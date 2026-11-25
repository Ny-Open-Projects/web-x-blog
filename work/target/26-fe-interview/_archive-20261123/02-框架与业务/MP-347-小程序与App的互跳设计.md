---
title: [MP-347] 小程序与 App 互跳：launchApp 与开放标签
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-347：小程序与 App 互跳：launchApp 与开放标签

**答**：
- 互跳能力矩阵：小程序 → App（open-type="launchApp"——需 App 内嵌小程序且绑定）、App → 小程序（App 拉起指定页面）、H5 → 小程序（开放标签 wx-open-launch-weapp——需认证公众号 JSSDK）
- launchApp 的约束：只在「App 内嵌的 web-view 中的小程序」可用——独立运行的小程序无法直接拉 App（只能通过客服消息/URL scheme 引导）
- URL scheme（weixin://dl/business）：服务端生成（getwxacodeunlimit 类似接口）——短信/邮件「拉起小程序」的通道；有效期与次数限制
- 参数透传：互跳链路的参数协议（source/traceid 归因）——「App 与小程序的会话打通」（同一账号体系 + 登录态共享）
- 深水点：互跳的降级链：拉 App 失败（未安装）→ 应用宝/落地 H5 → 引导下载——「互跳失败体验」的设计

```xml
<!-- 小程序内拉起 App (App 内嵌场景) -->
<button open-type="launchApp" app-parameter="from=miniprogram" binderror="onLaunchFail">
  打开 App
</button>
<!-- H5 拉起小程序 -->
<wx-open-launch-weapp appid="wx123" path="pages/index/index.html?src=h5">
  <script type="text/wxbrowser-template"><button>打开小程序</button></script>
</wx-open-launch-weapp>
<!-- URL scheme: 服务端 POST /urlscheme → weixin://dl/business/?t=xxx → 短信触达 -->
```
