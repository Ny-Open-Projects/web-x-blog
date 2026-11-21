---
title: [OPT-040] 如何建立性能预算与 CI 卡口？优化前后如何科学度量？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-040：如何建立性能预算与 CI 卡口？优化前后如何科学度量？

**答**：
- 性能预算分层：**传输层**（首页 JS gzip ≤ 200KB、总资源 ≤ 1MB）、**指标层**（LCP ≤ 2.5s、INP ≤ 200ms、CLS ≤ 0.1）、**数量层**（请求数、第三方脚本数）。
- CI 卡口：Lighthouse CI 每次提 PR 跑 Lab 数据 + `size-limit`/bundlesize 卡 bundle 体积，超预算直接 fail，把"性能回归"变成合并阻塞项。
- 度量方法：优化前先建基线（同机型/同网络环境测 Lab，取 RUM P75 而非均值）；一次只改一个变量，对比才有因果；Lab（Lighthouse）与 RUM（真实用户）数据互补。
- 上线后持续观测 RUM 大盘，指标劣化自动告警，回到 09 章的监控体系闭环。

```javascript
// 一一对应：lighthouserc 性能预算 + size-limit CI 卡口
// lighthouserc.js —— Lighthouse CI 断言配置
module.exports = {
  ci: {
    collect: {
      numberOfRuns: 3, // 多次取中位数，降低抖动
      settings: { preset: 'desktop' },
    },
    assert: {
      assertions: {
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-byte-weight': ['error', { maxNumericValue: 1024 * 1024 }],
        'resource-summary:script:size': ['error', { maxNumericValue: 200 * 1024 }],
        'third-party-summary': ['warn', { allowlist: { url: ['https://cdn.example.com'] } }],
      },
    },
  },
};

// package.json —— size-limit 体积卡口
// "size-limit": [
//   { "path": "dist/assets/index-*.js", "limit": "80 KB" },
//   { "path": "dist/assets/vendor-*.js", "limit": "120 KB" }
// ]
// CI 中执行：npx size-limit && npx @lhci/cli autorun，任一超标即 fail
```

## 九、测量与分析体系
