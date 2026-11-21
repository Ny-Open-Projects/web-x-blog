# 画面线理解：07.Kubernetes集群搭建Master安装-etcd服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\07.Kubernetes集群搭建Master安装-etcd服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:23, 00:47, 01:03, 01:25, 01:33, 02:07, 02:34, 02:54, 03:23, 03:31, 03:41, 03:53, 04:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:39:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 系统上下载、解压并配置 etcd 服务，为后续安装 Kubernetes 集群做准备。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开浏览器，准备访问 GitHub。
画面 2: 在 GitHub 上浏览 etcd 项目，选择下载 etcd-v3.3.9-linux-amd64.tar.gz 文件。
画面 3: 使用 SecureCRT 连接到远程服务器，准备进行文件传输。
画面 4: 在 SecureCRT 中打开文件传输对话框，准备上传文件。
画面 5: 在 SecureCRT 中执行命令，解压下载的 etcd 文件。
画面 6: 在 SecureCRT 中执行命令，进入解压后的 etcd 目录。
画面 7: 在 SecureCRT 中执行命令，将 etcd 可执行文件复制到 /usr/bin 目录。
画面 8: 在 PPT 中查看 etcd 服务的配置说明，包括服务文件路径和启动命令。
画面 9: 展示多个窗口，包括 PPT、SecureCRT、GitHub 和 VMware Workstation，说明接下来要安装的组件。
画面 10: 在 PPT 中查看 kube-apiserver 服务的配置说明，包括服务文件路径和启动命令。
画面 11: 展示多个窗口，包括 PPT、SecureCRT、GitHub 和 VMware Workstation，说明接下来要安装的组件。
画面 12: 在 SecureCRT 中执行命令，创建并编辑 etcd 服务文件。
画面 13: 在 SecureCRT 中执行命令，启动 etcd 服务并查看服务状态。
画面 14: 在 PPT 中查看 etcd 服务的配置说明，确认服务已配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 7:
```bash
[root@localhost etcd]# cd etcd-v3.3.9-linux-amd64
[root@localhost etcd-v3.3.9-linux-amd64]# cp etcd /usr/bin/
```

画面 8:
```ini
[Unit]
Description=etcd Server
After=network.target
[Service]
Type=simple
EnvironmentFile=/etc/etcd/etcd.conf
WorkingDirectory=/var/lib/etcd
ExecStart=/usr/bin/etcd
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

画面 10:
```ini
[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes
After=network.target
[Service]
Type=simple
EnvironmentFile=/etc/kubernetes/apiserver
ExecStart=/usr/bin/kube-apiserver $KUBE_APISERVER_OPTS
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

画面 12:
```ini
[Unit]
Description=etcd Server
After=network.target
[Service]
Type=simple
EnvironmentFile=/etc/etcd/etcd.conf
WorkingDirectory=/var/lib/etcd
ExecStart=/usr/bin/etcd
Restart=on-failure
[Install]
WantedBy=multi-user.target
```

画面 13:
```bash
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl daemon-reload
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl enable etcd.service
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl start etcd.service
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl status etcd.service
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 8:
标题：2.2.2 etcd服务
内容：
- 下载 etcd 二进制文件
  - https://github.com/etcd-io/etcd/releases
  - etcd-v3.3.9-linux-amd64.tar.gz
- 上传到 master
  - 可以使用 rpm 安装，如果使用 yum 安装，可以通过 yum install rpm
- 将 etcd 和 etcdctl 文件复制到 /usr/bin 目录
- 配置 systemd 服务文件 /usr/lib/systemd/system/etcd.service
  ```ini
  [Unit]
  Description=etcd Server
  After=network.target
  [Service]
  Type=simple
  EnvironmentFile=/etc/etcd/etcd.conf
  WorkingDirectory=/var/lib/etcd
  ExecStart=/usr/bin/etcd
  Restart=on-failure
  [Install]
  WantedBy=multi-user.target
  ```
- 启动与测试 etcd 服务
  ```bash
  systemctl daemon-reload
  systemctl enable etcd.service
  mkdir -p /var/lib/etcd
  systemctl start etcd.service
  etcdctl cluster-health
  ```

画面 10:
标题：2.2.3 kube-apiserver 服务
内容：
- 解压后将 kube-apiserver、kube-controller-manager、kube-scheduler 以及管理使用的 kube-cfg 二进制命令文件放到 /usr/bin 目录，即完成这几个服务的安装。
- 下面是 kube-apiserver 服务进行配置
  ```ini
  [Unit]
  Description=Kubernetes API Server
  Documentation=https://github.com/kubernetes/kubernetes
  After=network.target
  [Service]
  Type=simple
  EnvironmentFile=/etc/kubernetes/apiserver
  ExecStart=/usr/bin/kube-apiserver $KUBE_APISERVER_OPTS
  Restart=on-failure
  [Install]
  WantedBy=multi-user.target
  ```

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
