---
title: [PER-237] 如何用 CrUX History API 追踪 28 天趋势？两次发版之间怎么对齐时间轴？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-237：如何用 CrUX History API 追踪 28 天趋势？两次发版之间怎么对齐时间轴？

**答**：
- History API 返回过去 25 个"收集周期"（每个约 28 天滚动窗口）的直方图序列，可以画趋势线、看优化动作有没有生效。普通 API 只有一个快照。
- 窗口重叠的本质：每个点是"过去 28 天"的滑动平均，所以优化上线后曲线要 2~4 周才完全反映；对比发版效果要把发版日期标在时间轴上，至少跨 2 个周期再看结论。
- 取数细节：History 返回的每个点只有 histogram（无 p75），要自己用直方图近似或直接看 good 占比趋势；origin 与 URL 需分别请求；formFactor 可拆。
- 自建 RUM 的 7 天/28 天滚动窗口应与 CrUX 对齐，避免"RUM 说变好了、CrUX 还没动"的口径误会。

```bash
curl -s -X POST 'https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord?key=KEY' \
  -d '{"origin": "https://example.com", "formFactor": "PHONE",
       "metrics": ["largest_contentful_paint", "cumulative_layout_shift"]}' \
  | jq '.record.metrics.largest_contentful_paint.histogramTimeseries |
        map({firstDate: .[0].endDay, goodRatio: (.[0].density * 100)})'
# 输出 25 个周期的 good 占比序列；把发版日期叠加进去看拐点是否对上
```
