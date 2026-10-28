---
disableNunjucks: true
title: "mksz892 云原生 CI/CD → 博客 转换进度（相近主题合并版 + 代码关联）"
date: 2026-10-15 00:52:26
categories: [云原生CI/CD实战]
tags: [云原生CI/CD实战]
---

**合并原则**：只合并「人为拆分的薄篇」与「同主题连续篇」，源内容全部保留（不减少字数）；主题边界清晰的大篇保持独立。176 篇源讲稿 → **90 篇博客**。

**代码关联**：156 个课件代码文件 100% 关联到文章（见「关联代码」列）；标  的 16 篇为导学/方案/无配套代码篇，文中如实标注，不虚构路径。

**质量红线（字节口径，覆盖正文+代码+mermaid）**：单篇产出字节 / 合并源字数 **≥ 3.0x**（合并篇按源字数等比加深，不减总量）。实测 7 篇：最低 4.0x、最高 14.2x、合计 5.9x。

状态：`pending` 待处理 / `done` 已完成

**agent 每写完一篇，把该行状态改成 `done` 并填上产出文件名。**

| 状态 | # | 章 | 标题 | 合并源篇 | 源字符数 | 关联代码 | 产出博客 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| done | 1 | 1 | 云原生 CI/CD 课程导学：一门课打通 Jenkins、Tekton、Drone 到 Argo CD | 1-1 | 2177 | — | `work/target/mksz892/1-1_云原生CI-CD课程导学.md` |
| done | 2 | 2 | 为什么要学云原生 CI/CD：岗位价值与学习路线 | 2-1 + 2-2 | 889 | — |   `work/target/mksz892/2_为什么要学云原生CICD.md` |
| done | 3 | 2 | 云原生 CI/CD 工程化实践的工具有哪些？如何选型及构建最优技术方案 | 2-3 | 2352 | — |   `work/target/mksz892/3_云原生CICD工具全景与选型方法论.md` |
| done | 4 | 3 | Jenkins 是什么：CI 工具定位与核心概念 | 3-1 + 3-2 | 746 | 教学课件.md、Jenkinsfile-流水线基础（基础课程所有笔记都在此文件） |   `work/target/mksz892/4_Jenkins是什么与本章学习地图.md` |
| done | 5 | 3 | Jenkins 三种部署方式：Docker / Helm / 原生 YAML | 3-3 + 3-4 + 3-5 | 3912 | install.sh、jenkins-sa.yaml、jenkins-values.yaml、namespace.yaml、deployment.yaml、service.ya… |   `work/target/mksz892/5_Jenkins三种部署方式实战.md` |
| done | 6 | 3 | Jenkins 接入 OpenLDAP 统一认证 | 3-6 | 1245 | 教学课件.md |   `work/target/mksz892/6_Jenkins接入OpenLDAP统一认证.md` |
| done | 7 | 3 | Jenkins 多项配置：凭据体系、系统配置与项目规范 | 3-7 + 3-8 | 4324 | 教学课件.md、Jenkinsfile-流水线基础（基础课程所有笔记都在此文件） |   `work/target/mksz892/7_Jenkins基础配置四件套.md` |
| done | 8 | 3 | Role-Based Strategy 细粒度用户权限配置 | 3-9 | 3407 | 教学课件.md |   `work/target/mksz892/8_Jenkins精细化权限控制.md` |
| done | 9 | 3 | Pipeline 流水线介绍与基础语法 | 3-10 | 2695 | 教学课件.md、Jenkinsfile-流水线基础（基础课程所有笔记都在此文件） | `work/target/mksz892/3-10_Pipeline流水线介绍与基础语法.md` |
| done | 10 | 3 | 构建代理与 options 全局配置 | 3-11 + 3-12 | 4255 | 教学课件.md、Jenkinsfile-静态代理节点 |   `work/target/mksz892/10_构建代理与options全局配置.md` |
| done | 11 | 3 | sh 的三种用法与 Groovy 沙箱机制 | 3-13 + 3-14 | 1435 | 教学课件.md |   `work/target/mksz892/11_sh引号用法与Groovy沙箱.md` |
| done | 12 | 3 | 环境变量与凭据使用 | 3-15 + 3-16 | 2902 | 教学课件.md |   `work/target/mksz892/12_环境变量四种定义与凭据安全调用.md` |
| done | 13 | 3 | post 阶段、postbuild 与清理工作空间 | 3-17 + 3-18 + 3-24 | 2966 | 教学课件.md |   `work/target/mksz892/13_post条件块与清理工作空间.md` |
| done | 14 | 3 | 内置变量使用与构建信息展示 | 3-19 | 2095 | 教学课件.md |   `work/target/mksz892/14_内置变量与构建信息展示.md` |
| done | 15 | 3 | 如何生成声明式指令与计划任务 | 3-20 + 3-21 | 2323 | 教学课件.md |   `work/target/mksz892/15_声明式指令生成器与计划任务.md` |
| done | 16 | 3 | 并行执行与 Blue Ocean 蓝海项目 | 3-22 | 2721 | 教学课件.md |   `work/target/mksz892/16_并行执行与BlueOcean.md` |
| done | 17 | 3 | when 语法与 input 语法 | 3-23 | 3136 | Jenkinsfile-when语法2与input的使用、教学课件.md |   `work/target/mksz892/17_when条件判断与input人工审核.md` |
| done | 18 | 3 | Jenkinsfile 的存储方式与 CLI 使用 | 3-25 + 3-26 + 3-27 | 4768 | Jenkinsfile-流水线基础（基础课程所有笔记都在此文件）、教学课件.md |   `work/target/mksz892/18_Jenkinsfile存储方式与CLI使用.md` |
| done | 19 | 3 | GitLab 集成：构建状态回写与 Webhook 自动触发 | 3-28 + 3-29 | 7445 | Jenkinsfile-将jenkins构建状态发送到GitLAB、Jenkinsfile-trigger使用、教学课件.md |   `work/target/mksz892/19_GitLab集成与Webhook自动触发.md` |
| done | 20 | 3 | 多分支流水线使用与本章小结 | 3-30 + 3-31 | 1748 | 教学课件.md |   `work/target/mksz892/20_多分支流水线与本章小结.md` |
| done | 21 | 4 | Jenkins Slave 节点静态配置 | 4-1 + 4-2 | 4551 | Jenkinsfile-静态代理节点、教学课件.md |   `work/target/mksz892/21_Slave节点静态配置.md` |
| done | 22 | 4 | Docker 流水线使用：容器化构建代理 | 4-3 | 6216 | Jenkinsfile-Docker流水线-1、Jenkinsfile-Docker流水线-2 |   `work/target/mksz892/22_Docker流水线使用.md` |
| done | 23 | 4 | K8s 动态节点使用 | 4-4 | 4495 | Jenkinsfile-K8S流水线、deployment.yaml、serviceAccount.yaml |   `work/target/mksz892/23_K8s动态节点使用.md` |
| done | 24 | 4 | Groovy 基础语法学习 | 4-5 | 2537 | checkout.groovy、color.groovy、test.groovy、log.groovy |   `work/target/mksz892/24_Groovy基础语法学习.md` |
| done | 25 | 4 | 基于共享库进行 CICD 流程优化 | 4-6 | 2416 | checkout.groovy、color.groovy、test.groovy、log.groovy、Jenkinsfile-共享库使用 |   `work/target/mksz892/25_基于共享库进行CICD流程优化.md` |
| done | 26 | 4 | 参数化构建：基础参数与活跃参数 | 4-7 + 4-8 | 5706 | Jenkinsfile-参数化构建、教学课件.md |   `work/target/mksz892/26_参数化构建与活跃参数.md` |
| done | 27 | 4 | Kaniko 无守护进程构建镜像（含本章小结） | 4-9 + 4-10 | 2840 | Jenkinsfile-kaniko使用、教学课件.md |   `work/target/mksz892/27_Kaniko无守护进程构建镜像.md` |
| done | 28 | 5 | Jenkins 企业级实战开篇：测试流水线与飞书报警 | 5-1 + 5-2 | 4348 | Jenkinsfile-小实战 |   `work/target/mksz892/28_Jenkins企业级实战开篇-测试流水线与飞书报警.md` |
| done | 29 | 5 | SonarQube 部署、插件安装与 LDAP 接入 | 5-3 + 5-4 | 2670 | docker-compose.yaml、sonar-pvc.yaml、教学课件.md |   `work/target/mksz892/29_SonarQube部署插件与LDAP接入.md` |
| done | 30 | 5 | SonarQube 质量门禁、权限令牌与 Jenkins 扫描 Go 代码 | 5-5 + 5-6 | 4917 | Jenkinsfile-sonar扫描测试、教学课件.md |   `work/target/mksz892/30_SonarQube质量门禁令牌与Jenkins扫描Go代码.md` |
| done | 31 | 5 | MeterSphere 接口测试：部署、用例定义与 Jenkins 集成 | 5-7 + 5-8 + 5-9 | 7067 | Jenkinsfile-MehtereSphere接口测试、Jenkinsfile-sonar扫描测试 |   `work/target/mksz892/31_MeterSphere接口测试与Jenkins集成.md` |
| done | 32 | 5 | 项目实战：Jenkins + Docker + SonarQube + MeterSphere 静态代理 | 5-10 | 4042 | Jenkinsfile-docker静态代理实战、KubernetesPod.yaml、docker-config.yaml、kube-config.yaml、sonar-pv… | `work/target/mksz892/32_项目实战-Jenkins+Docker+SonarQube+MeterSphere静态代理.md` |
| done | 33 | 5 | 项目实战：Jenkins + K8S + SonarQube + MeterSphere 动态代理（含课程总结） | 5-11 + 5-12 | 3133 | Jenkinsfile-K8S动态代理实战、KubernetesPod.yaml、docker-config.yaml、kube-config.yaml、color.groov… | `work/target/mksz892/33_项目实战-Jenkins+K8S+SonarQube+MeterSphere动态代理与课程总结.md` |
| done | 34 | 6 | Tekton 快速入门：核心概念与基础夯实 | 6-1 + 6-2 | 3601 | pipeline1-hello-goodby.yaml、hello-task.yaml、goodby-task.yaml、hello-taskrun.yaml | `work/target/mksz892/34_Tekton快速入门-核心概念与基础夯实.md` |
| done | 35 | 6 | Tekton 部署到 K8s 集群 | 6-3 | 2037 | — | `work/target/mksz892/35_Tekton部署到K8s集群.md` |
| done | 36 | 6 | Tekton 定义 Task 运行 | 6-4 | 3286 | hello-task.yaml、goodby-task.yaml、hello-taskrun.yaml、sleep-task.yaml、ls-code.yaml | `work/target/mksz892/6-4_如何实现Tekton定义Task运行.md` |
| done | 37 | 6 | Tekton Pipeline：task 组合与四种引用方式 | 6-5 + 6-6 | 6610 | pipeline1-hello-goodby.yaml、pipeline2-git-clone.yaml、pipeline3-taskSpec.yaml、pipelinerun… | `work/target/mksz892/37_TektonPipeline-task组合与四种引用方式.md` |
| done | 38 | 6 | Pipeline 执行方式控制：retries / timeout / when / finally | 6-7 | 3490 | pipeline4-when.yaml、pipeline5-timeout.yaml、pipeline6-retries.yaml、pipeline7-runAfter.yam… | `work/target/mksz892/38_Pipeline执行方式控制-when-timeout-retries-runAfter-finally.md` |
| done | 39 | 6 | Parameters：task 与 pipeline 两级参数 | 6-8 + 6-9 | 4310 | pipeline9-param.yaml、parameters-git-clone-task.yaml、pipelinerun4-params.yaml | `work/target/mksz892/39_Parameters-task与pipeline两级参数.md` |
| done | 40 | 6 | Workspace：VCT 共享存储与 Secret | 6-10 + 6-11 | 6810 | pipeline10-vct.yaml、vct-git-clone-task.yaml、pipelinerun5-vct.yaml、pipeline11-secret.yaml… | `work/target/mksz892/40_Workspace-VCT共享存储与Secret实战.md` |
| done | 41 | 6 | Volume 持久化数据与 Results 数据传递 | 6-12 + 6-13 | 4074 | pipeline12-volume.yaml、pipelinerun7-volume.yaml、pv.yaml、pvc.yaml、pipeline13-results.yaml… | `work/target/mksz892/41_Volume持久化数据与Results数据传递.md` |
| done | 42 | 6 | Tekton Trigger 部署与 YAML 配置 | 6-14 + 6-15 | 5607 | eventListener.yaml、triggertemplage.yaml、binding.yaml、pipeline.yaml、task.yaml、secret.yaml… | `work/target/mksz892/42_TektonTrigger部署与GitLab自动触发.md` |
| done | 43 | 6 | Tekton Trigger 实战与项目部署（含课程总结） | 6-16 + 6-17 + 6-18 | 7277 | eventListener.yaml、triggertemplage.yaml、pipeline.yaml、secret.yaml、01-git-clone.yaml、02-g… | `work/target/mksz892/43_Tekton项目实战-Webhook一键触发全自动流水线.md` |
| done | 44 | 7 | Drone 概述与快速介绍 | 7-1 + 7-2 | 1486 | — |   `work/target/mksz892/44_Drone概述与快速介绍.md` |
| done | 45 | 7 | Drone 部署与 GitLab 接入 | 7-3 | 2845 | — |   `work/target/mksz892/45_Drone部署与GitLab接入.md` |
| done | 46 | 7 | Drone 权限管理 | 7-4 + 7-5 | 4199 | — |   `work/target/mksz892/46_Drone权限管理.md` |
| done | 47 | 7 | Docker 与 K8s 两种管道运行流水线 | 7-6 + 7-7 | 1216 | drone.yml-镜像拉取方式与拉取私有镜像、drone.yml-工作空间与步骤 |   `work/target/mksz892/47_Docker与K8s两种管道运行流水线.md` |
| done | 48 | 7 | K8s 管道配置：克隆、步骤插件空间、触发器与 when | 7-8 + 7-9 + 7-10 | 5347 | drone.yml-克隆操作、drone.yml-工作空间与步骤、drone.yml-触发器与when |   `work/target/mksz892/48_K8s管道配置-克隆步骤插件空间触发器与when.md` |
| done | 49 | 7 | 镜像拉取方式、并行执行与卷的使用 | 7-11 + 7-12 + 7-13 | 4728 | drone.yml-镜像拉取方式与拉取私有镜像、drone.yml-并行执行、drone.yml-PVC共享存储 |   `work/target/mksz892/49_镜像拉取方式并行执行与卷的使用.md` |
| done | 50 | 7 | Secret 配置使用与内置环境变量 | 7-14 + 7-15 | 3932 | drone.yml-secret使用、drone.yml-内置变量 |   `work/target/mksz892/50_Secret配置使用与内置环境变量.md` |
| done | 51 | 7 | 代码扫描与镜像构建：sonar / Kaniko / Docker | 7-16 + 7-17 + 7-18 | 2894 | drone.yml-sonar扫描、drone.yml-kaniko与docker插件使用 |   `work/target/mksz892/51_代码扫描与镜像构建-sonar-kaniko-docker.md` |
| done | 52 | 7 | Deploy 部署与 SSH/SCP/S3、钉钉 Webhook 插件 | 7-19 + 7-20 + 7-21 | 3413 | drone.yml-deployment插件使用、drone.yml-ssh与scp插件使用、drone.yml-钉钉与企业微信报警插件使用 |   `work/target/mksz892/52_Deploy部署与SSH-SCP-S3与钉钉Webhook报警插件.md` |
| done | 53 | 7 | Drone 项目部署与 CI 工具对比分析（含课程总结） | 7-22 + 7-23 + 7-24 | 2429 | drone.yml-项目实战、drone.yml-Jenkins插件使用 |   `work/target/mksz892/53_Drone项目实战七步流水线与三大CI工具对比.md` |
| done | 54 | 8 | KubeVela 概述、部署与核心概念 | 8-1 + 8-2 + 8-3 | 4466 | first-app.yaml、hello-world.yaml |   `work/target/mksz892/54_KubeVela概述部署与核心概念.md` |
| done | 55 | 8 | KubeVela 接入 OpenLDAP | 8-4 | 2688 | — | `work/target/mksz892/55_KubeVela接入OpenLDAP统一认证.md` |
| done | 56 | 8 | 交付目标与接入 K8s 集群部署首个应用 | 8-5 + 8-6 | 6000 | go-deploy.yaml、my-deploy.yaml、raw.yaml | `work/target/mksz892/56_交付目标与接入K8s集群部署首个应用.md` |
| done | 57 | 8 | KubeVela 项目配置 | 8-7 | 1743 | — | `work/target/mksz892/57_KubeVela项目配置.md` |
| done | 58 | 8 | 容器镜像部署与金丝雀发布 | 8-8 + 8-9 | 5559 | canary-app-one.yaml、canary-app-two.yaml、vela.yaml | `work/target/mksz892/58_容器镜像部署与金丝雀发布.md` |
| done | 59 | 8 | Sidecar 与 Worker 的使用、K8s-Object 多集群交付 | 8-10 + 8-11 | 2361 | sidecar.yaml、step-group.yaml、object.yaml | `work/target/mksz892/59_Sidecar与Worker组件及K8s-Object多集群交付.md` |
| done | 60 | 8 | if-and-timeout 工作流与组件编排参数传递 | 8-12 + 8-13 | 3598 | if-timeout.yaml、cm-with-message.yaml、step-group.yaml | `work/target/mksz892/60_if-and-timeout工作流与组件编排参数传递.md` |
| done | 61 | 8 | 资源托管与触发器构建 | 8-14 + 8-15 | 2061 | gateway-app.yaml | `work/target/mksz892/61_资源托管与触发器构建.md` |
| done | 62 | 8 | GitOps 部署、报警配置与角色权限分配 | 8-16 + 8-17 + 8-18 | 2930 | gitops.yaml、app-gitops.yaml、git-secret.yaml、alert-app.yaml | `work/target/mksz892/62_GitOps部署报警配置与角色权限分配.md` |
| done | 63 | 8 | 内置组件、运维特征、策略与工作流操作 | 8-19 + 8-20 + 8-21 + 8-22 | 4989 | — | `work/target/mksz892/63_内置组件运维特征策略与工作流操作.md` |
| done | 64 | 8 | CUE 基础语法与自定义扩展模板 | 8-23 + 8-24 + 8-25 | 6872 | foundation.cue、my-comp.cue | `work/target/mksz892/64_CUE基础语法与自定义扩展模板.md` |
| done | 65 | 8 | KubeVela 项目实战与总结 | 8-26 + 8-27 | 2294 | canary-app-one.yaml、go-deploy.yaml、gateway-app.yaml | `work/target/mksz892/65_KubeVela项目实战与总结.md` |
| done | 66 | 9 | Zadig 概述与介绍 | 9-1 + 9-2 | 1177 | — | `work/target/mksz892/66_Zadig概述与介绍.md` |
| done | 67 | 9 | Zadig 部署于 K8s 集群 | 9-3 | 2560 | install.sh、minio-pv.yaml | `work/target/mksz892/67_Zadig部署于K8s集群.md` |
| done | 68 | 9 | Zadig 系统集成：OpenLDAP、集群、镜像仓库与系统配置 | 9-4 | 6382 | install.sh | `work/target/mksz892/68_Zadig系统集成与基础配置.md` |
| done | 69 | 9 | Zadig 接入 Jenkins / GitLab / Sonar 与权限、项目创建 | 9-5 | 5037 | install.sh、go、node、backend、node | `work/target/mksz892/69_Zadig接入Jenkins-GitLab-Sonar与项目创建.md` |
| done | 70 | 9 | Zadig 服务与环境 | 9-6 + 9-7 | 6535 | — | `work/target/mksz892/70_Zadig服务与环境管理.md` |
| done | 71 | 9 | Zadig 构建模板 | 9-8 | 4791 | go、node、backend、node、test-node.sh | `work/target/mksz892/71_Zadig构建模板实战.md` |
| done | 72 | 9 | 产品工作流与自定义工作流 | 9-9 + 9-10 | 5105 | go、node、backend、node、test-node.sh | `work/target/mksz892/72_产品工作流与自定义工作流.md` |
| done | 73 | 9 | 构建缓存与持久化存储实战 | 9-11 + 9-12 | 5464 | minio-pv.yaml、test-node.sh | `work/target/mksz892/73_构建缓存与持久化存储实战.md` |
| done | 74 | 9 | 测试、代码扫描与集成 Jenkins 构建 | 9-13 + 9-14 | 5350 | test-node.sh、go、node、backend、node | `work/target/mksz892/74_测试代码扫描与集成Jenkins构建.md` |
| done | 75 | 9 | Zadig 项目实战与本章小结 | 9-15 + 9-16 | 1962 | go、node、backend、node、test-node.sh | `work/target/mksz892/75_Zadig项目实战与本章小结.md` |
| done | 76 | 10 | Argo CD 概述、介绍与部署 | 10-1 + 10-2 + 10-3 | 1640 | application-1.yaml | `work/target/mksz892/76_ArgoCD概述介绍与部署.md` |
| done | 77 | 10 | Argo CD Application 资源详解与实战 | 10-4 + 10-5 | 7827 | application-1.yaml、application-2.yaml、application-3.yaml | `work/target/mksz892/77_ArgoCD_Application资源详解与实战.md` |
| done | 78 | 10 | ApplicationSet 介绍与实战 | 10-6 | 1201 | applicationset.yaml | `work/target/mksz892/78_ApplicationSet介绍与实战.md` |
| done | 79 | 10 | 同步选项：配置介绍与执行 | 10-7 + 10-8 | 6033 | application-1.yaml | `work/target/mksz892/79_同步选项配置介绍与执行.md` |
| done | 80 | 10 | Argo CD 应用删除、回滚、Webhook 与横幅终端配置 | 10-9 + 10-10 | 3526 | app-cli.txt、argocd-secret.txt | `work/target/mksz892/80_应用删除回滚Webhook与横幅终端配置.md` |
| done | 81 | 10 | Argo CD LDAP 接入、权限配置与终端命令行 | 10-11 + 10-12 + 10-13 | 3854 | ldap-config.txt | `work/target/mksz892/81_LDAP接入权限配置与终端命令行.md` |
| done | 82 | 10 | Argo Rollout 与蓝绿 / 灰度发布概念 | 10-14 + 10-15 + 10-16 | 1910 | Canary-Application.yaml、Canary-Deploy.yaml | `work/target/mksz892/82_ArgoRollout与蓝绿灰度发布概念.md` |
| done | 83 | 10 | Argo Rollout 蓝绿与灰度发布实战 | 10-17 + 10-18 | 5874 | BlueGreen-Application.yaml、BlueGreen-Deploy.yaml、Canary-Application.yaml、Canary-Deploy.y… | `work/target/mksz892/83_ArgoRollout蓝绿与灰度发布实战.md` |
| done | 84 | 10 | 分析模板介绍与 Istio / Prometheus 部署 | 10-19 + 10-20 | 3650 | build-alert.sh、Canary-Application.yaml、Blue-Green-Application.yaml | `work/target/mksz892/84_分析模板介绍与Istio-Prometheus部署.md` |
| done | 85 | 10 | 蓝绿发布：流量分析自动回滚实战 | 10-21 | 3884 | Blue-Green-Application.yaml、Blue-Green-Deploy.yaml | `work/target/mksz892/85_蓝绿发布流量分析自动回滚实战.md` |
| done | 86 | 10 | 灰度发布：流量分析自动回滚与部署状态获取 | 10-22 + 10-23 | 3475 | Canary-Application.yaml、Canary-Deploy.yaml | `work/target/mksz892/86_灰度发布流量分析自动回滚与部署状态获取.md` |
| done | 87 | 10 | 三大 CD 工具对比分析与课程总结 | 10-24 + 10-25 | 1355 | — | `work/target/mksz892/87_三大CD工具对比分析与课程总结.md` |
| done | 88 | 11 | 阿里云云效：企业与项目创建、仓库模板使用（含本章总结） | 11-1 + 11-2 + 11-3 + 11-4 | 2955 | — | `work/target/mksz892/88_阿里云云效企业与项目创建仓库模板使用.md` |
| done | 89 | 12 | 综合实战：项目 1~4 场景下的工具选型与方案制定 | 12-1 + 12-2 | 3544 | — | `work/target/mksz892/89_综合实战项目1-4工具选型与方案制定.md` |
| done | 90 | 12 | 综合实战：项目 5~7 讲解与全课程总结 | 12-3 + 12-4 + 13-1 | 2767 | — | `work/target/mksz892/90_综合实战项目5-7讲解与全课程总结.md` |

## 统计

- 源讲稿：**176 篇 / 335,489 字**
- 合并后：**90 篇**（篇数减半，字数全保留）
- 课件代码：**156 个文件**（100 YAML + 8 Groovy/Jenkinsfile + 39 含 Jenkinsfile/drone.yml + shell/cue/md/txt），YAML 语法 100% 通过、括号配平 0 异常
- 已完成：**90 篇**（#1~#90）
- 待写：**0 篇**（全部完成；审核脚本全量通过，无 pending 行）
- 产出总量：**1,611,489 字节 / 335,489 源字符 = 4.80x**；字节比红线（≥3.0x）**90/90 达标**，品牌残留 0，156 个代码文件 100% 关联

## 运维检测与附录（2026-10-15）

- **运维专家检测**：`ops/OPS_AUDIT_REPORT.md` —— 全量扫描 11 个维度，发现问题 3 类（境外资源不可达 6 篇 23 处、`chmod 777` 安全反模式 1 处、高危删除缺提醒 2 处）+ 隐患 3 类（GNU-only 命令 8 篇 15 处、硬编码示例 IP 19 篇 70 处、RHEL 双系命令缺失），**全部已整改落地并复验通过**
- **运维落地附录**：`ops/OPS_NOTES.md` —— 国内镜像替代总表、示例地址替换清单、GNU/macOS 命令差异、Debian/RHEL 双系命令（含 SELinux 坑）、高危操作清单（确认点 + 回滚方案）、验收自检命令
- 状态：**未 commit / 未 push**，等用户验收
