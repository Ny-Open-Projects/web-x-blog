# 04.Kubernetes基本架构与常用术语

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\04.Kubernetes基本架构与常用术语_【海量资源尽在 ubkz.com】.mp4
- 时长 10分36秒（音频 636s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们介绍一下Kubernetes的基本架构以及一些常用的术语。
[00:06] Kubernetes集群包含有节点代理,Kubernetes和Master。
[00:12] 它的一切都是基于这种分布式的存储系统。
[00:14] 下面这张图就是关于Kubernetes的一些基本架构。
[00:18] 大家刚才看到的节点代理就是指的我们当前的Kubernetes Proxy,还有我们的Kubernetes。
[00:26] 整个左边这部分其实是Master。
[00:29] 那在这张图里边呢,我们看到了我们是把服务啊,分为什么运行在工作节点上的服务和组成集群级别控制板的服务,也就是说大家看到的右边这部分就是我们的工作在节点上服务,我们也管它叫做node节点,而左边这部分呢,其实就是整个的master。
[00:47] 那我们Kubernetes节点呢,有运行应用容器必备的服务,这些呢都是受master控制的,那就是说我们的所有的node都是受master控制。
[00:59] 每个节点上都要运行我们的Docker,在我们的每个node上都有Docker,Docker是负责我们的具体的image的下载和运行。
[01:09] ChromeLines主要由以下几个核心的主件组成,首先第一个叫ETCD,它是保存整个集群的状态,在这里边我们看到的这一部分就是我们的ETCD,它是保存整个状态的。
[01:22] 然后还有一个叫API Server,它是提供资源操作的唯一入口。
[01:27] 认证啊授权的访问控制API辐射和发现等机制那你看到的这一部分其实就是我们的一个发现服务然后还有一个是叫做Controller Manager它是负责维护集群的状态我们的比如故障检测呀自动扩展的滚动更新那在这张图里边我们当前的这一部分就是我们的Controller还有呢再往下看ScheduleSchedule的一看这个名字你就应该知道它是负责我们的资源调度的对吧
[01:55] 那在这个图里边,我们这一部分就是我们的schedule。
[01:59] container runtime是负责竞现管理以及pod和容器的真正运行,还有一个是coupon proxy,刚才我们已经看到了。
[02:10] 它是负责我们Service提供cluster内部的服务发现和负载的。
[02:15] 那除了这些合音主件呢,还有一些推荐的主件,大家可以自己去看一看。
[02:20] 那这些呢,我们在后面的高级课程里面会讲解。
[02:23] 那整个Combinance它设计的理念和功能其实就是一个类似于Linux的分层架构,它的核心层就是Combinance最核心的功能,对外提供API的构建高层的应用,对内提供这种插件式的应用执行环境,然后应用层就是我们这种部署和路由,还有管理层系统的质量,基础设施,容器和网络的质量,还有自动化,自动的扩容等等。
[02:47] 还有这个接口城那么Kubernetes CTL命令行工具客户端SDK那后续我们在做这个练习的时候我们就可以用到这个Kubernetes CTL那它的生态系统是在接口城之上的庞大容器机群管理调度生态系统可以分为以下两个范畴Kubernetes内部的和Kubernetes外部的那刚才跟大家在这里面提到说我们这个里面提到一个叫Cluster对吧那这Cluster指的是什么呢
[03:16] Cluster其实是我们的计算存储和网络资源的一个集合,Compliance是利用这些资源运行各个机器容器的应用,那整个Compliance cluster是由master和node组成,也就是说我们刚才看到的整个这张图里面,它其实整个我们都叫做什么呢?
[03:35] Cluster,那么节点上运行的若干的Compliance服务,那刚才我们也提到说我们整个Compliance集群,也就是说它这里边架构呢?
[03:45] 我们分成master和node对吧那master它干什么的呢master主要职责是调度即决定将应用放在哪运行master运行linux系统可以是物理机或者是虚拟机master是我们整个community cluster的一个大脑运行着我们devel的服务包括了cooper api servercooper schedulecooper Controller然后我们的etc和pod网络
[04:13] 那刚才你在这张图里面其实也看到了,我们这里边也有server,有我们的manager,有我们的schedule,还有我们的etc等等。
[04:23] 那在这里大家看一下,刚才我们提到的说master里面包含这几部分,那这几部分分别具体功能,像我们的api server,那api server呢,它是提供这种http的RESTful的api,那即是我们的kubernetes的api。
[04:39] 那是Chromlet里所有资源CRUD就是增长改查等操作的唯一入口也是我们整个集群控制的一个入口那Schedule呢我们说过了它是一个负责我们资源调度的它决定了是将Pod放在哪个Node上运行那这里面提到一个PodPod呢后续我们会去把它去讲解一下Pod呢这里面其实大家看到了它就是我们整个Chromlet里面的最小的一个单元啊
[05:06] 那ControllerManager他是所有资源对象的一个自动化控制中心那ControllerManager呢负责管理我们class各种资源也就是他相当于一个大管家那这些资源保证我们这些资源呢处于这种预期的状态我们不同的Controller管理不同的资源如我们这个ReplaceController他是管理我们的Deployment然后呢什么StatefulSite呀DemoSite等等
[05:32] 那我们还有个ETCD,那ETCD呢,它是负责保存我们Kubernetes cluster配置信息和各种资源状态信息,当数据发生变化时呢,ETCD呢会快速的通知我们这个Kubernetes相关的主架,还有个POD网络,它呢是干什么呢,保障我们这个部署的POD网络,然后保障我们相互之间的POD中的通信,那这是整个master,master其实就是一个核心的控制,
[06:00] 那Node刚才我们说过Node其实是真正做事的那除了Master以外呢Kubernetes机器中其他的这个机器都成为Node节点Node的职责就是运行我们的容器我们的容器呢就是跑到我们的具体的镜像Node是由Master管理的Node呢负责我们监控并汇报容器的状态同时根据Master的要求管理容器的寿命周期Node也是运行在我们的Linux系统上
[06:25] 在Node节点上运行的一些相关的主架,我们在这张图里面其实也看到了,我们Node里面有Kubernetes还有Proxy。
[06:34] 大家看一下Kubernetes还有Proxy。
[06:37] Kubernetes是负责Po的对应的容器的创建,启动的。
[06:41] 同时也是Maths.mygc这个协作的实现我们集群的管理。
[06:46] Proxy你看这个名字你就知道它是一个代理,它是保证我们Kubernetes Server的通信以及负载等。
[06:54] 还有一个是DAO科引擎,也就是刚才我们在这张图里面,其实你发现Proxy,我们的Kubernetes其实还有个DAO科引擎,这是我们Node,那我们再来看看Pod,Pod它是我们Kubernetes的一个最小的单元,在这张图里面大家发现了,我们这里面是不是都是一个个Pod对吧,那这是我们当前Kubernetes的这个技术里面,它最核心或者说最有特色的一点,
[07:22] 那Pod是Kubernetes最小单元也是最重要和最基本的概念每个Pod包含一个或多个容器Pod里边你可以去有一个容器或者是多个那Pod容器会作为整体被master调到我们的node运行Kubernetes为每个Pod分配唯一的IP地址称为Pod IP一个Pod有多个容器互相的Pod IP地址在Kubernetes里边一个Pod的容器与另外组织上Pod容器之间是能够直接通信的
[07:52] 这点大家知道,Pod和Pod之间是可以直接通信的,它不局限于说我们是在不同的主机上。
[07:59] 所以在这张图里面大家看到了你这个Pod,那这些Pod它是可以互相通信的。
[08:06] 那还有一个概念就是Service,Service刚才我们其实提到了,它是外界访问我们一定一组特定的Pod的唯一的方式,或者说指定的那么一个服务。
[08:19] 那Service有自己的IP和端口,它也有自己的IP和端口,跟Code不一样。
[08:24] 那Service为Code提供了负载,它提供了简单的这些负载操作,它与Crumulize最核心的资源对象之一,然后每个Service其实就是我们经常提到的V服务架构中的一个V服务。
[08:36] 那大家知道一下就是我们的Crumulize跟我们的V服务其实是紧密相连的。
[08:41] 那最后一个叫做Replication Controller,那Replication Controller简称我们叫做RC。
[08:49] 那Kubernetes系统中的核心概念之一,它其实是定义了一个期望的场景,即声明某种POD的副本数量在任何时刻都符合某个预期,所以POD定义了以下的一些内容,大家看一下,POD期待的副本数,那我们之前呢,在去定义我们当前的这个replication的时候,其实看到有一个叫replicase,它写个2,这就是说我们可以去控制我们当前的一个副本数。
[09:17] 然后呢,用于筛选目标POD的Label Selector,那刚才你看到这里边,我们的Label Selector,这里边可以去通过我们设置我们的标签,然后还有呢,POD的副本数量小于一期时,用于创建POD的一个POD模板,刚才我们指定这个副本数时,当你把某一个POD干掉时,它会自动的去创建我们这个POD的模板,那在大多数情况下,我们可以通过一个RC实现POD的创建过程,以及副本数量的自动控制,
[09:46] 那简单说就是只要我创建了这个一个RC其实我就可以设置我们的镜像啊以及我们的这个副本数量以及它这个最小的这个数量还有呢RC里面包括完整的一个POD定义的模板RC通过Label Select机制实现对POD副本的自动控制也就是说整个这个RC啊对于我们来说是比较重要的它呢定义了我们一个期望的一个运行的一个场景并且呢规范了我们整个POD的一个数量
[10:16] 那这是对我们当前这个Crumeless的一个基本架构的介绍,以及我们一些常用术语,其实我们这里边这个关于一些常用的术语啊,还有很多,那我们先了解到这儿,后续我们在高级课程里边呢,再去介绍一些相关的这些术语。

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
  - Controller manager负责维护集群的状态，比如故障检测、自动扩 展、滚动更新等；
  - scheduler负责资源的调度，按照预定的调度策略将Pod调度到相应的机器上；
  - kubelet负责维护容器的生命周期，同时也负责Volume (CV) 和网络 (CN) 的管理；
  - Container runtime负责容器镜像管理及Pod和容器的真正运行（CRI）；
  - kube-proxy负责Service和cluster内部的服务发现和负载均衡。

画面 4:
- 与画面 3 内容基本一致，仅鼠标位置不同。
- 展示 Kubernetes 核心组件列表：
  - etcd保存了整个集群的状态；
  - apiserver提供了资源操作的唯一入口，并提供认证、授权、访问控制、API注册和发现等机制；
  - Controller manager负责维护集群的状态，比如故障检测、自动扩 展、滚动更新等；
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
  - Master主要职责是调度，即决定将应用放在哪运行。Master运行Linux系统，可以是物理机或虚拟机。Master是Kubernetes Cluster的大脑，运行着的Daemon服务包括kube-apiserver、kube-scheduler、kube-Controller-manager、etcd和Pod网络。
  - API Server (kube-apiserver)：提供HTTP/HTTPS RESTful API，即Kubernetes API，是Kubernetes里所有资源的CRUD等操作的唯一入口，也是集群控制的入口进程。
  - Scheduler (kube-scheduler)：负责资源调度的进程，简单说，它决定将Pod放在哪个Node上运行。

画面 8:
- 与画面 7 内容基本一致，仅鼠标位置不同。
- 展示 1.2.1 Master 的详细内容：
  - Master主要职责是调度，即决定将应用放在哪运行。Master运行Linux系统，可以是物理机或虚拟机。Master是Kubernetes Cluster的大脑，运行着的Daemon服务包括kube-apiserver、kube-scheduler、kube-Controller-manager、etcd和Pod网络。
  - API Server (kube-apiserver)：提供HTTP/HTTPS RESTful API，即Kubernetes API，是Kubernetes里所有资源的CRUD等操作的唯一入口，也是集群控制的入口进程。
  - Scheduler (kube-scheduler)：负责资源调度的进程，简单说，它决定将Pod放在哪个Node上运行。

画面 9:
- 展示 1.2.2 Node 的内容：
  - Controller Manager (kube-Controller-manager)：所有资源对象的自动化控制中心，Controller Manager负责管理Cluster各种资源，保证资源处于预期的状态。Controller Manager有多种，如replication Controller、endpoints Controller、namespace Controller、serviceaccounts Controller等。
  - 不同的Controller管理不同的资源，如replication Controller管理Deployment、StatefulSet、DaemonSet的生命周期，namespace Controller管理Namespace资源。
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

