---
disableNunjucks: true
title: "Kubernetes 认证考点: Pod 创建和启动流程 —— 一条命令背后所有组件的握手"
date: 2026-10-02 02:45:00
categories: [kcna, Kubernetes]
tags: [Pod, 创建流程, watch, 绑定, 调度, kubelet, 容器运行时, 健康检查, 驱逐, CRI]
---

# Kubernetes 认证考点: Pod 创建和启动流程 —— 一条命令背后所有组件的握手

这一节通过**一个典型的执行过程**，把前面讲过的核心组件串起来：涉及 kubectl、APIServer、etcd、scheduler、kubelet、容器运行时（docker/containerd）；**回顾一下讲过的 K8s 核心组件，只剩下 controller-manager 和 kube-proxy 没有在流程里体现 —— 其实只是这个流程没体现出来，所有的组件在 K8s 的各类操作中或多或少都会用到。**

结论：**用户用 kubectl 或 API 客户端提交 PodSpec 给 APIServer → APIServer 把 Pod 对象的初始化信息存入 etcd 并返回确认 → 各组件用 watch 机制跟踪资源变动 → scheduler 通过 watch 发现新 Pod 且未绑定节点，按资源需求过滤、打分、选出最合适节点并绑定回写 APIServer（再落 etcd）→ 目标节点上的 kubelet 通过 watch 发现要绑到自己节点的 Pod，调用容器运行时创建并启动 Pod 和容器 → 容器启动成功后 kubelet 把 Pod 与容器状态更新到 APIServer（落 etcd 后返回确认）。**

## 纲要

- 涉及哪些组件
- 完整七步：从 kubectl 到 Running
- 一张时序图
- 为什么每步都要"写 etcd + watch"
- 课后三问：探针、驱逐、容器运行时

## 涉及哪些组件

```mermaid
flowchart LR
    K["kubectl"] --> API["kube-apiserver"]
    API --> ETCD[("etcd")]
    API --> SCH["kube-scheduler"]
    API --> KL["kubelet（节点上）"]
    KL --> RT["容器运行时<br/>docker / containerd"]
    SCH --> ETCD
    KL --> ETCD
```

| 组件 / 工具 | 在流程里的角色 |
| --- | --- |
| **kubectl** | 用户提交 PodSpec 的入口（或任何其他 API 客户端） |
| **APIServer** | **K8s 对外的接口服务**，所有写与读都经它 |
| **etcd** | **K8s 的持久化数据库** |
| **kube-scheduler** | **调度器**：选节点、绑定 |
| **kubelet** | **普通集群节点上的核心组件**：建 Pod、起容器、回状态 |
| **容器运行时** | **容器运行与管理工具**（docker / containerd） |
| （controller-manager、kube-proxy） | 本流程没直接体现，但几乎所有操作都会用到 |

## 完整七步

1. **用户要创建一个 Pod，可以通过 kubectl 或其他 API 客户端提交 PodSpec 给到 APIServer，告知需要创建 Pod**；
2. **APIServer 尝试着将 Pod 对象的初始化信息存入 etcd 中，待写入操作执行完成，APIServer 就会返回确认信息给到客户端**；
3. **所有的 K8s 组件都是用 watch 机制来跟踪检查 APIServer 上资源的变动 —— kube-scheduler 通过其 watch 发现 APIServer 创建了新的 Pod 对象，而且还没有绑定到任何集群节点上**；
4. **kube-scheduler 根据 Pod 资源需求规格，经过集群节点过滤找到可调度节点，并且给这些节点打分，最后为 Pod 对象挑选一个最合适的工作节点，然后将这个 Pod 与节点的信息绑定、更新到 APIServer**；
5. **同样的，APIServer 收到这个绑定对象会写入到 etcd 数据库中**；
6. **此时这个 Pod 要绑定的目标节点上的 kubelet 通过 watch 机制发现有需要绑定的新的 Pod；于是这个节点上 kubelet 就会开始尝试在当前节点上调用容器运行时来创建 Pod 和启动容器**；
7. **最后等容器启动成功后，kubelet 将 Pod 和容器的状态信息更新到 APIServer 中，在 etcd 确认写入操作完整后，APIServer 将返回确认信息给到 kubelet —— 这就是 Pod 创建和启动流程完成了。**

```mermaid
sequenceDiagram
    autonumber
    participant U as 用户 / kubectl
    participant API as kube-apiserver
    participant E as etcd
    participant S as kube-scheduler
    participant K as kubelet
    participant R as 容器运行时
    U->>API: 提交 PodSpec（创建 Pod）
    API->>E: 写入 Pod 初始化信息
    E-->>API: 写入完成
    API-->>U: 返回确认
    Note over S: 通过 watch 发现：新 Pod 且未绑定节点
    S->>S: 过滤 + 打分 → 选最合适节点
    S->>API: 绑定：Pod → Node
    API->>E: 写入绑定信息
    E-->>K: 目标节点 kubelet 通过 watch 发现新 Pod
    K->>K: 生成 PodSpec、准备 volume
    K->>R: 调用容器运行时（CRI）创建并启动容器
    R-->>K: 容器已启动
    K->>API: 上报 Pod / 容器状态
    API->>E: 写入状态
    E-->>API: 写入完成
    API-->>K: 返回确认
```

## 为什么每步都是"写 etcd + watch"

**这个流程有个反复出现的 pattern：每一次状态变化都是"组件写 APIServer → 落 etcd → 别人 watch 到 → 再接手"。**

```text
组件之间不直接调用，全部经由 APIServer 中转
kubectl ──写──> apiserver ──写──> etcd
                    │
                    ├── watch(发现新Pod) ──> scheduler ──写绑定──> apiserver ──> etcd
                    └── watch(发现待绑Pod) ─> kubelet ──写状态──> apiserver ──> etcd
```

三个推论（考试与排障都用得着）：

- **组件无点对点调用** —— 所以"某步没做"要往"谁没 watch 到"上排查；
- **APIServer 是唯一写入口** —— 组件只能改 etcd 里的数据，不能直接写；
- **状态永远从 etcd 出发** —— 任何一步中断，恢复后组件从 etcd 的当前状态继续收敛。

## 课后三问

**现在知道了 Pod 创建和启动流程，现实中还有很多操作，只要稍微变化一下，整个过程也会有变化。**

```mermaid
flowchart TD
    Q1["问题一：Pod 容器的健康检查有哪些探针，有哪几种实现方式？<br/>整段过程会涉及哪些核心组件，完整过程是怎样的？"] --> A1["startupProbe / readinessProbe / livenessProbe<br/>探针失败 → kubelet 重启或摘流量"]
    Q2["问题二：Pod 驱逐是怎么做到的？驱逐后怎么保证服务还能正常访问？"] --> A2["节点压力驱逐 / 抢占<br/>控制器重建 Pod，Service 转发到健康实例"]
    Q3["问题三：容器运行时是 K8s 的一个接口规范"] --> A3["CRI：containerd / CRI-O<br/>镜像与容器管理"]
```

1. **问题一**：**Pod 容器的健康检查有哪些探针，有哪几种实现方式？整段过程又会涉及到哪些核心组件，完整过程是怎样的？**
2. **问题二**：**前面提到过 Pod 驱逐是怎么做到的？驱逐之后是怎么保证服务可以正常运行和访问的？整个过程能否尽可能完整地描述一下？**
3. **问题三**：**容器运行时是 K8s 的一个接口规范，课程中没有详细讲解，可以再找资料了解，毕竟镜像和容器管理也是非常重要的。**

## API 速览

| 步骤 | 谁在做 | 写到哪 | 谁 watch 到 |
| --- | --- | --- | --- |
| 提交 PodSpec | 用户 / kubectl → APIServer | etcd（初始化信息） | 客户端拿到确认 |
| 发现新 Pod | **kube-scheduler（watch）** | — | — |
| 过滤 + 打分 + 选节点 | **kube-scheduler** | — | — |
| **绑定 Pod → Node** | **kube-scheduler → APIServer** | **etcd（绑定对象）** | 目标节点 kubelet |
| 创建并启动容器 | **kubelet → 容器运行时（CRI）** | 节点本地 | — |
| 上报状态 | **kubelet → APIServer** | **etcd（状态信息）** | 控制器 / scheduler |

## Demo 示例

把七步逐段打点观测：

```bash
# 先给变量赋值，例如：POD=$(kubectl get pod -o jsonpath='{.items[0].metadata.name}')
# ① 步骤 1-2：提交并落库
kubectl apply -f pod-demo.yaml
kubectl get pod $POD --show-managed-fields -o yaml | head -40

# ② 步骤 3-5：scheduler 还没绑定时（比如无可用节点），nodeName 为空
kubectl get pod $POD -o jsonpath='{.spec.nodeName}'   # 空 = 未调度
kubectl describe pod $POD | grep -A5 -i events        # FailedScheduling

# ③ 步骤 6：kubelet 在本地拉起容器（看事件顺序：Pulled → Created → Started）
kubectl describe pod $POD | grep -i -E "pulled|created|started|scheduled"

# ④ 步骤 7：状态写回 etcd
kubectl get pod $POD -o jsonpath='{.status.phase}'    # Running
kubectl get --raw /api/v1/namespaces/default/pods/$POD

# ⑤ 全程 watch：另一终端挂着看，本终端反复 apply/delete
kubectl get pod -w
```

排障对应表：

| 症状 | 卡在哪一步 | 看什么 |
| --- | --- | --- |
| Pending 不动 | 步骤 4（调度） | `describe pod` 的 Events / `kubectl get events` |
| ContainerCreating 卡住 | 步骤 6（容器创建） | describe 的 Events、镜像是否可拉、volume 是否就绪 |
| Running 但不服务 | 步骤 7（状态与探针） | readinessProbe、Endpoints 是否挂上 |
| 重启次数涨 | 步骤 6-7（liveness 探活失败） | `kubectl get pod` 的 RESTARTS |

## 总结

1. **涉及组件**：**kubectl（命令行工具）、APIServer（K8s 对外的接口服务）、etcd（K8s 的持久化数据库）、scheduler（调度器）、kubelet（普通集群节点上的核心组件）、docker（容器运行时与容器管理工具）**；**回顾讲过的核心组件，只剩 controller-manager 和 kube-proxy 没在流程中体现，其实所有组件在 K8s 各类操作中或多或少都会用到**；
2. **第 1-2 步**：**用户通过 kubectl 或其他 API 客户端提交 PodSpec 给到 APIServer，APIServer 把 Pod 对象的初始化信息存入 etcd，写入完成后返回确认信息给客户端**；
3. **第 3 步**：**所有的 K8s 组件都是用 watch 机制来跟踪检查 APIServer 上资源的变动 —— kube-scheduler 通过 watch 发现 APIServer 创建了新的 Pod 对象且还没绑定到任何集群节点**；
4. **第 4-5 步**：**kube-scheduler 根据 Pod 资源需求规格，经过集群节点过滤找到可调度节点、给节点打分，挑选最合适的工作节点，把 Pod 与节点的信息绑定更新到 APIServer；APIServer 收到绑定对象会写入 etcd**；
5. **第 6 步**：**目标节点上的 kubelet 通过 watch 发现有需要绑定的新 Pod，就在这个节点上调用容器运行时来创建 Pod 和启动容器**；
6. **第 7 步**：**容器启动成功后，kubelet 将 Pod 和容器的状态信息更新到 APIServer，在 etcd 确认写入完整后 APIServer 返回确认给 kubelet —— 创建和启动流程完成**；
7. **这个流程很好记**：**涉及到的组件不多、步骤也不复杂，很容易记住**；现实中很多操作只要稍微变化一下，整个过程也会有变化；
8. **三道课后题值得自己答一遍**：**① Pod 容器的健康检查有哪些探针、有哪几种实现方式，完整过程涉及哪些核心组件；② Pod 驱逐是怎么做到的、驱逐之后怎么保证服务正常运行和访问、完整过程能否描述；③ 容器运行时是 K8s 的一个接口规范（CRI），需要自己再找资料深入了解**。

