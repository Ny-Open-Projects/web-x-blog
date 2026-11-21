---
title: [MFW-375→MFW-375] 健康检查的依赖深度分级（readiness 的合理半径）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→375：健康检查分级

**答**:
- 反模式：readiness ping 全部下游（第三方支付挂了→整站摘流——雪崩放大器）；liveness 里做 DB 查询（DB 抖动→全实例被 K8s 杀光——自杀循环）
- 分级协议：liveness=进程自证（<5ms 零外部依赖）；readiness=关键路径依赖（DB 主/KV——超时 200ms 快失败）；第三方依赖不进 readiness（进独立的 degradation 状态页供路由级降级决策 MFW-326）
- 语义联动：摘流时长上限（readiness 失败 >5min 自动升级人工——自动摘流不是无限免责）；启动顺序（init 未完成 ready=false——MFW-281 标志位对接）
- 演练：分别打挂 DB/KV/第三方，断言「哪些端点摘流、哪些只降级、页面哪些段变占位」——分级写错演练立刻现形

```text
分级：liveness 自证 <5ms / readiness=关键链 200ms 快失败 / 第三方→degradation 页不摘流
护栏：摘流 >5min 自动升级人工；三类依赖挂掉的行为差异必须演练断言
```
