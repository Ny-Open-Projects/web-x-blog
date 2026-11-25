---
title: [OPS-236] 影子发布（新版本只跑流量不服务用户）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-236：影子发布怎么做的？
**答**：
- 影子形态：新版本部署完整环境但入口不切换（0% 流量）——用于验证「部署本身」（资源完整性/服务连通/监控上报），发布前最后一级验证。
- 影子验证清单：新入口可达、chunk 引用完整、buildinfo 正确、哨兵数据上报正常、CDN 命中正常——全部通过才允许真实灰度。
- 影子期时长：30 分钟（部署验证足够）——影子不是灰度，不做功能验证。
- 与灰度衔接：影子通过 → 自动进入 1% 灰度（同一编排链），失败 → 阻断并告警。
- 追问钩子：为什么影子验证重点在「部署完整性」而不是「功能正确性」——功能问题灰度 1% 也能发现（且需要真实用户行为）；部署问题（资源缺失/上报断链）在 0 流量下就能验证且一旦灰度会造成全量级故障——影子发布把「部署失败」这类最廉价可测的风险提前归零。

```yaml
shadow_release:
  duration: 30min
  checks: [entry-reachable, chunk-manifest-complete, buildinfo-correct,
           telemetry-flowing, cdn-hit-ok]
  onPass: auto-advance-to-1%
  onFail: block-and-alert
```
