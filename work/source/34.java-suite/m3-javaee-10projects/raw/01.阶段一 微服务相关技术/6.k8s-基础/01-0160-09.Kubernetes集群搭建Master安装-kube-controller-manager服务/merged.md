# 09.Kubernetes集群搭建Master安装-kube-controller-manager服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\09.Kubernetes集群搭建Master安装-kube-controller-manager服务_【海量资源尽在 ubkz.com】.mp4
- 时长 2分12秒（音频 133s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们就要安装这个叫做Kubernetes Controller Manager这里面有这句话非常重要Kubernetes Controller Manager服务它是依赖于Kubernetes API Server的所以你要注意如果你之前的Kubernetes API Server失败了安装那么我们Kubernetes Controller Manager肯定是不OK的这个时候你也需要去执行一些操作所以我们来看一下首先它告诉你还是在System D下你要去创建一个叫做Kubernetes Controller Manager Service这个文件
[00:29] 这里边我就不写了我直接copy过来Ctrl C在这里呢我们去编辑这个文件在这个文件里边呢你看一下它要写一些东西OK把这部分Ctrl C粘贴过来这样呢我们当前的Cooper Controller Manager就安装完成然后呢我们需要去配置一下这里边配置的时候你注意了一定要注意你的IP地址
[01:00] 注意那我们当前的电脑的IP是147所以你在去用的时候你不能说我只是把这个粘贴过来了你要去注意一下你自己的IP地址OK所以这里边我们看一下它呢需要去创建这么一个文件那这个文件呢我们把这些配置信息copy一下粘贴过来这个路径啊这格式位促进一下
[01:39] 然后呢我们一定要去把这一块改了我master这个机器它是147ok吧192.168.126.147那你在安装时你要根据你自己master这个主机的IP啊去设置那如果你设置有问题那我们这个服务啊就不会起来了ok吧那这样的话呢我现在把我这个Controller manager这服务啊也就安装完成
[02:09] save the jj 退出保存

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并创建 Kubernetes 的 kube-Controller-manager 服务的 systemd 单元文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 页面，标题为“2.2.4 kube-Controller-manager服务”，并显示了该服务的 systemd 服务文件路径和内容（Unit 和 Service 部分）。
画面 2: 在 SecureCRT 会话中，执行了命令 `vi /etc/kubernetes/Controller-manager`，并成功创建了配置文件。
画面 3: SecureCRT 会话窗口显示了空的编辑器界面，准备进行下一步操作。
画面 4: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容，同时 PPT 页面显示了“2.2.5 kube-scheduler服务”的标题。
画面 5: PPT 页面显示了“2.2.4 kube-Controller-manager服务”的完整内容，包括 Unit 和 Service 部分。
画面 6: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容，包括 Unit 部分。
画面 7: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容。
画面 8: PPT 页面底部显示了黑马程序员的公司信息和标语。
画面 9: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容。
画面 10: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容。
画面 11: 屏幕截图显示了多个窗口的切换，包括课程 PPT、SecureCRT、GitHub、VMware Workstation 等。
画面 12: SecureCRT 会话窗口中显示了配置文件内容，其中 `KUBE_CONTROLLER_MANAGER_ARGS` 参数被修改。
画面 13: SecureCRT 会话窗口中显示了配置文件内容，其中 `KUBE_CONTROLLER_MANAGER_ARGS` 参数被修改。
画面 14: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
[Unit]
Description=kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.Service
Requires=kube-apiserver.Service

[Service]
EnvironmentFile=/etc/kubernetes/Controller-manager
ExecStart=/usr/bin/kube-Controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

画面 2:
/etc/kubernetes/Controller-manager

画面 4:
[Unit]
Description=kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.Service
Requires=kube-apiserver.Service

[Service]
EnvironmentFile=/etc/kubernetes/Controller-manager
ExecStart=/usr/bin/kube-Controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

画面 6:
[Unit]
Description=kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes

画面 12:
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://192.168.126.140:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

画面 13:
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://192.168.126.140:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“2.2.4 kube-Controller-manager服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-Controller-manager.Service”。
画面 4: 标题为“2.2.5 kube-scheduler服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service”。
画面 6: 标题为“2.2.5 kube-scheduler服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service”。
画面 8: 底部有“黑马程序员”的公司信息和标语“改变中国IT教育，我们正在行动”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

