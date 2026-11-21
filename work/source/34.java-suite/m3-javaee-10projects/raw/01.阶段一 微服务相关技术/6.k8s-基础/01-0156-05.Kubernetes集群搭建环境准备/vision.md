# 画面线理解：05.Kubernetes集群搭建环境准备

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\05.Kubernetes集群搭建环境准备_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:22, 02:03, 02:08, 02:31, 02:34, 02:46, 02:51, 02:57, 03:00, 03:12, 03:20, 03:25, 03:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:38:12

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 集群环境准备与规划，包括节点角色、IP 分配、防火墙配置及二进制包下载。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面“2.1 环境准备与规划”，列出推荐配置（2核2G）、Docker 版本（17.05.0-ce），并提供三节点的 IP 和组件表。
画面2：同画面1，无新增要点。
画面3：在 PPT 页面中，鼠标选中“node01”行的“docker”组件，强调其安装。
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
master	192.168.126.140	etcd, kube-apiserver, kube-controller-manager, kube-scheduler, docker
node01	192.168.126.141	kube-proxy, kubelet, docker
node02	192.168.126.142	kube-proxy, kubelet, docker

画面3：
firewall-cmd --state

画面4：
systemctl stop firewalld.service
systemctl disable firewalld.service

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
