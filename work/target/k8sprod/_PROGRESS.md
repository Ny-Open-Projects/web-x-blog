# 5.k8s5-prod → 博客 转换进度

状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、课程总结、本章未完结）
**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**

| 状态 | # | 组名 | 文件数 | 总字数 | 产出博客 |
| --- | --- | --- | --- | --- | --- |
| skip | 1 | 课程介绍(更多IT教程 微信352852792) | 1 | 3913 | 导学，不写文 |
| done | 2 | ingress --- 四层代理、session保持、定制配置、流量控制（上）(更多IT教程 微信352852792) | 1 | 5094 | `10-1_ingress_nginx的DaemonSet部署与四层TCP代理.md` |
| done | 3 | ingress -- 四层代理、session保持、定制配置、流量控制（中）(更多IT教程 微信352852792) | 1 | 4272 | `10-2_ingress_nginx自定义响应头配置模板与TLS证书配置.md` |
| 4435 | `10-3_ingress_nginx的会话保持与金丝雀流量控制.md` |
| 5625 | `10-4_共享存储_PV_PVC与StorageClass的绑定机制.md` |
| 8946 | `10-5_用Heketi初始化GlusterFS并让StorageClass动态供给PV.md` |
| 10362 | `10-6_StatefulSet的有序启动与独立持久存储.md` |
| 6471 | `10-7_KubernetesAPI的分组版本设计与REST接口实战.md` |
| 2652 | `11-1_容器日志采集的三种方案对比与LogPilot原理.md` |
| 6874 | `11-2_LogPilot加ES加Kibana的日志采集落地.md` |
| 4387 | `11-3_监控体系的目标采集流程与监控对象.md` |
| done | 4 | ingress --- 四层代理、session保持、定制配置、流量控制（下）(更多IT教程 微信352852792) | 1 | 4435 | `10-3` 起 |
| done | 5 | 共享存储 --- PV、PVC和StorageClass（上）.mp4(更多IT教程 微信352852792) | 1 | 5625 | `10-4` 起 |
| done | 6 | 共享存储 --- PV、PVC和StorageClass（下）(更多IT教程 微信352852792) | 1 | 8946 | `10-5` 起 |
| done | 7 | StatefulSet --- 有状态应用的守护者(更多IT教程 微信352852792) | 1 | 10362 | `10-6` 起 |
| done | 8 | KubernetesAPI ---如何开发一个基于kubernetes的容器管理平台(更多IT教程 微信352852792) | 1 | 6471 | `10-7` 起 |
| done | 9 | 常见日志采集问题和解决方案分析(更多IT教程 微信352852792) | 1 | 2652 | `11-1` 起 |
| done | 10 | logpilot+elasticsearch+kibana日志实践(更多IT教程 微信352852792) | 1 | 6874 | `11-2` 起 |
| done | 11 | 监控入门---从整体把握监控(更多IT教程 微信352852792) | 1 | 4387 | `11-3` 起 |
| done | 12 | Prometheus入门---架构和原理(更多IT教程 微信352852792) | 1 | 3875 | `11-4_Prometheus的架构组件与四种指标类型.md` |
| done | 13 | 部署前奏 - Helm & Operator(更多IT教程 微信352852792) | 1 | 3721 | `11-5_Helm包管理与Tiller安装以及Operator原理.md` |
| done | 14 | 监控部署实战 - Helm+PrometheusOperator(更多IT教程 微信352852792) | 1 | 5809 | `11-6_用本地chart部署PrometheusOperator并打通访问入口.md` |
| done | 15 | 监控落地 - 指标完善、Grafana看板和邮件报警（上）(更多IT教程 微信352852792) | 1 | 5538 | `11-7_PrometheusWeb界面与Targets巡检及组件指标补齐.md` |
| done | 16 | 监控落地 - 指标完善、Grafana看板和邮件报警（中）(更多IT教程 微信352852792) | 1 | 4628 | `11-8_ETCD证书Secret配置与重装Operator清理CRD.md` |
| done | 17 | 监控落地 - 指标完善、Grafana看板和邮件报警（下）(更多IT教程 微信352852792) | 1 | 5035 | `11-9_报警规则Grafana看板与Alertmanager邮件告警打通.md` |
| done | 18 | 什么是ServiceMesh？什么是Istio？(更多IT教程 微信352852792) | 1 | 1606 | `12-1_ServiceMesh概念与LinkerdIstio两大实现对比.md` |
| done | 19 | istio核心功能实践 - 分布式追踪(更多IT教程 微信352852792) | 1 | 10484 | `12-10_用Jaeger与Zipkin做分布式链路追踪.md` |
| done | 20 | istio核心功能实践 - grafana和kiali(更多IT教程 微信352852792) | 1 | 3181 | `12-11_用Grafana看板与Kiali做网格可视化管理.md` |
| done | 21 | Istio架构和原理(更多IT教程 微信352852792) | 1 | 4117 | `12-2_Istio的架构原理EnvoyPilotMixerGalleyCitadel.md` |
| done | 22 | 部署面向生产的istio - istio-init(更多IT教程 微信352852792) | 1 | 4427 | `12-3_下载Istio发行版与istio-init安装踩坑.md` |
| done | 23 | 部署面向生产的istio - 核心组件（上）(更多IT教程 微信352852792) | 1 | 4363 | `12-4_Istio核心组件与Gateway端口排错及MetricsServer补位.md` |
| done | 24 | 部署面向生产的istio - 核心组件（中）(更多IT教程 微信352852792) | 1 | 3585 | `12-5_MetricsServer部署与apiserver授权证书补齐.md` |
| done | 25 | 署面向生产的istio - 核心组件（下）(更多IT教程 微信352852792) | 1 | 4099 | `12-6_补kube-proxy与CoreDNShosts插件让MetricsServer跑通.md` |
| done | 26 | istio核心功能实践 - 部署bookinfo(更多IT教程 微信352852792) | 1 | 5687 | `12-7_部署Bookinfo示例应用并通过Istio网关访问.md` |
| done | 27 | istio核心功能实践 - 智能路由(更多IT教程 微信352852792) | 1 | 3792 | `12-8_Istio智能路由之请求路由故障注入与流量迁移.md` |
| done | 28 | istio核心功能实践 - 指标收集和查询(更多IT教程 微信352852792) | 1 | 5320 | `12-9_Istio遥测之Mixer收集指标与Prometheus查询.md` |
| skip | 29 | 课程总结(更多IT教程 微信352852792) | 1 | 1716 | `13-1` 起 |
| done | 30 | 了解kubernetes(更多IT教程 微信352852792) | 1 | 2214 | `2-1_了解Kubernetes的名字由来与核心特征.md` |
| done | 31 | kubernetes的核心概念(更多IT教程 微信352852792) | 1 | 2287 | `2-2_Pod副本集Deployment与Service的核心概念.md` |
| done | 32 | kubernetes的架构设计(更多IT教程 微信352852792) | 1 | 1575 | `2-3_Kubernetes集群架构与核心组件工作流.md` |
| done | 33 | kubernetes认证的密码学原理(更多IT教程 微信352852792) | 1 | 4145 | `2-4_Kubernetes认证的密码学原理与TLS握手.md` |
| done | 34 | kubernetes的认证与授权(更多IT教程 微信352852792) | 1 | 5158 | `2-5_Kubernetes三种认证方式RBAC授权与准入控制.md` |
| done | 35 | 集群搭建方案对比(更多IT教程 微信352852792) | 1 | 2187 | `2-6_三种集群搭建方案对比社区方案kubeadm与二进制.md` |
| done | 36 | 实践环境准备(更多IT教程 微信352852792) | 2 | 11463 | `3-1_用kubeadm搭建高可用集群的实践环境准备.md` |
| done | 37 | 高可用集群部署(更多IT教程 微信352852792) | 1 | 4362 | `3-2_kubeadm高可用集群部署之keepalivedetcd三master与calico落地.md` |
| done | 38 | 集群可用性测试(更多IT教程 微信352852792) | 2 | 2665 | `3-3_集群可用性测试Pod网络Service与DNS四项验证.md` |
| done | 39 | 部署dashboard(更多IT教程 微信352852792) | 2 | 4533 | `3-4_部署KubernetesDashboard与Token登录和nginx代理访问.md` |
| done | 40 | 高可用集群部署（上）(更多IT教程 微信352852792) | 1 | 4667 | `4-2_二进制高可用集群部署之上-etcd三节点与apiserverkeepalivedkubectl落地.md` |
| done | 41 | 高可用集群部署（下）(更多IT教程 微信352852792) | 1 | 4139 | `4-3_二进制高可用集群部署之下_三节点控制面补齐与worker加入kubeletbootstrap和kube-proxy.md` |
| done | 42 | Harbor入门(更多IT教程 微信352852792) | 1 | 4834 | `5-1_Harbor入门云原生镜像仓库的特性架构与高可用方案选型.md` |
| done | 43 | Harbor高可用部署（上）(更多IT教程 微信352852792) | 1 | 2764 | `5-2_Harbor高可用部署之上_两个worker节点安装Harbor与nginx负载均衡.md` |
| done | 44 | Harbor高可用部署（下）(更多IT教程 微信352852792) | 1 | 5801 | `5-3_Harbor高可用部署之下_域名访问用户授权双主复制规则与镜像推送拉取.md` |
| done | 45 | kubernetes的服务发现 | 1 | 4883 | `5-4_Kubernetes的服务发现与通讯的三种场景.md` |
| done | 46 | 部署ingress-nginx（上） | 1 | 5078 | `5-5_部署ingress-nginx之上_Ingress概念与控制清单逐段解读.md` |
| done | 47 | 部署ingress-nginx（下） | 1 | 4228 | `5-6_部署ingress-nginx之下_hostNetwork暴露入口与域名实测.md` |
| done | 48 | 定时任务迁移kubernetes | 1 | 5304 | `6-1_定时任务迁移Kubernetes之镜像制作与CronJob调度.md` |
| done | 49 | springboot的web服务迁移kubernetes | 1 | 2965 | `6-3_SpringBootWeb服务迁移Kubernetes之镜像与三段配置.md` |
| done | 50 | 传统dubbo服务迁移kubernetes（上） | 1 | 4748 | `6-5_传统Dubbo服务迁移Kubernetes之上_非SpringBoot项目的打包与镜像构建.md` |
| done | 51 | 传统dubbo服务迁移kubernetes（下） | 1 | 3863 | `6-6_传统Dubbo服务迁移Kubernetes之下_host模式注册与端口集中管理.md` |
| done | 52 | kubernetes与cicd | 1 | 3224 | `7-1_Kubernetes与CI-CD流程变迁_从停起式发布到镜像化滚动发布.md` |
| done | 53 | cicd实践（1） | 1 | 3420 | `7-2_CICD实践之一_Jenkins安装与拉代码加Maven构建流水线.md` |
| done | 54 | cicd实践（2） | 1 | 3190 | `7-3_CICD实践之二_构建镜像脚本与Dockerfiles目录规范化.md` |
| done | 55 | cicd实践（3） | 1 | 3023 | `7-4_CICD实践之三_推送镜像配置模板化与deploy脚本.md` |
| done | 56 | cicd实践（4）(更多IT教程 微信352852792) | 1 | 3813 | `7-5_CICD实践之四_发布后健康检查与kubectl认证踩坑.md` |
| done | 57 | Namespace --- 集群的共享与隔离(更多IT教程 微信352852792) | 1 | 5788 | `8-1_Namespace集群的共享与隔离.md` |
| done | 58 | Resources---多维度集群资源管理（上）(更多IT教程 微信352852792) | 1 | 5621 | `8-2_Resources多维度集群资源管理之上_requests与limits落地到cgroup.md` |
| done | 59 | Resources---多维度集群资源管理（下）(更多IT教程 微信352852792) | 1 | 6624 | `8-3_Resources多维度集群资源管理之下_LimitRange与ResourceQuota落地.md` |
| done | 60 | Label---小标签大作为(更多IT教程 微信352852792) | 1 | 5990 | `8-4_Label小标签大作为_selector匹配与nodeSelector调度.md` |
| done | 61 | 健康检查---高可用的守护者(更多IT教程 微信352852792) | 1 | 7054 | `9-1_健康检查高可用的守护者_两种探针与三种探测方式.md` |
| done | 62 | Scheduler--- 玩转pod调度（上）(更多IT教程 微信352852792) | 1 | 4236 | `9-2_Scheduler玩转pod调度之上_优先级队列与nodeAffinity.md` |
| done | 63 | Scheduler --- 玩转pod调度（下）(更多IT教程 微信352852792) | 1 | 3992 | `9-3_Scheduler玩转pod调度之下_podAffinity与污点容忍.md` |
| done | 64 | 部署策略详解 --- 重建、滚动、蓝绿、金丝雀(更多IT教程 微信352852792) | 1 | 7177 | `9-4_部署策略详解_重建滚动更新蓝绿金丝雀与rollout.md` |
| done | 65 | 深入Pod - pod相关的点点滴滴（上）(更多IT教程 微信352852792) | 1 | 5744 | `9-5_深入Pod之上_pause容器与网络存储共享及生命周期钩子.md` |
| done | 66 | 深入Pod - pod相关的点点滴滴（下）(更多IT教程 微信352852792) | 1 | 6545 | `9-6_深入Pod之下_ProjectedVolume与SecretConfigMapDownwardAPI.md` |

## 节流约定（防 429）

- 一次只推进**一组**，不并发、不一次读多个大文件
- 每写完一篇 `sleep 45~60`；每 6 篇 `sleep 300`
- 中断随时可从 `pending` 行续跑，不重跑全量

## 已落盘产物
- `9-4_部署策略详解_重建滚动更新蓝绿金丝雀与rollout.md`
- `9-5_深入Pod之上_pause容器与网络存储共享及生命周期钩子.md`
- `9-6_深入Pod之下_ProjectedVolume与SecretConfigMapDownwardAPI.md`
- `8-4_Label小标签大作为_selector匹配与nodeSelector调度.md`
- `9-1_健康检查高可用的守护者_两种探针与三种探测方式.md`
- `9-2_Scheduler玩转pod调度之上_优先级队列与nodeAffinity.md`
- `9-3_Scheduler玩转pod调度之下_podAffinity与污点容忍.md`
- `7-5_CICD实践之四_发布后健康检查与kubectl认证踩坑.md`
- `8-1_Namespace集群的共享与隔离.md`
- `8-2_Resources多维度集群资源管理之上_requests与limits落地到cgroup.md`
- `8-3_Resources多维度集群资源管理之下_LimitRange与ResourceQuota落地.md`

- `5-3_Harbor高可用部署之下_域名访问用户授权双主复制规则与镜像推送拉取.md`

- `5-2_Harbor高可用部署之上_两个worker节点安装Harbor与nginx负载均衡.md`

- `5-1_Harbor入门云原生镜像仓库的特性架构与高可用方案选型.md`

- `4-3_二进制高可用集群部署之下_三节点控制面补齐与worker加入kubeletbootstrap和kube-proxy.md`

- `4-2_二进制高可用集群部署之上-etcd三节点与apiserverkeepalivedkubectl落地.md`

- `3-4_部署KubernetesDashboard与Token登录和nginx代理访问.md`

- `3-3_集群可用性测试Pod网络Service与DNS四项验证.md`

- `3-2_kubeadm高可用集群部署之keepalivedetcd三master与calico落地.md`

- `3-1_用kubeadm搭建高可用集群的实践环境准备.md`

- `2-6_三种集群搭建方案对比社区方案kubeadm与二进制.md`

- `2-5_Kubernetes三种认证方式RBAC授权与准入控制.md`

- `2-4_Kubernetes认证的密码学原理与TLS握手.md`

- `2-3_Kubernetes集群架构与核心组件工作流.md`

- `2-2_Pod副本集Deployment与Service的核心概念.md`

- `2-1_了解Kubernetes的名字由来与核心特征.md`

- `12-11_用Grafana看板与Kiali做网格可视化管理.md`

- `12-10_用Jaeger与Zipkin做分布式链路追踪.md`

- `12-9_Istio遥测之Mixer收集指标与Prometheus查询.md`

- `12-8_Istio智能路由之请求路由故障注入与流量迁移.md`

- `12-7_部署Bookinfo示例应用并通过Istio网关访问.md`

- `12-6_补kube-proxy与CoreDNShosts插件让MetricsServer跑通.md`

- `12-5_MetricsServer部署与apiserver授权证书补齐.md`

- `12-4_Istio核心组件与Gateway端口排错及MetricsServer补位.md`

- `12-3_下载Istio发行版与istio-init安装踩坑.md`

- `12-2_Istio的架构原理EnvoyPilotMixerGalleyCitadel.md`

- `12-1_ServiceMesh概念与LinkerdIstio两大实现对比.md`

- `11-9_报警规则Grafana看板与Alertmanager邮件告警打通.md`

- `11-8_ETCD证书Secret配置与重装Operator清理CRD.md`

- `11-7_PrometheusWeb界面与Targets巡检及组件指标补齐.md`

- `11-6_用本地chart部署PrometheusOperator并打通访问入口.md`

- `11-5_Helm包管理与Tiller安装以及Operator原理.md`

- `11-4_Prometheus的架构组件与四种指标类型.md`

- `11-3_监控体系的目标采集流程与监控对象.md`

- `11-2_LogPilot加ES加Kibana的日志采集落地.md`

- `11-1_容器日志采集的三种方案对比与LogPilot原理.md`

- `10-7_KubernetesAPI的分组版本设计与REST接口实战.md`

- `10-6_StatefulSet的有序启动与独立持久存储.md`

- `10-5_用Heketi初始化GlusterFS并让StorageClass动态供给PV.md`

- `10-4_共享存储_PV_PVC与StorageClass的绑定机制.md`

- `10-3_ingress_nginx的会话保持与金丝雀流量控制.md`

- `10-2_ingress_nginx自定义响应头配置模板与TLS证书配置.md`

- `10-1_ingress_nginx的DaemonSet部署与四层TCP代理.md`
- `5-4_Kubernetes的服务发现与通讯的三种场景.md`
- `5-5_部署ingress-nginx之上_Ingress概念与控制清单逐段解读.md`
- `5-6_部署ingress-nginx之下_hostNetwork暴露入口与域名实测.md`
- `6-1_定时任务迁移Kubernetes之镜像制作与CronJob调度.md`
- `6-3_SpringBootWeb服务迁移Kubernetes之镜像与三段配置.md`
- `6-5_传统Dubbo服务迁移Kubernetes之上_非SpringBoot项目的打包与镜像构建.md`
- `6-6_传统Dubbo服务迁移Kubernetes之下_host模式注册与端口集中管理.md`
- `7-1_Kubernetes与CI-CD流程变迁_从停起式发布到镜像化滚动发布.md`
- `7-2_CICD实践之一_Jenkins安装与拉代码加Maven构建流水线.md`
- `7-3_CICD实践之二_构建镜像脚本与Dockerfiles目录规范化.md`
- `7-4_CICD实践之三_推送镜像配置模板化与deploy脚本.md`
