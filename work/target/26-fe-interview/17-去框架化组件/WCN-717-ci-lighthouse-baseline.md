---
title: [WCN-717] 如何在 CI 里跑 Lighthouse 给 WC 组件建立性能基线并防回归？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-717：如何在 CI 里跑 Lighthouse 给 WC 组件建立性能基线并防回归？

**答**：
- 结论：把组件 demo 页部署到预览环境，用 lighthouse-ci 在固定硬件/网络条件下跑分，对 FCP/LCP/TBT/CLS 设阈值，超阈值即失败。
- 对 WC 关注自定义元素升级耗时、Shadow DOM 渲染成本；用预设的 throttling 配置保证可比性，结果上传趋势看板。
- 追问钩子：CI 机器性能抖动导致分数波动怎么办？考察「多次取中位数 + 相对阈值 + 稳定环境」的策略。

```javascript
// lighthouserc.js 配置
module.exports = {
  ci: {
    collect: { url: ['http://preview/ds-table-demo'], numberOfRuns: 3 },
    assert: {
      assertions: {
        'first-contentful-paint': ['error', { maxNumericValue: 1500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-blocking-time': ['error', { maxNumericValue: 300 }],
      },
    },
    upload: { target: 'temporary-public-storage' },
  },
};
console.log('多跑几次取中位数，缓解机器抖动');
```
