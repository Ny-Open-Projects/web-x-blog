# 11_高级特性-日志与监控

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\11_高级特性-日志与监控_【海量资源尽在 ubkz.com】.mp4
- 时长 5分29秒（音频 329s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍RabbitMQ高级特性的第七个日志与监控那么这一部分内容我们了解一下即可首先我们先来说第一个日志RabbitMQ的日志它默认存放在这么一个路径下的这么一个文件VR log RabbitMQ下边有一个文件当然它有很多的log结尾的文件我们一般查看的是Rabbit
[00:25] at符号这个xx指的是你的主机名点log这么一个文件我们可以来看一下这个文件我们去我们cdcd到vr-log-rabbit这个目录好看一下看一下之后呢你看这里边是不是有很多log的文件啊我们一般看的是这个这个文件啊这个文件呢后边这个就是你的主机名我的主机名叫做super你的主机名可能不叫这个那么我们可以看一下这个文件cat一下
[00:55] 好rabbit at super s-u-p-e-r.loglog好我们可以看一下这个文件这个文件很大这个文件其实随便找一条读一下这条吧connection对吧连接哪个连接呢134这个端口到哪个呢到我们的主机133133是不是当前这个RabbitMQ的这个机器到这个机器已经
[01:19] 已经has a client provider有一个客户端的提供者名字是这么一个factory建立了相当于是建立了个连接对吧然后呢接收了一个连接accepting对吧然后呢又建立了个连接然后呢关闭了closing一个连接等等其实这个日志呢就是寄了一些流水账把你客户端所有的操作跟服务器的一个交互的状态都给你记下来了然后你想看你可以看什么时候关闭的什么时候启动的对吧这里边一大堆的流水账想看一看
[01:48] 可以去看一下这个信息这是我们的日志将来可能出现一些问题的时候我们要通过日志来排查哪个地方有问题好嘞那么日志存放的路径和日志我们简单的看了一下接下来我们来说它的一个web管控台的一个监控这个管控台呢就是我们这个web的客户端那么它里边呢有很多的一些信息我们之前也看过再来简单的说一下比如说totaloverview里边total一共
[02:16] 这个里边有多少的消息所有堆类里边一共有26条消息没有被消费对吧OK啊Unchecked就是被确认的是零条总共呢26条对吧然后呢消费的一个速率是怎么怎么样子的这里边都有一些个参数信息然后呢包括下边你的节点信息是什么样的你的文件然后呢连接进程数内存以及磁盘和硬盘这些数量的空余数都有一个监控信息可以去查看一下
[02:45] 当然你想看的更详细的话呢可以点进去在这个地方呢可以看一下上边呢是你使用的量下边呢它是它限制的量对吧每一个都有啊比如说socket的连接数它使用了一个我们现在使用了一个它限制呢829个那么如果这个绿颜色表示的要接近于红颜色了你就应该注意了这个地方可能会存在一些问题将来可以去排查这些个问题啊OK吧
[03:13] 所以呢这个地方呢指导一下这么一个管理控制台我们可以去查看一下这些信息那么包括这些信息这里边呢有用户的信息对吧然后还有呢虚拟机的一些个信息是不是都是有的呀包括我们可以添加虚拟机呀对吧我们可以去添加用户信息呀而且呢可以让用户和虚拟机进行一个绑定呀是不是都是可以的OK呀那么当然我们可以通过这个图形化界面的这种方式来查看
[03:41] 也可以通过一些命令的方式来查看有一个命令是rabbitmqctlcontrol这么一个命令这个命令有很多的子命令可以帮我们完成一些功能我们来演示一下比如说清平rabbitmqctl你不知道咋用你help一下help一下help一下之后它会罗列出来这个命令的所有参数信息OK那你看一下
[04:09] 这个help里边呢你可以去加很多很多的选项参数信息子命令都可以哈比如说我们在这里边呢我们看一下一共有哪些交换机呢vhost好可以看一下有两个斜杠默认的我们自己创建了一个斜杠itcast对吧可以看一下哎我们在这个里边来看一下是不是有两个呀而且呢你通过命令呢其实呢看的呢并没有我们这个里边的权对吧
[04:37] 那么当然你也可以去看一下它有哪些用户信息呀list users对吧都是可以的两个用户一个guest一个黑马他们的角色呢都是都是这个超级管理员的角色那么包括呢你还可以去看一下gon connectionsecetlons好现在呢可以看到在guest用户下有一个连接然后呢正在运行那么这个IP就是我当前这个windows系统的一个IP啊OK啊
[05:06] 大概呢这个命令呢我们参考一下这个笔记上的就这么一些命令可以去查看一下包括内存的使用情况图形化界面可以看对应的一个命令也是可以来查看的那么这一部分日志和监控我们就简单的介绍了一下这个东西好嘞这块呢就说到这个地方

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 RabbitMQ 的日志与监控，重点演示了通过 rabbitmqctl 命令行工具查看系统状态和管理信息。

2) 按时间顺序列出每张画面的要点：
画面 1: SSH 登录到 RabbitMQ 服务器，终端提示符为 [root@super RabbitMQ]#。
画面 2: 显示 RabbitMQ 日志，INFO REPORT 提示 Statistics garbage collector 启动。
画面 3: 显示连接建立与关闭的日志，包括客户端连接和异常关闭的 TCP 连接。
画面 4: 显示连接建立与关闭的日志，包含 ERROR REPORT，提示 channel exception 和 operation queue.declare caused a channel exception。
画面 5: 显示连接建立与关闭的日志，包含 ERROR REPORT，提示 channel exception 和 operation queue.declare caused a channel exception。
画面 6: PPT 页面，标题为“1. RabbitMQ 高级特性”，子标题“1.7 日志与监控”，小节“1.7.1 RabbitMQ日志”，内容为“RabbitMQ默认日志存放路径：/var/log/RabbitMQ/rabbit@xxx.log”。
画面 7: RabbitMQ Management Web 界面，显示“Totals”部分，包括 Queued messages 和 Message rates 图表，以及 Global counts（Connections: 1, Channels: 1, Exchanges: 26, Queues: 20, Consumers: 1）。
画面 8: RabbitMQ Management Web 界面，显示“Process statistics”部分，包括 File descriptors、Socket descriptors、Erlang processes 和 Memory 的图表与数值。
画面 9: RabbitMQ Management Web 界面，显示“Admin”页面下的“Users”部分，列出用户“guest”和“heime”，并提供“Add a user”表单。
画面 10: SSH 终端，显示连接建立与关闭的日志，最后提示符为 [root@super RabbitMQ]#。
画面 11: SSH 终端，用户输入命令 rabbitmqctl help，显示帮助信息，包括选项 -n, -q, -t 和默认节点 rabbit@server。
画面 12: SSH 终端，用户输入命令 rabbitmqctl list_vhosts，显示帮助信息，列出可用的命令参数。
画面 13: SSH 终端，用户输入命令 rabbitmqctl list_vhosts，显示输出结果“Listing vhosts ...”。
画面 14: PPT 页面，标题为“1. RabbitMQ 高级特性”，子标题“1.7 日志与监控”，小节“1.7.3 rabbitmqctl管理和监控”，列出多个查看命令及其对应参数。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 6:
RabbitMQ默认日志存放路径：/var/log/RabbitMQ/rabbit@xxx.log

画面 11:
rabbitmqctl [-n <node>] [-t <timeout>] [-q] [<command> [<command options>]]
Options:
-n node
-q
-t timeout
Default node is "rabbit@server", where server is the local host. On a host
named "server.example.com", the node name of the RabbitMQ Erlang node will
usually be rabbit@server (unless RABBITMQ_NODENAME has been set to some
non-default value at broker startup time). The output of hostname -s is usually
the connect suffix to use after the "@" sign. See RabbitMQ-server(1) for
details of configuring the RabbitMQ broker.

画面 12:
The list_queues, list_exchanges and list_bindings commands accept an optional
virtual host parameter for which to display results. The default value is "/".
<queueinfoitem> must be a member of the list [name, durable, auto_delete, arguments, policy, pid, owner_pid, exclusive, exclusive_consumer_pid,
exclusive_consumer_tag, messages_ready, messages_unacknowledged, messages,
messages_ready_ram, messages_unacknowledged_ram, messages_ram,
messages_unacknowledged_ram, message_bytes, message_bytes_ram,
message_bytes_ready, message_bytes_unacknowledged, message_bytes_ram,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram, message_bytes_ready,
message_bytes_unacknowledged_ram, message_bytes_ram,

