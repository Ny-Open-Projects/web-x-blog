# 画面线理解：29.kubernetes核心技术-Service(2)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\29.kubernetes核心技术-Service(2)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:36, 00:59, 01:30, 01:49, 02:08, 02:31, 03:29, 03:52, 04:25, 04:31, 04:53, 05:04, 05:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:55:22

1) 这一组画面整体在讲什么（一句话）：
讲解 Kubernetes 中 Service 的两种类型：多端口 Service 和外部服务 Service，并通过 YAML 配置文件和命令行操作进行演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 2: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 3: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 4: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 5: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 6: 展示了 SecureCRT 中的网页内容，包含 Tomcat 官网的导航链接，如下载连接器、文档、参与项目等。
画面 7: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 8: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。
画面 9: 展示了 SecureCRT 中的命令行界面，执行了 kubectl get svc 命令，查看了 Service 列表，包括 my-service、mywebapp-svc 等。随后执行了 kubectl describe svc mywebapp-svc 命令，查看了 Service 的详细信息。
画面 10: 展示了 SecureCRT 中的命令行界面，执行了 curl 命令，访问了 10.254.113.110 的 8080 端口。
画面 11: 展示了 SecureCRT 中的命令行界面，执行了 curl 命令，访问了 10.254.113.110 的 8080 端口，返回了 Tomcat 的默认页面 HTML 代码。
画面 12: 展示了“9.2.1 多端口Service”章节，其中 YAML 配置文件定义了名为 mywebappservice 的 Service，包含两个端口映射：8080 映射到 8080（用于 web），8085 映射到 8085（用于 management）。
画面 13: 展示了“9.1 Service 的定义”章节，其中 YAML 配置文件定义了 Service 的通用结构，包括 apiVersion、kind、metadata、spec 等字段。
画面 14: 展示了“9.2.2 外部服务Service”章节，其中 YAML 配置文件定义了名为 my-service 的 Service，其端口为 80，协议为 TCP。下方还展示了通过 kubectl get svc 命令查看 Service 列表。

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
  name: my-service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

apiVersion: v1
kind: Endpoints
metadata:
  name: my-service
subsets:
- addresses:
  - IP: 10.254.74.3
  ports:
  - port: 8080

画面 8:
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80

apiVersion: v1
kind: Endpoints
metadata:
  name: my-service
subsets:
- addresses:
  - IP: 10.254.74.3
  ports:
  - port: 8080

画面 9:
[root@localhost test]# kubectl get svc
NAME         CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
kubernetes   10.254.0.1       <none>        443/TCP    7d
my-service    10.254.113.110   <none>        80/TCP     29m
mywebapp-svc  10.254.113.4     <none>        8080/TCP   42m
nginx        10.254.41.35     <none>        80:33333/TCP   13h
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
  <link href="https://tomcat.apache.org/favicon.ico" rel="icon" type="image/x-icon">
  <link href="https://tomcat.apache.org/docs/images/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="https://tomcat.apache.org/docs/stylesheets.css" rel="stylesheet" type="text/css">
