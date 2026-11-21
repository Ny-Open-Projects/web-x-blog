# 画面线理解：12.Kubernetes集群搭建Node安装-准备工作

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\12.Kubernetes集群搭建Node安装-准备工作_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:24, 00:31, 00:40, 01:01, 01:03, 01:24, 01:26, 01:48, 01:53, 02:00, 02:04, 02:06, 02:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:42:42

1) 这一组画面整体在讲什么（一句话）：
在Kubernetes集群部署过程中，通过SecureCRT远程连接到Node1节点，解压并安装Kubernetes组件（如kubelet、kube-proxy等）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，讲解Docker安装步骤，包括配置yum源和安装docker-engine命令。
画面2：SecureCRT终端界面，显示已连接到目标服务器，准备执行命令。
画面3：在SecureCRT中执行“pwd”命令查看当前目录，并弹出文件传输窗口，准备上传文件。
画面4：在SecureCRT中执行“rz”命令，开始从本地上传文件，显示传输进度。
画面5：文件传输继续进行，显示传输进度和剩余时间。
画面6：切换到PPT页面，显示“2.3 Node1安装”章节，提示在Node1节点上安装Docker并启动Docker服务。
画面7：在SecureCRT终端中，执行“tar -zxvf kubernetes-server-linux-amd64.tar.gz”命令，解压Kubernetes服务器组件。
画面8：继续解压操作，显示解压后的文件列表。
画面9：切换到PPT页面，显示“2.1 环境准备与规划”章节，列出各节点角色、IP地址和组件。
画面10：切换回PPT页面，显示“2.3 Node1安装”章节，提示配置systemd服务文件。
画面11：在SecureCRT终端中，执行“cd server”命令，进入解压后的server目录。
画面12：在SecureCRT终端中，执行“mkdir -p /usr/local/bin”命令，创建bin目录。
画面13：在SecureCRT终端中，执行“cp kubelet kube-proxy /usr/local/bin/”命令，复制Kubernetes组件到bin目录。
画面14：在SecureCRT终端中，执行“cp kubelet kube-proxy /usr/local/bin/”命令，继续复制Kubernetes组件到bin目录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
[...]
[ dockerrepo ]
name=Docker repository
baseurl=https://mirrors.aliyun.com/docker-ce/linux/centos/7/$basearch/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/docker-ce/linux/centos/7/docker-ce.repo
[...]
画面1：
[...]
yum install docker-engine
[...]
画面1：
[...]
docker -v
[...]
画面7：
tar -zxvf kubernetes-server-linux-amd64.tar.gz
[...]
画面11：
cd server
[...]
画面12：
mkdir -p /usr/local/bin
[...]
画面13：
cp kubelet kube-proxy /usr/local/bin/
[...]
画面14：
cp kubelet kube-proxy /usr/local/bin/
[...]

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.2.1 Docker安装”，包含三个步骤：(1) 配置yum源，(2) 安装docker，(3) 安装后查看docker版本。
画面6：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。
画面9：PPT标题为“2.1 环境准备与规划”，表格包含三列：角色、IP、组件，内容包括“etcd, kube-apiserver, kube-controller-manager, kube-scheduler”等。
画面10：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。
画面13：PPT标题为“2.3 Node1安装”，内容包括“在Node1节点上，以同样的方式把从压缩包中解压出的二进制文件kubelet kube-proxy放到/usr/bin目录中。”和“在Node1节点上需要先安装Docker，请参考Master上Docker的安装，并启动Docker”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
