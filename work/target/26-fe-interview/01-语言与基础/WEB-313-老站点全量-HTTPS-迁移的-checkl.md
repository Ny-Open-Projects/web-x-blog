---
title: [WEB-313] 老站点全量 HTTPS 迁移的 checklist 怎么排？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 笔试题
---

## WEB-313：老站点全量 HTTPS 迁移的 checklist 怎么排？
**答**：
- 前置：证书（含中间链完整）、所有子域覆盖、CDN/网关证书一致；DNS 预留短 TTL 方便回退。
- 页面内：全站扫描 http:// 硬链接（img/css/js/xhr）、第三方 SDK 是否支持 https、CSP 先 report-only 观察。
- 流量层：301 重定向保留 query、HSTS 从短 max-age 起步、混合内容监控、SEO 提交 https 站点地图；观察 p99 错误率与转化再收紧。

```javascript
// 迁移扫描脚本思路
const scan = files => files.flatMap(f =>
  f.content.match(/http:\/\/[a-z0-9.-]+/gi) || []);
const found = scan([{ content: '<img src="http://cdn.com/a.png">' }]);
console.log('硬编码 http 资源:', [...new Set(found)]);
// 阶段: http 可用+观察 → 301 → HSTS 1天 → 1周 → 1年 → preload
```

**评分点**：
- 结论先行，能一句话说清核心机制
- 要点覆盖主流程与关键分支（异常/并发/边界）
- 代码可运行且体现安全或性能意识
- 能主动说出"工程上怎么选"与常见坑
