# 画面线理解：26.kubernetes核心技术-volume

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\26.kubernetes核心技术-volume_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:07, 01:31, 01:41, 02:17, 03:15, 03:25, 03:40, 03:56, 04:04, 04:23, 04:30, 04:35, 04:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:52:54

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
name: nginx-deployment
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
  - image: docker.io/nazanpc/webserver
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
  - image: docker.io/nazanpc/webserver
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
  - image: docker.io/nazanpc/webserver
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
  - image: docker.io/nazanpc/webserver
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
  - image: docker.io/nazanpc/webserver
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
  - image: docker.io/nazanpc/webserver
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
          path: /k8s-nfs/redis/data
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
          path: /k8s-nfs/redis/data
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
          path: /k8s-nfs/redis/data
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
