# 11.Kubernetes集群搭建Master安装-启动

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\11.Kubernetes集群搭建Master安装-启动_【海量资源尽在 ubkz.com】.mp4
- 时长 4分31秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们去把所有的服务都启动一下那么我们先systemctl daem1我们先去daem1我先去把整个去reload一下重新加载一下然后我们先去启动我们当前的etcd服务什么吧ableetcd然后我再去
[00:32] Start的ETCD大家可以看一下我当前的ETCD服务它是一个Active Running然后我们再把Docker服务起来然后我们可以看一下当前的Docker服务它也是一个Running接下来我们就可以去起我们当前的
[01:02] Kubernetes相关的服务首先我们起这个Kubernetes的API Server服务systemctl enabre kuber-api-server我们先把它进它enabre kuber-sorrystart应该是start kuber-api-server然后呢你呢在起完以后啊一定要看一下它的状态它是
[01:32] Active running说明我们的没问题的然后呢systemctl cooper-cuntoler-mnh1r我们把Controller manager起一下systemctl start cooper-Controller-mnh1rsystemctl sttus cooper-cuntoler-mnh1r这也是一个running
[02:03] 接下来我们要去起的是我们当前的这个scheduleStateCouple-SCHEDULERStateCouple-SCHEDULERStateCouple-SCHEDULER大家看一下我们当前的这个schedule服务他说我报错了
[02:33] 他说我这里边有问题应该是我们整个服务失败了我们看一下说我们这个位置并一下的Kuber Schedule告诉我们什么东西呢应该是我们在这个Schedule里面呢找不到应该是他的配置文件有问题我们看一下他的配置文件我们找一下Schedule我们这个Service文件应该没问题
[03:00] 他能找到这个服务那应该是我们这个配置文件里面有问题我们可以看看啊呃vi一下我们的etc下的cubernetes下的shedu l1看一下他你看一下这个值master没问题我们47找到这儿没问题然后你看看是不是其他的呢ok吧是不是前面这块我们在
[03:29] Coffee的时候应该少钻东西了,Kuber-SCH Schedule,Shift这回我们再重新去把我们这个Kuber-SCHEDULE进一下System Start Kuber-SCHEDULE我们重新起一下这回我们再看一下它的状态OK吧,这样的话呢,我这个
[03:59] 服务就起来了那整体上我整个服务全都起来也就是说我master这个节点基本搭建完了但是大家别忘了其实前期我们说过了你应该把你的防火墙都需要去禁掉或者说把它关闭所以你在这里边你要去把我们的fire wld防火墙关了因为你现在单击没问题一会儿我们要去通过node节点去连你的master那这个时候你要是不关防火墙
[04:28] 那么影响就大了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中启动并检查 Kubernetes 的 kube-scheduler 服务，包括配置文件修改和命令行操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 的“2.2.6 启动”章节，列出了需要执行的 systemctl 命令，包括 daemon-reload、enable 和 start 等操作。
画面 2: 在 SecureCRT 会话中执行了命令 `systemctl daemon-reload`。
画面 3: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 4: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 5: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 6: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 7: 在 SecureCRT 会话中执行了 `systemctl start kube-scheduler.Service`，并显示了服务启动失败的错误信息。
画面 8: 展示了 PPT 中关于“配置 kube-scheduler 服务文件”的内容，包括服务文件的描述、环境变量和安装部分。
画面 9: 展示了 PPT 中“配置文件 vi /etc/kubernetes/scheduler”的内容，其中包含环境变量配置。
画面 10: 在 SecureCRT 会话中执行了 `vi /etc/kubernetes/scheduler` 命令，显示了配置文件内容。
画面 11: 在 SecureCRT 会话中执行了 `systemctl status kube-scheduler.Service`，显示了服务状态为“active (running)”。
画面 12: 展示了 PPT 中关于“关闭防火墙”的内容，包括命令 `systemctl stop firewalld.Service` 和 `systemctl disable firewalld.Service`。
画面 13: 在 SecureCRT 会话中执行了 `systemctl status kube-scheduler.Service`，显示了服务状态为“active (running)”。
画面 14: 在 SecureCRT 会话中执行了 `systemctl stop firewalld` 命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
2.2.6 启动
完成以上配置后，按顺序启动服务
systemctl daemon-reload
systemctl enable kube-apiserver.Service
systemctl start kube-apiserver.Service
systemctl enable kube-Controller-manager.Service
systemctl start kube-Controller-manager.Service
systemctl enable kube-scheduler.Service
systemctl start kube-scheduler.Service
检查每个服务的健康状态：
systemctl status kube-apiserver.Service
systemctl status kube-Controller-manager.Service
systemctl status kube-scheduler.Service
```

画面 7:
```
[root@localhost ~]# systemctl start kube-scheduler.Service
Loaded: loaded (/usr/lib/systemd/system/kube-scheduler.Service; enabled; vendor preset: disabled)
Active: failed (Result: exit-code) since 二 2018-09-15 00:32:41 CST; 5s ago
Docs: https://github.com/GoogleCloudPlatform/kubernetes
Process: 19678 ExecStart=/usr/bin/kube-scheduler --kube-scheduler-args (code=exited, status=1/FAILURE)
Main PID: 19678 (code=exited, status=1/FAILURE)
```

画面 8:
```
[Install]
WantedBy=multi-user.target
```

画面 9:
```
KUBE_SCHEDULER_ARGS="--master=http://192.168.126.147:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"
```

画面 10:
```
KUBE_SCHEDULER_ARGS="--master=http://192.168.126.147:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"
```

画面 11:
```
Active: active (running) since 二 2018-09-15 00:34:11 CST; 5s ago
Docs: https://github.com/GoogleCloudPlatform/kubernetes
Main PID: 19714 (kube-scheduler)
Tasks: 9
Memory: 9.9M
CGroup: /system.slice/kube-scheduler.Service
└─19714 /usr/bin/kube-scheduler --master=http://192.168.126.147:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2
```

画面 12:
```
systemctl stop firewalld.Service
systemctl disable firewalld.Service
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.2.6 启动”，内容为启动服务的命令列表。
画面 8: PPT 标题为“配置 kube-scheduler 服务文件”，内容包括服务文件的描述、环境变量和安装部分。
画面 9: PPT 标题为“配置文件 vi /etc/kubernetes/scheduler”，内容包括环境变量配置。
画面 12: PPT 标题为“关闭防火墙”，内容包括命令和链接。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

