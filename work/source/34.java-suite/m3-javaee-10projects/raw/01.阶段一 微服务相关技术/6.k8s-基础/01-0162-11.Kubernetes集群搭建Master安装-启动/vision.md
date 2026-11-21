# 画面线理解：11.Kubernetes集群搭建Master安装-启动

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\11.Kubernetes集群搭建Master安装-启动_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:18, 00:41, 00:58, 01:34, 02:01, 02:27, 02:59, 03:02, 03:14, 04:04, 04:09, 04:12, 04:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:42:09

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中启动并检查 Kubernetes 的 kube-scheduler 服务，包括配置文件修改和命令行操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 的“2.2.6 启动”章节，列出了需要执行的 systemctl 命令，包括 daemon-reload、enable 和 start 等操作。
画面 2: 在 SecureCRT 会话中执行了命令 `systemctl daemon-reload`。
画面 3: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 4: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 5: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 6: SecureCRT 会话中光标停留在命令行提示符 `[root@localhost ~]#`。
画面 7: 在 SecureCRT 会话中执行了 `systemctl start kube-scheduler.service`，并显示了服务启动失败的错误信息。
画面 8: 展示了 PPT 中关于“配置 kube-scheduler 服务文件”的内容，包括服务文件的描述、环境变量和安装部分。
画面 9: 展示了 PPT 中“配置文件 vi /etc/kubernetes/scheduler”的内容，其中包含环境变量配置。
画面 10: 在 SecureCRT 会话中执行了 `vi /etc/kubernetes/scheduler` 命令，显示了配置文件内容。
画面 11: 在 SecureCRT 会话中执行了 `systemctl status kube-scheduler.service`，显示了服务状态为“active (running)”。
画面 12: 展示了 PPT 中关于“关闭防火墙”的内容，包括命令 `systemctl stop firewalld.service` 和 `systemctl disable firewalld.service`。
画面 13: 在 SecureCRT 会话中执行了 `systemctl status kube-scheduler.service`，显示了服务状态为“active (running)”。
画面 14: 在 SecureCRT 会话中执行了 `systemctl stop firewalld` 命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
2.2.6 启动
完成以上配置后，按顺序启动服务
systemctl daemon-reload
systemctl enable kube-apiserver.service
systemctl start kube-apiserver.service
systemctl enable kube-controller-manager.service
systemctl start kube-controller-manager.service
systemctl enable kube-scheduler.service
systemctl start kube-scheduler.service
检查每个服务的健康状态：
systemctl status kube-apiserver.service
systemctl status kube-controller-manager.service
systemctl status kube-scheduler.service
```

画面 7:
```
[root@localhost ~]# systemctl start kube-scheduler.service
Loaded: loaded (/usr/lib/systemd/system/kube-scheduler.service; enabled; vendor preset: disabled)
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
CGroup: /system.slice/kube-scheduler.service
└─19714 /usr/bin/kube-scheduler --master=http://192.168.126.147:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2
```

画面 12:
```
systemctl stop firewalld.service
systemctl disable firewalld.service
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.2.6 启动”，内容为启动服务的命令列表。
画面 8: PPT 标题为“配置 kube-scheduler 服务文件”，内容包括服务文件的描述、环境变量和安装部分。
画面 9: PPT 标题为“配置文件 vi /etc/kubernetes/scheduler”，内容包括环境变量配置。
画面 12: PPT 标题为“关闭防火墙”，内容包括命令和链接。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
