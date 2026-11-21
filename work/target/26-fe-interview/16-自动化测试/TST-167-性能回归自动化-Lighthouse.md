---
title: [TST-167] 性能回归怎么自动化？Lighthouse CI 与 Web Vitals 预算门禁
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-167：性能回归怎么自动化？Lighthouse CI 与 Web Vitals 预算门禁
**答**：
- 两条路：① 合成监控（Lighthouse CI）——每次部署/每夜在固定环境跑 Lighthouse，断言分数与指标阈值（LCP/TBT/CLS），产物是可 trend 的报告；② 真实用户监控（RUM + web-vitals SDK）——线上采样上报 LCP/INP/CLS，回归告警。合成稳定可门禁，RUM 真实但有噪声，两者互补。
- 资源预算（performance budget）比「分数」更有指导性：JS 总量 < 200KB gzip、图片单张 < 100KB、第三方脚本 < 10 个——用 `bundlesize`/Lighthouse budget.json 在 CI 阻断超标 PR。
- E2E 场景内的性能断言：Playwright 里 `page.evaluate` 读 `performance.getEntriesByType('navigation')`、`PerformanceObserver` 收 LCP；关键页断言「首屏图片都有 width/height（防 CLS）」「路由切换后无 layout shift」。数值波动大，用「预算 + 相对基线」而非绝对毫秒。
- 防 flaky 要点：固定机器规格（Docker + CPU 节流一致）、多次采样取中位数、预热首跑丢弃。
- 追问钩子：INP 为什么取代 FID？——FID 只测首次输入延迟，INP 覆盖整个生命周期所有交互的响应性，更能代表体验。

```javascript
// lighthouserc.json：部署后跑，断言指标预算
{
  "ci": {
    "collect": { "numberOfRuns": 3, "settings": { "throttling": { "rttMs": 150, "throughputKbps": 1600 } } },
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.85 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "total-byte-weight": ["error", { "maxNumericValue": 1200000 }],
        "resource-summary:script:size": ["error", { "maxNumericValue": 200000 }]
      }
    }
  }
}
```
