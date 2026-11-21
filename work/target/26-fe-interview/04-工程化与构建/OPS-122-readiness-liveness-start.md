---
title: [OPS-122] readiness/liveness/startup 三种探针对前端服务分别意味着什么？怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-122：readiness/liveness/startup 三种探针对前端服务分别意味着什么？怎么设计？
**答**：
- readiness：不就绪就摘流量——滚动更新、扩容、依赖抖动时防 502，是发布平滑的基石；检查要能反映"能处理请求"。
- liveness：只判断进程是否死锁/卡死，失败即重启；检查必须轻量且不依赖数据库等下游，否则下游抖动引发全量重启雪崩。
- startup：给冷启动慢的服务（Node 大依赖初始化）一个宽限期，覆盖 liveness 检查直至启动完成，避免"启动慢被误杀循环"。
- 纯静态 nginx 容器探针极简（探测端口 + 入口文件存在即可）；SSR/BFF 才需要精细设计。
- 反模式清单：liveness 查数据库、探针路径恰好做了重逻辑、failureThreshold 太小导致网络抖动就重启。

```yaml
# 前端 SSR 容器三类探针
spec:
  containers:
    - name: web
      image: registry.example.com/web-ssr:1.42.0
      startupProbe:                # 冷启动宽限：最多等 60s，期间不跑 liveness
        httpGet: { path: /healthz, port: 3000 }
        periodSeconds: 2
        failureThreshold: 30
      readinessProbe:              # 不就绪即摘流量：发布/扩容/依赖抖动时防 502
        httpGet: { path: /ready, port: 3000 }
        periodSeconds: 5
        timeoutSeconds: 2
        failureThreshold: 3
      livenessProbe:               # 只查进程活性，不碰数据库/下游，防雪崩重启
        httpGet: { path: /healthz, port: 3000 }
        periodSeconds: 10
        failureThreshold: 3
      # /healthz 只做进程与事件循环检查；/ready 可检查关键依赖（但失败只摘流量不重启）
```
