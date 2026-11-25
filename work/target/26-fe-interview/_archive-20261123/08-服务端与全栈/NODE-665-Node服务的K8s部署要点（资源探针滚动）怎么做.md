---
title: [NODE-665] Node 服务的 K8s 部署要点（资源/探针/滚动）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## NODE-665：K8s 部署要点怎么做？
**答**：
- 资源配置：requests（调度依据——按稳态用量）与 limits（上限——Node 堆要与 limit 对齐：max-old-space-size ≈ limits.memory × 0.75——容器 OOMKill 前先让 GC 工作）；CPU limit 的节流问题（Node 事件循环被 CPU limit 节流造成延迟毛刺——多数团队去掉 CPU limit 或只留 request）。
- 探针三件套：liveness 极简/readiness 查依赖/startup 保护慢启动（SCN-NODE-664）。
- 滚动发布：maxSurge/maxUnavailable（平滑换版——配合优雅关闭 SCN-NODE-638 与 preStop）；发布风暴的 PDB（PodDisruptionBudget——最少存活副本）。
- 有状态与无状态：Node 服务无状态化（内存状态外置——SCN-NODE-637 集群状态原则的 K8s 版）；单例任务的 StatefulSet + leader election。
- 追问钩子：为什么「Node 堆大小要与容器 memory limit 对齐」——limit < 堆时：GC 还没来得及回收就被 cgroup OOMKill（内核先杀，V8 不知道）；limit >> 堆时：内存浪费；公式 max-old-space-size = limit × 0.75（留 25% 给堆外/Buffer/栈）——V8 与 cgroup 的「内存视图对齐」是容器化 Node 的第一配置。

```yaml
resources:
  requests: { memory: "1Gi", cpu: "500m" }
  limits: { memory: "1.5Gi" }                          # 不设 cpu limit（节流毛刺）
env:
  - { name: NODE_OPTIONS, value: "--max-old-space-size=1150" }   # 1.5Gi × 0.75
strategy:
  rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }    # 平滑滚动
lifecycle: { preStop: { exec: { command: ["sleep", "5"] } } }   # 摘流缓冲
```
