---
title: [WEB-461] 灰度发布出问题，定位与回滚 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-461：灰度发布出问题，定位与回滚 SOP

**答**：
- 先止血后复盘：确认「问题规模与灰度占比是否一致」，一致则立即回滚（前端静态资源回滚 = 指回旧版本目录/CDN 源），不要恋战修 bug
- 前端回滚要点：HTML 入口不带强缓存（否则回滚不生效），旧版本目录保留而非覆盖发布，CDN 刷新 HTML
- 快速归因三问：错误监控的新增堆栈指纹是什么？灰度桶与稳定桶的指标 diff（JS 错误率、白屏率、接口成功率）在哪一条？
- 常见事故类型：静态资源 404（新 HTML + 旧资源被清理/旧 HTML + 新资源指纹变了）、接口字段不兼容、CSP/安全头误配
- 预防机制：发布前保留 N 个历史版本、HTML 与资源版本联动校验、灰度看板默认带上错误率而非只看流量

```javascript
// 灰度看板核心指标（前端可自查）
const nav = performance.getEntriesByType('navigation')[0];
report({ ver: BUILD_VERSION, white: nav.domContentLoadedEventEnd === 0, jsErr: window.__errCount || 0 });
```
