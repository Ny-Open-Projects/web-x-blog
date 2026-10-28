---
disableNunjucks: true
title: "1516 Pod 创建流程深挖：list-watch、调度细节与 Pending 排查 深挖"
date: 2026-10-10 08:54:50
categories: [Go面试题集]
tags: [Go面试题集]
---

> 覆盖源 15-16 全文的工程延伸：list-watch 机制为什么这样设计、调度两阶段（过滤+打分）、声明式层级的控制循环分工、Pending 卡壳的实测排查路径。主卡已给四棒主线，本附录做机制与实战四层深挖。

## 思路与架构

```text
Pod 创建全链路组件视角 (谁碰 etcd? 谁只 watch?)
├─ kubectl
│   └─ 只与 apiserver 说话 (HTTPS + 证书/令牌)
├─ kube-apiserver
│   ├─ 唯一的 etcd 读写方 (认证->鉴权->准入->落库)
│   └─ 对外提供 list-watch 长连接 (组件的"眼睛")
├─ kube-scheduler
│   ├─ watch: nodeName 为空的 Pod
│   ├─ 两阶段: 过滤(Predicates) -> 打分(Priorities)
│   └─ 动作: Binding 写 spec.nodeName [实测: 秒级完成]
├─ kubelet (每节点)
│   ├─ watch: nodeName == 本节点的 Pod
│   ├─ CRI 建容器 / CNI 配网络 / CSI 挂卷
│   └─ 状态回写 apiserver (永不直连 etcd)
└─ controller-manager
    └─ Deployment/RS 控制循环: 维持副本数, Pod 被删则补
```

## 方案取舍
- **list-watch vs 组件直连 etcd**：K8s 把 etcd 锁进 apiserver 一层，所有组件靠 watch API 长连接感知变更。代价是多一跳、事件有毫秒级延迟；换来**统一的认证鉴权、版本化资源对象、watch 断线重连即全量 resync**。若组件直连 etcd，鉴权模型要 reinvent 一遍，且 etcd 的 raft 写入会被高频轮询拖垮。与「一切经网关」的微服务边界思想同构 [经验]。
- **调度两阶段的取舍**：过滤阶段做**硬性裁剪**（资源不足、端口冲突、亲和性不满足、污点不容忍的节点直接出局）；打分阶段对幸存者**软性排序**（资源均衡、镜像本地性、亲和性权重）。先过滤后打分保证调度是 O(可用节点) 的局部计算，且过滤失败有明确原因可上报（`FailedScheduling` 事件会写明 predicate 名）——排障时这是第一线索 [经验]。
- **kubelet 重启 vs 控制器重建的两层保障**：Pod 内**容器**崩溃由 kubelet 按 `restartPolicy` 在节点内重启（始终健康检查的本层）；**Pod 对象**被删除/节点宕机由上层控制器（ReplicaSet）在别处重建新 Pod。两层各管各的故障域——「进程级自愈」和「对象级自愈」分开答，比笼统说「K8s 会自动恢复」精确得多 [经验]。
- **命令式 create vs 声明式 apply**：create 是一次性动作，重复执行报 AlreadyExists；apply 把 YAML 提交为期望状态，可反复对账。生产一律 apply/GitOps——因为控制循环的收敛语义只有声明式才能闭环，这与主卡「期望状态」的立论互为表里 [经验]。

## 答题技巧
- 主线答四棒接力，主动补一句「**只有 apiserver 碰 etcd**」——这一句就是区分背诵与理解的分水岭 [经验]。
- 用实测案例落地：k3d 环境里镜像拉不通时，`Scheduled` 事件照常出现、Pod 却停在 Pending（FailedCreatePodSandBox 反复刷屏）——**调度成功 ≠ 容器运行**，两阶段独立排障 [实测]。
- 被问「Pod 卡 Pending 怎么排查」→ `kubectl describe pod` 看 Events：无 Scheduled 事件查调度（资源/亲和性/污点），有 Scheduled 而 FailedCreatePodSandBox/ErrImagePull 查镜像与网络——一条 describe 分流两种病根 [实测]。
- 主动边界到 `1515-k8s-architecture`（组件全景与控制循环总述）、`1515-k8s.deep`（架构深挖）、`1512-docker-internals`（容器底座 namespace/cgroup——kubelet 经 CRI 调 runtime 做的正是这层事），构成「容器底座 → 编排调度」专题 [边界]。

## 细节与核心 API

**关键架构事实 + 排查命令：**

```bash
# 只有 apiserver 碰 etcd；所有组件靠 list-watch 长连接感知变更
kubectl describe pod <pod>   # 看 Events 分流两种病根：
#   无 Scheduled 事件 → 查调度(资源/亲和性/污点)
#   有 Scheduled + FailedCreatePodSandBox/ErrImagePull → 查镜像与网络
kubectl get events --sort-by=.lastTimestamp
```

**调度两阶段 + 两层自愈：**

```text
调度：过滤(Predicates 硬裁剪：资源/端口/亲和/污点) → 打分(Priorities 软排序：均衡/镜像本地性)
两层故障域：
  容器崩溃 → kubelet 按 restartPolicy 节点内重启（进程级自愈）
  Pod 对象删除/节点宕 → 上层 ReplicaSet 别处重建新 Pod（对象级自愈）
命令式 create(一次性) vs 声明式 apply(期望状态，可反复对账，生产 GitOps 用)
```
