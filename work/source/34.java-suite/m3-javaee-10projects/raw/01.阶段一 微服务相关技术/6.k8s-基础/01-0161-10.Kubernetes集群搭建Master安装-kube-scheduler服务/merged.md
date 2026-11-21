# 10.Kubernetes集群搭建Master安装-kube-scheduler服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\10.Kubernetes集群搭建Master安装-kube-scheduler服务_【海量资源尽在 ubkz.com】.mp4
- 时长 1分47秒（音频 107s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们就是Kubernetes Schedule这幅那么它也一样它也是依赖于Kubernetes API所以我们首先也去编辑一下它的Service你编辑它Service的时候其实你就会看到它里面会指定我们当前是依赖于我们刚才所说的Kubernetes API这里边不有个request吗Kubernetes API.Service所以大家要看一下这个
[00:28] 我粘贴的时候注意一下我别去把所有东西都粘过来因为这个讲义上中间会有一些东西啊所以这里边呢我这么一点点分开粘OK那粘贴完以后呢我们退出保存接下来呢我们就要去做它的一个配置文件跟刚才差不多我们过来编辑这个文件那这个文件大家也注意看哦原来我们那个叫做什么呢上面那个服务
[01:00] 我们叫KuberControllerManager看到了吗而现在这个是KuberSchedule所以这里边大家粘贴也要注意了然后同样的道理你一定要注意的就是我们要修改我当前的IP地址因为这时候会涉及到什么我们当前的Master的IP你就必须再告诉他我当前Master IP是谁所以在这里边告诉他我们当前是147
[01:29] OK吧保存退出那这样呢我们整个Kubernetes这个集群的相关服务啊我们都配置完了那么我们Kubernetes的API ServerKubernetes Controller Manager还有Kubernetes Schedule一会儿呢我们就要去启动它

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 kube-scheduler 服务的配置文件内容及启动流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 页面，标题为“2.2.5 kube-scheduler服务”，内容包含服务依赖关系、配置文件路径及服务单元文件结构。
画面 2: 在终端中执行命令 `vi /etc/kubernetes/Controller-manager`，准备编辑控制器管理器配置文件。
画面 3: PPT 页面保持不变，继续讲解 kube-scheduler 服务。
画面 4: PPT 页面保持不变，继续讲解 kube-scheduler 服务。
画面 5: 终端窗口显示空内容，准备进行下一步操作。
画面 6: PPT 页面显示“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service”。
画面 7: 终端中编辑并保存了 kube-scheduler 的 systemd 服务文件，内容包含[Unit]、[Service]、[Install] 部分。
画面 8: PPT 页面显示 kube-scheduler 服务的配置文件内容。
画面 9: 展示多个窗口，包括终端、文件资源管理器、GitHub 页面和 VMware Workstation 界面。
画面 10: PPT 页面显示“2.2.6 启动”部分，列出启动服务的命令。
画面 11: PPT 页面显示“2.2.5 kube-scheduler服务”和“2.2.6 启动”部分的内容。
画面 12: PPT 页面显示“2.2.6 启动”部分的内容。
画面 13: 展示多个窗口，包括终端、文件资源管理器、GitHub 页面和 VMware Workstation 界面。
画面 14: PPT 页面显示“2.2.6 启动”部分的内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
kube scheduler服务也依赖于kube-apiserver服务。
配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service
[Unit]
Description=kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
```

画面 6:
```
配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service
[Unit]
Description=kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
```

画面 7:
```
[Unit]
Description=kubernetes scheduler
After=kube-apiserver.Service
Requires=kube-apiserver.Service

[Service]
EnvironmentFile=/etc/kubernetes/scheduler
ExecStart=/usr/bin/kube-scheduler $KUBE_SCHEDULER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

画面 10:
```
2.2.6 启动
完成以上配置后，按顺序启动服务
systemctl daemon-reload
systemctl enable kube-apiserver.Service
systemctl start kube-apiserver.Service
```

画面 14:
```
2.2.6 启动
完成以上配置后，按顺序启动服务
systemctl daemon-reload
systemctl enable kube-apiserver.Service
systemctl start kube-apiserver.Service
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题“2.2.5 kube-scheduler服务”，内容包含服务依赖关系、配置文件路径及服务单元文件结构。
画面 6: 标题“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.Service”，内容包含服务单元文件的[Unit]、[Service]、[Install]部分。
画面 10: 标题“2.2.6 启动”，内容包含启动服务的命令。
画面 14: 标题“2.2.6 启动”，内容包含启动服务的命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

