---
title: [OPT-045] CrUX 数据是什么？怎么在选型和验收中使用它？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-045：CrUX 数据是什么？怎么在选型和验收中使用它？

**答**：
- CrUX（Chrome UX Report）是 Chrome 真实用户匿名上报的 CWV 数据集，提供 P75 分位，有 API/BigQuery/Data Studio 三种入口。
- 用途一：**竞品与行业基线**——立项时查对标站点的真实 P75，定合理目标而非拍脑袋"首屏 1 秒"。
- 用途二：**域名健康度验收**——上线后 28 天滚动窗口的数据才是 SEO/用户真实感知。
- 局限要清楚：只统计 Chrome、流量少的域名无数据、滞后约一个月、只有 P75 不给分布尾部。

```bash
# 一一对应：curl 调用 CrUX API 查询某页面真实用户 P75 指标
# 前置：在 https://console.cloud.google.com 申请 CrUX API Key
curl -s "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=$CRUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "origin": "https://example.com",
    "formFactor": "PHONE",
    "metrics": ["largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift"]
  }' | jq '.record.metrics'

# 输出示例解读（P75 是唯一口径）：
# largest_contentful_paint.percentiles.p75 = 2800  -> <2500 达标，2800 需治理
# interaction_to_next_paint.percentiles.p75 = 150  -> <200 达标
# cumulative_layout_shift.percentiles.p75 = 0.05  -> <0.1 达标

# 大流量站点用 BigQuery 拉全国/类目分布做基线：
# SELECT p75s.largest_contentful_paint FROM `chrome-ux-report.materialized.country_summary`
# WHERE yyyymm = 202610 AND country_code = 'CN' AND origin LIKE '%example%'
```
