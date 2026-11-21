---
title: [PER-233] CrUX 数据是什么？它和自建 RUM 有什么区别，怎么配合使用？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-233：CrUX 数据是什么？它和自建 RUM 有什么区别，怎么配合使用？

**答**：
- CrUX（Chrome UX Report）是 Google 收集的**真实 Chrome 用户的 Web Vitals 数据集**，按 origin/URL 聚合，口径固定（p75、28 天滚动窗口），是 Core Web Vitals SEO 评判的官方数据源（PageSpeed Insights / Search Console 都引用它）。
- 三个局限：① 粒度只有 origin 或高流量 URL，长尾页面没有数据；② 维度极少（设备类型、连接类型），不能按业务线/版本/用户群拆；③ 只覆盖 Chrome 用户，Safari/iOS 用户不在内。
- 自建 RUM 的价值正好补齐：任意粒度、任意维度、自定义指标（业务首屏、接口成功率）、覆盖全浏览器。两者口径（p75、CWV 阈值）对齐后互为校验。
- 配合姿势：选型/竞品分析/SEO 风险预警用 CrUX（看竞对 origin、看自己 28 天趋势）；日常迭代与问题定位用自建 RUM；两者差异过大（>30%）先查口径实现是否一致。

```bash
# CrUX API 查询自己与竞品的 origin p75 口径
curl -s -X POST 'https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"origin": "https://www.example.com", "formFactor": "PHONE", "metrics": {
        "largest_contentful_paint": { "percentiles": {}, "histogram": {} },
        "interaction_to_next_paint": {},
        "cumulative_layout_shift": {} }}'
# 返回 histogram 分桶（good/needs-improvement/poor 占比）与 p75 值，28 天窗口
```
