# 画面线理解：14.Kubernetes集群搭建Node安装-kube-proxy服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\14.Kubernetes集群搭建Node安装-kube-proxy服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:04, 00:05, 00:10, 00:12, 00:17, 00:18, 00:31, 00:50, 00:57, 01:23, 01:31, 01:51, 01:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:44:00

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 集群中 kube-proxy 服务的配置与启动方法，包括禁用 NetworkManager、创建服务文件、配置参数并启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前选中“2.3.3 启动”章节，右侧页面显示“2.3.2 kube-proxy服务”内容，介绍其作用及常见解决方案。
画面2：切换至 SecureCRT 远程终端，显示连接到 IP 192.168.126.147 的会话，提示符为 [root@localhost ]#。
画面3：终端窗口保持打开状态，未执行任何命令。
画面4：返回到 PDF 页面，显示“2.3.2 kube-proxy服务”内容，鼠标指针在页面上移动。
画面5：PDF 页面内容保持不变，鼠标指针在“2.3.2 kube-proxy服务”标题附近。
画面6：PDF 页面内容保持不变，鼠标指针在“2.3.2 kube-proxy服务”标题附近。
画面7：PDF 页面内容保持不变，鼠标指针在“2.3.2 kube-proxy服务”标题附近。
画面8：切换至 SecureCRT 远程终端，显示连接到 IP 192.168.126.147 的会话，提示符为 [root@localhost ]#。
画面9：PDF 页面显示“2.3.3 启动”和“2.4 Node2安装”章节，同时展示配置文件内容，包括 [Unit]、[Service] 和 [Install] 部分。
画面10：切换至桌面，显示多个窗口，包括 PDF、WPS 文档、VMware Workstation 和文件资源管理器。
画面11：PDF 页面显示“2.3.3 启动”和“2.4 Node2安装”章节，同时展示配置文件内容，包括 [Unit]、[Service] 和 [Install] 部分。
画面12：切换至 SecureCRT 远程终端，显示连接到 IP 192.168.126.147 的会话，提示符为 [root@localhost ]#。
画面13：切换至 SecureCRT 远程终端，显示连接到 IP 192.168.126.147 的会话，提示符为 [root@localhost ]#。
画面14：切换至 SecureCRT 远程终端，显示连接到 IP 192.168.126.147 的会话，提示符为 [root@localhost ]#。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9：
[Unit]
Description=kubernetes kube-proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.service
Requires=network.service

[Service]
EnvironmentFile=/etc/kubernetes/proxy
ExecStart=/var/lib/kube-proxy KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536
KillMode=process

[Install]
WantedBy=multi-user.target

配置文件：vi /etc/kubernetes/proxy
KUBE_PROXY_ARGS="--master=http://192.168.126.147:8080 --hostname-override=192.168.126.147 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

画面11：
[Unit]
Description=kubernetes kube-proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.service
Requires=network.service

[Service]
EnvironmentFile=/etc/kubernetes/proxy
ExecStart=/var/lib/kube-proxy KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536
KillMode=process

[Install]
WantedBy=multi-user.target

配置文件：vi /etc/kubernetes/proxy
KUBE_PROXY_ARGS="--master=http://192.168.126.147:8080 --hostname-override=192.168.126.147 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

画面14：
/etc/kubernetes/proxy [New] 146C written
[root@localhost ]#

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.3.2 kube-proxy服务”，内容为“kube-proxy服务依赖于network服务，所以一定保证network服务正常，如果network服务启动失败，常见解决方案有以下几种：”。
画面5：PPT标题为“2.3.2 kube-proxy服务”，内容为“kube-proxy服务依赖于network服务，所以一定保证network服务正常，如果network服务启动失败，常见解决方案有以下几种：”。
画面9：PPT标题为“2.3.3 启动”，内容为“systemctl daemon-reload”、“systemctl enable kubelet”、“systemctl start kubelet”、“systemctl status kubelet”、“systemctl enable kube-proxy”、“systemctl start kube-proxy”、“systemctl status kube-proxy”。
画面11：PPT标题为“2.3.3 启动”，内容为“systemctl daemon-reload”、“systemctl enable kubelet”、“systemctl start kubelet”、“systemctl status kubelet”、“systemctl enable kube-proxy”、“systemctl start kube-proxy”、“systemctl status kube-proxy”。
画面14：PPT标题为“2.3.3 启动”，内容为“systemctl daemon-reload”、“systemctl enable kubelet”、“systemctl start kubelet”、“systemctl status kubelet”、“systemctl enable kube-proxy”、“systemctl start kube-proxy”、“systemctl status kube-proxy”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
