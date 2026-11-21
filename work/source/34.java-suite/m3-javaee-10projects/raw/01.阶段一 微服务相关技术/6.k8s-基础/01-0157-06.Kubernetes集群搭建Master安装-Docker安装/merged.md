# 06.Kubernetes集群搭建Master安装-Docker安装

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\06.Kubernetes集群搭建Master安装-Docker安装_【海量资源尽在 ubkz.com】.mp4
- 时长 2分29秒（音频 149s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们要讲解一下Master安装中的Docker安装在前期的快速入门里边我们在安装ETCD的时候其实就已经帮助我们把Docker安装了现在因为我们要进行这种二进制安装所以我们的Docker也需要去手段安装一下我们来看一下怎么去安装这里边告诉我们首先设置一下亚米源然后安装Docker最后我们可以查看版本在进行这个操作之前
[00:30] 我们呢需要先去把YAM update一下那这里边大家需要注意的一点是我在讲义里边呢我们环境规划时说我的master是140这台机器那我现在给大家安装时呢我是选择147那这一点呢是方便同学们后续啊在自己去安装时如果IP地址与我不一样应该如何去调整那大家来看啊首先我们把Docker安装上那我刚才说了你首先呢要去进行一个YAM update
[00:59] 那么这是根据你不同的机器啊它这个更新速度呢可能不太一样我们稍等一下update完成以后呢我们再按照讲义上所讲解的进行安装我们已经更新完毕接下来呢我们就可以去安装一下我们的Docker那首先呢你去编辑一下我们这个文件如果这个文件没有它就会帮我创建一下然后呢我们把这段代码copy过来
[01:29] 这里边有点小问题我应该是先去切到insert我再去把它粘贴过来就会合适一点现在呢我再去粘贴ok退出保存然后呢我们可以通过yam installdockr-enjne我们去安装或者加个参数-y也行这样的话呢我们就可以去把
[01:58] DAO科安装上它会去下一些相关的依赖包稍等一下我们这里面需要安装10个这里面已经快安装完成好了我们已经安装完成然后呢我们可以DAO科-V看一下我们安装的版本那这样呢我们就手动的把DAO科安装完成了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 CentOS 系统上安装 Docker 以准备 Kubernetes 环境。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的“1.1.2 Kubernetes快速入门”章节，列出环境准备步骤，包括关闭防火墙、安装 etcd 和 Kubernetes 软件、启动服务等命令。
画面 2: 显示 SecureCRT 连接终端，提示符为 [root@localhost ~]#，准备执行命令。
画面 3: 展示 PPT 的“2.1 环境准备与规划”章节，包含推荐配置（2核2G）、Docker 版本（17.05.0-ce）和三节点角色分配表。
画面 4: 展示 PPT 的“2.1 环境准备与规划”章节，光标在“查看默认防火墙状态”文字处，准备执行命令。
画面 5: 展示 PPT 的“2.2.1 Docker安装”章节，包含三个步骤：设置 yum 源、安装 Docker、查看版本。
画面 6: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为系统信息和 Docker 版本信息。
画面 7: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为系统信息和 Docker 版本信息。
画面 8: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示多个窗口，包括 VMware、Kubernetes 资源、Kubernetes 资源等。
画面 9: 展示 PPT 的“2.2.1 Docker安装”章节，包含三个步骤：设置 yum 源、安装 Docker、查看版本。
画面 10: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为编辑并保存了 /etc/yum.repos.d/Docker.repo 文件。
画面 11: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为执行 yum install Docker-engine 命令的输出。
画面 12: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为 yum install Docker-engine 命令的输出，显示正在下载和安装包。
画面 13: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为 yum install Docker-engine 命令的输出，显示安装完成。
画面 14: 展示 PPT 的“2.2.1 Docker安装”章节，同时显示终端窗口，内容为执行 Docker -v 命令，输出 Docker 版本信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
- 关闭CentOS防火墙
  systemctl disable firewall
  systemctl stop firewall
- 安装etcd和kubernetes软件
  yum install -y etcd kubernetes
- 启动服务
  systemctl start etcd
  systemctl start Docker
- 如果Docker启动失败，参考（vi /etc/sysconfig/selinux 把selinux后面的改为disabled，重启机器，再重启Docker就可以了）

画面 3:
- 推荐配置2核2G
- Docker version 17.05.0-ce
- 角色 IP 组件
  master 192.168.126.140 etcd, kube-apiserver, kube-Controller-manager, kube-scheduler, Docker
  node01 192.168.126.141 kube-proxy, kubelet, Docker
  node02 192.168.126.142 kube-proxy, kubelet, Docker

画面 5:
- (1) 设置yum源
  vi /etc/yum.repos.d/Docker.repo
  [dockerrepo]
  name=Docker Repository
  baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
  enabled=1
  gpgcheck=1
  gpgkey=https://yum.dockerproject.org/gpg
- (2) 安装Docker
  yum install Docker-engine
- (3) 安装后查看Docker版本
  Docker -v

画面 10:
- vi /etc/yum.repos.d/Docker.repo
  [dockerrepo]
  name=Docker Repository
  baseurl=https://yum.dockerproject.org/repo/main/centos/$releasever/
  enabled=1
  gpgcheck=1
  gpgkey=https://yum.dockerproject.org/gpg

画面 11:
- yum install Docker-engine

画面 12:
- yum install Docker-engine
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
  Docker-engine-selinux-17.05.0-ce-1_64.rpm 6/10
  Docker-engine-17.05.0-ce-1_64.rpm 6/10
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

