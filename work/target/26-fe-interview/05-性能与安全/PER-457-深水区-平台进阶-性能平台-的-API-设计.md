---
title: [PER-457] 性能平台的对外 API：发布系统/工单系统如何程序化消费性能数据与结论？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-457：发布系统/工单系统如何程序化消费性能数据？

**答**:
- API 三组：① 查询类——GET /metrics（指标查询：页面/版本/时间窗/分位数）、GET /versions/{v}/health（版本健康度，PER-450）；② 结论类——POST /compare（双版本 bootstrap 对照，返回 verdict + evidence，PER-422 联动协议）、GET /diagnose/{alertId}（诊断包）；③ 行动类——POST /tickets（慢日志转工单，带全部归因上下文）、POST /budgets（预算更新触发卡口同步）。
- 设计纪律：结论类 API 返回结构化 verdict（不是人读报表的截图）——自动化联动的契约；幂等与限流（发布系统的轮询查询打挂平台）；版本化（v1 API 冻结，变更走 v2）；鉴权按租户（PER-447）。
- 消费方矩阵：发布系统（对照 verdict）、工单系统（自动建单/关闭回传）、CI（预算卡口拉取 budgets.json）、周报机器人（聚合查询）——每个消费方的 SLA 不同（发布对照要秒级、周报可批量）。

```text
性能平台对外 API 契约：
查询类：GET /metrics?page&version&window&percentile / GET /versions/{v}/health
结论类：POST /compare → { verdict: pass|warn|block, evidence, significance }（PER-422）
        GET /diagnose/{alertId} → 诊断包（PER-390）
行动类：POST /tickets（慢日志转工单，带归因）/ POST /budgets（卡口同步）
纪律：结构化 verdict（自动化契约）、幂等限流、API 版本化、租户鉴权
消费方 SLA：发布对照秒级 / CI 批量 / 周报异步
```
