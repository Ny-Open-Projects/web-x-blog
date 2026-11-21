# 画面线理解：03.Kubernetes环境搭建常见问题解决

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\03.Kubernetes环境搭建常见问题解决_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:41, 01:28, 02:27, 02:39, 02:49, 03:04, 03:44, 04:22, 04:47, 05:04, 05:18, 05:35, 05:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:36:31

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kubernetes 集群中部署并调试一个名为 mytomcat 的 ReplicaSet 应用，包括解决镜像拉取失败、kubelet 配置错误、服务访问问题等常见部署故障。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程 PPT 的目录结构，当前章节为“2.2 Master安装”，子章节包括“Docker安装”、“kube-apiserver服务”、“kube-controller-manager服务”、“kube-scheduler服务”、“Node安装”、“kubeadm安装”、“kube-proxy服务”、“自启”、“Node安装”。
- PPT 内容显示了“问题解决”部分，标题为“docker pull失败”，解决方案包括：
  1. yum install -y
  2. docker pull registry.access.rechat.com/.../pod-infrastructure:latest
- 画面底部有“黑马程序员”的水印和宣传语。

画面 2：
- 在 SecureCRT 中执行了命令：`kubectl get pods`。
- 输出结果显示了三个 Pod：`mytomcat-fzg2`、`mytomcat-pb6d2`、`mytomcat-pb6d2`，状态均为 `ContainerCreating`，表明应用正在启动但尚未就绪。

画面 3：
- PPT 内容显示了“解决方法”部分，标题为“docker pull失败”，解决方案包括：
  1. docker pull kubernetes/pause
  2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_POD_INFRA_CONTAINER 变量：
     KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.143:5000/pod-infrastructure:latest"
  6. 重启服务：systemctl restart kube-apiserver systemctl restart kube-controller-manager systemctl restart kube-scheduler systemctl restart kubelet

画面 4：
- 在 SecureCRT 中执行了命令：`systemctl restart kubelet`。
- 执行 `kubectl get pods` 后，输出显示 `mytomcat-fzg2` 和 `mytomcat-pb6d2` 的状态变为 `Running`，表明应用已成功启动。
- 画面底部显示了 `/etc/kubernetes/kubelet` 文件的配置内容，其中包含：
  KUBELET_API_SERVER="--api-servers=http://127.0.0.1:8080"
  KUBELET_POD_INFRA_CONTAINER="--pod-infra-container-image=192.168.126.144:5000/pod-infrastructure:latest"
  KUBELET_ARGS="--pod-infra-container-image=192.168.126.144:5000/pod-infrastructure:latest"

画面 5：
- PPT 内容显示了“解决方法”部分，标题为“docker pull失败”，解决方案包括：
  1. docker pull kubernetes/pause
  2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet

画面 6：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 7：
- 在 SecureCRT 中执行了命令：`net.ipv4.ip_forward=1`。
- 画面底部显示了 `/etc/sysctl.conf` 文件的内容，其中包含：
  net.ipv4.ip_forward=1

画面 8：
- 浏览器访问了 `http://192.168.126.144:8080`，显示 Apache Tomcat 8.5.33 的欢迎页面，表明应用已成功通过外部访问。

画面 9：
- 在 SecureCRT 中执行了命令：
  1. cat /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. kubectl get svc
  4. kubectl delete svc mytomcat-svc
  5. kubectl delete svc --all
- 输出显示了服务列表和删除操作的结果。

画面 10：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 11：
- PPT 内容显示了“systemctl start kube-proxy”和“Tomcat配置”部分。
- 显示了名为 `mytomcat-svc.yaml` 的 YAML 配置文件内容：
  apiVersion: v1
  kind: ReplicationController
  metadata:
    name: mytomcat
  spec:
    replicas: 2
    selector:
      app: mytomcat
    template:
      metadata:
        labels:
          app: mytomcat
      spec:
        containers:
          - name: mytomcat

画面 12：
- PPT 内容显示了“解决方法”部分，标题为“docker pull失败”，解决方案包括：
  1. docker pull kubernetes/pause
  2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet

画面 13：
- PPT 内容显示了“外网不能访问”的问题及解决方案：
  1. vim /etc/sysctl.conf
  2. net.ipv4.ip_forward=1
  3. 解决 kubectl get pods 无资源问题：vim /etc/kubernetes/apiserver，找到 KUBE_ADMISSION_CONTROL="..."，并添加 admission_control_namespaces=... 等参数。
  4. 重启服务：systemctl restart kube-apiserver

画面 14：
- PPT 内容显示了“解决方法”部分，标题为“docker pull失败”，解决方案包括：
  1. docker pull kubernetes/pause
  2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
  3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
  4. vi /etc/kubernetes/kubelet
  5. 修改 KUBELET_ARGS 变量：
     KUBELET_ARGS="--pod-infra-container-image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
  6. 重启 kubelet 服务：systemctl restart kubelet
