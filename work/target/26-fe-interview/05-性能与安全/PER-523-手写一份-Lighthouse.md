---
title: [PER-523] 手写一份 Lighthouse CI 的性能预算配置：对页面产物体积、资源数量、指标值三层面设卡口
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-523：手写一份 Lighthouse CI 的性能预算配置：对页面产物体积、资源数量、指标值三层面设卡口

**答**：
- `lighthouserc` 的 `assertions` 三层卡口：指标预算（lcp/tbt/cls）、资源体积（resource-summary 各类目）、资源数量；`assertMatrix` 可对多档位矩阵分别设阈值。
- 要点：预算要配 `aggregationMethod: 'median'` + `pessimistic` 取多次运行的最差值，防抖动漏过卡口。
- 边界：预算值来自 RUM 用户档位反推而不是拍的，且要留 10% 缓冲带，否则每次依赖升级都红灯，团队会开始无视卡口。
- 评分点：budgeted 系列的 key 写法与 weightedMode 无关，重点是否理解 assert 严重级别（error 才挡合并，warn 只提示）。

```javascript

// lighthouserc.cjs —— 三层卡口配置
module.exports = {
  ci: {
    collect: {
      numberOfRuns: 3,                       // 3 次取最差，防抖动
      settings: { throttling: { cpuSlowdownMultiplier: 4 } },
    },
    assert: {
      assertions: {
        // 指标层
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'total-blocking-time':       ['error', { maxNumericValue: 300 }],
        'cumulative-layout-shift':   ['error', { maxNumericValue: 0.1 }],
        // 体积层（resource-summary 类目）
        'resource-summary:script:size':  ['error', { maxNumericValue: 300 * 1024 }],
        'resource-summary:image:size':   ['warn',  { maxNumericValue: 900 * 1024 }],
        'resource-summary:third-party:size': ['error', { maxNumericValue: 150 * 1024 }],
        // 数量层
        'resource-summary:requests': ['error', { maxNumericValue: 60 }],
      },
      aggregationMethod: 'median',           // 聚合方式
    },
    upload: { target: 'temporary-public-storage' },
  },
};
// CI 跑法：npx @lhci/cli autorun —— error 级断言失败则退出码非 0，阻断合并
```
