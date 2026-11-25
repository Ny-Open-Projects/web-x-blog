---
title: [PER-109] 性能预算如何平台化？CI 卡口与看板怎么搭？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-109：性能预算如何平台化？CI 卡口与看板怎么搭？

**答**：
- 三层体系：**预算定义**（bundle 体积/LCP/INP/TTFB 的分位数目标，json 化）、**CI 卡口**（PR 阶段跑 Lighthouse 与包体对比，超预算阻断）、**趋势看板**（每日基线跑分入时序库，按版本/页面出趋势）。
- 体积预算比运行时指标更稳定，适合做硬卡口；Lighthouse 分数受环境影响大，适合看趋势不适合做绝对卡口。
- 卡口设计要点：对比对象是 **main 分支基线**而非固定值（允许合理增长、禁止无故劣化）；豁免机制走 PR 标签 + 评审。
- 看板反哺预算：某页面长期 P75 远好于预算，说明预算过松可收紧；反复豁免的项要立专项。

```json
{
  "budgets": [
    {
      "page": "/",
      "resourceSizes": [
        { "resourceType": "script", "budget": 170 },
        { "resourceType": "total", "budget": 300 }
      ],
      "resourceCounts": [{ "resourceType": "third-party", "budget": 5 }],
      "timings": [
        { "metric": "largest-contentful-paint", "budget": 2500 },
        { "metric": "interactive", "budget": 3500 }
      ]
    },
    {
      "page": "/checkout",
      "resourceSizes": [{ "resourceType": "script", "budget": 200 }],
      "timings": [{ "metric": "largest-contentful-paint", "budget": 2500 }]
    }
  ]
}
```

```yaml
# Lighthouse CI：PR 阶段按预算断言，趋势数据上报看板
name: perf-budget
on: [pull_request]
jobs:
  lhci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22 }
      - run: npm ci && npm run build
      - name: Lighthouse CI 断言
        run: |
          npm i -g @lhci/cli
          lhci autorun \
            --collect.staticDistDir=dist \
            --assert.budgetsFile=budgets.json \
            --assert.assertionsresource-summary:off=false \
            --upload.serverBaseUrl=$LHCI_SERVER \
            --upload.token=$LHCI_TOKEN   # 数据进趋势看板
```
