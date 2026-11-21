# 画面线理解：14-Zookeeper的节点操作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\14-Zookeeper的节点操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 03:55, 04:37, 05:34, 06:41, 07:44, 08:22, 09:17, 09:36, 10:40, 11:26, 12:28, 13:00, 13:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:33:31

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 ZooKeeper 的 Shell 客户端进行节点（Znode）的创建、读取、修改和删除等基本操作，并展示其特性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 2: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，列出了可用的命令，如 stat、set、ls、delquota、ls2、setAcl、setquota、history 等。
画面 3: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 4: 展示了 Typora 文档中“Znode 的特点”部分，说明 Znode 是文件系统的核心，选取时需用路径形式，Znode 本身不是文件，是树状结构，具有原子性，数据最大长度为 1M。
画面 5: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create /app1 hello、create -s /app2 world、create -s /app3 world 等命令，创建了三个节点。
画面 6: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create -e /tempnode java 命令创建了一个临时节点，然后执行 quit 命令退出会话。
画面 7: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，显示了客户端连接 ZooKeeper 服务器的详细日志，包括 session id 和连接建立成功。
画面 8: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create -s -e /tempnode2 aaa 命令创建了一个带数据的临时节点。
画面 9: 展示了 Typora 文档中“7.3 Zookeeper 的 Shell 客户端操作”章节，列出了 create、ls、ls2、set、delete、rmr、setquota、history 等命令及其说明和参数。
画面 10: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 create /app1/test1 hadoop、get /app1 命令，获取了节点数据。
画面 11: 展示了 Typora 文档中列出的 ZooKeeper 操作步骤，包括创建普通节点、创建有序节点、创建临时节点、获取节点数据、修改节点数据、删除节点。
画面 12: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 delete /app1 命令，提示节点不为空，无法删除。
画面 13: 展示了 SecureCRT 中的 ZooKeeper Shell 交互界面，执行了 rmr /app1 命令删除节点，然后执行 ls / 和 history 命令查看目录和历史记录。
画面 14: 展示了 Typora 文档中列出的 ZooKeeper 操作步骤，包括创建临时节点、获取节点数据、修改节点数据、删除节点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
/export/servers/zookeeper-3.4.9/bin/zkServer.sh status
```
画面 2:
```
ZooKeeper -server host:port cmd args
stat path [watch]
set path data [version]
ls path [watch]
delquota [-n|-b] path
ls2 path [watch]
setAcl path acl
setquota -n|-b val path
history
redo cmdno
printwatches on|off
delete path [version]
sync path
listquota path
rmr path
get path [watch]
create [-s] [-e] path data acl
```
画面 3:
```
/export/servers/zookeeper-3.4.9/bin/zkServer.sh status
```
画面 4:
```
Znode 的特点
• 文件系统的核心是 Znode
• 如果想要选取一个 Znode，需要使用路径的形式，例如 /test1/test11
• Znode 本身并不是文件，也不是文件夹。Znode 因为具有一个类似于 Name 的路径，所以可以从逻辑上实现一个树状文件系统
• ZK 保证 Znode 之间的原子性，不会出现部分 ZK 节点更新成功，部分 ZK 节点更新失败的问题
• Znode 中数据是有大小限制的，最大只能为 1M
```
画面 5:
```
[zk: localhost:2181(CONNECTED) 1] ls /
[zookeeper, app1]
[zk: localhost:2181(CONNECTED) 2] create /app1 hello
Created /app1
[zk: localhost:2181(CONNECTED) 3] ls /
[zookeeper, app1]
[zk: localhost:2181(CONNECTED) 4] create -s /app2 world
Created /app2000000001
[zk: localhost:2181(CONNECTED) 5] ls /
[zookeeper, app1, app2000000001]
[zk: localhost:2181(CONNECTED) 6] create -s /app3 world
Created /app3000000002
[zk: localhost:2181(CONNECTED) 7] ls /
[zookeeper, app1, app2000000001, app3000000002]
[zk: localhost:2181(CONNECTED) 8] 
```
画面 6:
```
[zk: localhost:2181(CONNECTED) 9] create -e /tempnode java
Created /tempnode1
[zk: localhost:2181(CONNECTED) 10] quit
Quitting...
2019-04-22 15:32:59,601 [myid:] - INFO [main:ZooKeeper@684] - Session: 0x16a43cbfb150003 closed
2019-04-22 15:32:59,603 [myid:] - INFO [main-EventThread:ClientCnxnEventThread@519] - EventThread shut down f
or session: 0x16a43cbfb150003
[root@node01 zookeeper-3.4.9]#
```
画面 7:
```
2019-04-22 15:33:02,441 [myid:] - INFO [main:Environment@100] - Client environment:user.name=root
2019-04-22 15:33:02,442 [myid:] - INFO [main:Environment@100] - Client environment:user.home=/root
2019-04-22 15:33:02,442 [myid:] - INFO [main:Environment@100] - Client environment:user.dir=/export/servers/zoo
keeper-3.4.9
2019-04-22 15:33:02,449 [myid:] - INFO [main:ZooKeeper@438] - Initiating client connection, connectString=loca
lhost:2181 sessionTimeout=30000 watcher-org.apache.zookeeper.ZooKeeperMain$MainWatcher#950c6589e
Welcome to ZooKeeper!
2019-04-22 15:33:02,504 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@1032] - Opening
socket connection to server localhost:0:0:0:0:0:0:1:2181. Will not attempt to authenticate using SASL (unknow
n error)
JLine support is enabled
2019-04-22 15:33:02,600 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@876] - Socket co
nnection established to localhost:0:0:0:0:0:0:1:2181, initiating session
2019-04-22 15:33:02,623 [myid:] - INFO [main-SendThread(localhost:2181):ClientCnxn$SendThread@129
