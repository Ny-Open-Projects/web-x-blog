---
title: [WCN-148] WCN 在 SSR 站点落地有哪些坑？FOUC、DSD 兼容性、CDN 预取与 CSP 怎么处理？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-148：WCN 在 SSR 站点落地有哪些坑？

**答**：
- 坑一 FOUC：define 前 unknown element 无样式——解法是 DSD（服务端输出影子树）+ `:not(:defined)` 占位兜底（WCN-023）。
- 坑二 DSD 兼容：Chrome 90+/Safari 16.4+/Firefox 123+；老浏览器需要 polyfill（@webcomponents/template-shadowroot），要在关键 CSS 前同步加载，否则闪烁依旧。
- 坑三 CDN 与 CORS：组件 ESM 必须允许跨域（Access-Control-Allow-Origin）；CSP 需白名单 script-src；若走 importmap，注意 Safari 对多 importmap 的支持。
- 坑四 样式加载顺序：DSD 影子样式在 HTML 内联会增大 HTML 体积——抽公共 token 到全局 link、组件样式内联，平衡 TTFB 与样式正确性。
- 坑五 水合竞态：define 延迟到交互（islands）时，服务端渲染的表单控件在 define 前不可交互——首屏可交互组件必须同步 define（preload）。

```html
<!-- head 内的预取与 polyfill 顺序 -->
<link rel="modulepreload" href="https://cdn.acme.com/wc/button/1.4.2/button.js" crossorigin>
<script async src="https://unpkg.com/@webcomponents/template-shadowroot/template-shadowroot.js"></script>
<!-- CSP：script-src 'self' cdn.acme.com; connect-src api.acme.com -->
```
