---
title: [WEB-473] HTTPS 页面加载 http 资源被拦截怎么排查
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-473：HTTPS 页面加载 http 资源被拦截怎么排查

**答**：
- 现象分级：被动混合内容（图片等）会被自动升级或放行但警告；主动混合内容（script/xhr）直接被 Chrome 拦截——控制台报 `Mixed Content`
- 排查顺序：DevTools Console 逐条看 blocked URL 来源（模板写死、配置下发、第三方 SDK 回调里的 http 链接）
- 自动升级的坑：浏览器会把 http 资源自动升级为 https，若服务端不支持 https 就直接失败——表现为「资源 URL 明明是 http 却报 https 错」
- 修复路径：站内资源协议相对/绝对 https；第三方 SDK 检查其回传字段；富文本用户内容做服务端改写（http→https 白名单）
- 兜底：CSP 的 `upgrade-insecure-requests` 全站强制升级，配合 Report-Only 观察存量

```javascript
// 富文本入库前的协议改写（服务端/前端皆可）
html = html.replace(/(<img[^>]+src=["'])http:\/\//gi, '$1https://')
           .replace(/(<a[^>]+href=["'])http:\/\//gi, '$1https://');
```
