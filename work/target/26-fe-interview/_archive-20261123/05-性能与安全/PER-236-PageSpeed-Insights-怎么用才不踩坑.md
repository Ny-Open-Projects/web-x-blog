---
title: [PER-236] PageSpeed Insights 的实验室分与 CrUX 真实分打架时信谁？如何正确使用 PSI？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-236：PageSpeed Insights 的实验室分与 CrUX 真实分打架时信谁？如何正确使用 PSI？

**答**：
- 先分清两类数据：PSI 页面上半部分是 CrUX 真实用户数据（p75、28 天），下半部分是 Lighthouse 实验室数据（单次、模拟设备 Moto G4 + 慢 4G）。两者口径不同，直接对比本身就不公平。
- 优先级：**评估用户真实体验以 CrUX 为准**（它是 SEO 判分依据）；实验室数据用于诊断与回归（能复现、可归因、不受真实流量波动影响）。真实分好实验室分差 → 常见于高端设备占比高；实验室分好真实分差 → 真实环境更差（弱网/低端机/三方脚本动态加载）。
- PSI 分数陷阱：Performance Score 是加权合成的"总评"，单看分数没意义；正确姿势是点开各个 CWV 指标的 p75 值与诊断项。
- 实践：CI 里用 Lighthouse CLI 跑实验室回归（固定环境才可比），线上看 CrUX + 自建 RUM；两侧分工而不是互相否定。

```bash
# PSI API 拉取：labResult（Lighthouse）与 fieldData（CrUX）分开处理
curl -s 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile' \
  | jq '{lab: .lighthouseResult.categories.performance.score,
         field: .loadingExperience.metrics.largest_contentful_paint.percentile,
         fieldCat: .loadingExperience.metrics.largest_contentful_paint.category}'
# lab 是 0~1 的加权分数；field 是真实 p75 毫秒值 —— 两者不可互换
```
