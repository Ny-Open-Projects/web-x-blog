---
title: "Kubernetes 核心组件 本章小结"
date: 2026-10-04 04:20:00
categories: [kcna, Kubernetes]
tags: [Kubernetes, 本章小结, 控制平面, 节点组件, APIServer, controller-manager, etcd, scheduler, kubelet, kube-proxy, 资源对象, Pod创建流程]
disableNunjucks: true
---

# Kubernetes 核心组件 本章小结

最后对本章做一个小结。本章关于 K8s 核心组件以及运行机制原理等内容都是偏理论性的：一开始回顾了部署历史，然后看了 K8s 的架构图，清楚核心组件有哪些；之后用最多篇幅详细讲解了各核心组件的原理；最后用 Pod 创建和启动流程把部分组件串起来。

## 纲要

- 回顾部署历史与架构图
- 控制平面四大组件：APIServer / controller-manager / etcd / scheduler
- 节点两大组件：kubelet / kube-proxy
- K8s 几十种资源对象：简单与复杂并存
- 各核心组件原理回顾（建议回看课程）
- Pod 创建流程串起组件
- 带着问题去复习

## 控制平面与节点组件

```mermaid
flowchart TD
    subgraph 控制平面（master 节点）
        A["kube-apiserver"] --> E[("etcd")]
        CM["kube-controller-manager"]
        S["kube-scheduler"]
    end
    subgraph 常规集群节点
        K["kubelet"]
        P["kube-proxy"]
    end
    A --- CM
    A --- S
    K --- A
    P --- A
```

| 位置 | 组件 | 角色 |
| --- | --- | --- |
| **控制平面（master）** | **kube-apiserver** | 所有能力的入口，资源真相来源 |
| 控制平面 | **kube-controller-manager** | 自愈、扩缩容、故障转移的执行者 |
| 控制平面 | **etcd** | 持久化数据库，存所有集群状态 |
| 控制平面 | **kube-scheduler** | 给未调度 Pod 选最优节点 |
| **常规节点** | **kubelet** | 节点端核心组件：管 Pod 生命周期、上报状态 |
| 常规节点 | **kube-proxy** | Service 的负载均衡转发（本章未详讲，需自学） |

> 课程里特别提醒：**kube-proxy 本次课程没有详细讲解，大家可以自学补充了解。** 控制平面上这四大组件都运行在 master 节点上；常规节点上只有 kubelet 和 kube-proxy。

## 几十种资源对象：简单与复杂并存

看完核心组件，可能会觉得 K8s 挺简单；再看 K8s 有几十种资源对象，又会觉得它超级复杂 —— **这种感觉都很正常，要全面精通和掌握确实有困难**。但学习和使用中遇到问题，**记得来 K8s 官方文档查找，总会有新发现**。

```dir
本章知识落点
├── 部署历史回顾
│   └── 物理机 → 虚拟化 → 容器（标准集装箱）
├── 架构图：核心组件
│   ├── 控制平面：APIServer / controller-manager / etcd / scheduler
│   └── 节点：kubelet / kube-proxy
├── 各组件原理（重点篇幅）
│   ├── APIServer 原理
│   ├── controller-manager 原理
│   ├── scheduler 原理
│   └── kubelet 原理
└── 串起来：Pod 创建和启动流程
```dir

## 各核心组件原理回顾

本章最多篇幅都在讲各核心组件原理：

- **APIServer 原理**：对外接口服务，所有读写经它，是唯一写入口；
- **controller-manager 原理**：通过控制器模式实现自愈、扩缩容、故障转移；
- **scheduler 原理**：过滤 → 打分 → 绑定三阶段，以及抢占、驱逐、调度框架；
- **kubelet 原理**：节点端控制器模式（事件 + syncLoop），PLEG、PodWorkers、CRI 抽象。

> 课程原话说得很实在：**"相信大家听完这些原理到现在没隔多久，但肯定已经忘了大部分，全部忘了也很正常，毕竟理论性的东西不经过实践很容易忘记。"** 如果要应对面试或真遇到问题，**记得回到课程里再听一遍相关的内容，也许会有更深入的理解**。

## Pod 创建和启动流程：把组件串起来

最后讲了一遍 Pod 创建和启动流程：用户提交 PodSpec → APIServer 落 etcd → scheduler watch 后调度并绑定 → kubelet watch 后调容器运行时创建容器 → 上报状态回 etcd。通过这个例子，能对部分核心组件有更多了解。

## 带着问题去复习

本章内容偏理论，建议带着问题学习和复习，效果更好：

1. 控制平面四大组件分别是什么、各跑在哪类节点上？
2. 节点上只有哪两个核心组件？kube-proxy 本章讲了吗？
3. scheduler 的三阶段是哪三阶段？抢占与驱逐的区别？
4. kubelet 的控制循环由什么组成？为什么要有 CRI 这一层？
5. Pod 从提交到 Running，依次经过了哪些组件、各写了什么到 etcd？

## 总结

1. **本章定位**：核心是 K8s 核心组件与运行机制原理，偏理论；开头回顾部署历史，再看架构图认清核心组件，中间用最多篇幅讲各组件原理，最后用 Pod 创建流程串起组件；
2. **控制平面四大组件**：**kube-apiserver、kube-controller-manager、etcd、kube-scheduler，都运行在 master 节点上**；
3. **节点两大组件**：**kubelet 与 kube-proxy**；**kube-proxy 本章未详讲，需自学补充**；
4. **资源对象很多**：K8s 有几十种资源对象，"觉得简单又觉得复杂"都正常，全面精通有难度，但**遇到问题记得查官方文档**；
5. **原理易忘是正常的**：理论性内容不经过实践容易忘，**应对面试或排障时回到课程再听一遍，会有更深入理解**；
6. **四个组件原理**：APIServer（唯一入口）、controller-manager（自愈/扩缩容/故障转移）、scheduler（过滤/打分/绑定 + 抢占/驱逐/框架）、kubelet（节点控制器模式 + CRI 抽象）；
7. **Pod 创建流程的价值**：通过这个例子能对部分核心组件有更多了解，建议带着问题学习和复习以提高效果；
8. **后续安排**：本章之后会有 K8s 集群的多个相关内容与实操环节，欢迎一起学习和观看。
