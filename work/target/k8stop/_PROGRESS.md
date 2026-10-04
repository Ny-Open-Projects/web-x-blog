# 3.k8s3-top → 博客 转换进度

状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、课程总结、本章未完结）
**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**

| 状态 | # | 组名 | 文件数 | 总字数 | 产出博客 |
| --- | --- | --- | --- | --- | --- |
| skip | 1 | 课时1：课程介绍 | 1 | 3955 | 导学「课程介绍」，无技术内容，跳过（按 SKILL 约定导学一律 skip） |
| done | 2 | 课时1：二进制Kubernetes升级说明 | 1 | 2752 | 10-1_二进制升级到1.19的版本策略与升级路径规划.md |
| done | 3 | 课时2：二进制Etcd集群升级 | 1 | 3268 | 10-2_etcd集群3.3到3.4的滚动升级与快照备份.md |
| done | 4 | 课时3：二进制Kubernetes 1.19升级说明 | 1 | 7158 | 10-3_Kubernetes-1.19变更点解读与升级前参数体检.md |
| done | 5 | 课时4：二进制Kubernetes升级Master组件 | 1 | 2288 | 10-4_Master控制面组件的逐台升级实操.md |
| done | 6 | 课时5：二进制Kubernetes升级Node和Calico | 1 | 6691 | 10-5_Node端kubelet升级与Calico网络插件版本校准.md |
| done | 7 | 课时6：二进制Kubernetes升级CoreDNS | 1 | 3483 | 10-6_CoreDNS从1.6.6升级到1.6.7的容器化流程.md |
| done | 8 | Kubeadm高可用安装基本说明 | 1 | 4886 | 2-1_kubeadm高可用安装的整体规划与环境设计.md |
| done | 9 | 集群验证 | 1 | 1717 | 2-10_集群验证的网络连通性与组件就绪检查.md |
| done | 10 | Kuboard：Dashboard另一种选择 | 1 | 4395 | 2-11_Kuboard安装与Dashboard的能力对比.md |
| done | 11 | k8s高可用架构解析 | 2 | 5330 | 2-2_Kubernetes高可用架构解析与组件通信路径.md |
| done | 12 | Kubeadm基本环境配置 | 1 | 4105 | 2-3_Kubeadm安装前的基本环境配置清单.md |
| done | 13 | Kubeadm基本组件安装 | 1 | 2373 | 2-4_Docker与kubeadm组件的选定版本及容器运行时配置.md |
| done | 14 | Kubeadm高可用组件安装 | 1 | 1743 | 2-5_haproxy与keepalived搭建apiserver负载均衡.md |
| done | 15 | Kubeadm集群初始化 | 1 | 3714 | 2-6_kubeadm-init初始化高可用控制面与Calico网络插件安装.md |
| done | 16 | 高可用Master及Token过期处理 | 1 | 2368 | 2-7_高可用Master扩容与token过期后的join处理.md |
| done | 17 | Kubeadm Node节点配置 | 1 | 604 | 2-8_Node节点加入集群后的配置与就绪判定.md |
| done | 18 | Dashboard&Metrics Server安装 | 1 | 1143 | 2-9_Metrics-Server与Dashboard的安装.md |
| done | 19 | 二进制高可用安装k8s1.19集群说明 | 1 | 3470 | 3-1_二进制安装1.19的版本说明与升级前变更评估.md |
| done | 20 | 二进制Metrics&Dashboard安装 | 1 | 2718 | 3-10_二进制集群安装Metrics-Server与Dashboard.md |
| done | 21 | 二进制高可用集群可用性验证 | 1 | 2808 | 3-11_二进制高可用集群的可用性验证四步法.md |
| done | 22 | 生产环境k8s集群关键性配置 | 1 | 4615 | 3-12_生产环境Kubernetes集群的关键性配置清单.md |
| done | 23 | Bootstrapping Kubelet启动过程 | 1 | 4332 | 3-13_TLS-Bootstrapping下kubelet的启动流程拆解.md |
| done | 24 | Bootstrapping CSR申请和证书颁发原理 | 1 | 7105 | 3-14_Bootstrapping的CSR申请与证书颁发原理.md |
| done | 25 | Bootstrapping 证书自动续期原理 | 1 | 4312 | 3-15_Bootstrapping证书自动续期原理与配置.md |
| done | 26 | 二进制高可用基本配置 | 1 | 5757 | 3-3_二进制安装前的基本环境配置清单.md |
| done | 27 | 二进制系统和内核升级 | 1 | 1790 | 3-4_二进制安装前的系统与内核升级.md |
| done | 28 | 二进制基本组件安装 | 1 | 3214 | 3-5_二进制基本组件安装_IPVS内核模块与容器运行时与kube二进制分发.md |
| done | 29 | 二进制生成证书详解 | 1 | 10308 | 3-6_二进制生成证书详解_cfssl自签CA与etcd_apiserver等组件证书.md |
| done | 30 | 二进制高可用及k8s组件配置 | 1 | 4541 | 3-7_二进制高可用集群_etcd集群与master控制面组件配置.md |
| done | 31 | 二进制安装TLS Bootstrapping自动颁发证书 | 1 | 1949 | 3-8_二进制安装TLS-Bootstrapping自动颁发kubelet证书.md |
| done | 32 | 二进制Node节点配置 | 1 | 5140 | 3-9_二进制集群的Node节点配置与kubelet_kube-proxy_Calico_CoreDNS安装.md |
| done | 33 | 课时1：Docker基础 | 1 | 3714 | 4-1_Docker基础_什么是容器与镜像分层.md |
| done | 34 | 课时2：Docker基本命令上 | 1 | 10157 | 4-2_Docker基本命令上_version_info镜像拉取与容器启停.md |
| done | 35 | 课时3：Docker基本命令下 | 1 | 3015 | 4-3_Docker基本命令下_端口映射_copy_commit与容器清理.md |
| done | 36 | 课时4：Dockerfile用法 | 1 | 10513 | 4-4_Dockerfile用法_常用指令详解与镜像构建.md |
| done | 37 | 课时5：制作小镜像上 | 1 | 3720 | 4-5_制作小镜像上_基础镜像选型与alpine精简.md |
| done | 38 | 课时6：多阶段制作小镜像下 | 1 | 4384 | 4-6_多阶段制作小镜像下_Go与PHP多阶段构建与COPY--from.md |
| done | 39 | 课时7：Scratch镜像 | 1 | 2126 | 4-7_Scratch空镜像_纯静态二进制极限瘦身与build--pull.md |
| done | 40 | 为什么要用Kubernetes？ | 1 | 3388 | 5-1_为什么要用Kubernetes_裸容器部署的五个真实痛点与k8s解法.md |
| done | 41 | 零宕机必备知识：Pod退出流程 | 1 | 6024 | 5-10_零宕机必备知识_Pod退出流程与preStop实战.md |
| done | 42 | 零宕机必备知识：PreStop的使用 | 1 | 1814 | 5-11_零宕机必备知识_PreStop用法实测与terminationGracePeriodSeconds联动.md |
| done | 43 | RC&ReplicaSet | 1 | 1725 | 5-12_RC与ReplicaSet_复制控制器与复制集的区别与它们被谁接管.md |
| done | 44 | 无状态服务Deployment概念 | 1 | 5909 | 5-13_无状态服务Deployment概念_三种控制器对比与Deployment字段解读.md |
| done | 45 | Deployment的更新 | 1 | 2918 | 5-14_Deployment的更新_滚动发布过程与set-image--record.md |
| done | 46 | Deployment的回滚 | 1 | 2620 | 5-15_Deployment的回滚_undo与指定revision回滚和record历史.md |
| done | 47 | Deployment扩容和缩容 | 1 | 1268 | 5-16_Deployment扩容和缩容_scale命令定时任务与HPA分工.md |
| done | 48 | Deployment更新暂停和恢复 | 1 | 2015 | 5-17_Deployment更新暂停恢复_暂停编辑与恢复触发一次滚动发布.md |
| done | 49 | Deployment更新注意事项 | 1 | 2650 | 5-18_Deployment更新注意事项_revisionHistoryLimit-minReadySeconds与两种更新策略.md |
| done | 50 | 有状态应用管理StatefulSet概念 | 1 | 3255 | 5-19_StatefulSet概念_有状态应用入门与稳定网络标识.md |
| done | 51 | Master节点 | 1 | 5484 | 5-2_Master节点_控制面四组件与apiserver调度器控制器管理器etcd.md |
| done | 52 | 创建一个StatefulSet应用 | 1 | 2734 | 5-20_创建StatefulSet应用_headless服务解析与有序扩容实测.md |
| done | 53 | StatefulSet扩容缩容 | 1 | 2601 | 5-21_StatefulSet扩容缩容_有序创建与倒序删除实测.md |
| done | 54 | StatefulSet更新策略 | 1 | 2635 | 5-22_StatefulSet更新策略_RollingUpdate倒序更新与partition灰度.md |
| done | 55 | StatefulSet灰度发布 | 1 | 1452 | 5-23_StatefulSet灰度发布_partition分段更新与灰度放量.md |
| done | 56 | StatefulSet级联删除和非级联删除 | 1 | 1199 | 5-24_StatefulSet级联删除_级联与非级联删除与孤儿Pod.md |
| done | 57 | 守护进程服务DaemonSet | 1 | 2000 | 5-25_DaemonSet_守护进程集概念_每节点一个Pod的适用场景.md |
| done | 58 | DaemonSet的使用 | 1 | 2155 | 5-26_DaemonSet使用_改造清单_去除replicas与nodeSelector标签筛选.md |
| done | 59 | DaemonSet的更新和回滚 | 1 | 1950 | 5-27_DaemonSet更新回滚_OnDelete策略与影响范围控制.md |
| done | 60 | Label&Selector | 1 | 5798 | 5-28_Label与Selector_标签分组与选择器查询语法.md |
| done | 61 | 在k8s上是如何发布服务的 | 1 | 5594 | 5-29_在k8s上如何发布服务_东西流量走Service南北流量走Ingress.md |
| done | 62 | Node节点 | 1 | 7371 | 5-3_Node节点_节点上四大组件与IPVS转发模式解析.md |
| done | 63 | 什么是Service | 1 | 3386 | 5-30_什么是Service_Service作为Pod的稳定入口与Endpoint机制.md |
| done | 64 | 定义一个Service | 1 | 5285 | 5-31_定义Service_端口selector与clusterIP自动生成.md |
| done | 65 | 使用Service代理k8s外部服务 | 1 | 5363 | 5-32_Service代理外部服务_无selector的Service与手动Endpoint.md |
| done | 66 | 使用Service反代外部域名 | 1 | 1518 | 5-33_Service反代外部域名_ExternalName类型与跨域限制.md |
| done | 67 | Service常用类型 | 1 | 3036 | 5-34_Service常用类型_ClusterIPNodePortExternalName与LoadBalancer.md |
| done | 68 | 什么是Ingress？ | 1 | 3773 | 5-35_什么是Ingress_Ingress概念与为什么不用NodePort.md |
| done | 69 | 使用helm安装ingress | 1 | 5887 | 5-36_helm安装Ingress_ingress-nginx的values参数改造与DaemonSet部署.md |
| done | 70 | Ingress简单使用 | 1 | 7875 | 5-37_Ingress简单使用_域名发布一个Service的完整流程与nginx配置自动生成.md |
| done | 71 | Ingress多域名使用 | 1 | 1372 | 5-38_Ingress多域名_一个Ingress配多个host与replace更新.md |
| done | 72 | HPA自动扩缩容 | 1 | 4680 | 5-39_HPA自动扩缩容_基于metrics-server的CPU扩缩容与压力实测.md |
| done | 73 | 什么是Pod？ | 1 | 3882 | 5-4_什么是Pod_Pod基本概念_pause容器与namespace隔离性.md |
| done | 74 | k8s配置管理ConfigMap | 1 | 12101 | 5-40_ConfigMap配置管理_四种创建方式与挂载为环境变量和配置文件.md |
| done | 75 | k8s加密数据管理Secret | 1 | 6989 | 5-41_Secret加密数据管理_从文件创建与imagePullSecrets拉取私有镜像.md |
| done | 76 | ConfigMap&Secret使用SubPath | 1 | 2680 | 5-42_SubPath挂载_解决ConfigMap挂载覆盖目录目录的问题.md |
| done | 77 | ConfigMap&Secret热更新 | 1 | 4327 | 5-43_ConfigMap热更新_更新方式_subPath感知不到更新与dry-run技巧.md |
| done | 78 | k8s1.19的不可变Secret和ConfigMap | 1 | 922 | 5-44_不可变ConfigMap_immutable参数与热加载的安全风险.md |
| done | 79 | k8s存储Volumes介绍 | 1 | 3759 | 5-45_Volumes介绍_为什么需要卷与存储选型.md |
| done | 80 | Volumes HostPath挂载宿主机路径 | 1 | 2247 | 5-46_HostPath挂载_把宿主机文件挂进容器与type取值区别.md |
| done | 81 | Volumes EmptyDir实现数据共享 | 1 | 3577 | 5-47_EmptyDir数据共享_同Pod多容器共享目录与medium内存盘.md |
| done | 82 | 挂载NFS至容器 | 1 | 2787 | 5-48_挂载NFS至容器_NFS服务端配置与Pod直挂volume的实测.md |
| done | 83 | 持久化存储PV&PVC概念上 | 1 | 9048 | 5-49_PV与PVC概念上_存储解耦原理与PV回收策略访问模式解读.md |
| done | 84 | 为什么要引入Pod | 1 | 2265 | 5-5_为什么要引入Pod_从使用方与容器运行时两个视角看Pod的由来.md |
| skip | 85 | PV&PVC概念下 | 1 | 460 | `5-50` 源文件仅 4 行 / 462 字符，转写残缺，无素材可写（不凭空补写） |
| done | 86 | PV&PVC入门 | 1 | 3880 | 5-51_PV与PVC入门_从创建PV到Pod挂载实测的完整流程.md |
| done | 87 | PV&PVC补充 | 1 | 6073 | 5-52_PV与PVC补充_PVC绑不上与删除卡死的排查以及selector与CSI快照.md |
| done | 88 | CronJob计划任务 | 1 | 4678 | 5-53_CronJob计划任务_类Linux定时任务如何跑进容器并解读并发策略.md |
| done | 89 | 污点和容忍Taint&Toleration入门 | 1 | 5509 | 5-54_Taint与Toleration入门_污点排斥与容忍声明的调度控制.md |
| done | 90 | Taint&Toleration补充 | 1 | 5444 | 5-55_Taint与Toleration补充_容忍写法的三种形态与tolerationSeconds调优.md |
| done | 91 | 初始化容器InitContainer | 1 | 3145 | 5-56_InitContainer_初始化容器_启动前的预处理与依赖等待.md |
| done | 92 | Affinity亲和力入门 | 1 | 4335 | 5-57_Affinity亲和力_三类亲和力与硬软两种约束的概念.md |
| done | 93 | 节点亲和力NodeAffinity使用 | 1 | 5263 | 5-58_NodeAffinity使用_节点亲和字段逐条写法的实测.md |
| done | 94 | Pod亲和力和反亲和力 | 1 | 3681 | 5-59_Pod反亲和_Pod亲和与反亲和的关联写法与拓扑域.md |
| done | 95 | 定义一个Pod | 1 | 9463 | 5-6_定义Pod_Pod资源清单字段逐条解读与创建流程.md |
| done | 96 | Topology拓扑域概念 | 1 | 2954 | k8stop-5-60_Topology拓扑域概念_拓扑域的三个层级与hostname导致的副本堆叠.md |
| done | 97 | 使用Topology实现多地多机房部署 | 1 | 4108 | k8stop-5-61_使用Topology实现多地多机房部署_机柜级拓扑域实测与软硬反亲和的容量天花板.md |
| done | 98 | 临时容器概念和配置 | 1 | 3191 | k8stop-5-62_临时容器概念和配置_为什么小镜像没法排错与EphemeralContainers的全组件开启.md |
| done | 99 | 使用临时容器在线debug | 1 | 3896 | k8stop-5-63_使用临时容器在线debug_ephemeralcontainers的注入与exec排错实测.md |
| done | 100 | RBAC权限管理概念 | 1 | 11393 | k8stop-5-64_RBAC权限管理概念_四类顶级资源与Role和ClusterRole的唯一区别.md |
| done | 101 | RBAC使用 | 1 | 8582 | k8stop-5-65_RBAC使用_官方写法的九种subjects形态与聚合ClusterRole.md |
| done | 102 | 零宕机发布应用必备知识：Pod三种探针 | 1 | 3629 | k8stop-5-7_零宕机必备知识Pod三种探针_三种探针的分工与exec-tcpSocket-httpGet检测方式.md |
| done | 103 | 零宕机必备知识：StartupProbe | 1 | 7591 | k8stop-5-8_零宕机必备知识StartupProbe_慢启动应用的探针死循环与五个超时参数.md |
| done | 104 | 零宕机必备知识：Liveness和Readiness | 1 | 3008 | k8stop-5-9_零宕机必备知识Liveness和Readiness_exec命令缺失持续重启与pgrep-java的致命写法.md |
| done | 105 | 课时1： 安装一键式k8s资源平台Ratel到k8s集群中 | 1 | 3023 | k8stop-6-1_课时1安装一键式k8s资源平台Ratel到k8s集群中_kubeconfig挂Secret与Ingress暴露.md |
| done | 106 | 课时10：Rook部署 | 1 | 5067 | k8stop-6-10_课时10Rook部署_operator先行的部署顺序与useAllNodes和裸盘取舍.md |
| skip | 107 | 课时11：使用Rook部署Ceph集群上 | 1 | 396 | `6-11` 源文件仅 6 行 / 400 字符，转写残缺，无素材可写（不凭空补写） |
| done | 108 | 课时12：使用Rook部署Ceph集群下 | 1 | 3273 | k8stop-6-12_课时12使用Rook部署Ceph集群下_CephCluster的CRD本质与组件启动顺序.md |
| done | 109 | 课时13：创建块存储类型的动态存储 | 1 | 3121 | k8stop-6-13_课时13创建块存储类型的动态存储_CephBlockPool的副本失败域与StatefulSet的volumeClaimTemplates.md |
| done | 110 | 课时14：StatefulSet动态申请存储 | 1 | 3180 | k8stop-6-14_课时14StatefulSet动态申请存储_volumeClaimTemplates不可编辑与每副本独立PVC的实测.md |
| done | 111 | 课时15：使用PVC动态申请存储 | 1 | 1870 | k8stop-6-15_课时15使用PVC动态申请存储_imageFormat与imageFeatures和一步到位的动态绑定.md |
| done | 112 | 课时16：共享文件系统类型的StorageClass | 1 | 3121 | k8stop-6-16_课时16共享文件系统类型的StorageClass_CephFileSystem的主备MDS与内核4.17门槛.md |
| done | 113 | 课时17：PVC在线扩容和PVC快照 | 1 | 1604 | k8stop-6-17_课时17PVC在线扩容和PVC快照_为什么按量申请与全组件打开feature-gates.md |
| done | 114 | 课时18：Rook集群清理和重建 | 1 | 1158 | k8stop-6-18_课时18Rook集群清理和重建_清理磁盘与数据目录并把CSI镜像升到2.0.md |
| done | 115 | 课时19：PVC在线扩容使用 | 1 | 2304 | k8stop-6-19_课时19PVC在线扩容使用_allowVolumeExpansion与使用中的PVC在线扩容实测.md |
| done | 116 | 课时2： Ratel简单使用 | 1 | 7145 | k8stop-6-2_课时2Ratel简单使用_一键创建带ResourceQuota的namespace与Deployment表单全字段.md |
| done | 117 | 课时20：PVC快照和回滚 | 1 | 3562 | k8stop-6-20_课时20PVC快照和回滚_VolumeSnapshotClass的用法与xfs踩坑转ext4.md |
| done | 118 | 课时21：Rook Ceph xfs_repair问题修复 | 1 | 8213 | k8stop-6-21_课时21RookCeph_xfs_repair问题修复_复现现场与direct-mount修复流程.md |
| done | 119 | 课时22：存储回顾 | 1 | 3353 | k8stop-6-22_课时22存储回顾_静态与动态两条链路与快照和CSI的完整闭环.md |
| done | 120 | 课时23：容器化中间件基本说明 | 1 | 1479 | k8stop-6-23_课时23容器化中间件基本说明_本章路线与Redis-Helm-监控-日志的安排.md |
| done | 121 | 课时24：如何部署一个容器到k8s | 1 | 7422 | k8stop-6-24_课时24如何部署一个容器到k8s_以单实例Redis为例的通用流程与Service统一配置.md |
| done | 122 | 课时25：部署Redis Operator | 1 | 5649 | k8stop-6-25_部署RedisOperator_单实例Redis的连接方式与Operator选型.md |
| done | 123 | 课时26：在k8s上部署Redis集群上 | 1 | 931 | k8stop-6-26_部署Redis集群上_Operator的CR声明与CRD前置依赖.md |
| done | 124 | 课时27：在k8s上部署Redis集群下 | 1 | 4503 | k8stop-6-27_部署Redis集群下_三主三从的StatefulSet结构与持久化与分片路由.md |
| done | 125 | 课时28：Redis集群扩容和缩容 | 1 | 4764 | k8stop-6-28_Redis集群扩容和缩容_改CR的masterSize与集群配置文件的持久化底线.md |
| done | 126 | 课时29：部署RabbitMQ集群到k8s | 1 | 5767 | k8stop-6-29_部署RabbitMQ集群到k8s_StatefulSet加k8s服务发现自动组网.md |
| done | 127 | 课时3： 准入控制 | 1 | 5166 | k8stop-6-3_准入控制_ResourceQuota与LimitRange的默认值注入和上下限约束.md |
| done | 128 | 课时30：解决RabbitMQ密码不生效问题 | 1 | 2291 | k8stop-6-30_解决RabbitMQ密码不生效问题_ConfigMap挂载覆盖了镜像生成的配置.md |
| done | 129 | 课时31：RabbitMQ扩容和缩容 | 1 | 3248 | k8stop-6-31_RabbitMQ扩容和缩容_服务发现自动入群与固定节点的持久化方案.md |
| done | 130 | 课时32：Helm v3安装使用 | 1 | 3666 | k8stop-6-32_Helm-v3安装使用_二进制安装仓库管理与v2到v3的命令变化.md |
| done | 131 | 课时33：Helm目录层级 | 1 | 2406 | k8stop-6-33_Helm目录层级_Chart.yaml与values.yaml与templates的分工.md |
| done | 132 | 课时34：Helm语法上 | 1 | 2283 | k8stop-6-34_Helm语法上_Values与Chart取值_with作用域与nindent缩进.md |
| done | 133 | 课时35：Helm语法下 | 1 | 5140 | k8stop-6-35_Helm语法下_dry-run调试与_helpers.tpl全名生成与range遍历.md |
| done | 134 | 课时36：编写Helm部署RabbitMQ集群 | 1 | 10875 | k8stop-6-36_编写Helm部署RabbitMQ集群_把散落参数抽进values.yaml的改造实录.md |
| done | 135 | 课时37：运行自己编写的Helm | 1 | 4399 | k8stop-6-37_运行自己编写的Helm_install与upgrade与uninstall的实操踩坑.md |
| done | 136 | 课时38：部署Zookeeper和Kafka集群 | 1 | 4641 | k8stop-6-38_部署Zookeeper和Kafka集群_用bitnami的Helm-chart一键搭建.md |
| done | 137 | 课时39：测试Kafka和Zookeeper集群 | 1 | 3495 | k8stop-6-39_测试Kafka和Zookeeper集群_建topic与生产消费消息验证可用性.md |
| done | 138 | 课时4： Kubernetes服务质量QoS | 1 | 4743 | k8stop-6-4_Kubernetes服务质量QoS_三个等级判定与OOM时的驱逐顺序.md |
| done | 139 | 课时40：Kafka和Zookeeper集群扩容缩容 | 1 | 1091 | k8stop-6-40_Kafka和Zookeeper扩容缩容_用upgrade改副本数与set参数的回填陷阱.md |
| done | 140 | 课时5： 使用PodPreset预配置容器时区 | 1 | 7539 | k8stop-6-5_使用PodPreset预配置容器时区_准入插件开启与hostPath挂载与selector匹配.md |
| done | 141 | 课时6： Dashboard基于用户名密码认证 | 1 | 4222 | k8stop-6-6_Dashboard基于用户名密码认证_basic-auth-file开启与ClusterRole通配授权.md |
| done | 142 | 课时7： RBAC实现不同用户不同权限 | 1 | 2379 | k8stop-6-7_RBAC实现不同用户不同权限_ClusterRole模板加RoleBinding按namespace下发.md |
| done | 143 | 课时8： ServiceAccount权限管理 | 1 | 4944 | k8stop-6-8_ServiceAccount权限管理_专用namespace集中托管与token登录.md |
| done | 144 | 课时9： 云原生存储Rook介绍 | 1 | 6187 | k8stop-6-9_云原生存储Rook介绍_在k8s与Ceph之间搭桥的编排工具与组件拆解.md |
| done | 145 | 课时1：EFK日志收集 | 1 | 8015 | k8stop-7-1_EFK日志收集_Fluentd收集容器控制台日志写入Elasticsearch.md |
| done | 146 | 课时10：Prometheus监控etcd集群 | 1 | 7727 | k8stop-7-10_Prometheus监控etcd集群_Endpoint与ServiceMonitor与HTTPS证书接入.md |
| done | 147 | 课时11：Prometheus Exporter | 1 | 8324 | k8stop-7-11_Prometheus-Exporter_给没有metrics接口的中间件做代理采集.md |
| done | 148 | 课时12：Prometheus黑盒监控 | 1 | 3765 | k8stop-7-12_Prometheus黑盒监控_blackbox_exporter部署与URL和TCP探测.md |
| done | 149 | 课时13：Prometheus additional传统配置 | 1 | 7080 | k8stop-7-13_Prometheus传统配置方式_additionalScrapeConfigs接入黑盒监控与IPv4踩坑.md |
| done | 150 | 课时14：Alertmanager入门 | 1 | 5745 | k8stop-7-14_Alertmanager入门_告警路由分组抑制与receiver配置.md |
| done | 151 | 课时16：Prometheus使用微信告警 | 1 | 2168 | k8stop-7-16_Prometheus使用微信告警_企业微信应用创建与wechat_configs配置.md |
| done | 152 | 课时17：Prometheus自定义告警模板 | 1 | 2769 | k8stop-7-17_Prometheus自定义告警模板_templates目录挂载与wechat模板改造.md |
| done | 153 | 课时18：Prometheus自动发现 | 1 | 5248 | k8stop-7-18_Prometheus自动发现_基于kubernetes_sd_configs自动监控Ingress域名.md |
| done | 154 | 课时19：Prometheus监控Java JVM | 1 | 6398 | k8stop-7-19_Prometheus监控JavaJVM_micrometer埋点与Actuator接入.md |
| done | 155 | 课时2：使用Filebeat收集容器内日志 | 1 | 6414 | k8stop-7-2_使用Filebeat收集容器内日志_sidecar共享emptyDir与Kafka链路.md |
| done | 156 | 课时20：基于Eureka自动发现监控Java JVM | 1 | 5103 | k8stop-7-20_基于Eureka自动发现监控JavaJVM_eureka-consul-adapter与consul_sd配置.md |
| done | 157 | 课时3：使用不同资源名称查询日志 | 1 | 4819 | k8stop-7-3_使用不同资源名称查询日志_Filebeat排错与Kibana按字段过滤.md |
| done | 158 | 课时4：Prometheus安装及入门 | 1 | 7834 | k8stop-7-4_Prometheus安装及入门_kube-prometheus部署与三个入口.md |
| done | 159 | 课时5：Prometheus Latest安装入门 | 1 | 7810 | k8stop-7-5_Prometheus-Latest安装入门_版本对应关系与manifests目录结构.md |
| done | 160 | 课时6：Prometheus Metrics类型 | 1 | 7689 | k8stop-7-6_Prometheus-Metrics类型_Counter与Gauge与Histogram与Summary.md |
| done | 161 | 课时7：PromQL基本操作 | 1 | 6587 | k8stop-7-7_PromQL基本操作_瞬时向量与区间向量与过滤和聚合.md |
| done | 162 | 课时8：PromQL常用函数 | 1 | 7335 | k8stop-7-8_PromQL常用函数_rate与irate与predict_linear与label处理.md |
| done | 163 | 课时9：解决Scheduler监控问题 | 1 | 4467 | k8stop-7-9_解决Scheduler与ControllerManager监控告警_监听地址与无selector的Service.md |
| done | 164 | 课时1：Ingress Nginx入门 | 1 | 4504 | k8stop-8-1_Ingress-Nginx入门_集群入口链路与选型和部署要点.md |
| done | 165 | 课时10： Ingress Nginx基本认证 | 1 | 1291 | k8stop-8-10_Ingress-Nginx基本认证.md |
| done | 166 | 课时11： Ingress Nginx监控上 | 1 | 4685 | k8stop-8-11_Ingress-Nginx监控上.md |
| done | 167 | 课时12：Ingress Nginx监控下 | 1 | 1764 | k8stop-8-12_Ingress-Nginx监控下.md |
| done | 168 | 课时13：k8s1.19下的Ingress配置 | 1 | 2216 | k8stop-8-13_k8s1.19下Ingress配置.md |
| done | 169 | 课时2： Ingress Nginx域名重定向 | 1 | 4082 | k8stop-8-2_Ingress-Nginx域名重定向_permanent-redirect注解与301和308.md |
| done | 170 | 课时3： Ingress Nginx前后端分离 | 1 | 2837 | k8stop-8-3_Ingress-Nginx前后端分离_rewrite-target路径重写与捕获组.md |
| done | 171 | 课时4： Ingress Nginx SSL配置 | 1 | 4997 | k8stop-8-4_Ingress-Nginx-SSL配置.md |
| done | 172 | 课时5： Ingress Nginx黑白名单 | 1 | 3118 | k8stop-8-5_Ingress-Nginx黑白名单.md |
| done | 173 | 课时6： Ingress Nginx匹配请求头 | 1 | 1411 | k8stop-8-6_Ingress-Nginx匹配请求头.md |
| done | 174 | 课时7： Ingress Nginx速率限制 | 1 | 2071 | k8stop-8-7_Ingress-Nginx速率限制.md |
| done | 175 | 课时8： Ingress Nginx实现灰度金丝雀发布 | 1 | 5540 | k8stop-8-8_Ingress-Nginx灰度金丝雀发布.md |
| done | 176 | 课时9： Ingress Nginx自定义错误页面 | 1 | 4027 | k8stop-8-9_Ingress-Nginx自定义错误页面.md |
| done | 177 | 课时1：Jenkins CICD介绍 | 1 | 4310 | k8stop-9-1_Jenkins-CI-CD概述_一次构建到处发布.md |
| done | 178 | 课时10：Jenkins自动构建流水线设计 | 1 | 4731 | k8stop-9-10_Jenkins自动构建流水线设计_步骤拆解与镜像发布.md |
| done | 179 | 课时11：使用BlueOcean创建Jenkinsfile | 1 | 9368 | k8stop-9-11_BlueOcean创建Jenkinsfile_框架生成与变量分支处理.md |
| done | 180 | 课时12：Jenkins使用Kubernetes Pod执行 | 1 | 10606 | k8stop-9-12_Jenkins使用Kubernetes-Pod执行_Pod模板与容器步骤.md |
| done | 181 | 课时13：Jenkins配置Kubernetes多集群 | 1 | 2948 | k8stop-9-13_Jenkins配置Kubernetes多集群_Cloud与证书凭证.md |
| done | 182 | 课时14：KUBECONFIG多集群配置 | 1 | 2409 | k8stop-9-14_KUBECONFIG多集群配置_上下文切换与Secret挂载.md |
| done | 183 | 课时15：Jenkins自动化构建Java应用上 | 1 | 8523 | k8stop-9-15_Jenkins自动化构建Java应用_上_构建与部署验证.md |
| done | 184 | 课时16：Jenkins自动化构建Java应用下 | 1 | 1746 | k8stop-9-16_Jenkins自动化构建Java应用_下_镜像与挂载排错.md |
| done | 185 | 课时17：Jenkins自动化构建NodeJS应用 | 1 | 5889 | k8stop-9-17_Jenkins自动化构建NodeJS应用_构建镜像与缓存.md |
| done | 186 | 课时18：Docker镜像高级优化及自动化构建建议 | 1 | 6595 | k8stop-9-18_Docker镜像高级优化与统一Jenkinsfile建议.md |
| done | 187 | 课时19：Jenkins生产环境和UAT环境流水线设计 | 1 | 5536 | k8stop-9-19_生产环境与UAT环境流水线_选择镜像发版.md |
| done | 188 | 课时2：Jenkins安装 | 1 | 3902 | k8stop-9-2_Jenkins安装_部署形态与插件管理.md |
| done | 189 | 课时20：Jenkins基于角色的账户管理 | 1 | 4900 | k8stop-9-20_Jenkins基于角色的账户管理_Role-Strategy插件.md |
| done | 190 | 容器化SpringCloud项目说明 | 1 | 1769 | k8stop-9-21_容器化SpringCloud项目说明_理念与三步法.md |
| done | 191 | SpringCloud架构解析上 | 1 | 10269 | k8stop-9-22_SpringCloud架构解析_上_传统架构痛点与服务发现网关配置中心.md |
| done | 192 | SpringCloud架构解析下 | 1 | 1638 | k8stop-9-23_SpringCloud架构解析_下_组件独立部署与部署理念.md |
| done | 193 | 如何在k8s上正确部署Eureka | 1 | 3374 | k8stop-9-24_在k8s上正确部署Eureka_StatefulSet与HeadlessService.md |
| done | 194 | 到底要不要用Eureka | 1 | 3952 | k8stop-9-25_到底要不要用Eureka_k8s服务发现与服务网格权衡.md |
| done | 195 | 如何正确部署Zuul和ConfigServer到k8s | 1 | 2572 | k8stop-9-26_正确部署Zuul和ConfigServer到k8s_网关与配置中心.md |
| done | 196 | 到底要不要用Zuul和ConfigServer | 1 | 4725 | k8stop-9-27_到底要不要用Zuul和ConfigServer_配置管理替代方案.md |
| done | 197 | SpringCloud项目总结 | 1 | 3800 | k8stop-9-28_SpringCloud项目总结_部署方式与取舍建议.md |
| done | 198 | 课时3：Jenkins声明式流水线入门 | 1 | 9239 | k8stop-9-3_Jenkins声明式流水线入门_语法与agent并行条件.md |
| done | 199 | 课时4：Jenkins变量使用 | 1 | 4373 | k8stop-9-4_Jenkins变量使用_内置变量与参数化.md |
| done | 200 | 课时5：Jenkins级联变量 | 1 | 2878 | k8stop-9-5_Jenkins级联变量_Active-Choices联动.md |
| done | 201 | 课时6：镜像仓库配置 | 1 | 4374 | k8stop-9-6_镜像仓库配置_阿里云CLI与Harbor取tag.md |
| done | 202 | 课时7：GitLab安装配置 | 1 | 2432 | k8stop-9-7_GitLab安装配置_管理员Key与项目.md |
| done | 203 | 课时8： Jenkins Credentials配置 | 1 | 1597 | k8stop-9-8_Jenkins-Credentials配置_SSH与仓库账号.md |
| done | 204 | 课时9：Jenkins BlueOcean入门 | 1 | 8392 | k8stop-9-9_Jenkins-BlueOcean入门_可视化创建流水线.md |

## 节流约定（防 429）

- 一次只推进**一组**，不并发、不一次读多个大文件
- 每写完一篇 `sleep 45~60`；每 6 篇 `sleep 300`
- 中断随时可从 `pending` 行续跑，不重跑全量

## 已落盘产物
