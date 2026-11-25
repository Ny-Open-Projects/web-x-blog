---
title: [NODE-604] Node 服务的故障演练平台（演练编排/评分/报告）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-604：故障演练平台
**答**:
- 平台化：演练场景库（故障场景注册：依赖故障/资源耗尽/网络分区——参数化模板）、演练编排（场景 + 注入范围 + 观察指标 + 验收标准——剧本化 NODE-460 思想）、执行控制（灰度域注入/定时开始/一键终止——安全护栏 NODE-408）。
- 评分与报告：演练评分（验收标准达成率：降级生效/恢复时长/用户影响——量化演练结果）、自动报告（时间线/发现的问题/修复建议——闭环跟踪）、演练台账（各服务最近演练时间——覆盖度看板：超期未演练标红）。
- 发现问题闭环：演练缺陷 → 工单（自动创建——owner/优先级）→ 修复 → 复演验证（缺陷修复必须复演证明）。
- 演练文化：新服务准入演练（上线前必过基础演练场景——出生质量）、季度全员演练（大促前综合演练）。
- 与降级声明联动：NODE-479——每个降级声明自动关联演练场景与最近结果（声明了没演练过 = 红灯）。
```yaml
# 演练场景模板
scenario: redis-down
inject: { target: 'redis-proxy', chaos: 'network-delay 200ms + 50% err', scope: 'canary', duration: 5m }
observe: [errorRate, degradeRate, recoveryTime]
accept: { degrade: '<=5s 生效', recovery: '<=60s', userError: '<0.1%' }
report: auto → 工单闭环
```
