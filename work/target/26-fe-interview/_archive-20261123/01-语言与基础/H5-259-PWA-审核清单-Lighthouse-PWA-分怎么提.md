---
title: [H5-259] PWA 审核清单：Lighthouse PWA 分怎么提
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-259：PWA 审核清单：Lighthouse PWA 分怎么提

**答**：
- 可安装性检查项：manifest 完整（name/icons 192+512/start_url/display）/ SW 注册且有 fetch handler / HTTPS
- 常见扣分点：图标缺 512 尺寸、maskable 图标缺失、SW 没有 fetch 处理（只有注册不算）、start_url 跨源
- 体验项联动：PWA 分与性能分互相影响——install 预缓存过多资源会拖慢首次加载，要分层缓存
- 检查工具：Lighthouse CLI（CI 里跑防回退）+ `chrome://webapks`（Android 实际安装状态）+ DevTools Application 面板的 Installability 问题列表
- 现实认知：Lighthouse 的 PWA 审计已精简，真正的验收是「装到桌面后启动像 App」，以真机体验为准

```bash
npx lighthouse https://example.com --only-categories=pwa --output=json | jq '.categories.pwa'
# audit-results 里逐项看 failed
```
