# 画面线理解：08.Kubernetes集群搭建Master安装-kube-apiserver服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\08.Kubernetes集群搭建Master安装-kube-apiserver服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:25, 00:51, 01:08, 01:15, 01:36, 01:43, 01:53, 02:00, 02:34, 02:43, 03:17, 03:52, 05:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:40:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统中安装并配置 Kubernetes 的 etcd、kube-apiserver 和 kube-controller-manager 服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示了通过 SecureCRT 连接服务器后，执行 systemctl daemon-reload 命令，随后查看 etcd 服务状态，确认其已运行。
画面 2: 在文件资源管理器中，用户正在选择一个名为 “duheng” 的文件夹，准备进行后续操作。
画面 3: 在 SecureCRT 会话中，用户执行了 systemctl start etcd.service 命令，启动 etcd 服务。
画面 4: 用户在终端中执行了 tar -zxvf 命令，解压 Kubernetes 服务器的安装包。
画面 5: 继续解压操作，显示了解压后的文件列表，包括 kube-apiserver、kube-controller-manager 等组件。
画面 6: 展示了 PPT 页面，标题为 “2.2.4 kube-controller-manager 服务”，并显示了 kube-controller-manager 服务的配置文件路径。
画面 7: 继续解压操作，显示了解压后的文件列表，包括 kube-apiserver、kube-controller-manager 等组件。
画面 8: 用户在终端中执行了 cd 命令，进入 /usr/local/bin 目录，准备安装服务。
画面 9: 展示了 GitHub 上 Kubernetes 的 etcd 3.3.9 版本的发布页面，用户正在查看相关文件。
画面 10: 用户在终端中执行了 cp 命令，将解压后的组件复制到 /usr/bin 目录。
画面 11: 用户在终端中执行了 cp 命令，将解压后的组件复制到 /usr/bin 目录。
画面 12: 展示了 PPT 页面，标题为 “2.2.4 kube-controller-manager 服务”，并显示了 kube-controller-manager 服务的配置文件路径。
画面 13: 展示了 PPT 页面，标题为 “2.2.4 kube-controller-manager 服务”，并显示了 kube-controller-manager 服务的配置文件路径。
画面 14: 用户在终端中执行了 vi 命令，编辑 /etc/kubernetes/kube-controller-manager.service 文件。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
systemctl daemon-reload
systemctl enable etcd.service
systemctl start etcd.service
etcdctl cluster-health

画面 3:
systemctl start etcd.service
etcdctl cluster-health

画面 4:
tar -zxvf kubernetes-server-linux-amd64.tar.gz
cd kubernetes/server/bin
ls

画面 5:
ls

画面 6:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --service-cluster-ip-range=10.0.0.1/24 --service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 7:
ls

画面 8:
cd /usr/local/bin
ls

画面 9:
https://github.com/kubernetes/kubernetes/releases

画面 10:
cp kube-apiserver kube-controller-manager kube-scheduler kubelet /usr/bin/

画面 11:
cp kube-apiserver kube-controller-manager kube-scheduler kubelet /usr/bin/

画面 12:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --service-cluster-ip-range=10.0.0.1/24 --service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 13:
vi /etc/kubernetes/apiserver
KUBE_API_ARGS="-storage-backend=etcd3 -etcd-servers=http://127.0.0.1:2379 --insecure-bind-address=0.0.0.0 --insecure-port=8080 --service-cluster-ip-range=10.0.0.1/24 --service-node-port-range=30000-32767 --admission-control=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,ResourceQuota --log-dir=/var/log/kubernetes --v=2"

画面 14:
vi /etc/kubernetes/kube-controller-manager.service
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://127.0.0.1:8080 --log-dir=/var/log/kubernetes --v=2"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6:
标题: 2.2.4 kube-controller-manager 服务
内容: kube-controller-manager 服务依赖于 kube-apiserver 服务。
画面 12:
标题: 2.2.4 kube-controller-manager 服务
内容: kube-controller-manager 服务依赖于 kube-apiserver 服务。
画面 13:
标题: 2.2.4 kube-controller-manager 服务
内容: kube-controller-manager 服务依赖于 kube-apiserver 服务。
画面 14:
标题: 2.2.4 kube-controller-manager 服务
内容: kube-controller-manager 服务依赖于 kube-apiserver 服务。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
