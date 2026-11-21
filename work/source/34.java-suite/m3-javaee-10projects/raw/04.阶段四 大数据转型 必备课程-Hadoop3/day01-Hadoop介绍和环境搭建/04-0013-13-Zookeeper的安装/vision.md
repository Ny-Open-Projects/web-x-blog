# 画面线理解：13-Zookeeper的安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\13-Zookeeper的安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:23, 01:00, 01:50, 02:41, 03:39, 04:59, 05:48, 06:45, 08:37, 10:05, 11:24, 12:40, 13:34, 14:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:30:32

1) 这一组画面整体在讲什么（一句话）：
在三台 Linux 服务器上安装并配置 Zookeeper 3.4.9 集群，包括下载、解压、配置 myid 文件和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示课程 PPT 页面，内容为“7.2 Zookeeper安装”，包含服务器 IP、主机名和 myid 的对应关系表，以及下载地址 http://archive.apache.org/dist/zookeeper/。
画面 2：在 Apache Zookeeper 官网下载页面，显示了多个版本的文件夹，鼠标悬停在 zookeeper-3.4.9 上。
画面 3：在 node01 服务器的 SecureCRT 会话中，进入 /export/software 目录，准备上传下载的文件。
画面 4：在 node01 服务器的 SecureCRT 会话中，执行命令 ls，显示了 zookeeper-3.4.9 文件。
画面 5：在 node01 服务器的 SecureCRT 会话中，进入 /export/servers/zookeeper-3.4.9/conf 目录，查看了 zoo_sample.cfg 文件。
画面 6：在 node01 服务器的 SecureCRT 会话中，查看了 zoo.cfg 配置文件内容，包括 dataDir、clientPort、maxClientCnxns、autopurge.snapRetainCount、autopurge.purgeInterval 等配置项，并执行命令 mkdir -p /export/servers/zookeeper-3.4.9/zkdatas 创建数据目录。
画面 7：在 node01 服务器的 SecureCRT 会话中，显示了 zoo.cfg 配置文件内容，包括 clientPort、maxClientCnxns、autopurge.snapRetainCount、autopurge.purgeInterval 等配置项。
画面 8：展示课程 PPT 页面，内容为“第四步：添加 myid 配置”，指导在第一台机器的 /export/servers/zookeeper-3.4.9/zkdatas/ 目录下创建名为 myid 的文件，内容为 1。
画面 9：在 node01 服务器的 SecureCRT 会话中，执行命令 scp -r /export/servers/zookeeper-3.4.9/ node03:/export/servers/，将 Zookeeper 文件夹复制到 node03 服务器。
画面 10：展示课程 PPT 页面，内容为“第二台机器上修改 myid 的值为 2”、“第三台机器上修改 myid 的值为 3”、“第六步：三台机器启动 zookeeper 服务”，并给出了启动命令 /export/servers/zookeeper-3.4.9/bin/zkServer.sh start 和状态检查命令 /export/servers/zookeeper-3.4.9/bin/zkServer.sh status。
画面 11：在 node03 服务器的 SecureCRT 会话中，显示了空的命令行界面。
画面 12：在 node02 服务器的 SecureCRT 会话中，执行命令 echo 2 > /export/servers/zookeeper-3.4.9/zkdatas/myid，创建 myid 文件并写入值 2，然后执行命令 cd /export/servers/zookeeper-3.4.9/，再执行命令 bin/zkServer.sh start 启动服务，显示服务已启动，最后执行命令 jps 确认 QuorumPeerMain 进程。
画面 13：在 node02 服务器的 SecureCRT 会话中，执行命令 bin/zkServer.sh status，显示服务状态为 Mode: leader。
画面 14：在 node01 服务器的 SecureCRT 会话中，执行命令 bin/zkServer.sh status，显示服务状态为 Mode: follower。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 6 中的配置文件内容：
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just
# example sakes.
dataDir=/export/servers/zookeeper-3.4.9/zkdatas
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
# Be sure to read the maintenance section of the
# administrator guide before turning on autopurge.
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
# The number of snapshots to retain in dataDir
autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
autopurge.purgeInterval=1

画面 8 中的 PPT 内容：
第四步：添加 myid 配置
在第一台机器的
/export/servers/zookeeper-3.4.9/zkdatas/ 这个路径下创建一个文件，文件名为 myid 文件内容为 1

第五步：安装包分发并修改 myid 的值
安装包分发到其他机器
第一台机器上执行以下两个命令
scp -r /export/servers/zookeeper-3.4.9/ node02:/export/servers/

画面 10 中的 PPT 内容：
第二台机器上修改 myid 的值为 2
echo 2 > /export/servers/zookeeper-3.4.9/zkdatas/myid
[root@node02 servers]# more /export/servers/zookeeper-3.4.9/zkdatas/myid

第三台机器上修改 myid 的值为 3
echo 3 > /export/servers/zookeeper-3.4.9/zkdatas/myid
[root@node03 servers]# more /export/servers/zookeeper-3.4.9/zkdatas/myid

第六步：三台机器启动 zookeeper 服务
三台机器启动 zookeeper 服务
这个命令三台机器都要执行
/export/servers/zookeeper-3.4.9/bin/zkServer.sh start
查看启动状态
/export/servers/zookeeper-3.4.9/bin/zkServer.sh status

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：PPT 标题为“7.2 Zookeeper安装”，包含一个表格，列标题为“服务器IP”、“主机名”、“myid的值”，内容为：
| 服务器IP | 主机名 | myid的值 |
| --- | --- | --- |
| 192.168.174.100 | node01 | 1 |
| 192.168.174.110 | node02 | 2 |
| 192.168.174.120 | node03 | 3 |

画面 8：PPT 标题为“第四步：添加 myid 配置”，内容为“在第一台机器的 /export/servers/zookeeper-3.4.9/zkdatas/ 这个路径下创建一个文件，文件名为 myid 文件内容为 1”。

画面 10：PPT 标题为“第二台机器上修改 myid 的值为 2”、“第三台机器上修改 myid 的值为 3”、“第六步：三台机器启动 zookeeper 服务”，内容为“三台机器启动 zookeeper 服务”、“这个命令三台机器都要执行 /export/servers/zookeeper-3.4.9/bin/zkServer.sh start”、“查看启动状态 /export/servers/zookeeper-3.4.9/bin/zkServer.sh status”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
