# 画面线理解：04.Kubernetes基本架构与常用术语

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\04.Kubernetes基本架构与常用术语_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:49, 01:30, 01:59, 02:47, 03:27, 03:49, 04:24, 05:22, 06:30, 07:15, 09:00, 09:40, 10:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:37:28

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 集群的基本概念、架构组成及核心组件，包括 Master、Node、Pod、Service 和 Replication Controller。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示 Kubernetes 架构图，包含 Master、Node、Pod、Docker、etcd、Kubelet、Kube-proxy 等组件。
- 文字说明：“在这张系统架构图中，我们把服务分为运行在工作节点上的服务和组成集群级别控制板的服务。”
- 底部文字：“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”
- 底部文字：“黑马程序员 传智播客旗下 高薪IT教育品牌 改变中国IT教育，我们正在行动”

画面 2:
- 与画面 1 内容基本一致，仅鼠标位置不同。
- 文字说明：“在这张系统架构图中，我们把服务分为运行在工作节点上的服务和组成集群级别控制板的服务。”
- 底部文字：“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”
- 底部文字：“黑马程序员 传智播客旗下 高薪IT教育品牌 改变中国IT教育，我们正在行动”

画面 3:
- 展示 Kubernetes 核心组件列表：
  - etcd保存了整个集群的状态；
  - apiserver提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制；
  - controller manager负责维护集群的状态，比如故障检测、自动扩 展、滚动更新等；
  - scheduler负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上；
  - kubelet负责维护容器的生命周期，同时也负责Volume (CV) 和网络 (CN) 的管理；
  - Container runtime负责容器镜像管理及Pod和容器的真正运行（CRI）；
  - kube-proxy负责Service和cluster内部的服务发现和负载均衡。

画面 4:
- 与画面 3 内容基本一致，仅鼠标位置不同。
- 展示 Kubernetes 核心组件列表：
  - etcd保存了整个集群的状态；
  - apiserver提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制；
  - controller manager负责维护集群的状态，比如故障检测、自动扩 展、滚动更新等；
  - scheduler负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上；
  - kubelet负责维护容器的生命周期，同时也负责Volume (CV) 和网络 (CN) 的管理；
  - Container runtime负责容器镜像管理及Pod和容器的真正运行（CRI）；
  - kube-proxy负责Service和cluster内部的服务发现和负载均衡。

画面 5:
- 展示 Kubernetes 的分层架构：
  - 核心层：Kubernetes最核心的功能，对外提供API向构建高层的应用，对内提供插件式应用运行环境。
  - 应用层：部署（无状态应用、有状态应用、批处理任务、集群应用等）和路由（服务发现、DNS解析等）。
  - 管理层：系统度量（如基础设施、容器和网络的度量），自动化（如自动扩展、动态Provision）以及策略管理（RBAC、Quota、PSP、NetworkPolicy等）。
  - 接口层：kubect令进行工具、客户端SDK以及集群联邦。
  - 生态系统：在接口层之上的庞大容器集群管理调度的生态系统，可以划分为两个范畴：
    - Kubernetes外部：日志、监控、配置管理、CI、CD、Workflow、FaaS、OTS应用、ChatOps等。
    - Kubernetes内部：CRI、CNI、CVI、镜像仓库、Cloud Provider、集群自身的配置和管理等。
- 展示 1.2.1 Cluster 和 1.2.1 Master 的标题。

画面 6:
- 与画面 5 内容基本一致，仅鼠标位置不同。
- 展示 Kubernetes 的分层架构：
  - 核心层：Kubernetes最核心的功能，对外提供API向构建高层的应用，对内提供插件式应用运行环境。
  - 应用层：部署（无状态应用、有状态应用、批处理任务、集群应用等）和路由（服务发现、DNS解析等）。
  - 管理层：系统度量（如基础设施、容器和网络的度量），自动化（如自动扩展、动态Provision）以及策略管理（RBAC、Quota、PSP、NetworkPolicy等）。
  - 接口层：kubect令进行工具、客户端SDK以及集群联邦。
  - 生态系统：在接口层之上的庞大容器集群管理调度的生态系统，可以划分为两个范畴：
    - Kubernetes外部：日志、监控、配置管理、CI、CD、Workflow、FaaS、OTS应用、ChatOps等。
    - Kubernetes内部：CRI、CNI、CVI、镜像仓库、Cloud Provider、集群自身的配置和管理等。
- 展示 1.2.1 Cluster 和 1.2.1 Master 的标题。

画面 7:
- 展示 1.2.1 Master 的详细内容：
  - Master主要职责是调度，即决定将应用放在哪运行。Master运行Linux系统，可以是物理机或虚拟机。Master是Kubernetes Cluster的大脑，运行着的Daemon服务包括kube-apiserver、kube-scheduler、kube-controller-manager、etcd和Pod网络。
  - API Server (kube-apiserver)：提供HTTP/HTTPS RESTful API，即Kubernetes API，是Kubernetes里所有资源的CRUD等操作的唯一入口，也是集群控制的入口进程。
  - Scheduler (kube-scheduler)：负责资源调度的进程，简单说，它决定将Pod放在哪个Node上运行。

画面 8:
- 与画面 7 内容基本一致，仅鼠标位置不同。
- 展示 1.2.1 Master 的详细内容：
  - Master主要职责是调度，即决定将应用放在哪运行。Master运行Linux系统，可以是物理机或虚拟机。Master是Kubernetes Cluster的大脑，运行着的Daemon服务包括kube-apiserver、kube-scheduler、kube-controller-manager、etcd和Pod网络。
  - API Server (kube-apiserver)：提供HTTP/HTTPS RESTful API，即Kubernetes API，是Kubernetes里所有资源的CRUD等操作的唯一入口，也是集群控制的入口进程。
  - Scheduler (kube-scheduler)：负责资源调度的进程，简单说，它决定将Pod放在哪个Node上运行。

画面 9:
- 展示 1.2.2 Node 的内容：
  - Controller Manager (kube-controller-manager)：所有资源对象的自动化控制中心，Controller Manager负责管理Cluster各种资源，保证资源处于预期的状态。Controller Manager有多种，如replication controller、endpoints controller、namespace controller、serviceaccounts controller等。
  - 不同的controller管理不同的资源，如replication controller管理Deployment、StatefulSet、DaemonSet的生命周期，namespace controller管理Namespace资源。
  - etcd负责保存Kubernetes Cluster的配置信息和各种资源的状态信息。当数据发生变化时，etcd会快速通知Kubernetes相关组件。
  - Pod网络：Pod要能够相互通信，Kubernetes Cluster必须拥有Pod网络，flannel是其中一个可选方案。
- 展示 1.2.2 Node 的标题。

画面 10:
- 展示 Kubernetes 架构图，包含 Master、Node、Pod、Docker、etcd、Kubelet、Kube-proxy 等组件。
- 文字说明：“Kubernetes集群含有节点组件kubelet和Master组件(APIs, scheduler, etc.)，一切都基于分布式的存储系统。下面这张图是Kubernetes的架构图。”
- 底部文字：“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”
- 底部文字：“黑马程序员 传智播客旗下 高薪IT教育品牌 改变中国IT教育，我们正在行动”

画面 11:
- 展示 1.2.3 Pod 和 1.2.4 Service 的内容：
  - 1.2.3 Pod：Pod是Kubernetes的最小单元，也是重要和最基本的概念。每一个Pod包含一个或多个容器，Pod的容器作为一个整体被Master调度到一个Node上运行。Kubernetes为每个Pod都分配了唯一的IP地址，称为PodIP。一个Pod里的多个容器共享PodIP地址。在Kubernetes里，一个Pod里的容器与另外自主的Pod容器能够通信。
  - 1.2.4 Service：Kubernetes Service定义了外界访问一组特定Pod的方式。Service有自己的IP和端口，Service为Pod提供了负载均衡，它也是Kubernetes最核心的资源对象之一，每个Service其实就是我们经常提起的微服务架构中的一个“微服务”。
- 展示 1.2.5 Replication Controller 的标题。

画面 12:
- 与画面 11 内容基本一致，仅鼠标位置不同。
- 展示 1.2
