# 画面线理解：28.kubernetes核心技术-Service(1)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\28.kubernetes核心技术-Service(1)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:37, 00:45, 01:28, 01:49, 02:10, 02:29, 03:06, 03:13, 03:24, 04:07, 05:03, 05:14, 05:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:54:25

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Service 的定义、类型和基本用法，通过配置文件和命令行操作演示如何为 Pod 提供稳定的访问入口。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Service 的定义章节，列出 YAML 格式的 Service 定义文件结构。
画面 2: 展示 Service 的属性表格，包括 version、kind、metadata、spec 等字段的类型和说明。
画面 3: 展示 spec.type、spec.clusterIP、spec.sessionAffinity 等字段的详细说明。
画面 4: 展示一个 ReplicationController 的 YAML 文件，用于创建 Pod，并引出通过 Service 访问 Pod 的必要性。
画面 5: 展示通过 kubectl get pods 命令获取 Pod 列表，以及通过 grep 过滤出特定 Pod 的 IP 和端口。
画面 6: 展示在终端中执行 kubectl get pods 命令，列出所有 Pod 的状态和信息。
画面 7: 展示 Service 的多端口定义示例，以及如何通过 Service 访问后端 Pod。
画面 8: 展示通过浏览器访问 Tomcat 应用，页面显示 Tomcat 的官方文档和下载链接。
画面 9: 展示 Tomcat 官方文档页面，包含下载、连接器、部署指南等链接。
画面 10: 展示 Service 的多端口定义示例，以及如何通过 Service 访问后端 Pod。
画面 11: 展示 Service 的多端口定义示例，以及如何通过 Service 访问后端 Pod。
画面 12: 展示 Tomcat 官方文档页面，包含下载、连接器、部署指南等链接。
画面 13: 展示 ReplicationController 的 YAML 文件，用于创建 Pod。
画面 14: 展示 Service 的多端口定义示例，以及如何通过 Service 访问后端 Pod。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: string
  namespace: string
  labels:
    - name: string
  annotations:
    - name: string
spec:
  selector: []
  type: string
  clusterIP: string
  sessionAffinity: string
  ports:
    - name: string
    protocol: string
```

画面 2:
```yaml
status: int
loadBalancer:
  ingress:
    - ip: string
    hostname: string
```

画面 3:
```yaml
spec.type: string
spec.clusterIP: string
spec.sessionAffinity: string
spec.ports[]: list
spec.ports[].name: string
spec.ports[].protocol: string
```

画面 4:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: mywebapp
spec:
  replicas: 2
  template:
    metadata:
      name: mywebapp
      labels:
        app: mywebapp
    spec:
      containers:
        - name: mywebapp
          image: tomcat
          ports:
            - containerPort: 8080
```

画面 5:
```bash
[root@localhost test]# kubectl get pods -l app=mywebapp -o yaml | grep podIP
```

画面 6:
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: mywebapp
spec:
  replicas: 2
  template:
    metadata:
      name: mywebapp
      labels:
        app: mywebapp
    spec:
      containers:
        - name: mywebapp
          image: tomcat
          ports:
            - containerPort: 8080
```

画面 7:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mywebappService
spec:
  ports:
    - port: 8081
      targetPort: 8080
  selector:
    app: mywebapp
```

画面 8:
```html
<div class="col100">
  <div class="container">
    <h4>Other Documentation</h4>
    <ul>
      <li><a href="https://tomcat.apache.org/connector-docs/">Tomcat Connectors</a></li>
      <li><a href="https://tomcat.apache.org/taglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-stag
