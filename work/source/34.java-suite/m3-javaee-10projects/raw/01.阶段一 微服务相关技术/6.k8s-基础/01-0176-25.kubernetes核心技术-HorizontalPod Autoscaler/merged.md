# 25.kubernetes核心技术-HorizontalPod Autoscaler

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\25.kubernetes核心技术-HorizontalPod Autoscaler_【海量资源尽在 ubkz.com】.mp4
- 时长 3分53秒（音频 234s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们介绍一下这Horangito PO的Auto Scaler那么它其实简称叫做HPA全称是PO的一个横向的扩容
[00:12] 那我们的HPA呢,与RC或Deployment是一样的,那也属于我们的这个Kubernetes的一种资源对象,那它呢是通过分析我们RC控制的所有的目标POD的一个负载变化情况,来确定是否呢需要针对性的调整我们目标POD的副本数,那这是HPA的一个实现原理。
[00:33] 那Kubernetes呢对Po的扩容与缩容提供了这种手动和自动两种方式那手动的方式呢前期我们其实已经介绍过了是通过Kubernetes Scaler然后呢Deployment的这种方式
[00:47] 这是一个手动的手动模式通过Coopers Gala命令对一个Deployment或者RC进行POD的副本数量的一个设置自动模式则需要用户根据某个性能指标或者自定义的业务指标并指定POD副本的数量的范围系统将自动在这个范围根据性能指标的变化进行调整下面是一个自动扩容的一个小的实际代码大家可以看一下
[01:15] 那这里边说HPA控制器呢是基于Master的Coopers Controller Manager服务启动参数这项去定义的它默认值为30秒那它周期性的检测我们Pod的CPU的使用率那在满足条件时对RC或者是Deployment的这个副本Pod的副本呢进行一个数量调整以符合用户定义的一个平均Pod的CPU使用率那大家可以看一下这里我们定义了一个
[01:43] Deployment我们定义说我们当前这个Deployment的名字叫做index deployment然后呢我们下面呢说期待的一个replicate是1这下面其实就是我们的poll的定义我们当前这里边poll的它其实是一个index那再往下呢这是Service没什么好说的然后再往下这就是定义我们的一个HPA它这里边其实关联了我们当前的这个
[02:13] 类型是deployment然后呢name就是我刚才定义的ngx deployment那在这里边我们最小的一个期待数字是数值是1然后最大的是10也就是说这个1和10就是刚才在这里边说的我们是不是定义了我们当前预定的一个我们poll的副本的数量的范围这不是指定我们poll的副本数量的范围吗我们现在呢定义的就是1
[02:43] 核实那我们这里面有一个CPU的一个初始的一个使用率会百分比是50那如果你当前超过了我们指定的这么一个使用率它就会在我们当前指定的范围内去调整我们当前的这个POD副本的数量那这是给大家写了一个关于我们当前的这个CPU的
[03:11] 一个调整也说根据我们CPU的使用率进行自动的扩容和缩容其实我们也可以是基于内存去调整那大家呢后续可以自己找找怎么去基于内存去调整那这里呢我们可以
[03:27] 看一下这个代码那主要呢是关于我这个HPA这部分这部分呢就是定义了我们范围是1到10那我们初始的时候这个目标或者说初始的我们这个CPU的一个使用是50当超过了我们这个值我们就可以可以在指定的范围内去调整我们POD的副本的一个数量

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Kubernetes 中的 Deployment、Service 和 Horizontal Pod Autoscaler（HPA）的配置与原理，特别是如何通过 HPA 实现自动扩缩容。

2) 按时间顺序列出每张画面的要点：
画面 1: 讲解 HPA 的手动扩缩容命令 `kubectl scale deployment frontend --replicas 1`，并展示 Deployment 的 YAML 配置（含 metadata、spec.template.metadata.labels、spec.containers.image、spec.resources.requests.cpu、spec.ports.containerPort）。
画面 2: 展示 Deployment YAML 配置中 containers 部分的完整内容，包括 image、resources.requests.cpu、ports.containerPort。
画面 3: 展示 Service 的 YAML 配置，包含 apiVersion: v1、kind: Service、metadata.name: Nginx-svc、spec.ports.port: 80、spec.selector.app: Nginx。
画面 4: 展示 HPA 的 YAML 配置，包含 apiVersion: autoscaling/v1、kind: HorizontalPodAutoscaler、metadata.name: Nginx-hpa、spec.scaleTargetRef.kind: Deployment、spec.scaleTargetRef.name: Nginx-deployment、spec.minReplicas: 1、spec.maxReplicas: 10、spec.targetCPUUtilizationPercentage: 50。
画面 5: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 6: 展示 Service 的 YAML 配置，包含 apiVersion: v1、kind: Service、metadata.name: Nginx-svc、spec.ports.port: 80、spec.selector.app: Nginx。
画面 7: 展示 HPA YAML 配置中 minReplicas 和 maxReplicas 的值。
画面 8: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 9: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 10: 展示 Deployment YAML 配置中 spec.template.metadata.labels 的内容。
画面 11: 展示 HPA YAML 配置中 scaleTargetRef.name 的内容，以及 minReplicas 和 maxReplicas 的值。
画面 12: 展示 Deployment YAML 配置中 spec.replicas: 1。
画面 13: 展示 HPA YAML 配置中 kind: HorizontalPodAutoscaler、metadata.name: Nginx-hpa。
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
  name: Nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: Nginx
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
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
  name: Nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: Nginx
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
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
  name: Nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: Nginx
```
画面 4:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 5:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 6:
```
apiVersion: v1
kind: Service
metadata:
  name: Nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: Nginx
```
画面 7:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 8:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: Nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: Nginx
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
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
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 10:
```
apiVersion: v1
kind: Service
metadata:
  name: Nginx-svc
spec:
  ports:
  - port: 80
  selector:
    app: Nginx
```
画面 11:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 12:
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: Nginx-deployment
spec:
  replicas: 1
  template:
    metadata:
      name: Nginx
      labels:
        app: Nginx
    spec:
      containers:
      - name: Nginx
        image: Nginx
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
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```
画面 14:
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: Nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1beta1
    kind: Deployment
    name: Nginx-deployment
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

