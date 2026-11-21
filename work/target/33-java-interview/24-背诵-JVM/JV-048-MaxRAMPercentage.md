---
title: "[JV-048] 参数·MaxRAMPercentage（容器）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · MaxRAMPercentage（容器）

- **事实**：容器内用 -XX:MaxRAMPercentage=70 之类按比例设堆而非绝对值
- **原理**：JDK8u191+/JDK10 默认感知 cgroup 限制（UseContainerSupport），按 Pod 内存比例留出堆外与元空间余量，写死 -Xmx 换节点规格就错
- **常见误区**：
  1. 容器内 JVM 默认使用宿主机全部内存（错）
  2. MaxRAMPercentage 默认值是 100（错）
  3. JDK8 任何版本都能感知容器（错）
- **工程用法**：K8s 部署 JVM 标配参数
- **版本锚点**：JDK10 与 8u191 引入容器感知
