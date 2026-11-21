# 画面线理解：21.kubernetes核心技术-Pod(2)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\21.kubernetes核心技术-Pod(2)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:44, 01:26, 01:56, 02:10, 03:53, 05:03, 05:26, 05:42, 06:13, 06:28, 07:07, 08:35, 08:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:48:55

1) 这一组画面整体在讲 Kubernetes 中 Pod 的分类、生命周期、重启策略及资源配置等核心概念。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了 Typora 文档中“1.3 Pod的分类”章节，内容包括“普通Pod”和“静态Pod”的定义，以及“1.4 Pod生命周期和重启策略”和“1.5 Pod资源配置”的章节标题。
画面2: 展示了 Typora 文档中“1.3 Pod的分类”章节，内容与画面1相同，但底部任务栏显示了多个虚拟机窗口。
画面3: 展示了 SecureCRT 会话窗口，其中包含“kubect1 describe pod busybox”命令的输出结果，显示了 Pod 的详细信息，包括容器状态、镜像、端口等。同时，任务栏显示了多个虚拟机窗口。
画面4: 展示了 SecureCRT 会话窗口，其中包含“kubect1 describe pod busybox”命令的输出结果，显示了 Pod 的详细信息，包括容器状态、镜像、端口等。同时，任务栏显示了多个虚拟机窗口。
画面5: 展示了 Typora 文档中“1.3 Pod的分类”章节，内容与画面1相同。
画面6: 展示了 Typora 文档中“1.3 Pod的分类”章节，内容与画面1相同，但滚动条显示了“1.4 Pod生命周期和重启策略”章节。
画面7: 展示了 SecureCRT 会话窗口，其中包含“kubect1 describe pod busybox”命令的输出结果，显示了 Pod 的详细信息，包括容器状态、镜像、端口等。同时，任务栏显示了多个虚拟机窗口。
画面8: 展示了 Typora 文档中“1.4 Pod生命周期和重启策略”章节，内容包括“Pod的状态”和“Pod重启策略”两个表格。
画面9: 展示了 Typora 文档中“1.3 Pod的分类”章节，内容与画面1相同。
画面10: 展示了 Typora 文档中“1.4 Pod生命周期和重启策略”章节，内容包括“常见状态转换”表格。
画面11: 展示了 Typora 文档中“1.5 Pod资源配置”章节，内容包括“Requests”和“Limits”两个参数的说明。
画面12: 展示了 Typora 文档中“1.5 Pod资源配置”章节，内容包括“Requests”和“Limits”两个参数的说明，以及“2 Label详解”章节标题。
画面13: 展示了 Typora 文档中“1.4 Pod生命周期和重启策略”章节，内容与画面8相同。
画面14: 展示了 Typora 文档中“1.5 Pod资源配置”章节，内容与画面11相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面3:
```
bash: kubectl
[root@localhost test]# kubectl describe pod busybox
Name:         busybox
Namespace:    default
Node:         127.0.0.1/127.0.0.1
Start Time:   Sat, 29 Sep 2018 14:05:18 +0800
Labels:       <none>
Status:       Running
IP:           10.254.74.5
Containers:
  busybox:
    Image:      docker://78bee9e8467b6235cce86d0979741d62ed57cacaf5392b63ad4c6c38426d06
    Image ID:   registry.cn-hangzhou.aliyuncs.com/google_containers/busyboxsha256:99a788f7f4d44c2387c21093cc4147e1c0d3a7bef/e050206f37e30
    Port:       40900
    Command:
      sleep
      3000
    State:       Running
    Last State:  Terminated
    Reason:      Completed
    Started:     Fri, 05 Oct 2018 23:35:34 +0800
    Finished:    Fri, 05 Oct 2018 23:35:34 +0800
    Ready:       True
    Restart Count:  10
    Environment Variables:  <none>
Conditions:
  Type           Status
  Initialized    True
  Ready          True
  PodScheduled   True
No volumes.
QoS Class:       Besteffort
Tolerations:     <none>
No events.
[root@localhost test]# kubectl delete -f demo1.yaml
```

画面11:
```
spec:
  containers:
  - name: db
    image: mysql
    resources:
      requests:
        memory: "640M"
        cpu: "250m"
      limits:
        memory: "128M"
        cpu: "500m"
```

画面12:
```
spec:
  containers:
  - name: db
    image: mysql
    resources:
      requests:
        memory: "640M"
        cpu: "250m"
      limits:
        memory: "128M"
        cpu: "500m"
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8:
表格1: Pod的状态
| 状态值 | 说明 |
| :--- | :--- |
| Pending | API Server已经创建了该Pod,但Pod中的一个或多个容器的镜像还没有创建,包括镜像下载过程 |
| Running | Pod内所有容器已创建,且至少一个容器处于运行状态、正在启动状态或正在重启状态 |
| Completed | Pod内所有容器均已成功退出,且不会再重启 |
| Failed | Pod内所有容器均已退出,但至少一个容器退出失败 |
| Unknown | 由于某种原因无法获取Pod状态,例如网络通信不畅 |

表格2: Pod重启策略
| 重启策略 | 说明 |
| :--- | :--- |
| Always | 当容器失败时,由kubelet自动重启该容器 |
| OnFailure | 当容器终止运行且退出码不为0时,由kubelet自动重启该容器 |
| Never | 不论容器运行状态如何,kubelet都不会重启该容器 |

表格3: 常见状态转换
| Pod包含的容器数 | Pod当前的状态 | 发生事件 | Pod的结果状态 (RestartPolicy=Always) | Pod的结果状态 (RestartPolicy=OnFailure) | Pod的结果状态 (RestartPolicy=Never) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 包含两个容器 | Running | 1个容器失败退出 | Running | Succeeded | Succeeded |
| 包含两个容器 | Running | 容器被OOM杀掉 | Running | Running | Failure |
| 包含两个容器 | Running | 1个容器失败退出 | Running | Running | Running |
| 包含两个容器 | Running | 容器被OOM杀掉 | Running | Running | Failure |

画面10:
表格: 常见状态转换
| Pod包含的容器数 | Pod当前的状态 | 发生事件 | Pod的结果状态 (RestartPolicy=Always) | Pod的结果状态 (RestartPolicy=OnFailure) | Pod的结果状态 (RestartPolicy=Never) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 包含两个容器 | Running | 1个容器失败退出 | Running | Succeeded | Succeeded |
| 包含两个容器 | Running | 容器被OOM杀掉 | Running | Running | Failure |
| 包含两个容器 | Running | 1个容器失败退出 | Running | Running | Running |
| 包含两个容器 | Running | 容器被OOM杀掉 | Running | Running | Failure |

画面11:
表格: Pod的状态
| 状态值 | 说明 |
| :--- | :--- |
| Pending | API Server已经创建了该Pod,但Pod中的一个或多个容器的镜像还没有创建,包括镜像下载过程 |
| Running | Pod内所有容器已创建,且至少一个容器处于运行状态、正在启动状态或正在重启状态 |
| Completed | Pod内所有容器均已成功退出,且不会再重启 |
| Failed | Pod内所有容器均已退出,但至少一个容器退出失败 |
| Unknown | 由于某种原因无法获取Pod状态,例如网络通信不畅 |

表格: Pod重启策略
| 重启策略 | 说明 |
| :--- | :--- |
| Always | 当容器失败时,由kubelet自动重启该容器 |
| OnFailure | 当容器终止运行且退出码不为0时,由kubelet自动重启该容器 |
| Never | 不论容器运行状态如何,kubelet都不会重启该容器 |

表格: 常见状态转换
| Pod包含的容器数 | Pod当前
