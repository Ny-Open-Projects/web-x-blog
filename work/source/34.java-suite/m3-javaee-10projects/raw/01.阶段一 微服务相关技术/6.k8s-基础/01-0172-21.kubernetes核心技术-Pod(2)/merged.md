# 21.kubernetes核心技术-Pod(2)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\21.kubernetes核心技术-Pod(2)_【海量资源尽在 ubkz.com】.mp4
- 时长 8分44秒（音频 525s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们可以使用Kubernetes CTL create-f指定我们的YAML文件这种方式去创建一个我们当前的POD我们可以看一下例子在我们当前这里边有我们的demo2.yaml文件这就是帮助我们去创建了一个POD我们也可以通过Kubernetes CTL get
[00:27] pod 或者是 po 指定一个名字的方式来查看我们当前的这个pod那你也可以去指定 po 然后告外的这种方式以及 describe 这种方式去查看一个我们pod 的详细信息那我们可以演示一下在这里边我们可以 kuberctl get pod po或者是我们直接一个 pod
[00:52] 或者是你直接可以去直接一个叫做pose这都可以去查看我们所有当前的pose那么你后面也可以加上一个名字例如我们这里边加上busybox你去查看我们某一个具体的pose那你也可以通过dscrpe然后呢我们去通过一个pose的一个名字的方式哎写错了
[01:22] 去查看一个POD的详细信息这是我们说查看POD的相关信息我要想删除一个POD可以通过一个delete-f然后POD加上一个我们的央目文件或者一个delete-pod加上一个--out或者是一个POD的名字去删除我们这里边可以这么办Kubernetesctl delete-f
[01:51] 然后呢你加上一个当前我们的demo1.yaml这样的话呢我们可以去删除一个pod也可以delete刚刚out这样的话呢就是我们sorry了落一个pod去把所有的pod删除了那我这里边不去指定删除大家回去可以自己去尝试一下那这是说我们去怎样去查看呢
[02:19] 以及我们创建和删除Pod那下面呢再来看一下我们Pod分类前面我们说过Pod分类分成两种一种是普通的Pod还有一种是静态Pod那这两种有什么区别我们要知道一下
[02:33] 第一个普通的POD它是一旦被创建就会被放入到我们的ETCD中存储随后会被我们GrooveLines Master调度到我们某个具体的Node上也就会被我们的Master调到具体的Node上并进行绑定随后该POD对应的Node上的GrooveLines进程的实体化一组相关的Docker容器并启动它在默认情况下当POD里某个容器停止时
[02:57] Kubernetes会自动检测到这个问题并且重新启动这个POD里所有的容器如果POD所在的Node当机了那么将会将这个Node上的所有的POD重新调入其他节点上也就是说我们的普通POD我们是在整个我们当前的管理范围内如果它出了问题我们会自动的在整个Kubernetes进行中检测到
[03:21] 那静态的POD是什么呢静态POD是由Kubelet进行管理仅存在于特定Node上也就是说它是在具体的某一个节点上的而不能通过API Server进行管理无法与我们的RC然后Development或者是DepthSite进行关联并且Kubelet也无法对它进行健康检查那对于这种静态的POD我们很少用大家了解一下就行那我们用的更多的还是这种
[03:48] 普通的POD它是在整个集讯管理范围内的那我们可以去对它进行这个创建启动然后系统呢可以检测掉它如果出了问题呢它会帮我们自动的去调度到某一个具体的node上并重新去创建它
[04:05] 那这些说完以后呢我们来看一看我们Pod是有一个生命周期还有一个重启策略那Pod的状态那这里面状态呢一共有这么几种第一种就是Pending它是说我们当前API Server创建了该Pod该Pod但Pod中的一个或多个容器镜像还没有创建包括镜像下载过程那这个时候呢它就是一个准备Pending的过程那如果我们都准备好了那这时候就变成一个Running
[04:31] 就是说POD内所有容器已经创建但且至少一个容器处于运行状态正在启动状态或者是正在重启状态这时候就是一个Running那CompletedCompleted那是POD内所有的容器均成功执行并退出且不会再重启还有一个就是失败状态说我们POD内所有的容器均已退出但至少一个容器退出失败还有一种就是未知状态Unknown
[04:58] 由于某种原因无法获得POD状态,例如网络不畅通。
[05:03] 我们在这里可以看一下,在这里面,我把这个删掉。
[05:08] Kuberctl,我们getPOD当我过去这个状态时,你看我们的状态是running,就是说我们都是正在运行的状态。
[05:20] 大家知道一下,我们POD有这么一二三四五种状态。
[05:25] 这里面还有一个是关于
[05:27] POD的重启策略那POD的重启策略呢包含了always然后呢unfail还有是never默认是一个always那代表什么呢是说always说当容器失效时啊有Kubelag自动重启该容器那这也是我们前面说的一个普通的POD当它这个
[05:45] 出了一些问题那我们master呢会去检测到它那我们会把它在其他的动作节点上重新去调度然后呢去重新去启动它那这是因为你指定它的重启策略是always那如果是失败呢是说当容器终止运行且退出马步为零时由Kubelet自动重启该容器还有一个是never是不论容器运行状态如何我们Kubelet都不会重启该容器
[06:13] 那下面是给大家做了一个图,这是说一下我们当前的一个常见的转换图大家可以去看一看我们这几个状态的一个转换的情况那最后是一个关于我们这个Pod的一个资源配置其实简单点就是说,当我们创建一个Pod的时候我们是可以给它指定一些资源的,例如我们的CPU,例如我们的内存那我们来看
[06:41] 每个POD都可以对其能使用的服务器上的计算资源设置限额ChromeLens中可以设置限额的计算资源有CPU与Memory也就是说可以指定我们的CPU和内存其中CPU的这个资源单位为CPU的数量是一个绝对值而非相对值Memory配合也是一个绝对值它的单位是内存字结数那ChromeLens里面一个计算资源进行
[07:10] 配格限定需要两个参数也就是说我们在这里面有个例子当我们制定一个限格时我们可以制定两个参数一个是request还有一个是limitase那么这个request该资源最小申请数系统必须满足要求limitase是该资源最大的申请数也就是说一个是最小的一个是最大的那么这个最大的是不能突破的当容器试图使用某个超过这个资源时可能会被
[07:36] Cruise Q 调配重启那大家可以看一下这里面这是Request,这是Limits那么Request呢我们说Memorial我们是64MBCPU呢我们分配250那我们这里面Limits呢大家看这是一个必须最小的这是我们这个一个最大的限额那我们最大呢指定了128CPU指定了500那这里面就是表示啊我们MySQL容器这儿我们是一个
[08:05] 百色客的镜像吧那他呢申请最少0.25个CPU也就是说这里边我们指定250代表0.25个CPU以及64M的内存那在运行过程中所使用的这个资源配合为0.5个那0.5个CPU啊以及128M这个内存也就是说我们这里边允许最大使用的是这些如果你超过了那我们可能会被Kubernetes的Kill掉并重启
[08:32] 这是关于POD的一些相关的情况我们关于这个POD分类周期还有重启策略还有它一个资源配合的介绍

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    Image:      Docker://78bee9e8467b6235cce86d0979741d62ed57cacaf5392b63ad4c6c38426d06
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

