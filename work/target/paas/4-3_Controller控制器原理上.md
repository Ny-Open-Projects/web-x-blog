# Go PaaS 平台开发: Controller 控制器原理（上）

## 纲要

- kube-controller-manager 内部包含众多 controller，负责集群的"自愈"与"期望状态"管理
- 六大核心控制器之一：**副本控制器（ReplicaSet）**，保证集群中始终存在 N 个 Pod 实例
- 基于副本数可实现**自动扩缩容**与**滚动升级**
- **资源配额控制器（ResourceQuota）**：在容器 / Pod / Namespace 三个层级限制 CPU 与内存的使用
- 控制器设计哲学：声明期望状态，由控制器持续将实际状态向期望状态收敛

## 控制器的作用

kube-controller-manager 是 K8s 的"管理控制中心"，内部包含大量 controller，例如：副本控制器、节点控制器、资源配额控制器、命名空间控制器、Endpoint 控制器等。它们的共同目标是：**不断比对"期望状态"与"实际状态"，把实际状态修复到期望值**。下面重点讲解与日常开发最相关的两类。

## 副本控制器与自愈

副本控制器（ReplicaSet，早期称 ReplicationController）的核心职责是：**确保集群中始终运行指定数量的 Pod 副本**。

例如我们在清单中声明某个 Pod 的副本数为 3。当集群中因为宕机或程序异常退出导致实际只剩 2 个副本时，副本控制器会自动扫描到"少了一个"，并在资源充足的其他节点上把 Pod 重新拉起，使总数恢复为 3。

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
```

基于副本数，还能实现两个非常重要的能力：

- **自动扩缩容**：业务高峰（如 CPU/内存平均使用率达到 80%）时，通过增加副本数把应用横向扩展出去应对大量请求；高峰过去后再把多余的副本回收，让资源最大化利用。在 PaaS 平台中，这通常通过 HPA（HorizontalPodAutoscaler）配置阈值来实现。
- **滚动升级**：线上有 3 个 Pod 同时运行时，更新程序不能让业务停服。滚动升级会先更新 1 个 Pod，待其健康后再逐步更新其余副本，全程保证服务持续可用。这正是副本控制器的核心职责之一。

## 资源配额控制器

资源配额控制器（ResourceQuota）负责**三层级的资源管理**：

1. **容器级别**：限制单个容器能使用的 CPU 与内存上限，防止某个容器把节点资源吃满。
2. **Pod 级别**：限制一个 Pod 内所有容器使用资源的总和。
3. **Namespace 级别**：限制某个命名空间（可理解为某个租户/项目）下可创建资源的总量，例如最多 12 核 24G。该命名空间下创建的任何资源都不会超出这个配额。

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-a-quota
  namespace: team-a
spec:
  hard:
    requests.cpu: "12"
    requests.memory: 24Gi
    limits.cpu: "12"
    limits.memory: 24Gi
```

为什么不把所有资源都给一个 Pod？因为当某个应用写出死循环时，会无节制地占用 CPU/内存，导致其他 Pod 被异常调度甚至被挤垮。通过资源配额预先分配，可以让一台 32 核 64G 的工作节点被不同的 Pod 合理使用，保障集群整体的稳定性。

> 说明：受讲稿篇幅所限，本节只展开了副本控制器与资源配额控制器两个最具代表性的控制器；kube-controller-manager 中还有节点控制器、服务控制器、Endpoint 控制器等，将在后续章节结合调度与网络逐步展开。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/k8s-install/check_host.sh`
- `code/课件/k8s-install/install_master.sh`
- `code/课件/go-paas-html/pages-404.html`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/go-paas-html/pages-login.html`
- `code/课件/k8s-install/base_install.sh`
- `code/课件/go-paas-html/pages-login2.html`
- `code/课件/k8s-install/k8s 安装指导说明.md`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：否。
