# 29.kubernetes核心技术-Service(2)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\29.kubernetes核心技术-Service(2)_【海量资源尽在 ubkz.com】.mp4
- 时长 5分17秒（音频 318s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们说一下叫做多端口的Service有时我们一个容器应用也可能需要提供多个端口的服务那么在Service的定义中也可以相应的设置为将多个端口对应到多个应用服务
[00:15] 那下面大家看这个例子我们当前呢其实就是在这里边设置了多个端口我们一个8080端口映射到我们实际的8680那给它起个名字那我们这个8005呢映射到实际的8005我也给它起个名字那它真正对外的呢还是我这个myapp也就是我们最上面的这个Tomcat那这是允许我们说
[00:40] 将一个容器应用可以去提供多个端口的服务那这种情况呢大家知道一下无非就是在我的这个pose下面我去定义多个port然后呢你可以去通过映射不同的这个target port去指定那这是说我的一个多端口的Service我不去给大家演示了那我们再来看下面一个叫做外部服务Service那这些这个外部服务Service是什么意思呢
[01:06] 他说在某些特殊环境中应用系统需要将一个外部数据库作为后台的服务进行连接或将另一个集群或者namespace中的服务作为一个服务的后端这时可以通过创建一个无labor selector的Service来实现这里边他说你可以创建一个无labor selector的Service那大家往上看
[01:30] 无论我们上面怎么玩我们在创建某一个Service的时候我们都会去写一个selector然后app指定那它的目的是为了什么呢最终关联我们真正的这个控制器里面的我们当前的这个pod也就是说我们这里边pod是谁我们可以通过这个selectorapp my web去找到它因为你是在这里边去
[01:55] 定义的对吧那现在呢我们这时候呢一个叫做web的Service他呢是说我创建了一个Service而这时这个Service他根本就没有去指定label那大家可以看我们在这里呢vi一下我们当前的demo8的svc当天我就创建了一个我们的
[02:19] 他呢是没有指定label的也就是说你不知道他真正要访问的具体是哪一个后台的pool的对吧那我们可以怎么办呢我们可以去创建一个叫做andpoint你可以创建一个他通过指定一个相同名字这个名字一定要跟我们当前的这里边的我们Service的名字一致来去用
[02:41] 重新映射我们自己的endpoint也就是说去重新映射一下它的IP地址那大家看一下这个IP地址是什么呢我们可以来简单看一下Kubernetes CTL Guide SVC那我们找一下当前我们有一个叫做MyWebApp SVC对吧那我在这里边Kubernetes CTL DSCIBE我们SVC是它你看一下
[03:11] 在我们当前的这个myappsvc里边它真正的endpoint注意这是我们原来的是不是1025474.3那我在这里边定义了一个endpoint我也把它定义成1025474.3是不是就相当于说我这个Service虽然你最开始没有label但是我通过一个endpoint指定我们要真正访问的我们那个poll的IP值那这个时候我们就可以干什么
[03:40] 把它关联到我们一个具体的POD那我们可以看一下我们自己的demo8-我们的一个叫endpoint这个文件这个文件里边我们名字这个名字一定要跟我们当年创建Service时这个名字一致然后呢我们在自己的endpoint里边去指定了一个IP地址我指定完IP地址以后
[04:09] 注意我们Kuberctl get svc注意看我们自己的这叫MyService的svc那么我访问他DUR
[04:21] 我们对外端口是80那我是不是可以不写默认访问的就是80你会发现它其实也帮助我们访问了我们Tomcat的首页那么是不是也就相当于说虽然我当前的这个Service没有通过我们的label selector去具体访问哪一个poll的但是呢我做了一个underpoint它的名字和我的Service名字一致然后呢我指定了一个ip地址
[04:49] IP地址那这个IP地址呢其实就是我们最开始的时候我们定义的这个POD的IP地址那么我们在访问时你访问这个Service是不是也是帮助我们分发到我们当前的这个POD上了这个POD上OK所以呢这是我们最后一个关于说外部服务的一个Service大家可以回去尝试看一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Service 的两种类型：多端口 Service 和外部服务 Service，并通过 YAML 配置文件和命令行操作进行演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 2: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-Service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 3: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 4: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 5: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-Service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 6: 展示了 SecureCRT 中的网页内容，包含 Tomcat 官网的导航链接，如下载连接器、文档、参与项目等。
画面 7: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-Service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 8: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-Service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 9: 展示了 SecureCRT 中的命令行界面，执行了 kubectl get svc 命令，查看了 Service 列表，包括 my-Service、mywebapp-svc 等。随后执行了 kubectl describe svc mywebapp-svc 命令，查看了 Service 的详细信息。
画面 10: 展示了 SecureCRT 中的命令行界面，执行了 curl 命令，访问了 10.254.113.110 的 8080 端口。
画面 11: 展示了 SecureCRT 中的命令行界面，执行了 curl 命令，访问了 10.254.113.110 的 8080 端口，返回了 Tomcat 的默认页面 HTML 代码。
画面 12: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 13: 展示了“9.1 Service 的定义”章节，其中 YAML 配置文件定义了 Service 的通用结构，包括 apiVersion、kind、metadata、spec 等字段。
画面 14: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-Service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
apiVersion: v1
kind: Service
metadata:
  name: mywebAppService
spec:
  ports:
  - port: 8080
    targetPort: 8080
    name: web
  - port: 8085
    targetPort: 8085
    name: management
  selector:
    app: mywebapp

画面 2:
apiVersion: v1
kind: Service
metadata:
  name: mywebAppService
spec:
  ports:
  - port: 8080
    targetPort: 8080
  selector:
    app: mywebapp

画面 3:
apiVersion: v1
kind: Service
metadata:
  name: mywebAppService
spec:
  ports:
  - port: 8080
    targetPort: 8080
    name: web
  - port: 8085
    targetPort: 8085
    name: management
  selector:
    app: mywebapp

画面 4:
apiVersion: v1
kind: Service
metadata:
  name: mywebAppService
spec:
  ports:
  - port: 8080
    targetPort: 8080
    name: web
  - port: 8085
    targetPort: 8085
    name: management
  selector:
    app: mywebapp

画面 5:
apiVersion: v1
kind: Service
metadata:
  name: mywebAppService
spec:
  ports:
  - port: 8080
    targetPort: 8080
  selector:
    app: mywebapp

画面 6:
（无 YAML/代码内容）

画面 7:
apiVersion: v1
kind: Service
metadata:
  name: my-Service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

apiVersion: v1
kind: Endpoints
metadata:
  name: my-Service
subsets:
- addresses:
  - IP: 10.254.74.3
  ports:
  - port: 8080

画面 8:
apiVersion: v1
kind: Service
metadata:
  name: my-Service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

apiVersion: v1
kind: Endpoints
metadata:
  name: my-Service
subsets:
- addresses:
  - IP: 10.254.74.3
  ports:
  - port: 8080

画面 9:
[root@localhost test]# kubectl get svc
NAME         CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes   10.254.0.1       <none>        443/TCP    7d
my-Service    10.254.113.110   <none>        80/TCP     29m
mywebapp-svc  10.254.113.4     <none>        8080/TCP   42m
Nginx        10.254.41.35     <none>        80:33333/TCP   13h
[root@localhost test]# kubectl describe svc mywebapp-svc
Name:         mywebapp-svc
Namespace:    default
Labels:       <none>
Selector:     app=mywebapp
Type:         ClusterIP
IP:           10.254.113.4
Port:         8080/TCP
TargetPort:   8080/TCP
Endpoints:    10.254.113.4:8080
Session Affinity: None
Events:       <none>

画面 10:
（无 YAML/代码内容）

画面 11:
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tomcat</title>
  <link href="https://Tomcat.apache.org/favicon.ico" rel="icon" type="image/x-icon">
  <link href="https://Tomcat.apache.org/docs/images/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="https://Tomcat.apache.org/docs/stylesheets.css" rel="stylesheet" type="text/css">

