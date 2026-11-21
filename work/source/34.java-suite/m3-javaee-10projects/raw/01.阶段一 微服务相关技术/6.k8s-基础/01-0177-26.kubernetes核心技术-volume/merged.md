# 26.kubernetes核心技术-volume

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\26.kubernetes核心技术-volume_【海量资源尽在 ubkz.com】.mp4
- 时长 4分44秒（音频 284s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们介绍一下volumevolume是POD中能够被多个容器访问的一个共享目录Criminalize中的volume定义在POD上它被一个POD中的多个容器挂载到具体的一个文件目录下volume与POD的生命周期是相同的
[00:21] 但与容器的生命周期不相关当容器终止或重启时Volume中的数据也不会丢失要使用VolumePOD需要指令Volume的类型和内容fpc.volume是用来定义它的类型和内容的我们可以通过fpc.container.volumemounts字段来映射到我们容器的一个位置
[00:43] 那Chrome Lite中支持多种类型的volume包括了MTDR,HousePath等等那接下来呢我们就介绍两三种大家看一下首先第一个呢叫MTDR
[00:54] MTDR类型的volume创建于POD被调度到某个数数器上的时候而同一个POD内的容器都能读写MTDR中的同一个文件一旦这个POD离开这个数数器MTDR中的数据就会被永久的删除那么基于这样的特性我们一般用MTDR时是用于这种服务器的日之或者是临时文件的这么一个读写
[01:22] 那大家看一下下面是一个简单的MTDR类型的volume的一个定义首先呢我们定义了一个pod那我们这里边呢通过一个volumes定义了一个volume我们给它一个名字叫catch volume那它为什么叫MTDR呢其实很明显它就是一个最开始是空的那我们这里边呢指定一下我们容器里面的镜像
[01:47] 然后我们指定一个volume mouse我们是把我们当前容器中的镜像里面的路径挂载到我们当前的目录下也就是说我们把容器里面的我们当前的镜像的catch目录挂载进来了通过name指定我们当前是这个volumecatch volume
[02:11] 那这是一个简单的一个MTDR的实例那么大家再往下看这是一个叫做host path
[02:18] 那hostpass它的这种类型的volume使得对应的容器能够访问当前宿主机上的一个指定目录例如我们需要运行一个访问的Docker系统目录的容器那么我们就使用VRLAB下的Docker目录作为hostDR类型的volume或者要在一个容器内部运行我们cAdvisor那么就使用div dv cgroups目录作为一个hostDR类型的volume一旦这个pod离开这个宿主机
[02:48] HouseDR中的数据虽然不会被永久删除但数据也不会随Pod迁移到我们其他的数据机上因此需要注意的是由于各个数据机上的文件系统的结构和内容并不一样所以相同的Pod的HouseDR可能在不同的数据机上表现的是不同的行为
[03:12] 下面是一个简单的host path的定义那我们可以看一下这里边我们也是一样通过volumes指定一下我们当前的一个名字那我们树主机上的目录是这样的一个目录然后我们是在我们container下去通过一个volume mouse去定义我们指定在容器中挂载的一个路径其实这个时候就是把我们树主机上的这个目录和我们容器里边的这个目录去关联上了
[03:40] 那这是一个关于我们host path类型的那再往下看一个叫做NFS那NFS类型的volume它是允许一块现有的网络硬盘在同一个pod内的同一个pod内的这个容器间共享那下面呢是一个简单的例子那这里边我们是一个development我们可以通过
[04:03] 这么的一个定义volumes去定义我们当前自己的volume那我们指定了我当前的这个服务器上的这个路径然后呢我们给它起了一个名字那它映射到的是我们容器里边我们当前这个容器啊它是一个redisimage redis嘛然后呢我们
[04:25] 是映射到我们当前redis的datameter下也就是说我们现在是把我们当前这个redis的这个datameter映射到我们当前这个输出机那这是跟大家简单说了一下关于我们Kubernetes里边的volume

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Volume 的多种类型（如 emptyDir、hostPath、nfs）及其对应的 YAML 配置示例，并过渡到 Namespace 的概念。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 讲解 Volume 概念，列出 Kubernetes 支持的 Volume 类型，包括 emptyDir、hostPath、gcePersistentDisk、awsElasticBlockStore、nfs、iscsi、flocker、glusterfs、rbd、cephfs、gitRepo、secret、persistentVolumeClaim、downwardAPI、azureFileVolume、azureDisk、vsphereVolume、Quobyte、PortworxVolume、ScaleIO。
画面 2: 展示 emptyDir 类型 Volume 的 YAML 示例，定义了一个名为 test-pd 的 Pod，包含一个容器，挂载名为 cache-volume 的 emptyDir。
画面 3: 展示 emptyDir 类型 Volume 的 YAML 示例，继续展示容器和 volumeMounts 配置。
画面 4: 展示 emptyDir 类型 Volume 的 YAML 示例，继续展示 volumes 配置。
画面 5: 展示 hostPath 类型 Volume 的 YAML 示例，定义了一个名为 test-pd 的 Pod，包含一个容器，挂载名为 test-volume 的 hostPath，路径为 /data。
画面 6: 展示 hostPath 类型 Volume 的 YAML 示例，继续展示 volumeMounts 和 volumes 配置。
画面 7: 讲解 nfs 类型 Volume，展示一个 Deployment 的 YAML 示例，用于部署 Redis。
画面 8: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 Deployment 的 metadata 和 spec。
画面 9: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 Deployment 的 template 中的 containers 配置。
画面 10: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 containers 中的 ports 和 env 配置。
画面 11: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 volumeMounts 和 volumes 配置，其中 volumes 定义了名为 redis-persistent-storage 的 nfs 类型 Volume。
画面 12: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 volumes 中的 nfs 配置，指定 server 为 192.168.128.112。
画面 13: 展示 nfs 类型 Volume 的 YAML 示例，继续展示 volumes 中的 nfs 配置，指定 server 为 192.168.128.112。
画面 14: 回到 emptyDir 类型 Volume 的 YAML 示例，展示容器和 volumeMounts 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
apiVersion: app/v1beta1
kind: Deployment
name: Nginx-deployment
minReplicas: 1
maxReplicas: 10
targetCPUUtilizationPercentage: 50
```
画面 2:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /cache
    name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```
画面 3:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /cache
    name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```
画面 4:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /cache
    name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```
画面 5:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /test-pd
    name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      path: /data
```
画面 6:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /test-pd
    name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      path: /data
```
画面 7:
```yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: redis
```
画面 8:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: Docker.io/nazanpc/webserver
    name: test-container
  volumeMounts:
  - mountPath: /test-pd
    name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      path: /data
```
画面 9:
```yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: redis
spec:
  selector:
    matchLabels:
      app: redis
  revisionHistoryLimit: 2
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - image: redis
        name: redis
        ImagePullPolicy: IfNotPresent
        ports:
        - containerPort: 6379
          name: redis6379
        env:
        - name: ALLOW_EMPTY_PASSWORD
          value: "yes"
        - name: REDIS_PASSWORD
          value: "redis"
      volumeMounts:
      - name: redis-persistent-storage
        mountPath: /data
      volumes:
      - name: redis-persistent-storage
        nfs:
          path: /Kubernetes-nfs/redis/data
          server: 192.168.128.112
```
画面 10:
```yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: redis
spec:
  selector:
    matchLabels:
      app: redis
  revisionHistoryLimit: 2
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - image: redis
        name: redis
        ImagePullPolicy: IfNotPresent
        ports:
        - containerPort: 6379
          name: redis6379
        env:
        - name: ALLOW_EMPTY_PASSWORD
          value: "yes"
        - name: REDIS_PASSWORD
          value: "redis"
      volumeMounts:
      - name: redis-persistent-storage
        mountPath: /data
      volumes:
      - name: redis-persistent-storage
        nfs:
          path: /Kubernetes-nfs/redis/data
          server: 192.168.128.112
```
画面 11:
```yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: redis
spec:
  selector:
    matchLabels:
      app: redis
  revisionHistoryLimit: 2
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - image: redis
        name: redis
        ImagePullPolicy: IfNotPresent
        ports:
        - containerPort: 6379
          name: redis6379
        env:
        - name: ALLOW_EMPTY_PASSWORD
          value: "yes"
        - name: REDIS_PASSWORD
          value: "redis"
      volumeMounts:
      - name: redis-persistent-storage
        mountPath: /data
      volumes:
      - name: redis-persistent-storage
        nfs:
          path: /Kubernetes-nfs/redis/data
          server: 192.168.128.112
```
画面 12:
```yaml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: redis
spec:
  selector:
    matchLabels:
      app: redis
  revisionHistoryLimit: 2
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - image: redis
        name: redis
        ImagePullPolicy:

