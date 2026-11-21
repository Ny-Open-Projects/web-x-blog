# 14.Kubernetes集群搭建Node安装-kube-proxy服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\14.Kubernetes集群搭建Node安装-kube-proxy服务_【海量资源尽在 ubkz.com】.mp4
- 时长 2分4秒（音频 125s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面呢我们说一下当前我们这个Coopers Proxy那么对于Coopers Proxy来说啊它是依赖于Network的那么Network服务呢大家如果这个遇到了问题呢可以参考上我讲义上给大家提供的这四种解决方案基本上就能解决你的Network这个服务的问题那我们来看一下对于这个Coopers Proxy我们要想操作它呢首先第一件事啊
[00:25] 你需要去编辑一下kuberproxy.Service这个服务的配置文件所以我们在这里编vi-usr下的lab下的我们systemd下的system下的一个叫做kuber-proxy.pyxyvse在这个文件里面我们要去指定一下
[00:53] 大家来看一下这里边我们是不是需要了network serviceOK吧那我们把它呢配置一下然后呢我们的save.jj退出退出以后呢我们接下来要配置的是Kubernetes自己的配置文件一个叫etc下的Kubernetes下的proxy也就是说我们在这里边需要vi我们etc下的Kubernetes下的一个叫做proxyproxy这名配置文件在这个配置文件里边
[01:22] 你要注意了我们还涉及到IP地址的问题我们在这编辑它那我呢需要把这个位置控制一下我们要连接的master一定要注意它是1478080没问题而我们自己的IP是148这个一定要注意啊这是我们自己的IP这个是master IPOK我们save的JJ保存
[01:57] 这样的话呢我们就已经把我们当前的Cooper Proxy配置完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
After=network.Service
Requires=network.Service

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
After=network.Service
Requires=network.Service

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

