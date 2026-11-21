---
title: [NODE-374] Node 服务容器化与 K8s 适配（探针/资源/就绪）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-374：Node 服务容器化与 K8s 适配
**答**:
- 镜像工程：多阶段构建（build 层与 runtime 层分离）、基础镜像固定 tag + 定期升级（NODE-364）、非 root 用户运行、NODE_ENV=production 只装生产依赖、镜像签名与漏洞扫描进 CI。
- 探针：liveness（进程活着——只查进程自检，不查依赖！依赖挂了 liveness 重启会雪崩）、readiness（可接流量——检查依赖（DB/Redis）与预热完成）、startup（慢启动保护，避免初始化期间被 liveness 杀）。
- 资源：requests/limits 依据压测（NODE-373）设定——Node 的 limit 过低会导致 OOMKilled（heap 与容器内存关系：--max-old-space-size < limit 留余量给 native/Buffer）。
- 优雅关闭对接：SIGTERM 处理（NODE-351）+ terminationGracePeriodSeconds 匹配；滚动更新 maxUnavailable 控制。
- 单 Pod 单进程策略：Node 进程数 = 1（K8s 副本承担水平扩展），避免容器内 cluster 的资源对齐复杂度。
```yaml
livenessProbe: { httpGet: { path: /healthz, port: 3000 }, periodSeconds: 10 }   # 只查自检
readinessProbe: { httpGet: { path: /readyz, port: 3000 }, periodSeconds: 5 }    # 查依赖
resources:
  requests: { cpu: 500m, memory: 512Mi }
  limits:   { cpu: '2',  memory: 1Gi }
# Node 启动参数: node --max-old-space-size=768 server.js   # < limit 1Gi，留 native 余量
```
