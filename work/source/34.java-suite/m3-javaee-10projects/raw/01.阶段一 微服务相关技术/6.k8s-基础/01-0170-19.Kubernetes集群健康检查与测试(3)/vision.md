# 画面线理解：19.Kubernetes集群健康检查与测试(3)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\19.Kubernetes集群健康检查与测试(3)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:12, 02:18, 03:20, 04:02, 05:07, 05:59, 06:20, 06:52, 07:34, 09:29, 09:54, 10:44, 11:18, 11:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:47:15

1) 这一组画面整体在讲什么（一句话）：
演示 Kubernetes 集群的搭建、核心组件功能及常用命令操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: SSH 登录到 Kubernetes 主机，终端提示符为 [root@bogon k8s]#。
画面 2: PPT 页面，标题为“1.1 Master”，展示 Kubernetes Master 节点架构图，包含 api server、scheduler、replication controller、kubelet、kube-proxy 等组件，并列出各组件功能说明。
画面 3: 与画面 2 内容相同，PPT 页面展示 Kubernetes Master 节点架构图及组件功能。
画面 4: PPT 页面，标题为“1.1 Master”，内容与画面 2 相同，但下方新增“1.2 Node”部分，列出 Kubelet 和 Kube-proxy 的功能。
画面 5: PPT 页面，标题为“总结”，展示 Kubernetes 架构图，包含 api server、scheduler、replication controller、kubelet、kube-proxy、etcd、node、Internet 等组件，并列出各组件功能说明。
画面 6: PPT 页面，标题为“1.2 Node”，内容与画面 4 相同，展示 Kubelet 和 Kube-proxy 的功能。
画面 7: PPT 页面，标题为“3.常用命令”，列出获取容器、创建容器、删除容器、查看 Pod 状态、查看容器日志、进入容器终端等常用 kubectl 命令。
画面 8: PPT 页面，标题为“3.常用命令”，内容与画面 7 相同，展示常用 kubectl 命令。
画面 9: VS Code 编辑器界面，打开文件“nginx-rc.yaml”，内容为 ReplicationController 的 YAML 配置，定义了名称、副本数、标签选择器、容器镜像和端口。
画面 10: SecureCRT 终端界面，显示执行了 kubectl delete -f nginx-svc.yaml 命令，删除了服务，随后执行 kubectl create -f nginx-svc.yaml 创建服务，最后执行 kubectl get pods 查看 Pod 状态。
画面 11: SecureCRT 终端界面，显示执行了 kubectl delete -f nginx-rc.yaml 命令，删除了 ReplicationController，随后执行 kubectl create -f nginx-rc.yaml 创建 ReplicationController，最后执行 kubectl get pods 查看 Pod 状态。
画面 12: VS Code 编辑器界面，打开文件“nginx-svc.yaml”，内容为 Service 的 YAML 配置，定义了名称、类型、端口、选择器等。
画面 13: SecureCRT 终端界面，显示执行了 kubectl get pods 命令，查看 Pod 状态，显示多个 nginx Pod 正在运行。
画面 14: VS Code 编辑器界面，打开文件“nginx-rc.yaml”，内容与画面 9 相同，展示 ReplicationController 的 YAML 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9:
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80

画面 12:
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: nginx

画面 6:
o 解决方案1
1. yum install rhsm -y
2. docker pull registry.access.redhat.com/rhel7/pod-infrastructure:latest
如果以上两步解决了问题，那么就不需要在执行下面操作
3. docker search pod-infrastructure
4. docker pull docker.io/tianyeb/pod-infrastructure
5. docker tag tianyeb/pod-infrastructure 192.168.126.143:5000/pod-infrastructure
6. docker push 192.168.126.143:5000/pod-infrastructure
7. vi /etc/kubernetes/kubelet
修改 KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.143:5000/pod-infra-container-image:latest"
8. 重启服务
systemctl restart kube-apiserver
systemctl restart kube-controller-manager
systemctl restart kube-scheduler
systemctl restart kubelet
systemctl restart kube-proxy

o 解决方案2
1. docker pull docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
4. vi /etc/kubernetes/kubelet

画面 7:
- 获取当前命名空间下的容器
kubectl get pod
- 获取所有容器列表
kubectl get all
- 创建容器
kubectl create -f kubernetes-pvc.yaml
- 删除容器
kubectl delete pods/test-pd 或者 kubectl delete -f rc-nginx.yaml
- 查看指定pod跑在哪个node上
kubectl get pod /test-pd -o wide
- 查看容器日志
Kubectl logs nginx-8586cf59-mwwtc
- 进入容器终端命令
kubectl exec -it nginx-8586cf59-mwwtc /bin/bash
- 一个Pod里含有多个容器，用 -container or -c 参数。
例如:假如这里有个Pod名为my-pod,这个Pod有两个容器,分别为main-app 和 helper-app,下面的命令将打开main-app的shell的登录界面。
kubectl exec -it my-pod -c container main-app -/bin/bash
- 容器详情列表
kubectl describe pod/mysql-m8rb1
- 查看容器状态
kubectl get svc

画面 10:
kubectl delete -f nginx-svc.yaml
kubectl create -f nginx-svc.yaml
kubectl get pods

画面 11:
kubectl delete -f nginx-rc.yaml
kubectl create -f nginx-rc.yaml
kubectl get pods

画面 13:
kubectl get pods

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“1.1 Master”，架构图中，api server 指向 etcd、scheduler、replication controller、kubelet、kube-proxy；scheduler 指向 node；replication controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 4: PPT 标题为“1.1 Master”，架构图中，api server 指向 etcd、scheduler、replication controller、kubelet、kube-proxy；scheduler 指向 node；replication controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 5: PPT 标题为“总结”，架构图中，api server 指向 etcd、scheduler、replication controller、kubelet、kube-proxy；scheduler 指向 node；replication controller 指向 node；kubelet 指向 node；kube-proxy 指向 node；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 6: PPT 标题为“1.2 Node”，架构图中，kubelet 指向 node；kube-proxy 指向 node；api server 指向 kubelet、kube-proxy；etcd 指向 api server；fire wall 指向 api server；Internet 指向 api server。
画面 7: PPT 标题为“3.常用命令”，无架构图。
画面 12: PPT 标题为“nginx-svc.yaml”，无架构图。
画面 14: PPT 标题为“nginx-rc.yaml”，无架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
