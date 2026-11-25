---
title: [WEB-546] HTTP/3 迁移的回滚预案怎么做
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-546：HTTP/3 迁移的回滚预案怎么做

**答**：
- 回滚主开关在「停止下发 Alt-Svc」：客户端 ma 值过期后（默认 86400s，可临时缩到 300s 预热期）自动回归 h2，无需发版
- 回滚分级：L1 关 Alt-Svc（分钟级生效）、L2 CDN 边缘关 QUIC 监听（立即，但已建立的 h3 连接存活到超时）、L3 完整摘除 UDP 配置
- 预案要写清「回滚判据」：如 h3 请求失败率 > 3% 持续 5 分钟、或 P75 TTFB 劣化 > 20%，任何人可先回滚后复盘
- 别忘了客户端缓存惯性：ma 值存内存/磁盘视浏览器实现而定，紧急回滚时配合 CDN 强制在响应里返回空 Alt-Svc 覆盖
- 演练：迁移前先做一次「假回滚」演练，确认判据、通知链、CDN 工单 SLA 都能走通，否则预案是纸面的

```text
判据（Prometheus 示例）:
  sum(rate(h3_requests_failed[5m])) / sum(rate(h3_requests_total[5m])) > 0.03
动作:
  1) 配置中心: alt_svc_ma: 86400 → 0 (停止引导)
  2) 通知: CDN 关闭 quic listen
  3) 复盘: 保留 24h 内 h3 失败样本 (pcap)
```
