# 画面线理解：15.Kubernetes集群搭建Node安装-启动

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\15.Kubernetes集群搭建Node安装-启动_【海量资源尽在 ubkz.com】.mp4
- 抽帧：12 帧 @ 00:06, 00:23, 00:25, 00:40, 00:42, 01:07, 01:10, 01:12, 01:14, 01:15, 01:19, 01:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:44:41

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中通过 systemctl 命令启动并检查 Kubernetes 的核心组件（kubelet 和 kube-proxy）服务状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示终端中执行了 `systemctl daemon-reload`，并成功写入 `/etc/kubernetes/proxy` 配置文件。
画面 2: 执行 `systemctl start docker` 启动 Docker 服务，并显示服务状态为 active（running）。
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
[root@localhost /]# systemctl start docker
[root@localhost /]# systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 14:28:39 CST; 45 ago
     Docs: https://docs.docker.com/
   Main PID: 3871 (dockerd)
     Tasks: 26
     Memory: 46.0M
   CGroup: /system.slice/docker.service
           └─3871 /usr/bin/dockerd -H fd:// --containerd=/var/run/docker/containerd/containerd.toml
```
画面 3:
```
[root@localhost /]#
```
画面 4:
```
[root@localhost /]# systemctl start kubelet
[root@localhost /]# systemctl status kubelet
● kubelet.service - Kubernetes Kubelet Server
   Loaded: loaded (/usr/lib/systemd/system/kubelet.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 04:27:13 CST; 6s ago
     Docs: https://github.com/GoogleCloudPlatform/kubernetes
   Main PID: 4080 (kubelet)
     Tasks: 12
   CGroup: /system.slice/kubelet.service
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
● kube-proxy.service - Kubernetes kube-proxy Server
   Loaded: loaded (/usr/lib/systemd/system/kube-proxy.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-09-21 04:27:30 CST; 10s ago
     Docs: https://github.com/GoogleCloudPlatform/kubernetes
   Main PID: 4097 (kube-proxy)
     Tasks: 0
   CGroup: /system.slice/kube-proxy.service
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
controller-manager   Healthy   ok
etcd-0               Healthy   {"health": "true"}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8、9、10: PPT 页面标题为“2.4 Node2安装”，下方提示“请参考Node1安装，注意修改IP”。下方有“2.5 健康检查与示例测试”标题，其下有“查看集群状态”和“查看master集群组件状态”两个子项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
