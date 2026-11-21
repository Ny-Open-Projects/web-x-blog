# 画面线理解：02.Kubernetes快速入门

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\02.Kubernetes快速入门_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:00, 01:34, 02:17, 02:50, 03:53, 04:43, 05:27, 06:50, 08:23, 09:51, 10:22, 10:40, 11:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:35:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在 CentOS 系统上安装和配置 Kubernetes 集群，包括关闭防火墙、安装 Docker、启动 Kubernetes 各组件、创建并部署一个 Tomcat 应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了课程大纲，当前章节为“1.1.2 Kubernetes 快速入门”。
- 右侧列出安装步骤：关闭 CentOS 防火墙、安装 etcd 和 Kubernetes 软件、启动服务（systemctl start etcd、systemctl start docker）。
- 提示：如果 Docker 未自动生效，需参考 /etc/sysconfig/docker，将 selinux 后面的值改为 disabled。

画面 2:
- 展示了 Kubernetes 部署的 YAML 文件内容，用于创建名为 mytomcat 的 Service。
- YAML 文件内容：
  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: mytomcat
  spec:
    type: NodePort
    ports:
      - port: 8080
        nodePort: 30000
    selector:
      app: mytomcat
  ```
- 命令行提示：`kubectl create -f mytomcat.svc.yaml`

画面 3:
- 展示了多个窗口，包括 Kubernetes 集群的架构图、多个节点的 SSH 连接、以及一个正在运行的 Tomcat 应用。
- 窗口标题包括：“K8s 集群”、“K8s 集群架构图”、“Apache Tomcat 8.5.33”等。
- 画面下方显示了启动服务的命令：`systemctl start kube-scheduler` 和 `systemctl start kubelet`。

画面 4:
- 展示了 SecureCRT 连接的 CentOS 系统终端。
- 终端显示了 Docker 的安装包列表和系统信息。
- 系统信息：
  ```
  sshd AES-256-CTR 24.1 24日 11月19日 VT100
  ```

画面 5:
- 展示了 SecureCRT 终端中执行的命令：`systemctl status etcd` 和 `systemctl start docker`。
- `systemctl status etcd` 输出显示 etcd 服务正在运行。
- `systemctl start docker` 命令执行后，终端显示 Docker 服务启动成功。

画面 6:
- 展示了 VMware Workstation 中的虚拟机界面。
- 虚拟机名称为 “k8s-quickstart-demo”。
- 界面显示了多个虚拟机的列表，包括 “node1”、“node2”、“k8s-master” 等。

画面 7:
- 展示了 SecureCRT 终端中执行的命令：`systemctl start kube-apiserver`、`systemctl start kube-controller-manager`、`systemctl start kube-scheduler`。
- 命令执行后，终端显示服务启动成功。

画面 8:
- 展示了 SecureCRT 终端中执行的命令：`systemctl start kube-proxy`。
- 命令执行后，终端显示 kube-proxy 服务启动成功。
- 命令行提示：`[root@localhost k8s]#`

画面 9:
- 展示了 Notepad++ 编辑器中的 YAML 文件内容。
- 文件内容与画面 2 中的 YAML 文件相同。
- 右侧显示了网络配置文件夹结构，包括 “network-scripts”、“ifcfg-ens33”、“ifcfg-lo” 等。

画面 10:
- 展示了 PPT 页面，标题为“1.2 Kubernetes 基本架构与常用术语”。
- 内容包括：
  - 外部访问的限制：只能在节点上访问，其他主机无法访问。
  - 解决方案：
    1. `vim /etc/sysctl.conf`
    2. `net.ipv4.ip_forward=1`
  - 解决 kubelet get pods 无资源问题：
    1. `vim /etc/kubernetes/apiserver`
    2. 找 `KUBE_ADMISSION_CONTROL`
    3. 去掉 ServiceAccount，保存退出，`systemctl restart kube-apiserver`

画面 11:
- 展示了 PPT 页面，标题为“1.2 Kubernetes 基本架构与常用术语”。
- 内容与画面 10 相同。

画面 12:
- 展示了 SecureCRT 终端中执行的命令：`docker pull docker.io/tanyej/pod-infrastructure`、`docker tag tanyej/pod-infrastructure 192.168.126.143:5000/pod-infrastructure`、`docker push 192.168.126.143:5000/pod-infrastructure`。
- 修改了 KUBELET 的配置文件。
- 重启服务命令：`systemctl restart kube-apiserver`、`systemctl restart kube-controller-manager`、`systemctl restart kube-scheduler`、`systemctl restart kube-proxy`。
- 命令行提示：`[root@localhost k8s]# kubectl get pods`

画面 13:
- 展示了课程大纲，当前章节为“1.1.2 Kubernetes 快速入门”。
- 右侧列出安装步骤：关闭 CentOS 防火墙、安装 etcd 和 Kubernetes 软件、启动服务（systemctl start etcd、systemctl start docker）。
- 提示：如果 Docker 未自动生效，需参考 /etc/sysconfig/docker，将 selinux 后面的值改为 disabled。

画面 14:
- 展示了 PPT 页面，标题为“为什么使用 Kubernetes”。
- 内容包括：
  - 使用 Kubernetes 的原因：可以快速上线开发的系统，支持微服务架构。
  - Kubernetes 的特点：一个服务的请求可以被多个节点处理，支持横向扩展。
- 展示了“1.1.2 Kubernetes 快速入门”章节的详细内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 2:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mytomcat
spec:
  type: NodePort
  ports:
    - port: 8080
      nodePort: 30000
  selector:
    app: mytomcat
```

画面 12:
```bash
docker pull docker.io/tanyej/pod-infrastructure
docker tag tanyej/pod-infrastructure 192.168.126.143:5000/pod-infrastructure
docker push 192.168.126.143:5000/pod-infrastructure
```

画面 12:
```bash
修改 KUBELET, POD, INFRA_CONTAINER="pod-infra-container-image:192.168.126.143:5000/pod-infrastructure:latest"
```

画面 12:
```bash
systemctl restart kube-apiserver systemctl restart kube-controller-manager systemctl restart kube-scheduler systemctl restart kube-proxy
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 10:
- 标题：“1.2 Kubernetes 基本架构与常用术语”
- 内容：
  - 外部访问的限制：只能在节点上访问，其他主机无法访问。
  - 解决方案：
    1. `vim /etc/sysctl.conf`
    2. `net.ipv4.ip_forward=1`
  - 解决 kubelet get pods 无资源问题：
    1. `vim /etc/kubernetes/apiserver`
    2. 找 `KUBE_ADMISSION_CONTROL`
    3. 去掉 ServiceAccount，保存退出，`systemctl restart kube-apiserver`

画面 14:
- 标题：“为什么使用 Kubernetes”
- 内容：
  - 使用 Kubernetes 的原因：可以快速上线开发的系统，支持微服务架构。
  - Kubernetes 的特点：一个服务的请求可以被多个节点处理，支持横向扩展。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
