# 画面线理解：16.Kubernetes集群搭建Node2安装

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\16.Kubernetes集群搭建Node2安装_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:25, 00:42, 01:35, 02:07, 02:40, 02:59, 03:15, 03:44, 03:58, 04:15, 04:41, 04:54, 06:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:45:17

1) 这一组画面整体在讲什么（一句话）：
演示如何在 VMware Workstation 中启动并配置 Kubernetes 集群节点（k8s-node1-demo 和 k8s-node2-demo），并通过 SecureCRT 登录进行网络和服务配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: VMware Workstation 主界面，显示虚拟机列表，其中“k8s-node1-demo”被选中，右侧是 SecureCRT 会话窗口，显示登录到 192.168.126.148 的 Linux 系统（CentOS 7）。
画面 2: VMware Workstation 主界面，显示“创建和管理虚拟机”的欢迎页面。
画面 3: 在 VMware Workstation 中，选中“k8s-node1-demo”，弹出“虚拟机设置”对话框，显示“已分配”状态，配置信息包括：内存 8 GB，处理器 4，硬盘 20 GB，网络适配器为 NAT。
画面 4: 启动“k8s-node1-demo”虚拟机，屏幕显示 VMware 启动动画。
画面 5: “k8s-node1-demo”虚拟机启动后，SecureCRT 会话窗口显示登录成功，提示“Last Login: Sat Sep 15 04:15:08 2018 From 192.168.126.1”。
画面 6: “k8s-node1-demo”虚拟机启动后，SecureCRT 会话窗口显示登录成功，提示“Last Login: Sat Sep 15 04:15:08 2018 From 192.168.126.1”。
画面 7: 在 VMware Workstation 中，尝试关闭“k8s-node2-demo”虚拟机，弹出确认对话框，询问是否关闭。
画面 8: 在 VMware Workstation 中，选中“k8s-node2-demo”，右键菜单中显示“k8s-node2-demo”虚拟机路径。
画面 9: 启动“k8s-node2-demo”虚拟机，屏幕显示 VMware 启动动画。
画面 10: “k8s-node2-demo”虚拟机启动后，SecureCRT 会话窗口显示空白。
画面 11: 在 SecureCRT 会话中，执行“ifconfig”命令，弹出“网络配置”窗口，显示多个网络接口，包括“inet 192.168.126.148”。
画面 12: 在 SecureCRT 会话中，执行“ifconfig”命令，显示网络接口信息，包括“lo”和“eth0”接口的详细配置。
画面 13: 在浏览器中打开“马哥智学”网站，页面显示“Kubernetes”相关文档，包括“WorkingDirectory=/var/lib/kubelet”、“ExecStart=/usr/bin/kubelet”等配置。
画面 14: 在 SecureCRT 会话中，执行“vi /etc/kubernetes/kubelet.conf”命令，显示配置文件内容，包括“server: http://192.168.126.148:8080”、“context: local”、“current-context: mycontext”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 13: 
```
Documentaion:https://github.com/GoogleCloudPlatform/kubernetes
After-docker-service
Requires=docker.service

[Service]
WorkingDirectory=/var/lib/kubelet
ExecStart=/usr/bin/kubelet
ExecStartPre=/usr/bin/mkdir -p /var/lib/kubelet
Restart=on-failure
KillMode=process
RuntimeDirectory=/var/lib/kubelet
RuntimeDirectoryMode=0755
User=root
Group=root
EnvironmentFile=/etc/sysconfig/kubelet
Environment="KUBELET_ARGS=--kubeconfig=/etc/kubernetes/kubeconfig --hostname-override=192.168.126.148 --logtostderr=false --logtostderr=false --v=2 --fail-swap-on=false"
```

画面 14:
```
kind: Config
clusters:
- cluster:
    server: http://192.168.126.148:8080
  name: local
contexts:
- context:
    cluster: local
    user: root
  name: mycontext
current-context: mycontext
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13: PPT 标题为“高可用化的Kubernetes快速入门课程”，左侧目录结构包括“1.Kubernetes概述”、“2.Kubernetes安装”、“2.3 Node安装”等。页面内容包含“Documentaion:https://github.com/GoogleCloudPlatform/kubernetes”、“After-docker-service”、“Requires=docker.service”等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
