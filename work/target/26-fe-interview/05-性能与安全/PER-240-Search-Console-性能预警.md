---
title: [PER-240] Search Console 的 Core Web Vitals 报告报"需改进"，如何定位到具体页面与原因？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-240：Search Console 的 Core Web Vitals 报告报"需改进"，如何定位到具体页面与原因？

**答**：
- Search Console 按 URL 分组报 CWV 状态（好/需改进/差），粒度是"相似页面组"，示例 URL 是组代表。先进入报告拿问题组清单，再对每组示例 URL 用 CrUX URL 级 API 精查。
- 定位套路：① URL 级 CrUX 无数据 → 用 origin 数据 + 自建 RUM 补；② 按指标定位原因——LCP 差查资源加载（图/字体/render-blocking），INP 差查长任务与三方脚本，CLS 差查无尺寸媒体与动态插入；③ 用 PSI 的诊断项（"Reduce unused JavaScript"等）拿到具体文件清单。
- 治理优先级：按"流量 × 状态差"排序，核心流量页优先；修完等 28 天 CrUX 刷新（急不来），期间用自建 RUM 验证改善。
- 预防机制：CrUX 巡检脚本周跑 + Search Console API 拉问题组清单进工单系统，形成"预警→定位→修复→验证"闭环。

```bash
# URL 级精查：注意 url 前缀必须与实际收录 URL 完全一致（含协议、斜杠）
curl -s -X POST 'https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=KEY' \
  -d '{"url": "https://example.com/goods/123", "formFactor": "PHONE"}' \
  | jq '.record.metrics.interaction_to_next_paint.percentiles'
# 无数据时返回 error: "no data" —— 转用 origin 级 + 自建 RUM 聚合同模板页
```
