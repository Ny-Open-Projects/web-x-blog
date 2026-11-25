---
title: [PER-907] CI 中的性能门禁如何落地？拦截后怎么不阻塞业务
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-907：CI 中的性能门禁如何落地？拦截后怎么不阻塞业务

**答**：
- 门禁三件套：体积门禁（ bundlesize / size-limit 对比预算）、指标门禁（Lighthouse CI 断言）、快照门禁（关键页面截图 diff）。
- 分层拦截：超过预算硬拦（fail），进入预算 90%~100% 黄区（warning + 通知），豁免走审批单并设有效期。
- 只拦增量：门禁对比目标分支与主分支的产物 diff，新增超预算才拦，存量问题走专项治理，避免"历史债务堵死所有人"。
- 门禁速度优化：Lighthouse 用固定机型/网络模拟 + 只跑关键 3~5 条路由。

```javascript
// .lighthouserc.json：Lighthouse CI 断言
{
  "ci": {
    "collect": { "numberOfRuns": 3, "settings": { "preset": "desktop" } },
    "assert": {
      "assertions": {
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift":   ["error", { "maxNumericValue": 0.1 }],
        "resource-summary:script:size": ["error", { "maxNumericValue": 358400 }],
        "categories:performance": ["warn", { "minScore": 0.85 }]
      }
    },
    "upload": { "target": "temporary-public-storage" }
  }
}
```
