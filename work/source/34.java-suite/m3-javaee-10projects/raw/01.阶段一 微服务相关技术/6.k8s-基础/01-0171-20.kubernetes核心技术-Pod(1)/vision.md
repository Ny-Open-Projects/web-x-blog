# 画面线理解：20.kubernetes核心技术-Pod(1)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\20.kubernetes核心技术-Pod(1)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 01:07, 02:02, 02:51, 03:05, 03:17, 04:36, 05:10, 05:56, 06:15, 06:29, 07:02, 07:47, 07:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:48:05

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Pod 的核心概念、定义、基本用法及实际操作演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程标题“容器化进阶Kubernetes核心技术”，并列出目录结构，当前章节为“1 Pod详解”。图示说明一个 Pod 包含 Pause 容器和用户容器。
画面 2: 展示“Pod vs 应用”、“Pod vs 容器”、“Pod vs 节点”等对比要点。图示展示两个节点上的 Pod 及其内部容器，标注了 Labels 和 Service。
画面 3: 展示“1.1 Pod的定义”标题，下方文字说明“下面为yaml定义文件的Pod的完整内容”。
画面 4: 展示 YAML 文件中 Pod 的 metadata 和 spec 部分，包含 containers、image、ports、volumes 等字段的定义。
画面 5: 展示 YAML 文件中 Pod 的 memory、livenessProbe、exec、httpGet、tcpSocket、initialDelaySeconds、periodSeconds、successThreshold、failureThreshold、securityContext、privileged、restartPolicy、nodeSelector、imagePullSecrets、hostNetwork、volumes、emptyDir 等字段的定义。
画面 6: 展示 YAML 文件中 Pod 的 volumes、ports、env、resources、limits 等字段的定义。
画面 7: 展示“1.2 Pod的基本用法”标题，说明 Pod 可以由一个或多个容器组成，并给出“由一个容器组成的Pod示例”和“由两个容器组成的Pod示例”的 YAML 代码。
画面 8: 展示终端命令行，用户在目录中列出文件，查看并编辑名为“demo1.yaml”的文件。
画面 9: 展示终端命令行，用户执行“kubectl get pods”查看 Pod 状态，然后执行“kubectl replace -f demo1.yaml”更新 Pod，接着执行“kubectl delete -f demo1.yaml”删除 Pod。
画面 10: 展示终端命令行，用户执行“kubectl get pods”查看 Pod 状态，然后执行“kubectl get pods -o wide”查看详细信息，接着执行“kubectl describe pod/<Pod_name>”查看 Pod 详细描述。
画面 11: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（tomcat 和 redis）及其端口配置。
画面 12: 展示终端命令行，用户执行“kubectl create -f xxx.yaml”创建 Pod。
画面 13: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（tomcat 和 redis）及其端口配置。
画面 14: 展示“由两个容器组成的Pod示例”的 YAML 代码，包含两个容器（tomcat 和 redis）及其端口配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```yaml
metadata:
  # 元数据
  name: string
  namespace: string
  # 元数据，pod的命名空间
  labels:
    - name: string
    # 元数据，标签列表
    - name: string
    # 元数据，自定义注释
  annotations:
    - name: string
    # 元数据，自定义注释
spec:
  containers:
    - name: string
    # pod中的容器列表，可以有多个容器
    - name: string
    # 容器的名称
    image: string
    # 容器的镜像
    imagePullPolicy: [Always|Never|IfNotPresent]//获取镜像的策略，默认为Always，每次都会尝试重新下载
    command: [string]
    # 容器的启动命令列表（不配置的话使用镜像内的命令）
    args: [string]
    # 启动参数列表
    workingDir: string
    # 容器的工作目录
    volumes: []
    # 指定容器内部的存储卷设置
    ports:
      - name: string
      # 容器需要暴露的端口名列表
      - name: string
      # 容器需要暴露的端口名
      containerPort: int
      # 容器需要暴露的端口
      hostPort: int
      # 容器在主机监听的端口（容器暴露端口映射到宿主机的端口。设置hostPort时同一台宿主机将不能启动其它容器的端口）
      protocol: string
      # TCP和UDP，默认为TCP
      env:
        - name: string
        # 环境变量的名称
        value: string
        # 环境变量的值
```

画面 5:
```yaml
memory: string
# pod内存资源的设置
livenessProbe:
  exec:
    # exec方式需要执行的命令/脚本
    command: [string]
    # exec方式需要执行的命令/脚本
  httpGet:
    # 通过httpGet检查健康
    port: string
    # 端口
    host: string
    # 主机
    scheme: string
    # 协议
    httpHeaders:
      - name: string
      # http头名称
      value: string
      # http头值
  tcpSocket:
    # 通过tcpSocket检查健康
    port: string
    # 端口
  initialDelaySeconds: 0
  # 首次检查时间
  periodSeconds: 0
  # 检查间隔时间
  successThreshold: 0
  # 成功阈值
  failureThreshold: 0
  # 失败阈值
  securityContext:
    # 安全配置
    privileged: false
    # 是否允许特权模式
  restartPolicy: Always|Never|OnFailure
  # 重启策略，默认为Always
  nodeSelector: object
  # 节点选择器，表示将该Pod调度到指定的节点上，key:value格式描述
  imagePullSecrets:
    - name: string
    # 镜像拉取密钥
  hostNetwork: false
  # 是否使用主机网络模式，共用Docker网络，默认否
  volumes:
    - name: string
    # 在Pod上定义的共享存储卷
    emptyDir: {}
    # 是一种与生命周期相关的存储卷，是一个临时目录，内容为空
```

画面 6:
```yaml
volumes:
  - name: string
  # 存储卷的名称
  emptyDir: {}
  # 是一种与生命周期相关的存储卷，是一个临时目录，内容为空
ports:
  - name: string
  # 容器需要暴露的端口名
  containerPort: int
  # 容器需要暴露的端口
  hostPort: int
  # 容器在主机监听的端口（容器暴露端口映射到宿主机的端口。设置hostPort时同一台宿主机将不能启动其它容器的端口）
  protocol: string
  # TCP和UDP，默认为TCP
env:
  - name: string
  # 环境变量的名称
  value: string
  # 环境变量的值
resources:
  limits:
    cpu: string
    # 资源限制，容器的最大可用资源数量
    memory: string
    # 资源限制，容器的最大可用资源数量
  requests:
    cpu: string
    # 资源请求，容器启动时可使用的资源数量
    memory: string
    # 资源请求，容器启动时可使用的资源数量
livenessProbe:
  exec:
    # exec方式需要执行的命令/脚本
    command: [string]
    # exec方式需要执行的命令/脚本
```

画面 7:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: tomcat
      ports:
        - containerPort: 8000
```

画面 8:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: tomcat
      ports:
        - containerPort: 8000
```

画面 9:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: tomcat
      ports:
        - containerPort: 8000
```

画面 10:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mytomcat
  labels:
    name: mytomcat
spec:
  containers:
    - name: mytomcat
      image: tomcat
      ports:
        - containerPort: 8000
```

画面
