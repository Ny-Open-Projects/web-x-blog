---
title: [OPS-068] Sentry 怎么接入？告警规则怎么配？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-068：Sentry 怎么接入？告警规则怎么配？
**答**：
- 接入要点：release 关联（版本号与构建一致）、环境标签（prod/staging）、采样率控制成本、beforeSend 清洗敏感信息与已知噪音。
- 告警规则按"新问题 + 回归问题 + 崩溃率"分型：新版本出现的新 error 立刻报（回归），存量低频问题聚合日报（降噪）。
- 告警通道分级：issue 出现进值班群，崩溃率超阈值触发电话/短信（PagerDuty）。
- 与发布联动：部署事件发给 Sentry，release 标记 deployed，异常自动关联"哪次发布引入"。

```javascript
// sentry.js：生产级 Sentry 接入配置
import * as Sentry from '@sentry/react';

Sentry.init({
  dsn: config.sentryDsn,
  release: config.buildVersion,        // 与构建版本一致，用于定位引入版本
  environment: config.env,             // prod / staging
  tracesSampleRate: 0.1,               // 性能采样 10%，控制量
  sampleRate: 1.0,                     // 错误全量
  beforeSend(event) {
    // 1. 清洗敏感信息：URL 参数里的 token、手机号不进平台
    if (event.request?.url) {
      event.request.url = event.request.url.replace(/(token|phone)=[^&]+/g, '$1=***');
    }
    // 2. 降噪：已知第三方扩展报错、浏览器插件脚本直接丢弃
    const msg = event.exception?.values?.[0]?.value ?? '';
    if (msg.includes('chrome-extension://') || msg.includes('ResizeObserver loop')) {
      return null;
    }
    return event;
  },
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.replayIntegration({ maskAllInputs: true }),   // 回放脱敏
  ],
});

// 部署联动（在 CI 里执行等价 curl）：
// POST {SENTRY_API}/organizations/{org}/releases/{release}/deploys/
//   { "environment": "production", "name": "web-01" }
```
