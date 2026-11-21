# 13.Kubernetes集群搭建Node安装-kubelet服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\13.Kubernetes集群搭建Node安装-kubelet服务_【海量资源尽在 ubkz.com】.mp4
- 时长 4分12秒（音频 252s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面呢我完成一下我们node节点的cubelite服务那前期呢我们已经把cubelite这个配置文件二进制执行文件呢已经copy到user下的b目录下了那么我们现在呢参考我们的讲义去把这个cubelite服务啊创建一下那首先呢我们是创建一下我们当前的这个服务的文件我们编辑一下它在这里呢我们把这段内容
[00:30] copy一下然后还有下面这部分然后大家注意我们这里边需要去创建一些我们当前的文件这里你看一下我们是不是有个vr下lab-kuber-lag那么我们需要把这个working directory创建出来所以我们需要make dir我们vr下有个lab下的kuber-lag
[01:04] 这个目录创建下来那创建完它以后呢我们就可以去做我们当前Kubernetes的配置那我们需要去在这个ETC Kubernetes下面有一个Kubernetes的配置文件那我们这里面应该是没有当前这个Kubernetes这个目录所以我们在ETC下创建一个Kubernetes这么一个目录
[01:29] 然后呢我们再去ETC下的KUBERNETES我们在这下面再创建一个KUBERLITE这么一个文件在这个文件里边写上当前的配置信息然后呢这里边你要注意那个IP地址这个IP地址啊它写的是什么呢写的是我当前本机也就是说你当前这个
[01:58] node节点的IP是多少我们node节点的IP是148所以呢你把它写上一下然后你注意看啊它的前面指定了一个cuberectfig也就是说它需要在etc kubernetes下面有个cuberectfig这么一个文件这个文件是干什么用的呢其实非常简单这个文件呢它描述的就是我们连接的服务器是哪一个所以在这里我们要去
[02:27] VI一下ETC一下的Kubernetes下面有个Kuberconfig有个这么一个文件这个文件里边我们要写上我连接的当前的服务器是谁也就是千万注意了我们在这里有些地方啊我们需要去调整一下这个位置
[03:02] 我们应该调整成147这个147是我们当前master这个服务它的入期这个IP地址然后我们这个缩进有点问题我们要去控制一下我这个server要控制一下我的name要控制一下还有这个context还有它我们都要缩进一下
[03:36] 因为我们这是基于这种YAML的文件所以呢我们要让他能知道我们当前这个层次关键这个应该可以了好了那我们把这个文件呢保存一下这里边你要注意这个缩进格式还要注意我们当前要改成我们自己的master的IP地址这样的话呢我的Kubernetes的这个服务啊就OK了
[04:06] 那一会儿呢我们需要再配置一个Kubra proxy

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
在Node1节点上安装并配置Kubernetes的kubelet服务，包括创建systemd服务文件、设置kubelet配置文件以及配置kubectl的kubeconfig文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录结构，当前位于“2.3 Node1安装”章节，右侧PPT显示“2.3 Node1安装”标题及“在Node1节点上...”的安装说明。
画面2：PPT页面显示“2.3 Node1安装”章节，下方有多个窗口预览，包括SecureCRT、VMware等，说明在Node1节点上安装Docker并启动。
画面3：PPT页面显示“2.3.1 kubelet服务”小节，内容为“配置systemd服务文件：vi /usr/lib/systemd/system/kubelet.Service”，并展示“黑马程序员”Logo及宣传语。
画面4：PPT页面内容与画面3相同，但下方SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，准备执行命令。
画面5：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面6：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面7：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面8：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面9：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面10：SecureCRT窗口显示“[root@localhost ~]#”命令行提示符，光标在命令行等待输入。
画面11：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面12：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面13：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。
画面14：PPT页面显示“用于kubelet连接Master Apiserver的配置文件”及“vi /etc/kubernetes/kubelet”命令，SecureCRT窗口显示“[root@localhost ~]#”命令行提示符。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
WorkingDirectory=/var/lib/kubelet
ExecStart=/usr/bin/kubelet $KUBLET_ARGS
Restart=on-failure
KillMode=process
[Install]
WantedBy=multi-user.target
```
画面3：
```
[Unit]
Description=kubernetes kubelet Server

[Service]
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=Docker.Service
Requires=Docker.Service

[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet $KUBLET_ARGS
Restart=on-failure
KillMode=process

[Install]
WantedBy=multi-user.target
```
画面11：
```
KUBELET_ARGS="--kubeconfig=/etc/kubernetes/kubeconfig --hostname-override=192.168.126.148 --logtostderr=false --log-dir=/var/log/kubernetes --v=2 --fail-swap-on=false"
```
画面12：
```
apiVersion: v1
kind: Config
clusters:
- cluster:
    server: http://192.168.126.148:8080
    name: local
  context:
    cluster: local
    namespace: default
    user: myuser
  name: mycontext
current-context: mycontext
```
画面13：
```
apiVersion: v1
kind: Config
clusters:
- cluster:
    server: http://192.168.126.147:8080
    name: local
  context:
    cluster: local
    namespace: default
    user: myuser
  name: mycontext
current-context: mycontext
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“2.3 Node1安装”，内容为“在Node1节点上...”。
画面2：PPT标题为“2.3 Node1安装”，内容为“在Node1节点上...”。
画面3：PPT标题为“2.3.1 kubelet服务”，内容为“配置systemd服务文件：vi /usr/lib/systemd/system/kubelet.Service”。
画面12：PPT标题为“用于kubelet连接Master Apiserver的配置文件”，内容为“vi /etc/kubernetes/kubeconfig”。
画面13：PPT标题为“用于kubelet连接Master Apiserver的配置文件”，内容为“vi /etc/kubernetes/kubeconfig”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

