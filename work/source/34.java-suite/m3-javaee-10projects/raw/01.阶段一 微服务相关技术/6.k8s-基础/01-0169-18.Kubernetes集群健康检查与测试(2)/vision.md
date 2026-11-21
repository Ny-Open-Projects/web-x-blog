# 画面线理解：18.Kubernetes集群健康检查与测试(2)

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\18.Kubernetes集群健康检查与测试(2)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:31, 00:36, 01:04, 01:17, 01:40, 03:11, 03:39, 04:13, 05:24, 06:14, 06:32, 06:53, 07:19
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:46:26

1) 这一组画面整体在讲如何解决 Kubernetes 集群因镜像拉取失败导致的节点不可用问题，通过配置私有镜像仓库和修改 kubelet 配置来恢复服务。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个名为 nginx-service.yaml 的 YAML 文件，内容为：
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  ports:
    - port: 80
      nodePort: 8080
  selector:
    app: nginx

画面2：展示一个名为“k8s集群搭建常见问题”的文档，其中“解决方案2”部分列出：
1. docker pull kubernetes/pause
2. docker tag docker.io/kubernetes/pause:latest 192.168.126.143:5000/google_containers/pause-amd64:3.0
3. docker push 192.168.126.143:5000/google_containers/pause-amd64:3.0
4. vi /etc/kubernetes/kubelet配置为
KUBELLET_ARGS="-"
pod_infra_container_image=192.168.126.143:5000/google_containers/pause-amd64:3.0"
5. 重启kubelet服务 systemctl restart kubelet

画面3：展示一个 SecureCRT 会话窗口，终端中显示：
[root@bogon ~]#

画面4：展示文档“常用命令”部分，列出：
- 获取当前命名空间下的容器
  kubectl get pod
- 获取所有容器列表
  kubectl get all
- 创建容器
  kubectl create -f kubernetes-pvc.yaml
- 删除容器
  kubectl delete pods/test-pd 或者 kubectl delete -f nginx.yaml
- 查看指定pod跑在哪个node上

画面5：展示一个多窗口界面，包含 Typora 文档、SecureCRT 会话、WPS 文档和 VMware Workstation 窗口，其中 SecureCRT 会话显示命令行。

画面6：展示 SecureCRT 会话窗口，终端中显示：
registry-mirrors: ["https://docker.mirrors.ustc.edu.cn"]

画面7：展示 SecureCRT 会话窗口，终端中显示：
[root@bogon ~]#

画面8：展示多窗口界面，包含 Typora 文档、SecureCRT 会话、WPS 文档和 VMware Workstation 窗口，其中 SecureCRT 会话显示命令行。

画面9：展示 SecureCRT 会话窗口，终端中显示：
KUBELLET_ARGS="--kubelet-config=/etc/kubernetes/kubelet.conf --hostname-override=192.168.126.148 --logtostderr=false --log-oldest=false --v=2 --fail-swap-on=false"

画面10：展示 SecureCRT 会话窗口，终端中显示：
[root@bogon ~]#

画面11：展示 SecureCRT 会话窗口，显示容器信息，其中包含：
Containers:
  Container ID: docker://ac918b1e63e8e603f5d625d050b2d7508f3a2359123150285235ad03
  Image: nginx:latest
  Port: 80/tcp
  Status: Running
  Ready: True
Events:
  Type Reason Age From Message
  ---- ---- ---- --- -------
  Normal Created 1m kubelet Created container nginx
  Warning FailedScheduling 2m (x3 over 1h) kubelet Failed to schedule pod: No node available
  Warning MissingClusterDNS 2m (x3 over 1h) kubelet Failed to create pod sandbox: cannot create pod using "ClusterFirst" policy. Falling back to "Default" policy.

画面12：展示 Windows 资源管理器，路径为“本地磁盘 (C:) > docker 集群”，选中文件“docker集群.pdf”。

画面13：展示 SecureCRT 会话窗口，终端中显示：
[root@bogon ~]# docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
registry latest 2e2725273c88 4 days ago 11.3MB
nginx latest 00146d06f7844 11 days ago 100MB
...

画面14：展示 SecureCRT 会话窗口，终端中显示：
[root@bogon ~]# docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
registry latest 2e2725273c88 4 days ago 11.3MB
nginx latest 00146d06f7844 11 days ago 100MB
...
