# 23.kubernetes核心技术-Replication Controller

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\23.kubernetes核心技术-Replication Controller_【海量资源尽在 ubkz.com】.mp4
- 时长 5分19秒（音频 320s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们说一下replication controllerreplication Controller我们简称RC它也是Chrome OS和系统中核心概念之一当我们定义一个RC并提交到Chrome Lite基金中以后MAS的节点上的Controller-main的主件就会得到通知它会定期检查系统中存活的PoE的
[00:22] 并确保我们这个目标POD的实例数量刚好等于我们RC的一个预期值那这里面大家可以看上面这个例子这就是我们定义的一个预期值是3那我们在这里边看一下如果过多或者是过少的POD运行呢系统会停掉或者创建一些新的POD那此外呢我们也可以通过修改RC的副本来实现一个动态的缩容
[00:49] 那我们可以看一下在我们当前的这个例子里边我们可以cat一下我们的demo5.5的一个rtc.yaml文件在这里边呢其实就是你看到这个代码了我们是创建了一个replication Controller那现在呢我们当前的印象其实是一个index那我们replicate就是我们的预期值是3那现在我们
[01:18] Kuberctl get pose你会发现我们有Nginx 1,2,3这三个这是我们当前预期创建的那我们说你可以去通过这样的一段命令呢去查看我们当前的这个或者动态的去扩容或缩容我们可以通过Kuberctl seale rc然后我们这个Nginx-re plsas
[01:46] 我们假设改成5那这个时候就会帮助我们去进行一个扩容你看我们这里边关于这个Ninx开始的有5个了如果我们刚才这个操作我改成1那这时候你再查查看一遍你会发现我们这个时候就只有一个也就是说我们可以去完成这种动态的缩放功能
[02:11] 由于这个replication Controller与我们的chromalice代码中的模块一个叫做replicate Controller同名所以在这个chromalice 1.2以后它就升级了另外一个新概念就是我们接下来要讲的这个replicate site
[02:27] 官方解释为是下一代的RC它与RC的区别是什么呢我们这个replay size它支持这种什么呢基于集合的label selector而我们RC呢只支持这种等式的label selector我们很少单独使用这个replay size它呢一般是和我们这个
[02:47] Deployment这个更高层面的资源对象所使用的也就是说我们replicite和我们后续要讲的deployment是一起去使用的我们很少是单独使用一个那我们知道一下这个replicite和我们那个deployment
[03:08] 它们形成一个整套的POD创建更新的编排机制那我们最好不要越过RC直接创建POD这也是我之前跟大家说的说我们在创建POD的时候一般很少像我们之前这种定义的说直接创建而是在我们创建RC的过程中去直接指定我们当前的POD的创建过程
[03:31] 这里边也跟我们说了我们最好不要越过RC创建POD而是因为Replication Controller它会通过RC来帮助我们管理这些副本从而实现自动的创建补助替换三处POD的副本这样能提高我们应用的一个容栽能力减少由于节点崩溃等意外状况造成的损失
[03:52] 那即便是应用程序只有一个Po的副本呢我们也是建议要用RC那这张讲解啊大家知道一下就是说我们Replicit Controller呢是我们当前整个这个Coreless的一个核心概念那我们呢在定义它的时候呢一般不是一般是我在这里面可以去定义它的一个期望的副本我们也可以通过这样的命令呢去进行一个动态的一个缩放容
[04:19] 那我们知道一下POD一般不建议单独去定义而是在我们这一个RC里面去定义那在V1.2以后我们的一个新的就是说RC的升级版就Replication Set它跟RC的区别就是在我们这个Label Select在选择时我们是可以基于这种集合的那我们在这个Replication Set的使用时也不是单独用而是结合我们另外一个叫做Deployment一起去使用的
[04:49] 那好,这是关于这个replication Controller简单跟大家做一个介绍大家回去可以把这段代码呢自己去创建执行一下看看我在这里面呢其实已经创建完了刚才呢我们是一个replication Controller我们也可以通过KuberGateSVC大家可以看一下我其实这里面还有个endings那这个呢就是我当前的这个serverservice后续呢我们也会去讲这个关于Service

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Replication Controller、Replica Set 和 Deployment 的概念、区别与使用方法，通过命令行演示如何创建、查看和调整副本数量。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Replication Controller 的 YAML 配置文件，其中包含 metadata、spec（replicas、selector、template）等字段，以及一个示例命令 `kubectl scale rc Nginx --replicas=5`。
画面 2: 与画面 1 内容相同，为同一页面的截图。
画面 3: 展示了终端窗口中执行 `kubectl get pods` 命令后，显示了多个 Pod 的状态，包括 `busybox`、`myweb`、`Nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 4: 与画面 3 内容相同，为同一终端窗口的截图。
画面 5: 展示了终端窗口中执行 `kubectl get pods` 命令后，显示了多个 Pod 的状态，包括 `busybox`、`myweb`、`Nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 6: 展示了终端窗口中执行 `kubectl scale rc Nginx --replicas=5` 命令，用于调整 Replication Controller 的副本数量。
画面 7: 展示了终端窗口中执行 `kubectl scale rc Nginx --replicas=5` 命令后，再次执行 `kubectl get pods` 命令，显示了 Pod 的状态，包括 `busybox`、`myweb`、`Nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 8: 展示了文档中“4 Replica Set详解”和“5 Deployment详解”两个章节的标题，以及 Deployment 的 YAML 配置文件开头部分。
画面 9: 与画面 8 内容相同，为同一页面的截图。
画面 10: 展示了 Service 的 YAML 配置文件，其中包含 metadata、spec（type、ports、selector）等字段。
画面 11: 展示了 Service 的 YAML 配置文件中 `ports` 字段的详细内容，包括 `containerPort: 80`。
画面 12: 展示了 Service 的 YAML 配置文件中 `selector` 字段的内容，包括 `app: Nginx`。
画面 13: 展示了终端窗口中执行 `kubectl scale rc Nginx --replicas=5` 命令后，再次执行 `kubectl get pods` 命令，显示了 Pod 的状态，包括 `busybox`、`myweb`、`Nginx-xxx` 等，部分 Pod 状态为 `ContainerCreating`。
画面 14: 展示了 Service 的 YAML 配置文件中 `ports` 字段的详细内容，包括 `nodePort: 3333`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
type: NodePort
ports:
  - port: 80
    nodePort: 3333
selector:
  app: Nginx
```
画面 3:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: Nginx
spec:
  replicas: 3
  selector:
    app: Nginx
  template:
    metadata:
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
        ports:
        - containerPort: 80
```
画面 4:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: Nginx
spec:
  replicas: 3
  selector:
    app: Nginx
  template:
    metadata:
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
        ports:
        - containerPort: 80
```
画面 6:
```bash
kubectl scale rc Nginx --replicas=5
```
画面 8:
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
```
画面 10:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: Nginx
spec:
  type: NodePort
  ports:
  - port: 80
    nodePort: 3333
  selector:
    app: Nginx
```
画面 11:
```yaml
ports:
  - containerPort: 80
```
画面 12:
```yaml
app: Nginx
```
画面 13:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: Nginx
spec:
  replicas: 5
  selector:
    app: Nginx
  template:
    metadata:
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
        ports:
        - containerPort: 80
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8: PPT 标题为“4 Replica Set详解”和“5 Deployment详解”。
画面 13: PPT 标题为“4 Replica Set详解”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

