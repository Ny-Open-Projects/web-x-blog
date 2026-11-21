# 15.Kubernetes集群搭建Node安装-启动

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\15.Kubernetes集群搭建Node安装-启动_【海量资源尽在 ubkz.com】.mp4
- 时长 1分32秒（音频 92s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来呢我们就把我们的这些服务啊该启动的都起来那我们来看一下首先呢我们需要去systemctl daemon-reload然后呢我们去start一下我们的Docker吧然后我在这里边st2sdocker我们看一下是不是已经running了它是一个
[00:26] 然后我们把这个KuberLite和KuberProxy都启动一下System Start KuberLite我们看一下我们这也是running的然后呢我们Systemctl我们Start strt我们当前的Kuber-ProxySystemctl我们sttus tatus Kuber-Proxy
[00:58] 这里面应该是写错了吧SYSTEMOK我们现在呢所有的服务都启动了那这样的话呢我们一个节点已经做好了那么对于我们这个Node2节点呢大家呢可以把我们当前机器啊去copy一份然后呢你把IP改一下把配置文件呢也相应的改一下那这样的话呢我们就可以完成多个节点的配置

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中通过 systemctl 命令启动并检查 Kubernetes 的核心组件（kubelet 和 kube-proxy）服务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示终端中执行了 `systemctl daemon-reload`，并成功写入 `/etc/kubernetes/proxy` 配置文件。
画面 2: 执行 `systemctl start Docker` 启动 Docker 服务，并显示服务状态为 active（running）。
画面 3: 终端提示符显示为 `[root@localhost /]#`，准备执行下一步命令。
画面 4: 执行 `systemctl start kubelet` 启动 Kubernetes 的 kubelet 服务，并显示服务状态为 active（running）。
画面 5: 终端提示符显示为 `[root@localhost /]#`，准备执行下一步命令。
画面 6: 执行 `systemctl start kube-proxy` 启动 Kubernetes 的 kube-proxy 服务，并显示服务状态为 active（running）。
画面 7: 终端提示符显示为 `[root@localhost /]#`，准备执行下一步命令。
画面 8: PPT 页面标题为“2.4 Node2安装”，并提示“请参考Node1安装，注意修改IP”。
画面 9: PPT 页面标题为“2.4 Node2安装”，并提示“请参考Node1安装，注意修改IP”。
画面 10: PPT 页面标题为“2.5 健康检查与示例测试”，并列出“查看集群状态”和“查看master集群组件状态”两个操作。
画面 11: 终端中执行了 `kubectl get nodes` 命令，列出集群中节点的名称和状态。
画面 12: 终端中执行了 `kubectl get componentstatuses` 命令，列出集群中各个组件的状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
/etc/kubernetes/proxy [New] 148C written
```
画面 2:
```
[root@localhost /]# systemctl start Docker
[root@localhost /]# systemctl status Docker
● Docker.Service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/Docker.Service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 14:28:39 CST; 45 ago
     Docs: https://docs.Docker.com/
   Main PID: 3871 (dockerd)
     Tasks: 26
     Memory: 46.0M
   CGroup: /system.slice/Docker.Service
           └─3871 /usr/bin/dockerd -H fd:// --containerd=/var/run/Docker/containerd/containerd.toml
```
画面 3:
```
[root@localhost /]#
```
画面 4:
```
[root@localhost /]# systemctl start kubelet
[root@localhost /]# systemctl status kubelet
● kubelet.Service - Kubernetes Kubelet Server
   Loaded: loaded (/usr/lib/systemd/system/kubelet.Service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 04:27:13 CST; 6s ago
     Docs: https://github.com/GoogleCloudPlatform/kubernetes
   Main PID: 4080 (kubelet)
     Tasks: 12
   CGroup: /system.slice/kubelet.Service
           └─4080 /usr/bin/kubelet --pod-infra-container-image=192.168.126.142:5000/pod-infra-container:latest
```
画面 5:
```
[root@localhost /]#
```
画面 6:
```
[root@localhost /]# systemctl start kube-proxy
[root@localhost /]# systemctl status kube-proxy
● kube-proxy.Service - Kubernetes kube-proxy Server
   Loaded: loaded (/usr/lib/systemd/system/kube-proxy.Service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 04:27:30 CST; 10s ago
     Docs: https://github.com/GoogleCloudPlatform/kubernetes
   Main PID: 4097 (kube-proxy)
     Tasks: 0
   CGroup: /system.slice/kube-proxy.Service
           └─4097 /usr/bin/kube-proxy --master=http://192.168.126.147:8080 --hostname-override=192.168.126.147
```
画面 7:
```
[root@localhost /]#
```
画面 8:
```
2.4 Node2安装

请参考Node1安装，注意修改IP

2.5 健康检查与示例测试
  • 查看集群状态
  • 查看master集群组件状态
```
画面 9:
```
2.4 Node2安装

请参考Node1安装，注意修改IP

2.5 健康检查与示例测试
  • 查看集群状态
  • 查看master集群组件状态
```
画面 10:
```
2.5 健康检查与示例测试
  • 查看集群状态
  • 查看master集群组件状态
```
画面 11:
```
[root@bogon ~]# kubectl get nodes
NAME      STATUS     AGE
192.168.126.141   Ready    1m
192.168.126.147   Ready    1m
```
画面 12:
```
[root@bogon ~]# kubectl get componentstatuses
NAME                 STATUS    MESSAGE              ERROR
scheduler            Healthy   ok
Controller-manager   Healthy   ok
etcd-0               Healthy   {"health": "true"}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8、9、10: PPT 页面标题为“2.4 Node2安装”，下方提示“请参考Node1安装，注意修改IP”。下方有“2.5 健康检查与示例测试”标题，其下有“查看集群状态”和“查看master集群组件状态”两个子项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

