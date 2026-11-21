# 画面线理解：25.kubernetes核心技术-HorizontalPod Autoscaler

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\25.kubernetes核心技术-HorizontalPod Autoscaler_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:35, 01:40, 01:45, 01:59, 02:06, 02:17, 02:28, 02:51, 02:59, 03:06, 03:10, 03:22, 03:25, 03:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:51:57

1) 这一组画面整体在讲 Kubernetes 中的 Deployment、Service 和 Horizontal Pod Autoscaler（HPA）的配置与原理，特别是如何通过 HPA 实现自动扩缩容。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解 HPA 的手动扩缩容命令 `kubectl scale deployment frontend --replicas 1`，并展示 Deployment 的 YAML 配置（含 metadata、spec.template.metadata.labels、spec.containers.image、spec.resources.requests.cpu、spec.ports.containerPort）。
画面 2: 展示 Deployment YAML 配置中 containers 部分的完整内容，包括 image、resources.requests.cpu、ports.containerPort。
画面 3: 展示 Service 的 YAML 配置，包含 apiVersion: v1、kind: Service、metadata.name: nginx-svc、spec.ports.port: 80、spec.selector.app: nginx。
画面 4: 展示 HPA 的 YAML 配置，包含 apiVersion: autoscaling/v1、kind: HorizontalPodAutoscaler、metadata.name: nginx-hpa、spec.scaleTargetRef.kind: Deployment、spec.scaleTargetRef.name: nginx-deployment、spec.minReplicas: 1、spec.maxReplicas: 10、spec.targetCPUUtilizationPercentage: 50。
画面 5: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 6: 展示 Service 的 YAML 配置，包含 apiVersion: v1、kind: Service、metadata.name: nginx-svc、spec.ports.port: 80、spec.selector.app: nginx。
画面 7: 展示 HPA YAML 配置中 minReplicas 和 maxReplicas 的值。
画面 8: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 9: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 10: 展示 Deployment YAML 配置中 spec.template.metadata.labels 的内容。
画面 11: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 12: 展示 Deployment YAML 配置中 spec.replicas: 1。
画面 13: 展示 HPA YAML 配置中 kind: HorizontalPodAutoscaler、metadata.name: nginx-hpa。
画面 14: 展示 HPA YAML 配置中 minReplicas: 1、maxReplicas: 10、targetCPUUtilizationPercentage: 50。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面 1:
```
kubectl scale deployment frontend --replicas 1
```
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        resources:
          requests:
            cpu: 50m
          ports:
          - containerPort: 80
```
画面 2:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        resources:
          requests:
            cpu: 50m
          ports:
          - containerPort: 80
```
画面 3:
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: nginx
```
画面 4:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 5:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 6:
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: nginx
```
画面 7:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 8:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        resources:
          requests:
            cpu: 50m
          ports:
          - containerPort: 80
```
画面 9:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 10:
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: nginx
```
画面 11:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 12:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        resources:
          requests:
            cpu: 50m
          ports:
          - containerPort: 80
```
画面 13:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 14:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PPT 标题为“6 Horizontal Pod Autoscaler”，内容为 HPA 的手动扩缩容和自动扩缩容原理。
画面 2: PPT 标题为“6 Horizontal Pod Autoscaler”，内容为 HPA 的自动扩缩容原理。
画面 3: PPT 标题为“7 Service 详解”，内容为 Service 的基本用法。
画面 4: PPT 标题为“7 Service 详解”，内容为 HPA 的配置。
画面 5: PPT 标题为“7 Service 详解”，内容为 HPA 的配置。
画面 6: PPT 标题为“7 Service 详解”，内容为 Service 的基本用法。
画面 7: PPT 标题为“7 Service 详解”，内容为 HPA 的配置。
画面 8: PPT 标题为“6 Horizontal Pod Autoscaler”，内容为 HPA 的手动扩缩容和自动扩缩容原理
