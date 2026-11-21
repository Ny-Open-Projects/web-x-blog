# 画面线理解：13.Kubernetes集群搭建Node安装-kubelet服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\13.Kubernetes集群搭建Node安装-kubelet服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:13, 00:19, 00:22, 00:24, 00:32, 00:39, 01:07, 01:17, 01:49, 02:20, 02:38, 03:44, 04:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:43:20

1) 这一组画面整体在讲什么（一句话）：
在Node1节点上安装并配置Kubernetes的kubelet服务，包括创建systemd服务文件、设置kubelet配置文件以及配置kubectl的kubeconfig文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前位于“2.3 Node1安装”章节，右侧PPT显示“2.3 Node1安装”标题及“在Node1节点上...”的安装说明。
画面2：PPT页面显示“2.3 Node1安装”章节，下方有多个窗口预览，包括SecureCRT、VMware等，说明在Node1节点上安装Docker并启动。
画面3：PPT页面显示“2.3.1 kubelet服务”小节，内容为“配置systemd服务文件：vi /usr/lib/systemd/system/kubelet.service”，并展示“黑马程序员”Logo及宣传语。
画面4：PPT页面内容与画面3相同，但下方SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，准备执行命令。
画面5：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面6：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面7：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面8：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面9：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面10：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面11：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面12：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面13：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面14：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
WorkingDirectory=/var/lib/kubelet
ExecStart=/usr/bin/kubelet $KUBLET_ARGS
Restart=on-failure
KillMode=process
[Install]
WantedBy=multi-user.target
```
画面3：
```
[Unit]
Description=kubernetes kubelet Server

[Service]
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=docker.service
Requires=docker.service

[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet $KUBLET_ARGS
Restart=on-failure
KillMode=process

[Install]
WantedBy=multi-user.target
```
画面11：
```
KUBELET_ARGS="--kubeconfig=/etc/kubernetes/kubeconfig --hostname-override=192.168.126.148 --logtostderr=false --log-dir=/var/log/kubernetes --v=2 --fail-swap-on=false"
```
画面12：
```
apiVersion: v1
kind: Config
clusters:
- cluster:
    server: http://192.168.126.148:8080
    name: local
  context:
    cluster: local
    namespace: default
    user: myuser
  name: mycontext
current-context: mycontext
```
画面13：
```
apiVersion: v1
kind: Config
clusters:
- cluster:
    server: http://192.168.126.147:8080
    name: local
  context:
    cluster: local
    namespace: default
    user: myuser
  name: mycontext
current-context: mycontext
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.3 Node1安装”，内容为“在Node1节点上...”。
画面2：PPT标题为“2.3 Node1安装”，内容为“在Node1节点上...”。
画面3：PPT标题为“2.3.1 kubelet服务”，内容为“配置systemd服务文件：vi /usr/lib/systemd/system/kubelet.service”。
画面12：PPT标题为“用于kubelet连接Master Apiserver的配置文件”，内容为“vi /etc/kubernetes/kubeconfig”。
画面13：PPT标题为“用于kubelet连接Master Apiserver的配置文件”，内容为“vi /etc/kubernetes/kubeconfig”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
