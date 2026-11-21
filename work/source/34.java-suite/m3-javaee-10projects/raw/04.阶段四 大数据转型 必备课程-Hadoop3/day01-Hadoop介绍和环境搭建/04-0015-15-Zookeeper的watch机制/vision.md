# 画面线理解：15-Zookeeper的watch机制

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\15-Zookeeper的watch机制【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 04:40, 04:49, 05:03, 05:05, 05:23, 05:26, 05:29, 05:42, 05:45, 05:49, 05:56, 06:05, 06:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:36:20

1) 这一组画面整体在讲什么（一句话）：
演示 Zookeeper 的 Watch 机制，通过在客户端设置 Watcher 来监听节点数据变化，并展示数据变更后 Watcher 触发的通知事件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程目录结构，当前章节为“Zookeeper 的 Watch 机制”，并列出了 Znode 属性和通知机制的要点。
画面 2: 展示了“发布/订阅机制”的概念图，包含“主题”、“订阅者”、“发布者”；右侧是“Zookeeper 集群”架构图，显示“Zookeeper 节点”通过“watch 机制”与“Hadoop 集群”中的“node01”和“node02”节点交互。
画面 3: 在 SecureCRT 中，执行了 Zookeeper 命令，包括 `ls /`、`get /app1`、`create /app1/test1 hadoop`、`set /app1 xxx`、`delete /app1` 等操作，用于创建和管理 Znode。
画面 4: 继续在 SecureCRT 中执行命令，创建了节点 `/node01` 并设置其数据为 `hello`。
画面 5: 显示了 `ls /` 命令的输出，确认 `/node01` 节点已创建。
画面 6: 执行 `get /node01 watch` 命令，查看节点数据并设置 Watcher。
画面 7: 画面内容与画面 6 相同，未新增操作。
画面 8: 连接到 node03.hadoop.com 的 SSH 登录界面。
画面 9: 在 node03 上执行了 `cd /export/servers/zookeeper-3.4.9/bin` 命令，进入 Zookeeper 的 bin 目录。
画面 10: 画面内容与画面 6 相同，未新增操作。
画面 11: 在 node03 上执行了 `./zkCli.sh` 命令，连接到 Zookeeper 服务器，输出了连接成功的日志。
画面 12: 在 node03 上执行了 `set /node01 world` 命令，修改了节点 `/node01` 的数据。
画面 13: 执行 `get /node01 watch` 命令，输出了 Watcher 触发的通知事件 `WatchedEvent state:SyncConnected type:NodeDataChanged path:/node01`。
画面 14: 画面内容与画面 12 相同，未新增操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```
[zk: localhost:2181(CONNECTED) 10] rmr /app1
[zk: localhost:2181(CONNECTED) 11] ls /
[app3000000002, tempnode2000000004, app2000000001, zookeeper]
[zk: localhost:2181(CONNECTED) 12] history
2 - ls /
3 - get /app1
4 - create /app1/test1 hadoop
5 - get /app1
6 - set /app1 xxx
7 - get /app1
8 - delete /app1
9 - rmr /app1
10 - ls /
11 - history
12 - ls /
[zk: localhost:2181(CONNECTED) 13] ls /
[app3000000002, tempnode2000000004, app2000000001, zookeeper]
[zk: localhost:2181(CONNECTED) 14] create /node01 hello
Created /node01
```

画面 4:
```
[zk: localhost:2181(CONNECTED) 14] create /node01 hello
Created /node01
```

画面 5:
```
[zk: localhost:2181(CONNECTED) 16] ls /
[app3000000002, tempnode2000000004, app2000000001, node01, zookeeper]
```

画面 6:
```
[zk: localhost:2181(CONNECTED) 16] get /node01 watch
hello
cZxid = 0x100000014
ctime = Mon Apr 22 16:28:50 CST 2019
mZxid = 0x100000014
mtime = Mon Apr 22 16:28:50 CST 2019
pZxid = 0x100000014
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 5
numChildren = 0
```

画面 11:
```
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.dir=/export/servers/zookeeper-3.4.9
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.library.path=/usr/java64
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.tmpdir=/tmp
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:java.compiler=CNA
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:os.name=Linux
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:os.arch=x86_64
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.name=root
2019-04-22 16:29:29,707 [myid:] - INFO [main:Environment@100] - Client environment:user.home=/export/servers/zookeeper-3.4.9
```

画面 12:
```
[zk: localhost:2181(CONNECTED) 0] set /node01 world
```

画面 13:
```
WatchedEvent state:SyncConnected type:NodeDataChanged path:/node01
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
- PPT 标题：“发布/订阅机制”。
- 架构图：
  - 左侧：一个“主题”节点，通过箭头指向“订阅者”和“发布者”。
  - 右侧：一个“Zookeeper 集群”节点，通过“watch 机制”指向“Zookeeper 节点”。
  - “Zookeeper 节点”通过“create -e /tempnode”指向“node01”和“node02”节点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
