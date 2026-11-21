---
title: [PER-128] iframe 的 sandbox 属性各参数含义？如何给第三方页面最小权限？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-128：iframe 的 sandbox 属性各参数含义？如何给第三方页面最小权限？

**答**：
- sandbox 是**白名单机制**：不加的权限一律没有。常用参数：`allow-scripts`（跑脚本）、`allow-same-origin`（保留自身源）、`allow-forms`、`allow-popups`、`allow-top-navigation`（可劫持父页面，慎给）、`allow-downloads`。
- 铁律：`allow-scripts` + `allow-same-origin` 同时给等于沙箱失效——脚本可以摘掉自己的 sandbox 属性。
- 场景化最小权限：广告给 `allow-scripts allow-forms`；富文本预览给空 `sandbox=""`；文档协作再加 `allow-popups` 但不给 `allow-top-navigation`。
- 配套：`loading="lazy"` 延迟加载、`referrerpolicy` 控制引用来源、CSP `frame-src` 限制可嵌入来源。

```html
<!-- sandbox 是白名单机制：不给的权限一律没有，按需逐项开放 -->
<!-- 1. 广告位：允许脚本与表单提交，禁止同源与顶级导航 -->
<iframe src="https://ads.example.com/unit/42"
        sandbox="allow-scripts allow-forms"
        referrerpolicy="no-referrer" loading="lazy"></iframe>

<!-- 2. 富文本预览：完全沙箱，连脚本都没有，防存储型 XSS 复燃 -->
<iframe src="/preview/report.html" sandbox=""></iframe>

<!-- 3. 第三方文档协作：需要同源与弹窗，但绝不给顶级导航能力 -->
<iframe src="https://docs.partner.com/embed"
        sandbox="allow-scripts allow-same-origin allow-popups"
        referrerpolicy="origin"></iframe>

<!-- 4. 能力收敛：allow 属性只放行媒体能力 -->
<iframe src="https://player.example.com/v/9" sandbox="allow-scripts"
        allow="autoplay; encrypted-media" allowfullscreen loading="lazy"></iframe>
```
