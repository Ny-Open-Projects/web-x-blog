# 27.kubernetes核心技术-namespace

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\27.kubernetes核心技术-namespace_【海量资源尽在 ubkz.com】.mp4
- 时长 3分16秒（音频 196s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那下面呢我们再介绍一下Namespace那Namespace在很多情况下呢是用于实现多用户的一个资源隔离那么我们通过将集群内部的资源对象分配到不同的Namespace中啊形成这种逻辑上的一个分组注意啊它是一个逻辑上的
[00:19] 那么便于不同的分组在共享使用整个集群的资源同时还能被分别管理那ChromeLens集群在启动时会创建一个叫做Defund的一个Namespace如果你不指定Namespace则用户创建的Pos的RC Service都将被系统创建到这个默认的Defund的Namespace下我们可以看一下properctl.getPos那我们这里面创建了一些Pos那我们
[00:47] 可以Kuberctl dscrib我们可以看一个假设叫当前这里面有个叫myy吧那大家看一下我们当前这里边它的namespace就是一个defund那这是因为我在前期创建他们时我根本就没有指定我当前的namespace那它就呢
[01:08] 使用了一个默认的namespace那么我们也可以去手动创建一个namespace那大家看一下这是一个我们创建namespace过程那这是一个pose我给我这个pose呢去指定了当前的namespace是devicement然后呢我们就可以去在查看它的过程中通过杠杠namespace加上我们一个devicement去查看我们当前这个命名空间下的pose那我们可以看一下
[01:37] 这里边我已经把文件创建出来我们cat一下有个demo6我们的namespace这是我们创建了一个namespace这个名字就叫做我们的devaluant然后大家再看一个demo6我们当前有一个pod这是我通过创建一个pod来
[02:02] 指定它的名称空间叫Devaluement那我们可以通过Kubectl get pose这个时候你在创建它的时候你是找不到我们Devaluement下的这些pode而你看到的其实是默认的那如果说我们要看这个Devaluement下面你就可以这么办name of space等于Devaluement
[02:30] 这个时候你是能看到我当前definitment这个名称空间下的pose那好这是说我们namespace怎么去创建以及怎么查看那一定要知道我们通过namespace其实是做了一个什么逻辑上的分组那它的作用呢就是用于我们这个对资源的一个分别的管理或者说一个方便的管理那么
[02:57] 如果我们不去在创建这些RC啊POD的时候你没有去指定它的名称空间它是一个默认的那你要去想指定呢也可以在我们在创建它时可以通过Namespace然后呢去指定你当前的一个Namespace

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kubernetes 中使用 Namespace 来隔离资源，并通过 YAML 文件创建和查看 Namespace 中的 Pod。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在终端执行 `Docker search testwebserver` 命令，搜索 Docker Hub 上的镜像，结果包含多个与 webserver 相关的镜像。提示信息显示因私有仓库证书问题导致连接被拒绝。
画面2：在终端执行 `kubectl get pods` 命令，列出当前命名空间下的所有 Pod，显示多个 Pod 正在运行或创建中。
画面3：在 Typora 中打开《容器化进阶Kubernetes核心技术》文档，显示第8章“Namespace详解”内容，其中包含创建 Namespace 和 Pod 的 YAML 配置示例。
画面4：在 Typora 文档中，高亮显示了 YAML 配置文件中的 `kind: Pod` 部分，下方显示了 `kubectl get pods --namespace=development` 命令。
画面5：在 Typora 文档中，光标位于 `kubectl get pods --namespace=development` 命令行上，准备执行。
画面6：在终端执行 `kubectl get pods` 命令，显示了多个 Pod 的状态，包括 `Running` 和 `ContainerCreating`。
画面7：终端界面为空，等待输入命令。
画面8：在终端执行 `cat demo-namespace.yaml` 命令，显示了创建 Namespace 的 YAML 文件内容。
画面9：在终端执行 `cat demo-pod.yaml` 命令，显示了创建 Pod 的 YAML 文件内容。
画面10：在终端执行 `kubectl get pods` 命令，显示了所有 Pod 的状态。
画面11：在 Typora 文档中，光标位于“9 Service 详解”章节的开头，准备讲解 Service 的概念。
画面12：在 Typora 文档中，光标位于“9 Service 详解”章节的开头，准备讲解 Service 的概念。
画面13：在 Typora 文档中，光标位于“8. Namespace详解”章节的开头，准备讲解 Namespace 的概念。
画面14：在 Typora 文档中，光标位于“8. Namespace详解”章节的开头，准备讲解 Namespace 的概念。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: development
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面4：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面8：
```yaml
apiVersion: v1
kind: namespace
metadata:
  name: development
```

画面9：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

画面10：
```yaml
apiVersion: v1
kind: namespace
metadata:
  name: development
```

画面11：
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
  namespace: development
spec:
  containers:
  - image: busybox
    command:
    - sleep
    - "3600"
    name: busybox
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义、创建和查看命令。
画面4：PPT标题为“8. Namespace详解”，内容包括 Namespace 的创建和查看命令。
画面5：PPT标题为“8. Namespace详解”，内容包括 Namespace 的创建和查看命令。
画面11：PPT标题为“9 Service 详解”，内容包括 Service 的定义和基本用法。
画面12：PPT标题为“9 Service 详解”，内容包括 Service 的定义和基本用法。
画面13：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义和创建命令。
画面14：PPT标题为“8. Namespace详解”，内容包括 Namespace 的定义和创建命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

