# 28.kubernetes核心技术-Service(1)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\28.kubernetes核心技术-Service(1)_【海量资源尽在 ubkz.com】.mp4
- 时长 5分39秒（音频 340s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们介绍最后一个Service大家看一下Service是我们Kubernetes最核心的一个概念那么我们是通过Service可以为我们一组具有相同功能的容器提供一个统一的入口地址并且将这个请求负载分发到我们后端的各个容器上
[00:21] 下面大家看到的这个呢是一个完整的yam格式的Service的定义文件这里边我们的版本我们的类型然后呢我们的原数据它的namespace这个libs那这里边
[00:34] 都有关于它的定义下面给大家列了一个表这个表里面呢说明了一下我们每一个字段呢代表的意义那这里边我们就不过得细看大家呢回去可以参考看一下那么我们说完这些以后啊我们要来看一下对于一个Service我们的基本的用法那前面我们说过Service我们用它主要目的是什么是不是它可以为我们这个相同的功能容器提供一个统计的入口对吧那怎样去
[01:02] 提供一个统一的入口我们通过它的一个基本用法呢让大家去感受一下首先呢来看
[01:09] 一般说对外提供服务的应用程序需要通过某种机制来实现对于容器应用最简单的方式是通过TCP IP的机制以及监听IP和端口号来实现创建一个最基本的Service大家看到的这个代码其实就是我创建一个最基本的Service我们这时候它是叫做
[01:32] 这不是Service,这是一个RC那我这时候创建了一个RC它里面有个POD其实是一个MyWebApp它的镜像是TOMcat我们可以看一下我当前的代码我这里边应该有一个叫做cat-demo7-rc.yaml文件这个文件就跟我讲义上的这个文件差不多
[01:59] 那我们创建了这么一个当前的自己的RC那我们真实的镜像其实是一个Tomcat那我这个文件呢其实已经创建出来了我们可以get pose大家可以看到我们这里面有一个叫做mywebapp的这么一个pode那我们也可以通过Kuberctl get rc我们去看到我们应该有个叫做mywebapp的rc那我创建完它以后呢大家往下
[02:27] 我们可以通过这样的一个命令来获取我们当前POD的IP地址也就是说我们在这里边把这个代码粘过来我们可以去获取我当前的这个POD的IP地址那我可以通过CURL加上我们当前的IP地址去访问我们当前的应用CURL
[03:00] 我看一下我们对外的端口是8080也说我们在这里边可以通过8080去访问我们可以得到我当前Tomcat的这些页面对吧但是呢这种访问呢是我直接访问POD它是不合适的那为什么呢说我们这个POD呢这么说因为当我们的POD的IP地址和端口通过这种IP地址和端口号来访问时啊我们这个是我看一下
[03:29] 通过它的端口号访问时呢我们这种访问是不可靠的因为当我们的Pod所在的Node发生故障时Pod将被我们Kubernetes重新调度到另一个Node那这时候你的Pod的地址就会发生改变那我们再访问它呢就访问不到了那我们应该怎么去访问呢
[03:47] 刚才我们强调了说我们可以通过Service为我们提供一个统一的入口那来访问他那当你的pose这个失效了分配到另外的一个node上我们的Service还是存在的我们还是可以去访问他那这个时候呢我们就可以去创建一个Service在这里呢大家可以看一下我们创建一个Service我们可以通过访问他的8081端口去映射到我们真正的8080端口去访问
[04:17] 那我们来看一下代码VI我们有一个Demo7-我的SVC的一个YAML文件这就是我们真正映射到我们自己的那个叫做MyWebApp这不是Select吗我们的标签那我们可以看一下现在呢我们可以通过Kubernetes CTLget SVC获取到我当天有一个叫MyWeb-SVC就是它
[04:46] 它的这个IP地址是10254163.4也就是说我们在这里面curl.他然后呢我们的端口是8081刚才我们说了我们通过8081端口也可以访问到我们刚才的poll的也就是说我们原来
[05:06] 可以去通过Pod的IP直接访问但是这个IP访问有个问题问题就在于说我的当前Pod如果失效了那我们的Kubernetes集群呢重新帮我把这个Pod调度到另外一个node上时那我这个IP就失效了但是呢我可以通过一个Service去帮助我们做一个统一的入口无论你后台的Pod是否失效只要你这个Service跟这个Pod对应上那么我们可以访问我的Service
[05:34] 以达到访问我们后台pose的效果

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
          image: Tomcat
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
          image: Tomcat
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
      <li><a href="https://Tomcat.apache.org/connector-docs/">Tomcat Connectors</a></li>
      <li><a href="https://Tomcat.apache.org/taglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-staglibs-user-stag

