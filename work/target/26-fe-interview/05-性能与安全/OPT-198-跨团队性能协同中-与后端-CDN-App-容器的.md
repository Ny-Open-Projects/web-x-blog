---
title: [OPT-198] 跨团队性能协同中，与后端/CDN/App 容器的责任边界怎么划？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-198：跨团队性能协同中，与后端/CDN/App 容器的责任边界怎么划？

**答**：
- 原则：按链路段划责任，每段有唯一 owner + SLA，接口处用"契约数据"说话（TTFB 归后端、命中率归 CDN、启动耗时归容器）。
- 后端：接口 P75 时延、批量聚合接口、缓存失效通知机制；前端：资源体积、加载策略、渲染效率；CDN：命中率、回源率、预热响应时长；App 容器（混合开发）：WebView 启动耗时、离线包命中率、JSBridge 调用耗时。
- 协同机制：季度"链路联席会"对 SLA 达成率；跨域问题（如容器预加载不触发前端埋点）有联合排障 runbook；优化需求走"性能工单"带预期收益与复测方式。
- 推动技巧：给对方团队的诉求带上他们 KPI 的关联（CDN 命中率是他们的核心指标，预热需求挂他们看板）。

```yaml
# 一一对应：跨团队责任边界 SLA 矩阵 + 工单模板
sla_matrix:
  backend:
    owner: 服务端网关组
    scope: [接口 P75 时延, 批量聚合接口提供, 缓存失效主动通知]
    sla: { core_api_p75: 300ms, batch_api_availability: "≥ 99.9%" }
    evidence: APM 链路追踪
  cdn:
    owner: 基础架构
    scope: [静态资源命中率, 回源率, 预热任务响应]
    sla: { hit_ratio: "≥ 95%", warmup_complete: "发布后 10min" }
    evidence: CDN 日志看板
  app_container:
    owner: 客户端组
    scope: [WebView 启动耗时, 离线包命中率, JSBridge P95]
    sla: { webview_boot_p75: 800ms, offline_pkg_hit: "≥ 90%" }
    evidence: 容器自身 APM（前端只报 JS 侧）
  frontend:
    owner: 前端各组
    scope: [资源体积预算, 加载策略, 渲染与交互性能]
    sla: { lcp_p75: 2.5s, inp_p75: 200ms }
    evidence: RUM

perf_ticket:                    # 跨团队优化工单模板
  to: cdn
  ask: 大促页面预热接口接入
  expected_gain: 首发用户 CDN HIT 从 40%→90%（见 OPT-149）
  verify: 预热后抽样 x-cache 校验脚本
  linked_kpi: 贵组命中率 SLA
```
