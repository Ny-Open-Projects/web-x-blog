# 画面线理解：15_集群搭建-镜像队列

- 阶段：01.阶段一 微服务相关技术
- 章节：3.RabbitMQ/2.RabbitMQ第二天
- 源文件：01.阶段一 微服务相关技术\3.RabbitMQ\2.RabbitMQ第二天\15_集群搭建-镜像队列_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:50, 03:13, 04:23, 05:33, 06:25, 07:58, 08:51, 09:36, 10:15, 11:03, 13:27, 14:11, 14:52, 16:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 09:53:39

1) 这一组画面整体在讲什么（一句话）：
演示如何搭建和配置 RabbitMQ 集群，包括使用 HAProxy 负载均衡、节点管理、集群状态检查以及镜像队列配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 RabbitMQ 集群搭建的 PPT 内容，介绍集群方案原理，图示 Producer -> HAProxy -> Consumer 的架构。
画面 2：在 SecureCRT 中执行 `rabbitmq-server` 状态检查命令，显示 Erlang 环境和系统资源信息。
画面 3：在 SecureCRT 中执行 `service rabbitmq-server stop` 停止服务，然后执行 `RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rabbit rabbitmq-server start` 启动服务。
画面 4：在 RabbitMQ 管理界面（Queues 标签页）显示无队列，页面提示“no queues ...”。
画面 5：在 SecureCRT 中执行 `rabbitmq-server` 命令后，终端显示“已终止”。
画面 6：在 RabbitMQ 管理界面（Overview 标签页）显示节点状态，rabbit1@super 节点状态为“Node not running”。
画面 7：在 RabbitMQ 管理界面（Overview 标签页）显示节点状态，rabbit1@super 和 rabbit2@super 节点均正常运行。
画面 8：在 RabbitMQ 管理界面（Queues 标签页）显示一个名为 “aa” 的队列，状态为 Idle。
画面 9：在 SecureCRT 中执行 `service rabbitmq-server stop` 停止服务，然后执行 `RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rabbit rabbitmq-server start` 启动服务。
画面 10：在 RabbitMQ 管理界面（Admin 标签页）的 Users 页面显示用户 guest，角色为 administrator。
画面 11：展示 PPT 内容，介绍镜像队列配置，提供命令 `rabbitmqctl set_policy my_ha "ha-mode" "all"`。
画面 12：在 RabbitMQ 管理界面（Queues 标签页）的 “Publish message” 区域，设置 Delivery mode 为 Persistent，Payload 为 “666”。
画面 13：在 RabbitMQ 管理界面（Queues 标签页）的 “Get messages” 区域，设置 Requeue 为 Yes，点击 “Get Message(s)”。
画面 14：展示 PPT 内容，列出集群管理命令，包括 `rabbitmqctl join cluster`、`rabbitmqctl cluster_status`、`rabbitmqctl change_cluster_node_type` 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```
[stdib,"ERTS CXC 138 10","2.8"],
[os,unix,linux],
[erlang_version,"Erlang/OTP 18 [erts-7.3] [source] [64-bit] [async-threads:64] [hipe] [kernel-poll:true]vn"],
[total,55398680],
[connection_readers,0],
[connection_writers,0],
[connection_channels,0],
[connection_other,2800],
[queue_procs,26768],
[queue_slave_procs,0],
[plugins,127902],
[other_proc,18080792],
[eposta,124102],
[mgmt_db,904768],
[eg_index,69440],
[other_ets,1407728],
[binary,91144],
[code,2782048],
[atom,1000001],
[other_system,4407417]],
[listeners,[[clustering,25672,"::"],[amqp,5672,"::"]]],
[vm_memory_high_watermark,0.4],
[vm_memory_limit,411294105],
[disk_free_limit,50000000],
[disk_free,13270196224],
[file_descriptors,[total,924],[total_used,0],[sockets_limit,829],[sockets_used,0]],
[processes,[limit,1048576],[used,261]],
[uptime,220],
[kernel,[net_ticktime,60]],
[root@super~]#
```

画面 3：
```
[root@super ~]# service rabbitmq-server stop
Stopping rabbitmq-server: rabbitmq-server.
[root@super ~]# RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rabbit rabbitmq-server start
##########
RabbitMQ 3.6.5. Copyright (C) 2007-2016 Pivotal Software, Inc.
Licensed under the MPL. See http://www.rabbitmq.com/
##########
Logs: /var/log/rabbitmq/rabbit.log
/var/log/rabbitmq/rabbit-sasl.log
##########
Starting broker...
Completed with 0 plugins.
```

画面 9：
```
[root@super ~]# service rabbitmq-server stop
Stopping rabbitmq-server: rabbitmq-server.
[root@super ~]# RABBITMQ_NODE_PORT=5673 RABBITMQ_NODENAME=rabbit rabbitmq-server start
##########
RabbitMQ 3.6.5. Copyright (C) 2007-2016 Pivotal Software, Inc.
Licensed under the MPL. See http://www.rabbitmq.com/
##########
Logs: /var/log/rabbitmq/rabbit.log
/var/log/rabbitmq/rabbit-sasl.log
##########
Starting broker...
Completed with 0 plugins.
```

画面 11：
```
rabbitmqctl cancel_sync_queue [-p vhost] (queue)
取消队列queue同步镜像的操作。

rabbitmqctl set_cluster_name (name)
设置集群名称。集群名称在客户端连接时会通知给客户端。Federation和Shovel插件也会用到集群名称的地方。
集群名称就是集群中第一个节点的名称，通过这个命令可以重新设置。

3.4 RabbitMQ镜像集群配置

上面已经完成RabbitMQ默认集群模式，但并不能保证队列的高可用性，尽管交换机、绑定这些可以复制到集群里的任何一个节点，但是队列内容不会复制。当然该模式解决一项组节点压力，但队列节点宕机后导致该队列无法使用，只能等待重启，所以要想在队列节点宕机或故障也能正常使用，就要配置镜像队列。
镜像队列，我们基于普通的集群模式，然后再添加一些策略，所以你还是得先配置普通集群，然后才能设置镜像队列。
我们通过上面的集群设置。

设置的镜像队列可以通过开启的网页的管理端Admin->Policies，也可以通过命令。
rabbitmqctl set_policy my_ha "ha-mode" "all"
```

画面 14：
```
rabbitmqctl join cluster (cluster node) [-ram]
将节点加入指定集群中。在这个命令执行和需要停止RabbitMQ应用并重载节点。

rabbitmqctl cluster_status
显示集群的状态。

rabbitmqctl change_cluster_node_type [disc|ram]
修改集群节点的类型。在这个命令执行前需要停止RabbitMQ应用。

rabbitmqctl forget_cluster_node [-offline]
将节点从集群中删除，允许重新执行。

rabbitmqctl update_cluster_nodes (cluster node)
在集群中的节点启动时自动向客户端告知集群的最新信息，并更新相应的集群信息。这个和join_cluster不同，它不加入集群。专有这样一种情况，当节点A和节点B都在集群中，当节点A又离开了集群，节点C又和节点B组成了一个集群，然后节点B又离开了集群，它会尝试联系节点B，但这样会失败，因为节点B已经不在集群中了。

rabbitmqctl cancel_sync_queue [-p vhost] (queue)
取消队列queue同步镜像的操作。

rabbitmqctl set_cluster_name (name)
设置集群名称。集群名称在客户端连接时会通知给客户端。Federation和Shovel插件也会用到集群名称的地方。
集群名称就是集群中第一个节点的名称，通过这个命令可以重新设置。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
标题：3. RabbitMQ集群搭建
子标题：3.1 集群方案的原理
内容：介绍集群方案原理，图示：Producer -> HAProxy -> Consumer
画面 11：
标题：3.4 RabbitMQ镜像集群配置
内容：介绍镜像队列配置，提供命令 `rabbitmqctl set_policy my_ha "ha-mode" "all"`。
画面 14：
标题：集群管理命令
内容：列出集群管理命令，包括 `rabbitmqctl join cluster`、`rabbit
