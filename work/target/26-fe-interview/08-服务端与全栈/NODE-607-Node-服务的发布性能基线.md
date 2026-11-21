---
title: [NODE-607] Node 服务的发布性能基线（发布前后性能对比门禁）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-607：发布性能基线门禁
**答**:
- 门禁设计：发布前压测对比（新版本 vs 当前版本——同流量模型压测：P95/QPS 上限/资源占用对比 NODE-373/465）、劣化阈值（P95 +20% 或吞吐 -15% → 阻断或评估）、资源基线（内存增长/启动时间——也纳入）。
- 基线管理：当前基线快照（每发布后更新——基线随版本演进）、基线可比性（同机同数据量同并发——噪音控制 NODE-465）、基线豁免（有意改动（功能增加带来耗时）——评审豁免留痕）。
- 执行方式：CI 内基准测试（微基准快筛——性能回归早期）、发布前压测（staging 压测对比——关键服务强制）、灰度期线上对比（NODE-446 实时基线——真实流量验证）。
- 归因辅助：劣化时归因（CPU profile 对比/SQL diff——定位到改动点 ARC-582 服务端版）、性能改进识别（新版本更快也记录——优化积累）。
- 度量：性能回归拦截次数（门禁价值）、发布后性能事故（漏网——门禁改进依据）。
```yaml
# 发布性能门禁
perf-gate:
  compare: { base: current-stable, candidate: rc-build }
  load: replay-model(peak-1h)                                   # 真实流量模型
  thresholds: { p95: '+20% block', throughput: '-15% block', mem: '+30% warn' }
  attribution: auto-flame-diff                                  # 劣化自动归因报告
```
