---
title: "[DF-097] 云原生·service（K8s）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 云原生 · service（K8s）

- **事实**：K8s：Pod（实例）+Service（稳定虚拟 IP+负载均衡）+Deployment（副本管理）+ConfigMap/Secret（配置）
- **原理**：服务发现内建（Service DNS），滚动发布/自愈（探针）声明式，Java 应用适配：优雅停机（preStop）、探针配置（liveness 不做重检查）
- **常见误区**：
  1. K8s 需要额外注册中心（Service 已内建）（错）
  2. Pod IP 稳定（错）
  3. liveness 探针随便配（错）
- **工程用法**：云原生运行时
- **版本锚点**：实战共识
