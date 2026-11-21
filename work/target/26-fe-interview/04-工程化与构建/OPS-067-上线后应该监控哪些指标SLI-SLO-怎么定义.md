---
title: [OPS-067] 上线后应该监控哪些指标？SLI/SLO 怎么定义？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-067：上线后应该监控哪些指标？SLI/SLO 怎么定义？
**答**：
- 四类核心指标：可用性（页面可打开率）、错误（JS 错误率、接口错误率）、性能（LCP/INP/CLS、接口 P95）、业务（转化率、核心动作成功率）。
- SLI 是测量值（如"首页加载成功请求占比"），SLO 是目标（如 99.9%），错误预算（1-SLO）决定发布节奏的松紧。
- 指标必须有基线：没有基线就没有"异常"，发布后的对比对象是发布前 7 天同指标。
- 指标要分层到域名/页面/版本号维度，否则全站平均会掩盖单页面劣化。

```yaml
# sli-slo.yaml：前端 SLI/SLO 定义（监控平台配置的声明式表达）
service: web-mall
slis:
  page_availability:
    description: 首页与核心页可正常渲染的会话占比
    metric: dial_test_ok / dial_test_total
    dimensions: [page, region]
  js_error_rate:
    description: JS 错误会话占比（含 window.onerror 与 unhandledrejection）
    metric: error_sessions / total_sessions
    dimensions: [version, page]
  api_success_rate:
    description: 核心 API 2xx 占比
    metric: api_2xx / api_total
    dimensions: [api, upstream]
  web_vitals:
    description: 用户体验指标
    metrics: { LCP: p75, INP: p75, CLS: p75 }
    dimensions: [page, device_type]
slos:
  page_availability: 99.9%
  js_error_rate: <0.5%       # 会话口径
  api_success_rate: 99.95%
  LCP_p75: <2.5s
error_budget:               # 错误预算：耗尽则冻结非紧急发布
  window: 28d
  page_availability_budget: 0.1%
  policy: budget 剩余 < 25% 时，仅允许 P0/P1 修复类发布
dashboards:
  release: https://grafana.example.com/d/web-release   # 发布对比大盘
  business: https://grafana.example.com/d/web-biz
```
