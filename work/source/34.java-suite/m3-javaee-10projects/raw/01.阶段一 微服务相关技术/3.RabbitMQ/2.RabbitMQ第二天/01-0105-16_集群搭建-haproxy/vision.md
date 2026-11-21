# 画面线理解：16_集群搭建-haproxy

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\16_集群搭建-haproxy_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 02:00, 02:46, 03:12, 04:15, 05:18, 06:54, 07:39, 08:03, 08:58, 10:25, 11:18, 11:50, 12:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:54:19

1) 这一组画面整体在讲如何在Linux服务器上安装、配置并启动HAProxy作为RabbitMQ集群的负载均衡器。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT目录，当前章节为“3.5 优雅均衡-HAProxy”，并显示“3.5.1 安装HAProxy”小节的代码，包含安装依赖包、解压、编译安装、创建用户组和配置文件的命令。
画面2：在SecureCRT终端中执行yum安装命令，显示因镜像源问题导致的包冲突错误。
画面3：在SecureCRT终端中执行yum安装命令，显示成功更新了vim-common和wget包。
画面4：在SecureCRT终端中执行make命令，显示编译HAProxy源码的过程。
画面5：展示课程PPT，内容为“3.5.2 配置HAProxy”，并显示配置文件路径和部分配置内容。
画面6：展示课程PPT，内容为“3.5.2 配置HAProxy”，显示HAProxy配置文件的“global”和“defaults”部分。
画面7：在SecureCRT终端中编辑HAProxy配置文件，显示配置内容并提示“Can't open file for writing”。
画面8：在SecureCRT终端中尝试执行配置文件路径，提示“no such file or directory”。
画面9：展示课程PPT，内容为“启动HAProxy负载”，并显示启动命令和访问地址。
画面10：在SecureCRT终端中执行cd命令，提示“command not found”，并显示目录列表。
画面11：展示IDEA开发环境，显示项目结构和多个窗口，包括PPT和代码编辑器。
画面12：在SecureCRT终端中执行cd命令，提示“command not found”，并显示目录列表。
画面13：在IDEA开发环境中运行“HelloWorld”程序，显示程序运行成功。
画面14：展示课程PPT，内容为“3.2 单机多实例部署”，并显示架构图，图中Producer指向HAProxy，HAProxy指向多个RabbitMQ实例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
//下载依赖包
yum install gcc vim wget
//上传haproxy源码包
//解压
tar -zxvf haproxy-1.6.5.tar.gz -C /usr/local
//进入目录，进行编译、安装
cd /usr/local/haproxy-1.6.5
make TARGET=linux2611 PREFIX=/usr/local/haproxy
mkdir /etc/haproxy
//赋权
groupadd -r -g 149 haproxy
useradd -r -s /sbin/nologin -u 149 haproxy
//创建haproxy配置文件
vim /etc/haproxy/haproxy.cfg
```

画面5：
```bash
配置文件路径：/etc/haproxy/haproxy.cfg
#logging options
global
    log 127.0.0.1 local0 info
    maxconn 5120
    chroot /usr/local/haproxy
    uid 99
    gid 99
    daemon
    quiet
    nbproc 20
    pidfile /var/run/haproxy.pid
```

画面6：
```bash
#logging options
global
    log 127.0.0.1 local0 info
    maxconn 5120
    chroot /usr/local/haproxy
    uid 99
    gid 99
    daemon
    quiet
    nbproc 20
    pidfile /var/run/haproxy.pid
```

画面7：
```bash
#balance source //ip
balance roundrobin
server node1 127.0.0.1:5673 check inter 5000 rise 2 fall 2
server node2 127.0.0.1:5674 check inter 5000 rise 2 fall 2
listen stats
bind 172.16.98.133:8100
mode http
option httplog
stats enable
stats uri /rabbitmq-stats
stats refresh 5s
```

画面9：
```bash
/usr/local/haproxy/sbin/haproxy -f /etc/haproxy/haproxy.cfg
//查看haproxy进程状态
ps -ef | grep haproxy
访问如下地址对mq节点进行监控
http://172.16.98.133:8100/rabbitmq-stats
代码中访问mq集群地址，则变为访问haproxy地址:5672
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
标题：3.2 单机多实例部署
架构图：
- Producer 指向 HAProxy
- HAProxy 指向 RabbitMQ rabbit1
- HAProxy 指向 RabbitMQ rabbit2
- HAProxy 指向 RabbitMQ rabbit3
- HAProxy 指向 RabbitMQ rabbitN...

5) 不要评价画面美观，不要输出与课程无关的内容。
