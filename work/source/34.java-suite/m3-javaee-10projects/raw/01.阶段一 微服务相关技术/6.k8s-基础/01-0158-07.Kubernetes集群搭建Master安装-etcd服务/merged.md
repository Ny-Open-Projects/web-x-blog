# 07.Kubernetes集群搭建Master安装-etcd服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\07.Kubernetes集群搭建Master安装-etcd服务_【海量资源尽在 ubkz.com】.mp4
- 时长 4分4秒（音频 245s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们去安装一下ETCD这个服务那么ETCD它作为我们Kubernetes集群的一个主要服务在安装Kubernetes各个服务之前你要先把ETCD的服务安装并启动我们可以到这个网址去把它下载下来下载下来以后你肯定把它上传到你的Linux服务器我下载的是当前Linux AMD的TAR-GJ这个版本
[00:27] 那我这里面不下载了我的电脑已经下载完了那你如果已经下载完了你可以通过我们这个LRG S1去安装如果你的电脑没有呢你直接执行这种代码去可以安装我的电脑已经安装上了所以呢我在这里直接呢把它上传上来在这呢我在我的user local下去创建一个目录就叫做Kubernetes我进入这个Kubernetes目录下
[00:55] 大家注意一下我这个目录是user local下的那我现在呢通过RZ命令去把它上传一下我呢到我的桌面上我桌面上有个Kubernetes这里边我们有一个资料就是这个文件把它上传上来确定好了那上传上来以后呢我把它解压一下OK那现在呢我就进入这个etcd这个目录下面大家可以看这些文件
[01:31] 那文件是这个讲义上告诉你说呀你呢要把我们当前这个目录下的etcd和etcdctl就这个文件和这个文件copy到userbeam录下所以你要去copy谁呢我的etcd还有etcdctl这两个文件到哪呢到我的user的beam录下ok吧然后呢你还需要去编辑一个systemd的服务所以我们这里边需要vi一下
[02:01] 我们一个user下的bin下的叫做systemd然后我们下面有一个system看一下我是不是写错了viuserbin啊sorry好了bin去rib下的然后我们的systemd然后我们的system在这下面我们新创建一个文件就叫etcd.serviceok
[02:32] 在这个文件里边我们要copy一下这段话回来粘贴进去把它保存cpj好了那这样呢我们就可以去执行了但是大家注意一下这里边有个叫varribetcd这么一个叫做working directory我们是没有的所以下面告诉你了你要去手动的make一下make dir我们当前的
[03:02] VR下的LIB下我们要有一个ETCD这么一个目录他告诉我已经存在那就说明我的电脑是有的你们的应该是没有的那这个有了以后呢我们就可以去执行这些命令了我重新reload一下然后呢我们先进一下然后我们去把它启动这个时候你可以去看一下我们当前这个服务的
[03:37] 我们当前这个服务是active running正在运行中OK了你可以看看我们当前的健康状态OK我们当前是一个健康的状态所以这样呢我们就把我们当前的ETCD服务安装完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl enable etcd.Service
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl start etcd.Service
[root@localhost etcd-v3.3.9-linux-amd64]# systemctl status etcd.Service
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
- 配置 systemd 服务文件 /usr/lib/systemd/system/etcd.Service
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
  systemctl enable etcd.Service
  mkdir -p /var/lib/etcd
  systemctl start etcd.Service
  etcdctl cluster-health
  ```

画面 10:
标题：2.2.3 kube-apiserver 服务
内容：
- 解压后将 kube-apiserver、kube-Controller-manager、kube-scheduler 以及管理使用的 kube-cfg 二进制命令文件放到 /usr/bin 目录，即完成这几个服务的安装。
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

