# 画面线理解：12-Zookeeper的概述

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\12-Zookeeper的概述【海量资源尽在 ubkz.com】.mp4
- 抽帧：10 帧 @ 00:44, 08:16, 08:18, 08:19, 08:21, 08:22, 08:23, 08:24, 09:26, 09:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:27:46

1) 这一组画面整体在讲什么（一句话）：
讲解 Zookeeper 的基本概念、分布式文件系统特性、集群架构及客户端交互机制。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 Typora 文档中关于 Zookeeper 的介绍，包含其定义（开源分布式协调服务框架、Google Chubby 开源实现、分布式文件系统）。
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“Zookeeper 是一个开源的分布式协调服务框架，主要用来解决分布式集群中应用系统的一致性问题”、“Zookeeper 是 Google Chubby 思想的一个开源实现”、“Zookeeper 本质上是一个分布式文件系统，适合存放小文件，通过文件系统来实现分布式协调”。

画面 2:
- 展示了两个架构图：左侧是“Zookeeper 集群”指向“hadoop集群”（包含 node01、node02、node03）；右侧是“zookeeper集群”（包含 leader、follower）的详细结构，显示了客户端（client）向 follower 发送读请求和写请求。
- 文字：“zookeeper集群”、“ip=192.168.174.110”、“ip=192.168.174.110”、“ip=192.168.174.100”、“follower”、“leader”、“client”、“读请求”、“写请求”。

画面 3:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 4:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 5:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 6:
- 展示了“分布式文件系统？”的架构图：左侧是 Zookeeper 集群（包含 /servers/host1、/servers/host2、/servers/host3），右侧是文件系统（包含 /、/servers、/host1、/host2、/host3）。
- 文档中文字：“在上图左侧，Zookeeper 中存储的其实是一个又一个 Znode，Znode 是 Zookeeper 中的节点”、“Znode 是有路径的，例如 /data/host1、/data/host2，这个路径也可以理解为是 Znode 的 Name”、“Znode 也可以携带数据，例如说某个 Znode 的路径是 /data/host1，其值是一个字符串 “192.168.6.1””、“正因为 Znode 的特性，所以 Zookeeper 可以对外提供出一个类似于文件系统的试图，可以通过操作文件系统的方式操作 Zookeeper”。

画面 7:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 8:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 9:
- 展示了“Zookeeper 是分布式的”部分，包含两个架构图：上方是客户端（Client）通过 Zookeeper API 访问 Zookeeper 集群（包含 Leader、Follower1、Follower2）；下方是客户端（Client）与 Leader、Follower1 交互的简化图。
- 文档中文字：“首先呢，Zookeeper 是分为服务端和客户端的，客户端有 Java 的客户端，有 Shell 命令的客户端等，客户端通过一个类似于文件系统的 API 访问 Zookeeper 集群”、“但是事实上，客户端请求是直接访问 Zookeeper 集群，集群中有两大类角色，一类是 Leader，一类是 Follower，其实就是主从，Leader 负责读和写，Follower 只能读，遇到会产生修改的需求会转发给 Leader 处理，这是因为 Zookeeper 本质上就是为了在分布式环境中对常见的——一致性，而 Zookeeper 所属于的 ZAB 协议是一个变种，ZAB 协议中有一个全局的事务生成者，就是 Leader，修改设计在分布式环境下对事务达成一致，必须由 Leader 发起”。

画面 10:
- 展示了“举个例子？”部分，包含一个架构图：Zookeeper 集群（包含 /server/slave1、/server/slave2）连接到 Master、Slave1、Slave2。
- 文档中文字：“比如有一个常见的分布式主从系统，如果有 ZK 在的话，主节点不需要和每个从节点时连接，只需要监听从节点创建的 Znode，便可以知道在线”、“Zookeeper 能做什么？”、“发布订阅”、“命名服务”、“分布式锁”。

3)
