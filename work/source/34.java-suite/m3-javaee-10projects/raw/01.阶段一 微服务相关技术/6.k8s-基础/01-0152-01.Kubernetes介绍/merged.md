# 01.Kubernetes介绍

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\01.Kubernetes介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 4分10秒（音频 250s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好,下面我们讲解容器化进阶课程,Kubernetes的一个快速入门课程首先我们要对Kubernetes做一个简单的介绍我们了解什么是Kubernetes,它有什么作用那我们使用Kubernetes能做什么那这是我们这节课的一个主要内容首先来看一下,Kubernetes是谷歌在2014年发布的一个开源项目
[00:27] 那么我们把它呢简称叫做Kubernetes是因为K和S中间呢我们有八个英文字母所以我们简称叫Kubernetes那我们使用Chromalight最主要是用于什么呢自动化容器应用程序的部署扩展和管理那我们使用Chromalight一般是结合着DAO科容器工作它呢帮助我们整合多个运行的DAO科容器的主机机群可以那Chromalight的目标呢是让我们部署容器化的应用程序啊简单高效
[00:57] 它的一个核心特点就是能够自主的管理容器来保证云平台中的容器呢按照用户的期望去运行下面呢是关于Chromlight的相关特性这些特性啊是在Chromlight的官网上提供的大家可以打开Chromlight.io我这里边呢已经为大家打开了看一下在这呢你可以把它切换到中文或者英文那刚才我给大家展示的关于Chromlight的特性呢其实就是在这里边给大家
[01:24] 接取的那我们这里面说到了它能自动包装自我修复横向的缩放服务的发现和负载均衡自动的部署和回滚还有密钥和配置的管理还有这里面存储的编排批处理那这些特性它就使得我们使用Kubernetes可以更加高效的去工作那这些介绍完以后呢大家来看一下我们使用Kubernetes到底能做什么呢刚才我们介绍了说
[01:53] Combined是一个全新的基于我们这种容器化技术的分布式的一个架构的领先方案那它是谷歌一个开源性谷歌对这么一个项目的开源那Combined是一个开放平台它无侵入性现在系统很容易都迁到Combined上那Combined是一个完备的分布式的一个系统支撑平台我们使用Combined可以在物理机或虚拟机的Combined机群上运行我们的容器化应用
[02:21] 那Copenhagen能提供一个以容器为中心的基础架构满足我们生产环境中以及我们这个开发环境中一些需求那大家可以看一下下面的列了一些说例如我们多个进程协同工作呀存储系统的挂载呀应用健康检查呀
[02:39] Pod的自动伸缩和扩展负载呀等等这里边它都可以帮助我们去完成操作那我们为什么要使用ChromeNet呢其实刚才我们在前期已经说过了ChromeNet它在设计之初的一个核心的这个目标就是能让我们自主的管理容器来保证云平台中的
[02:59] 容器按照用户的期望去运行那这里呢又给大家做了一次总结你可以看一下我们使用ChromeLite最直接感受就是我们可以轻装上阵开发复杂的系统那其次呢ChromeLite呢在全面拥抱微服务这方面它做的非常好那我们知道微服务呢现在是我们的一个主流我们使用ChromeLite呢跟我们的微服务集成啊我们现在呢可以使我们的开发更加简单它这里面说了微服务的核心就是将一个巨大的单体应用
[03:29] 拆分为很多小的互相连接的微服务一个微服务还可以有很多的副本那副本数量可以随着我们这个系统的复格变化动态调整也就是说我们知道你真的一个微服务架构它最终的每一个服务它都可能会有副本它随着这个系统越来越大那我们整个需要管理的监控就越来越多
[03:50] 那Kubernetes呢可以帮助我们去简化一些操作它可以帮助我们动态的扩容前期我们已经提到过了那最后呢Kubernetes的系统具有超强的横向的一个扩容能力这也是我们为什么要去熟悉或者说学习Kubernetes的一个基本的原因

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 的基本概念、核心特性及其在生产环境中的应用场景。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了 PPT 的第1页，标题为“1. Kubernetes概述”，子标题“1.1 Kubernetes介绍”。
- 内容包括 Kubernetes 的定义（由 Google 于2014年发布，用于自动化容器应用的部署、扩展和管理）、官网链接（https://kubernetes.io/）和中文社区链接（https://www.kubernetes.org/docs）。
- 列出了 Kubernetes 的核心特性：自动包装、横向缩放、自动部署和回滚、存储编排、自我修复、服务发现和负载均衡、密钥和配置管理、批处理。

画面2：
- 展示了 PPT 的第2页，标题为“使用Kubernetes能做什么”。
- 内容包括“黑马程序员”的宣传语和对 Kubernetes 的描述，强调其作为“全新的基于容器技术的分布式架构领先方案”。
- 列出了 Kubernetes 的应用场景：多个协同工作、存储系统挂载、分发 secrets、应用镜像的复制、Pod 自动伸缩、负载均衡、滚动更新、资源监控、日志访问、调试应用程序、服务认证授权。

画面3：
- 展示了 PPT 的第2页，标题为“使用Kubernetes能做什么”。
- 内容与画面2相同，但鼠标光标位置不同。

画面4：
- 展示了 PPT 的第1页，标题为“1. Kubernetes概述”，子标题“1.1 Kubernetes介绍”。
- 内容与画面1相同，但鼠标光标位置不同。

画面5：
- 展示了浏览器页面，访问的是 Kubernetes 中文官网（https://kubernetes.io/zh/）。
- 页面顶部有“Home”、“Chinese”、“v1.11”和“Try Kubernetes”按钮。
- 页面主体展示了一位演讲者（Sue Gohd）的图片和文字“Kubernetes: 最后... 它是真正的云平台”。

画面6：
- 展示了浏览器页面，访问的是 Kubernetes 中文官网（https://kubernetes.io/zh/）。
- 页面标题为“Kubernetes 特性”。
- 内容包括“自动包装”、“自我修复”、“服务发现和负载均衡”、“密钥和配置管理”、“批处理”等特性描述。

画面7：
- 展示了浏览器页面，访问的是 Kubernetes 中文官网（https://kubernetes.io/zh/）。
- 页面标题为“Kubernetes 特性”。
- 内容包括“存储编排”和“批处理”等特性描述。

画面8：
- 展示了 PPT 的第1页，标题为“1. Kubernetes概述”，子标题“1.1 Kubernetes介绍”。
- 内容与画面1相同，但鼠标光标位置不同。

画面9：
- 展示了 PPT 的第2页，标题为“使用Kubernetes能做什么”。
- 内容与画面2相同，但鼠标光标位置不同。

画面10：
- 展示了 PPT 的第2页，标题为“使用Kubernetes能做什么”。
- 内容与画面2相同，但鼠标光标位置不同。

画面11：
- 展示了 PPT 的第2页，标题为“使用Kubernetes能做什么”。
- 内容与画面2相同，但鼠标光标位置不同。

画面12：
- 展示了 PPT 的第1页，标题为“1. Kubernetes概述”，子标题“1.1 Kubernetes介绍”。
- 内容与画面1相同，但鼠标光标位置不同。

画面13：
- 展示了 PPT 的第2页，标题为“1.1.2 Kubernetes快速入门”。
- 内容包括“环境准备”部分，列出的操作步骤：
  - 关闭 CentOS 防火墙：systemctl disable firewall
  - 关闭防火墙：systemctl stop firewall
  - 安装 etcd 和 Kubernetes 软件：yum install -y etcd kubernetes
  - 启动服务：systemctl start etcd

画面14：
- 展示了 PPT 的第1页，标题为“1. Kubernetes概述”，子标题“1.1 Kubernetes介绍”。
- 内容与画面1相同，但鼠标光标位置不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面13：
- 关闭 CentOS 防火墙：systemctl disable firewall
- 关闭防火墙：systemctl stop firewall
- 安装 etcd 和 Kubernetes 软件：yum install -y etcd kubernetes
- 启动服务：systemctl start etcd

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
- 标题：1. Kubernetes概述
- 子标题：1.1 Kubernetes介绍
- 子子标题：1.1.1 Kubernetes是什么及作用
- 内容：Kubernetes (Kubernetes) 是 Google 在 2014 年发布的一个开源项目，用于自动化容器应用的部署、扩展和管理。Kubernetes 通常结合 Docker 容器工作，并且整合多个运行 Docker 容器的主机集群。官网地址：https://kubernetes.io/ 中文社区：https://www.kubernetes.org/docs
- 特性列表：
  - 自动包装
  - 横向缩放
  - 自动部署和回滚
  - 存储编排
  - 自我修复
  - 服务发现和负载均衡
  - 密钥和配置管理
  - 批处理

画面2：
- 标题：使用Kubernetes能做什么
- 内容：黑马程序员宣传语和对 Kubernetes 的描述。
- 应用场景列表：
  - 多个协同工作
  - 存储系统挂载
  - Distributing secrets
  - 应用镜像的复制
  - Pod 自动伸缩
  - 负载均衡
  - 滚动更新
  - 资源监控
  - 日志访问
  - 调试应用程序
  - 服务认证授权

画面13：
- 标题：1.1.2 Kubernetes快速入门
- 子标题：环境准备
- 操作步骤：
  - 关闭 CentOS 防火墙：systemctl disable firewall
  - 关闭防火墙：systemctl stop firewall
  - 安装 etcd 和 Kubernetes 软件：yum install -y etcd kubernetes
  - 启动服务：systemctl start etcd

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

