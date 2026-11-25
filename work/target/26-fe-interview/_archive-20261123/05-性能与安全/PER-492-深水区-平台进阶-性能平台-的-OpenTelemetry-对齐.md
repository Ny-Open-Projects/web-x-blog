---
title: [PER-492] 与 OpenTelemetry 的对齐：RUM 数据模型的 OTel 化（trace/span/metric 映射）的收益与边界？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-492：RUM 数据模型的 OpenTelemetry 化映射？

**答**:
- 映射设计：CWV 指标 → OTel Metric（histogram）；页面加载/接口调用 → Span（navigation span 含资源子 span、接口 span 含 Server-Timing 属性）；慢交互 → Trace（交互 span 三段拆解为子 span）；会话 → Trace 上下文（traceId = sid）。对齐后前端数据可进统一可观测后端（与后端 APM 关联——用户点一下到后端 SQL 的全链路）。
- 收益：① 全链路关联——前端慢交互 trace 关联到后端接口 span，跨端归因（PER-257）从"分系统看"变"一条 trace 看完"；② 生态复用——OTel 采集器/存储/查询生态直接用（PER-420 自建决策的对齐项）；③ 厂商中立——换后端不换采集。
- 边界：CWV 的官方口径（分位数/p98 语义）与 OTel metric 模型的聚合语义有差异（OTel histogram 与 CWV 桶口径需适配）；浏览器 trace 的采样成本（全量 trace 太贵——trace 级采样独立于指标采样）。
- 落地节奏：指标层先对齐（成本最低收益直接），trace 层按需（慢交互场景采样开启）。

```text
RUM → OTel 映射：
CWV → Metric(histogram)；页面/接口 → Span（含 Server-Timing 属性）
慢交互 → Trace（三段子 span）；会话 → traceId = sid
收益：前端→后端全链路 trace（PER-257 跨端归因升级）；OTel 生态复用；厂商中立
边界：CWV 分位数语义与 OTel histogram 聚合适配；trace 采样独立控制（全量太贵）
节奏：Metric 层先对齐（低成本高收益）→ Trace 层按需
```
