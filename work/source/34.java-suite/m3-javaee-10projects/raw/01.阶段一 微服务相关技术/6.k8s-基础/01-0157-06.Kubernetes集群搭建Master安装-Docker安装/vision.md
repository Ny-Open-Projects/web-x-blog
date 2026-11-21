# 画面线理解：06.Kubernetes集群搭建Master安装-Docker安装

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\06.Kubernetes集群搭建Master安装-Docker安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:28, 00:38, 00:50, 00:54, 01:13, 01:17, 01:21, 01:24, 01:50, 01:58, 02:01, 02:18, 02:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:39:08

1) 这一组画面整体在讲什么（一句话）：
演示在 CentOS 系统上安装 Docker 以准备 Kubernetes 环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“1.1.2 Kubernetes快速入门”章节，列出环境准备步骤，包括关闭防火墙、安装 etcd 和 Kubernetes 软件、启动服务等命令。
画面 2: 显示 SecureCRT 连接终端，提示符为 [root@localhost ~]#，准备执行命令。
画面 3: 展示 PPT 的“2.1 环境准备与规划”章节，包含推荐配置（2核2G）、Docker 版本（17.05.0-ce）和三节点角色分配表。
画面 4: 展示 PPT 的“2.1 环境准备与规划”章节，光标在“查看默认防火墙状态”文字处，准备执行命令。
画面 5: 展示 PPT 的“2.2.1 Docker安装”章节，包含三个步骤：设置 yum 源、安装 docker、查看版本。
画面 6: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为系统信息和 Docker 版本信息。
画面 7: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为系统信息和 Docker 版本信息。
画面 8: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示多个窗口，包括 VMware、K8S 资源、K8S 资源等。
画面 9: 展示 PPT 的“2.2.1 Docker安装”章节，包含三个步骤：设置 yum 源、安装 docker、查看版本。
画面 10: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为编辑并保存了 /etc/yum.repos.d/docker.repo 文件。
画面 11: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为执行 yum install docker-engine 命令的输出。
画面 12: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为 yum install docker-engine 命令的输出，显示正在下载和安装包。
画面 13: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为 yum install docker-engine 命令的输出，显示安装完成。
画面 14: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为执行 docker -v 命令，输出 Docker 版本信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
- 关闭CentOS防火墙
  systemctl disable firewall
  systemctl stop firewall
- 安装etcd和kubernetes软件
  yum install -y etcd kubernetes
- 启动服务
  systemctl start etcd
  systemctl start docker
- 如果docker启动失败，参考（vi /etc/sysconfig/selinux 把selinux后面的改为disabled，重启机器，再重启docker就可以了）

画面 3:
- 推荐配置2核2G
- Docker version 17.05.0-ce
- 角色 IP 组件
  master 192.168.126.140 etcd, kube-apiserver, kube-controller-manager, kube-scheduler, docker
  node01 192.168.126.141 kube-proxy, kubelet, docker
  node02 192.168.126.142 kube-proxy, kubelet, docker

画面 5:
- (1) 设置yum源
  vi /etc/yum.repos.d/docker.repo
  [dockerrepo]
  name=Docker Repository
  baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
  enabled=1
  gpgcheck=1
  gpgkey=https://yum.dockerproject.org/gpg
- (2) 安装docker
  yum install docker-engine
- (3) 安装后查看docker版本
  docker -v

画面 10:
- vi /etc/yum.repos.d/docker.repo
  [dockerrepo]
  name=Docker Repository
  baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
  enabled=1
  gpgcheck=1
  gpgkey=https://yum.dockerproject.org/gpg

画面 11:
- yum install docker-engine

画面 12:
- yum install docker-engine
  正在下载：
  (1/10): audit-libs-python-2.8.1.3.1.8_64.rpm 75 k
  (2/10): checkpolicy-2.5.22.1_64.rpm 294 k
  (3/10): libgcrypt-1.6.1_64.rpm 65 k
  (4/10): libselinux-2.2.2_64.rpm 52 k
  (5/10): libsemanage-2.5.22.1_64.rpm 112 k
  (6/10): libsepol-2.5.22.1_64.rpm 35 k
  (7/10): policycoreutils-python-2.5.22.1_64.rpm 610 k
  (8/10): python-2.7.5_64.rpm 10 k
  (9/10): python-2.7.5_64.rpm 10 k
  (10/10): python-2.7.5_64.rpm 10 k
  正在安装：
  docker-engine-selinux-17.05.0-ce-1_64.rpm 6/10
  docker-engine-17.05.0-ce-1_64.rpm 6/10
  policycoreutils-python-2.5.22.1_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm 6/10
  python-2.7.5_64.rpm
