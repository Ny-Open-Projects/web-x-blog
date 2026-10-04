# 4.k8s4-cka → 博客 转换进度

状态：`pending` 待处理 / `done` 已完成 / `skip` 跳过（导学、课程总结、本章未完结）
**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**

| 状态 | # | 组名 | 文件数 | 总字数 | 产出博客 |
| --- | --- | --- | --- | --- | --- |
| skip | 1 | CKA认证实战班介绍 | 1 | 4395 | `1-1` 起 |
| done | 2 | K8s介绍 | 1 | 6957 | `1-2_有了Docker为什么还要K8s_分层关系.md` |
| done| 3 | K8s架构与核心概念 | 1 | 3849 | `1-3_K8s集群架构与五大核心概念.md` |
| done| 4 | 熟悉官方文档 | 1 | 5698 | `1-4_熟悉官方文档_考点分布与搜索技巧.md` |
| done| 5 | 应用程序故障排查 | 1 | 5875 | `10-1_应用程序故障排查_从Pod事件到容器日志.md` |
| done| 6 | 管理节点故障排查 | 1 | 4066 | `10-2_管理节点故障排查_区分kubeadm与二进制部署.md` |
| done| 7 | Service访问故障排查 | 2 | 20410 | `10-3_Service访问故障排查_七步定位法.md` |
| done| 8 | 容器交付流程 | 1 | 3641 | `11-1_容器交付流程_从本地开发到持续交付.md` |
| done| 9 | 在K8s平台部署项目流程 | 1 | 1349 | `11-2_在K8s平台部署项目的四个步骤.md` |
| done| 10 | 制作镜像并推送到镜像仓库 | 1 | 11215 | `11-3_制作镜像并推送到镜像仓库_从编译到Harbor.md` |
| done| 11 | 使用工作负载控制器部署镜像 | 1 | 4148 | `11-4_使用工作负载控制器部署镜像_Deployment与imagePullSecrets.md` |
| done| 12 | 使用configmap存储项目配置文件 | 1 | 2950 | `11-5_使用ConfigMap存储项目配置文件_挂载与subPath.md` |
| done| 13 | 对外暴露应用访问 | 1 | 7591 | `11-6_对外暴露应用访问_Service与Ingress.md` |
| done| 14 | 将项目暴露到公网访问 | 1 | 1736 | `11-7_将项目暴露到公网访问_负载均衡器方案.md` |
| done| 15 | 个CKA考试真题解析 | 1 | 24964 | `12-1-30_30道CKA考试真题解析.md` |
| done| 16 | CKA考试准备 | 1 | 2258 | `12-2_CKA考试准备_考试形式环境要求与答题技巧.md` |
| skip| 17 | 考试期间注意事项 | 1 | 438 | `12-3` 起 |
| done| 18 | 环境准备 | 1 | 8905 | `2-1_环境准备_集群规划主机初始化与部署选型.md` |
| done| 19 | 部署Master | 1 | 6628 | `2-2_部署Master_容器引擎安装与kubeadm初始化.md` |
| done| 20 | 部署Node | 1 | 1358 | `2-3_部署Node_kubeadmjoin加入节点与NotReady定位.md` |
| done| 21 | 部署CNI插件和Dashboard | 1 | 3009 | `2-4_部署CNI插件与Dashboard_节点Ready与token登录.md` |
| done| 22 | 部署过程中3个常见问题 | 1 | 6243 | `2-5_部署中3个常见问题_Token过期证书不受信与kubeadmreset.md` |
| done| 23 | 网络方案之Flannel | 1 | 4087 | `2-6_CNI网络方案选型_Flannel路由隧道模式与VXLAN原理.md` |
| done| 24 | 网络方案之Calico | 1 | 4859 | `2-7_网络方案之Calico_从flannel切换Pod网段与IPIP模式.md` |
| done| 25 | kubectl命令行管理工具 | 1 | 9167 | `2-8_kubectl命令行工具_命令分类自动补全与通用选项.md` |
| done| 26 | kubectl多集群管理 | 1 | 10816 | `2-9_kubectl多集群管理_kubeconfig结构与上下文切换.md` |
| done| 27 | 个命令查看集群资源状况 | 1 | 4969 | `3-1_5个命令查看集群资源状况_getnodes_cs_describe_wide_watch.md` |
| done| 28 | Metrics Server 监控数据聚合器部署 | 1 | 4867 | `3-2_MetricsServer部署_打通kubectltop数据链路.md` |
| done| 29 | 监控资源利用率 | 1 | 3043 | `3-3_监控资源利用率_API聚合层_top排序与CPU单位.md` |
| done| 30 | 管理 K8s 组件日志 | 1 | 4841 | `3-4_管理K8s组件日志_journalctl与kubectllogs两类日志形态.md` |
| done| 31 | 管理 K8s 应用程序日志 | 1 | 4602 | `3-5_管理K8s应用程序日志_hostPath与emptyDir挂载日志.md` |
| done| 32 | 在Kubernetes部署应用流程 | 1 | 2299 | `4-1_在K8s部署应用流程_镜像控制器暴露与发布四步.md` |
| done| 33 | Pod对象：InitContainer | 1 | 7042 | `4-10_初始化容器InitContainer_执行顺序与应用场景.md` |
| done| 34 | Pod对象：静态Pod | 1 | 2211 | `4-11_静态Pod_静态Pod目录机制与删除特性.md` |
| done | 35 | 使用Deployment控制器部署应用 | 1 | 6875 | `4-2_使用Deployment控制器部署应用_命令行部署与暴露.md` |
| done | 36 | YAML创建资源对象（上） | 1 | 2691 | `4-3_YAML创建资源对象上_服务编排与格式注意事项.md` |
| done | 37 | YAML创建资源对象（下） | 1 | 1858 | `4-4_YAML创建资源对象下_字段结构与标签选择器.md` |
| done | 38 | 字段很多，记不住怎么办？ | 1 | 4173 | `4-5_字段很多记不住怎么办_dryrun生成与导出改写.md` |
| done | 39 | 应用升级、弹性伸缩、回滚、删除 | 1 | 8349 | `4-6_应用升级弹性伸缩回滚删除_滚动更新原理.md` |
| done | 40 | Pod对象：Pod存在的意义 | 1 | 4419 | `4-7_Pod对象_Pod存在的意义与亲密型应用.md` |
| done | 41 | Pod对象：Pod中容器分类 | 1 | 2751 | `4-8_Pod对象_Pod中容器分类_infra与init与业务容器.md` |
| done | 42 | Pod对象：应用自修复 | 1 | 10068 | `4-9_Pod对象_应用自修复_重启策略与健康检查.md` |
| done | 43 | 创建一个Pod的工作流程 | 1 | 6475 | `5-1_创建一个Pod的工作流程_组件协作与listwatch.md` |
| done | 44 | Pod中调度影响调度的属性 | 1 | 1330 | `5-2_Pod中影响调度的属性_六字段速览.md` |
| done | 45 | 资源限制对Pod调度影响 | 1 | 4850 | `5-3_资源限制对Pod调度影响_requests与limits.md` |
| done | 46 | 节点标签选择器nodeSelector | 1 | 3345 | `5-4_节点标签选择器nodeSelector_把Pod固定到一类节点.md` |
| done | 47 | 节点亲和性 nodeAffinity | 1 | 4881 | `5-5_节点亲和性nodeAffinity_硬策略与软策略.md` |
| done | 48 | 污点与污点容忍 | 1 | 5948 | `5-6_污点与污点容忍_taint与toleration.md` |
| done | 49 | 绕过调度器 nodename | 1 | 1693 | `5-7_绕过调度器nodeName_绝对指定节点.md` |
| done | 50 | 每个节点起一个Pod（daemonset） | 1 | 2679 | `5-8_DaemonSet每个节点起一个Pod_守护进程集.md` |
| done | 51 | 调度原因分析 | 1 | 1386 | `5-9_调度失败原因分析_三种常见Pending.md` |
| done | 52 | Service存在的意义 | 1 | 7432 | `6-1_Service存在的意义_服务发现与负载均衡.md` |
| done | 53 | Ingress HTTP | 1 | 2926 | `6-10_Ingress_HTTP_用域名暴露应用.md` |
| done | 54 | Ingress HTTPS | 1 | 4379 | `6-11_Ingress_HTTPS_自签证书与Secret引用.md` |
| done | 55 | Ingress工作原理及高可用方案 | 1 | 5235 | `6-12_Ingress工作原理与高可用方案.md` |
| done | 56 | Service ClusterIP类型（上） | 1 | 4153 | `6-2_Service_ClusterIP类型上_创建与标签端口.md` |
| done | 57 | Service ClusterIP类型（下） | 1 | 1216 | `6-3_Service_ClusterIP类型下_虚拟IP与跨主机网络.md` |
| done | 58 | Service NodePort类型 | 1 | 4175 | `6-4_Service_NodePort类型_对外暴露与kubeproxy.md` |
| done | 59 | Service Loadbalancer类型 | 1 | 3346 | `6-5_Service_LoadBalancer类型_公有云自动挂LB.md` |
| done | 60 | 代理模式：Iptables与ipvs | 1 | 6313 | `6-6_代理模式_iptables与ipvs_转发规则落地.md` |
| skip | 61 | Service DNS解析 | 1 | 0 | `6-7` 源文件为空，无素材可写 |
| done | 62 | Ingress为弥补NodePort不足而生 | 1 | 6390 | `6-8_Ingress为弥补NodePort不足而生_四层与七层.md` |
| done | 63 | Ingress Controller | 1 | 7916 | `6-9_Ingress_Controller_部署与hostNetwork暴露.md` |
| skip | 64 | 数据卷概述 | 1 | 0 | `7-1` 源文件为空，无素材可写 |
| done | 65 | Statefulset之稳定的网络ID | 1 | 5130 | `7-10_StatefulSet之稳定的网络ID_HeadlessService.md` |
| done | 66 | Statefulset之稳定的存储 | 1 | 4156 | `7-11_StatefulSet之稳定的存储_volumeClaimTemplates.md` |
| done | 67 | ConfigMap配置文件存储 | 1 | 8337 | `7-12_ConfigMap存储配置文件_变量注入与卷挂载.md` |
| done | 68 | Secret存储敏感信息 | 1 | 4150 | `7-13_Secret存储敏感信息_编码与动态注入.md` |
| done | 69 | 临时存储卷：emptyDir | 1 | 3226 | `7-2_临时存储卷emptyDir_Pod内容器共享数据.md` |
| done | 70 | 节点存储卷：hostPath | 1 | 2267 | `7-3_节点存储卷hostPath_挂载宿主机目录.md` |
| done | 71 | 网络卷NFS | 1 | 6441 | `7-4_网络卷NFS_跨节点共享存储.md` |
| done | 72 | 持久数据卷概述 | 1 | 2901 | `7-5_持久数据卷概述_PV与PVC职责分离.md` |
| done | 73 | 静态PV供给（上） | 1 | 4588 | `7-6_静态PV供给上_存储池创建与自动绑定.md` |
| done | 74 | 静态PV供给（下） | 1 | 1868 | `7-7_静态PV供给下_多Pod共享验证与PV释放.md` |
| done | 75 | 动态PV供给 | 1 | 8493 | `7-8_动态PV供给_StorageClass与自动创建PV.md` |
| done | 76 | 有状态部署与无状态部署区别 | 1 | 2959 | `7-9_有状态部署与无状态部署区别_两个判断标准.md` |
| done | 77 | K8s安全框架 | 1 | 9342 | `8-1_K8s安全框架_认证授权准入三道关卡.md` |
| done | 78 | RBAC 概述 | 1 | 1281 | `8-2_RBAC概述_角色角色绑定与主体三件套.md` |
| done | 79 | 案例：为指定用户授权访问不同命名空间权限（上） | 1 | 7443 | `8-3_案例_为指定用户授权不同命名空间权限上_签发证书与kubeconfig.md` |
| done | 80 | 案例：为指定用户授权访问不同命名空间权限（下） | 1 | 2924 | `8-4_案例_为指定用户授权不同命名空间权限下_kubeconfig默认路径与主题三种类型.md` |
| done | 81 | 网络策略概述 | 1 | 6032 | `8-5_网络策略概述_Pod级入出流量隔离与CNI插件依赖.md` |
| done | 82 | 案例：对项目Pod出入流量访问控制 | 1 | 4829 | `8-6_案例_项目Pod出入流量访问控制_两则网络策略实战.md` |
| done | 83 | 二进制部署环境介绍 | 1 | 5648 | `9-1_二进制部署环境介绍_目录结构与配置文件三件套.md` |
| done | 84 | Bootstrap Token方式增加Node | 1 | 9745 | `9-2_BootstrapToken方式增加Node_四步配置与CSR审批.md` |
| done | 85 | K8s集群证书续签（kubeadm） | 1 | 5434 | `9-3_K8s集群证书续签kubeadm_证书清单与三种解法.md` |
| done | 86 | Etcd数据库备份与恢复 | 1 | 7109 | `9-4_Etcd数据库备份与恢复_快照备份与restore流程.md` |

## 节流约定（防 429）

- 一次只推进**一组**，不并发、不一次读多个大文件
- 每写完一篇 `sleep 45~60`；每 6 篇 `sleep 300`
- 中断随时可从 `pending` 行续跑，不重跑全量

## 已落盘产物
