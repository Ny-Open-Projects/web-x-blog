# 2.k8s2-KCNA → 博客 转换进度

状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、课程总结、本章未完结）
**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**

| 状态 | # | 组名 | 文件数 | 总字数 | 产出博客 |
| --- | --- | --- | --- | --- | --- |
| skip   | 1 | 课程导学 | 1 | 3041 |  导学/小结，不写文  |
| skip   | 2 | 本章导学_ev【 微信号：itcodeba 】 | 4 | 2708 |  导学/小结，不写文  |
| done   | 3 | 用K8S NodePort Service暴露服务的问_ev【 微信号：itcodeba 】 | 1 | 956 |  10.2-10-2_NodePort暴露服务的代价与适用边界.md  |
| done   | 4 | 在K8S上部署、配置和使用Ingress介绍_ev【 微信号：itcodeba 】 | 1 | 1691 |  10.3-10-3_在K8s上部署配置和使用Ingress的完整链路.md  |
| done   | 5 | 部署Ingress和配置Web服务转发_ev【 微信号：itcodeba 】 | 1 | 2050 |  10.4-10-4_部署Ingress实例与80端口Web服务转发规则.md  |
| done   | 6 | 配置Ingress支持gRPC服务转发_ev【 微信号：itcodeba 】 | 1 | 1238 |  10.5-10-5_用TLS证书与annotation为Ingress配置gRPC转发.md  |
| done   | 7 | 对比使用LB作为入口的差异_ev【 微信号：itcodeba 】 | 1 | 1213 |  10.6-10-6_NodePort_Ingress_与负载均衡器的入口选型对比.md  |
| done   | 8 | Ingress部署中常见问题汇总_ev【 微信号：itcodeba 】 | 1 | 778 | `10.7-10-7_Ingress部署中的三类高频故障与排查路径.md` |
| skip   | 9 | 本章小结_ev【 微信号：itcodeba 】 | 8 | 7829 |  导学/小结，不写文  |
| done   | 10 | 在K8S上部署Helm_ev【 微信号：itcodeba 】 | 文件数 | --- | 11.2-11-2_在K8s上部署Helm与tiller架构的演进.md  |
| done   | 11 | 给用户积分等级服务编写自定义Chart_ev【 微信号：itcodeba 】 | 文件数 | --- | 11.3-11-3_给用户积分等级服务编写自定义Chart.md  |
| done   | 12 | 用Helm安装、升级应用_ev【 微信号：itcodeba 】 | 文件数 | --- | 11.4-11-4_用Helm安装升级应用与命名空间的两个坑.md  |
| done   | 13 | ServiceMesh介绍_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.2-12-2_ServiceMesh是什么_边车代理构成的数据平面.md  |
| done   | 14 | Istio的原理_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.3-12-3_Istio的原理_Envoy边车与控制平面的分工.md  |
| done   | 15 | Istio的能力_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.4-12-4_Istio的三类能力_流量治理可观测与安全.md  |
| done   | 16 | K8S集群中应用Istio实现服务治理-创建集群（一）_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.5-12.5_用Istio做服务治理的准备_建集群建网格开注入部署v1v2.md  |
| done   | 17 | K8S集群中应用Istio实现服务治理-故障注入（二）_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.6-12.6_用Istio做TCP路由转发与四类故障注入.md  |
| done   | 18 | K8S集群中应用Istio实现服务治理-限速（三）_ev【 微信号：itcodeba 】 | 文件数 | --- | 12.7-12.7_用Envoy过滤器扩展Istio实现速率限制.md  |
| skip   | 19 | 云原生的监控、告警和日志服务-本章导学_ev【 微信号：itcodeba 】 | 文件数 | --- | 导学/小结，不写文  |
| done   | 20 | 云原生的Prometheus_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.2-13.2-1_云原生的Prometheus架构与采集链路.md  |
| done   | 21 | 云原生的Prometheus-集成SDK_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.3-13-3-2_用prometheus_client把自定义指标接进服务.md  |
| done   | 22 | Prometheus+Grafana避坑指南_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.5-13.5_Prometheus与Grafana的五个避坑要点.md  |
| done   | 23 | 本地安装和使用的演示_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.6-13.6-3_本地安装Prometheus与Grafana并配出第一张面板.md  |
| done   | 24 | 云原生的日志服务_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.7-13.7-2_云原生日志服务的采集投递与检索链路.md  |
| done   | 25 | 日志服务的成本优化_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.8-13.8-3_日志服务成本优化的六个抓手.md  |
| done   | 26 | 什么是云原生？_ev【 微信号：itcodeba 】 | 文件数 | --- | 13.9-13.9-2_到底什么才算云原生.md  |
| skip   | 27 | K8S监控及告警，让系统风险无处遁逃-本章导学_ev【 微信号：itcodeba 】 | 文件数 | --- | 导学/小结，不写文  |
| done   | 28 | Prometheus+AlertManager监控及告_ev【 微信号：itcodeba 】 | 文件数 | --- | 14.2-14-2-2_Prometheus与AlertManager监控告警体系的分工.md  |
| done   | 29 | 启用Prometheus和Grafana服务_ev【 微信号：itcodeba 】 | 文件数 | --- | 14.3-14-3-2_在K8s集群中部署监控服务并用Ingress暴露.md  |
| done   | 30 | 配置AlertManager告警_ev【 微信号：itcodeba 】 | 文件数 | --- | 14.4-14-4-2_配置Prometheus告警规则与AlertManager邮件告警.md  |
| done   | 31 | 在Grafana中查看服务的资源使用情况_ev【 微信号：itcodeba 】 | 文件数 | --- | 14.5-14-5-2_用动态服务发现采集K8s指标并在Grafana出资源报表.md  |
| done   | 32 | 通过代码实现Prometheus自定义告警_ev【 微信号：itcodeba 】 | 文件数 | --- | 14.6-14-6-2_用webhook接口代码实现自定义告警通知.md  |
| skip   | 33 | 试试服务的抗压能力-本章导学_ev【 微信号：itcodeba 】 | 文件数 | --- | 导学/小结，不写文  |
| done   | 34 | 压测的重要性_ev【 微信号：itcodeba 】 | 文件数 | --- | 15.2-15-2-1_压测为什么重要_五个理由与两类方法.md  |
| done   | 35 | 用wrk对服务做压力测试_ev【 微信号：itcodeba 】 | 文件数 | --- | 15.3-15-3-2_用wrk对服务做压力测试与参数调优.md  |
| done   | 36 | 分析wrk的压测报告_ev【 微信号：itcodeba 】 | 文件数 | --- | 15.4-15-4-2_读懂wrk压测报告的重点指标与性能梯度.md  |
| skip   | 37 | KCNA认证试题讲解-本章导学_ev【 微信号：itcodeba 】 | 文件数 | --- | 导学/小结，不写文  |
| done   | 38 | KCNA典型真题实操讲解（一）_ev【 微信号：itcodeba 】 | 文件数 | --- | 16.2-16-2-2_KCNA真题讲解一_云原生特征OCI与Serverless.md  |
| done   | 39 | KCNA典型真题实操讲解（二）_ev【 微信号：itcodeba 】 | 文件数 | --- | 16.3-16-3-2_KCNA真题讲解二_ServiceMesh到K8s基础概念.md  |
| done   | 40 | KCNA典型真题实操讲解（三）_ev【 微信号：itcodeba 】 | 文件数 | --- | 16.4-16-4-2_KCNA真题讲解三_CD术语GitOps与多选题.md  |
| done   | 41 | 更多的相关认证介绍_ev【 微信号：itcodeba 】 | 文件数 | --- | 16.5-16-5-2_更多相关认证介绍_CKA_CKAD_CKS与PCA.md  |
| skip   | 42 | 本章导学 | 7 | 7274 |  导学/小结，不写文  |
| skip   | 43 | 本章小结 | 文件数 | --- | 导学/小结，不写文  |
| done   | 44 | 后台技术架构的发展史 | 文件数 | --- | 2.2-2-2-3_后台技术架构的发展史_从单体到云原生.md  |
| done   | 45 | 服务发现与负载均衡 | 文件数 | --- | 2.3-2-4-2_服务发现与负载均衡_注册中心与两种模式.md  |
| done   | 46 | 从设计模式角度理解API网关 | 文件数 | --- | 2.4-2-6-2_从设计模式角度理解API网关_五个模式与两组能力.md  |
| done   | 47 | 服务调用的限频、限流、降级和熔断 | 文件数 | --- | 2.5-2-7-2_服务调用的限频限流降级与熔断.md  |
| done   | 48 | 为什么选择kubernets作为微服务框架 | 文件数 | --- | 2.9-2-12-2_为什么选择Kubernetes作为微服务框架.md  |
| done   | 49 | 第一个gRPC案例演示 | 文件数 | --- | 3.2-3-2-2_第一个gRPC案例演示.md  |
| done   | 50 | 设计模式之代理模式 | 文件数 | --- | 3.3-3-3-2_设计模式之代理模式.md  |
| done   | 51 | 从源码学习gRPC设计的概述 | 文件数 | --- | 3.4-3-5-2_从源码学习gRPC设计的概述.md  |
| done   | 52 | proto3使用及编解码原理介绍 | 文件数 | --- | 3.5-3-7-2_proto3使用及编解码原理.md  |
| done   | 53 | gRPC自定义protoc插件 | 文件数 | --- | 3.7-3-8-2_gRPC自定义protoc插件.md  |
| done   | 54 | 客户端与服务器通信流程 | 文件数 | --- | 3.8-3-9-2_客户端与服务器通信流程.md  |
| done   | 55 | K8S的核心组件 | 文件数 | --- | 4.2-4-2-2_K8S的核心组件.md  |
| done   | 56 | K8S的资源 | 文件数 | --- | 4.3-4-3-2_K8S的资源分类.md  |
| done   | 57 | APIServer原理 | 文件数 | --- | 4.4-4-5-2_APIServer原理.md  |
| done   | 58 | ControllerManager原理 | 文件数 | --- | 4.5-4-7-2_ControllerManager原理.md  |
| done   | 59 | Scheduler原理 | 文件数 | --- | 4.6-4-9-2_Scheduler原理.md  |
| done   | 60 | Kubelet原理 | 文件数 | --- | 4.7-4-11-2_Kubelet原理.md  |
| done   | 61 | Pod创建和启动流程 | 文件数 | --- | 4.8-4-13-2_Pod创建和启动流程.md  |
| done   | 62 | 腾讯云上的K8S集群选择和搭建 | 文件数 | --- | 5.2-5-2-2_腾讯云上K8S集群的选择和搭建.md  |
| done   | 63 | 使用kubeadm手动搭建k8s集群-手动 | 文件数 | --- | 5.3-5-3-2_使用kubeadm手动搭建K8s集群.md  |
| done   | 64 | 服务伸缩性的实现和原理 | 文件数 | --- | 5.4-5-4-2_服务伸缩性的实现和原理.md  |
| done   | 65 | 编写Docker文件，制作服务的运行镜像 | 文件数 | --- | 5.5-5-6-2_编写Dockerfile制作服务的运行镜像.md  |
| done   | 66 | 将服务的运行镜像部署到K8S集群中 | 文件数 | --- | 5.6-5-7-2_将服务的运行镜像部署到K8S集群中.md  |
| done   | 67 | 集群与服务的管理和配置 | 文件数 | --- | 5.7-5-8-2_集群与服务的管理和配置.md  |
| done   | 68 | 作业-动手实践 | 文件数 | --- | 5.8-5-9-2_作业-动手实践.md  |
| done   | 69 | 镜像仓库与Dockerfile的使用和管理 | 文件数 | --- | 5.9-5-10-2_镜像仓库与Dockerfile的使用和管理.md  |
| done   | 70 | 常见的用户成长系统设计 | 文件数 | --- | 6.2-6-2-2_常见的用户成长体系设计.md  |
| done   | 71 | 用户积分的作用和设计 | 文件数 | --- | 6.3-6-3-2_用户积分的作用和设计.md  |
| done   | 72 | 用户等级的作用和设计 | 文件数 | --- | 6.4-6-4-2_用户等级的作用和设计.md  |
| done   | 73 | 详细的数据库设计 | 文件数 | --- | 6.5-6-5-2_详细的数据库设计.md  |
| done   | 74 | 讨论：用户成长体系，简单好还是复杂好 | 文件数 | --- | 6.6-6-6-2_讨论_用户成长体系简单好还是复杂好.md  |
| done   | 75 | gRPC常见的配置参数说明 | 文件数 | --- | 7.10-7-10-2_gRPC常见的配置参数说明.md  |
| done   | 76 | gRPC使用中的常见问题及解决方案 | 1 | 1102 |  7.11-7-11-2_gRPC使用中的常见问题及解决方案.md  
| done   | 77 | 设计和编写Protobuf文件 | 1 | 2996 |  7.2-7-2-2_设计和编写Protobuf文件.md  
| done   | 78 | 自动生成框架代码，验证服务 | 1 | 3455 |  7.3-7-3-2_自动生成框架代码并验证服务.md  
| done   | 79 | models-dbhelper实现用户积分和等级系统的数据 | 1 | 3632 |  7.4-7-4-2_models与dbhelper实现数据模型与连接封装.md  
| done   | 80 | dao-service实现用户积分和等级系统的数据层、服务 | 1 | 3573 |  7.5-7-5-2_dao与service实现数据层与服务层.md  
| done   | 81 | 对服务层代码进行单元测试 | 1 | 3037 |  7.6-7-6-2_对服务层代码进行单元测试.md  
| done   | 82 | coin实现系统的应用层代码 | 1 | 4671 |  7.7-7-7-2_coin实现用户积分服务的应用层代码.md  
| done   | 83 | grade实现系统的应用层代码 | 1 | 3022 |  7.8-7-8-2_grade实现用户等级服务的应用层代码.md  
| done   | 84 | 验证用户积分等级系统的效果 | 1 | 1010 |  7.9-7-9-2_验证用户积分等级系统的效果.md  
| done   | 85 | gin路由框架使用 | 1 | 2255 |  8.2-8-2-2_gin路由框架使用.md  
| done   | 86 | 使用gRPC连接池复用连接 | 1 | 1899 |  8.3-8-3-2_使用gRPC连接池复用连接.md  
| done   | 87 | 用反射简化gRPC的调用 | 1 | 2273 |  8.4-8-4-2_用反射简化gRPC的调用.md  
| done   | 88 | gRPC服务转RestfulAPI-gin框架 | 1 | 2973 |  8.5-8-5-2_gRPC服务转RestfulAPI之gin框架.md  
| done   | 89 | gRPC服务转RestfulAPI-grpc-gatewa | 1 | 2984 |  8.6-8-6-2_gRPC服务转RestfulAPI之grpc-gateway.md  
| done   | 90 | 增加CORS跨域支持 | 1 | 3517 |  8.7-8-7-2_增加CORS跨域支持.md  
| done   | 91 | 讨论：为什么不用python实现restfulapi | 1 | 443 |  8.8-8-8-2_讨论为什么不用python实现restfulAPI.md  
| done   | 92 | K8S服务发现与负载均衡原理_ev【 微信号：itcodeba 】 | 1 | 3510 |  9.2-9-2-2_K8s服务发现与负载均衡原理.md  
| done   | 93 | 测试K8S服务的负载均衡_ev【 微信号：itcodeba 】 | 1 | 5098 |  9.3-9-3-2_测试K8s服务的负载均衡.md  
| done   | 94 | gRPC的天坑：K8S负载均衡失效_ev【 微信号：itcodeba 】 | 1 | 1410 |  9.4-9-4-2_gRPC的天坑K8s负载均衡失效.md  
| done   | 95 | Headless解决K8S负载均衡失效的问题_ev【 微信号：itcodeba 】 | 1 | 1327 |  9.5-9-5-2_Headless解决K8s负载均衡失效的问题.md  
| done   | 96 | 集群内服务之间的调用_ev【 微信号：itcodeba 】 | 1 | 1035 |  9.6-9-6-2_集群内服务之间的调用.md  

## 节流约定（防 429）

- 一次只推进**一组**，不并发、不一次读多个大文件
- 每写完一篇 `sleep 45~60`；每 6 篇 `sleep 300`
- 中断随时可从 `pending` 行续跑，不重跑全量

## 已落盘产物
