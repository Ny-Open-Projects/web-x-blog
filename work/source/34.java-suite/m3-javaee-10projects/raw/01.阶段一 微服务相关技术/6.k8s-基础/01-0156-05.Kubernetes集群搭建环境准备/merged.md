# 05.Kubernetes集群搭建环境准备

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\05.Kubernetes集群搭建环境准备_【海量资源尽在 ubkz.com】.mp4
- 时长 3分32秒（音频 213s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们要去搭建一下我们的Colonize集群前期我们的快速入门其实也是一个单体版的集群只不过我们的Master和Node还是在同一台机器上我们没有分得特别清晰现在我们要做的事情是让我们的Master和Node是分别出在不同的虚拟机上大家来看一下Colonize用于协调高度可用的计算机集群这些计算机集群被连接成为单个的单元工作
[00:30] 那Chromadisk在一个集群上以更有效的方式自动分发和调度容器的应用程序。
[00:35] 那Chromadisk集群有两种资源,前期我们已经介绍过了,一种是Master,一种是Node。
[00:42] 那Master是一个集群的调度控制接点,那Node它是应用程序实际上真正运行的接点,也就是Node才是真正干活的。
[00:51] 那我们接下来就讲解一下如何快速的部署一套Chromadisk集群。
[00:56] 那Chromadisk我们之前也说过,它简称叫Kubernetes。
[00:59] 那Kubernetes机器呢,部署有几种方式,我们可以通过这个Compliance ADM啊,Mini Cooper啊,或者是二进制包,那么前两者属于这种自动的部署,然后呢,简化部署操作,我们这里面呢,其实是建议大家使用这种二进制包,因为这种部署呢,可以让大家了解更多的细节,那你对我们每个模块啊,可以知道的更多,那大家来看一下啊。
[01:24] 在我们整个针对于这个空门爱机群部署时,那我们推荐的这个配置是两个2G的电脑,那我们如果没有这个宠物理机,也用虚拟机也可以,那我们这个Docker呢是用的是17.05这个版本,我们整个呢会分成Master Node,那Master呢我们只有一个Node呢,我们是有两个节点,也就是说我们有一个Master两个Node,那这是我们Master的IP,这是我们Node的IP,
[01:50] 然后master上面有主件呢大家看到了etcd啊server啊然后我的这个Controller还有我们的schedule Docker那在我的node上呢有我们的proxy collect那Docker是必备的那在你做整个这个操作之前你需要把你无论是master还node上你的防火墙都进行关闭那我们可以去查看防火墙的状态关闭我们的防火墙然后呢禁止我这个防火墙开启启动
[02:19] 那整个这些都做完以后呢你首先呢要下载下来我们相关的二进制包那这个网址呢我们可以打开看一看你下载包的时候啊你注意了我们只需要下载这个就可以就是Kubernetes Server Linux AMD64位就可以因为这个包里面呢它包含了我们整个这个K8s需要运行的全部的服务程序你可以打开稍微有点慢啊因为我们这是一个外网
[02:57] 好了我们已经打开了然后呢你在下载的时候例如说假设1.9.0你可以把它打开现在我已经把它打开了然后呢你要找的是哪一个呢是我们的server binaries也就是说我们可以把它呢下载下来那这里边呢我就为大家演示其实我已经把它下载下来了OK那这样的话呢我们前期的准备工作啊都准备好以后呢接下来我们就可以去搭建我的master搭建我的node基地

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 集群环境准备与规划，包括节点角色、IP 分配、防火墙配置及二进制包下载。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“2.1 环境准备与规划”，列出推荐配置（2核2G）、Docker 版本（17.05.0-ce），并提供三节点的 IP 和组件表。
画面2：同画面1，无新增要点。
画面3：在 PPT 页面中，鼠标选中“node01”行的“Docker”组件，强调其安装。
画面4：继续展示 PPT 页面，列出防火墙操作命令和获取二进制包的链接。
画面5：切换到桌面，显示任务栏，无新增技术要点。
画面6：在 PPT 页面中，鼠标移动至“获取Kubernetes二进制包”链接。
画面7：切换到浏览器，地址栏显示“https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.9.md”，页面空白。
画面8：浏览器显示“网页无法访问”的错误提示。
画面9：浏览器成功加载 GitHub 页面，显示“kubernetes / CHANGELOG-1.9.md”文件。
画面10：在 GitHub 页面中，鼠标移动至“v1.9.10”版本的“Downloads for v1.9.10”部分。
画面11：在 GitHub 页面中，鼠标选中“Server Binaries”部分的“kubernetes-server-linux-amd64.tar.gz”文件。
画面12：同画面11，无新增要点。
画面13：切换回 PPT 页面，鼠标在“获取Kubernetes二进制包”链接上。
画面14：切换回 PPT 页面，鼠标选中“2.2 Master安装”下的“2.2.1 Docker安装”标题，页面显示“Server Binaries”部分的文件列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
Docker version 17.05.0-ce
角色	IP	组件
master	192.168.126.140	etcd, kube-apiserver, kube-Controller-manager, kube-scheduler, Docker
node01	192.168.126.141	kube-proxy, kubelet, Docker
node02	192.168.126.142	kube-proxy, kubelet, Docker

画面3：
firewall-cmd --state

画面4：
systemctl stop firewalld.Service
systemctl disable firewalld.Service

画面6：
https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.9.md

画面11：
Server Binaries
filename	sha256 hash
kubernetes-server-linux-amd64.tar.gz	13299f858840219841a5e623348fa70952a459b1d7b5bc29998a8d1cf:fcf
kubernetes-server-linux-arm64.tar.gz	9cacacada44ab73113070920f38c132112144ac1f1c4b17cfd1f36b6e9b7ff
kubernetes-server-linux-arm64.tar.gz	c557f784538c83c82c8c7c950a1252421f05c7f0c8884a578a4c6a05051
kubernetes-server-linux-ppc64le.tar.gz	c50f17c24824a087218c73060d1c750990a4ff453536a06d2c28bc42200093
kubernetes-server-linux-s390x.tar.gz	449289491f6e3aa47cf58472bc9d3c638f6e762a40255d7563021c36b7fc7c

画面14：
Server Binaries
filename	sha256 hash
kubernetes-server-linux-amd64.tar.gz	13299f858840219841a5e623348fa70952a459b1d7b5bc29998a8d1cf:fcf
kubernetes-server-linux-arm64.tar.gz	9cacacada44ab73113070920f38c132112144ac1f1c4b17cfd1f36b6e9b7ff
kubernetes-server-linux-arm64.tar.gz	c557f784538c83c82c8c7c950a1252421f05c7f0c8884a578a4c6a05051
kubernetes-server-linux-ppc64le.tar.gz	c50f17c24824a087218c73060d1c750990a4ff453536a06d2c28bc42200093
kubernetes-server-linux-s390x.tar.gz	449289491f6e3aa47cf58472bc9d3c638f6e762a40255d7563021c36b7fc7c

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“2.1 环境准备与规划”，包含一个三列表格，列标题为“角色”、“IP”、“组件”，内容为三节点的配置。
画面4：PPT 标题为“2.1 环境准备与规划”，包含一个列表，列出防火墙操作命令和获取二进制包的链接。
画面14：PPT 标题为“2.2 Master安装”，包含一个“Server Binaries”表格，列出文件名和 sha256 hash。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

