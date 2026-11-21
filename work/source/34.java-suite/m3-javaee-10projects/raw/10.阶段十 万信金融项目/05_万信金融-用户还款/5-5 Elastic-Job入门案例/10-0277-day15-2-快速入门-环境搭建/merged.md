# day15-2-快速入门-环境搭建

- 阶段：10.阶段十 万信金融项目
- 章节：05_万信金融-用户还款/5-5 Elastic-Job入门案例
- 源文件：10.阶段十 万信金融项目\05_万信金融-用户还款\5-5 Elastic-Job入门案例\day15-2-快速入门-环境搭建_【海量资源尽在 666java.com】.mp4
- 时长 4分46秒（音频 287s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好学完这个一些重要概念和Columbia之后呢咱接下来就来一个什么呀Elastic Gun Job的快速入门通过这个入门案例呢我们整体上就能掌握Elastic Gun Job它的一个基本使用那咱这个入门案例是这个样子的业务呢非常简单就是在分布式架构下通过Elastic Job实现
[00:28] 分片查询数据的定时任务其实这个业务很简单就是查询数据库里边的某个表哪个表呢咱一会再说反正就是查询一下数据但是呢我们这个业务呢给它做成了什么呀定时任务比如说我们每隔多长时间对不对查验次而且呢我们是分布式架构我们要进行什么呀分片对吧分片的概念你还有印象吗咱前面是不是刚在重要概念这边讲过分片是不是其实我们模拟的就是这个意思
[00:59] 我们可以搞上两台服务器三台服务器对吧然后去执行这个什么呀这个定时任务分分工嘛我们当然说分片就是分工嘛这是我们这个入门案例它最终要实现什么样的一个效果这个大家先心里有数那接下来咱说一说这个环境搭建环境这一块大家注意GDKB是1.7以上的Maven是304以上的Zookeeper3.4.6以上的这些呢我就不再过多说了
[01:29] 然后呢我们这里边呢主要是不是依赖这个Zookeeper对吧咱前面也说过了嘛这个Elastic-Job它内部要用到什么呀或者依赖什么呀Zookeeper那Zookeeper到底是干啥呢我们前面提到我这呢给您做一个对比咱前面是不是学过Eureka是吧Eureka干啥你应该知道吧是不是一个微服务的注册中心发现中心对不对那么Zookeeper其实跟Eureka的作用非常非常相似它也是用来进行微服务注册和什么呀
[02:00] 管理的大家知道你像我们P2P项目是不是有一堆的微服务是不是我们每一个微服务是不是还可以搞成什么样集群那这么多的这个微服务将来是不是得通过谁啊优瑞卡或者说这个谁啊Zookeeper进行注册进行统一的一个什么样管理这个其实就是Zookeeper那我们这里边的其实主要是利用Zookeeper的那个什么样选举机制咱在哪提过这个事在前面对吧我们提到过这个
[02:32] 这Zookeeper会保证多台服务器选出来一个leader对不对就是领导领导干啥呢他负责进行什么呀分辨就是你多台服务器当中得有一个服务器负责进行这个什么呀分工就这个意思这是ZookeeperZookeeper的话你需要去官网上进行下载然后一解压就完事了不需要单独的怎么进行安装然后呢你下载完之后呢需要注意它有个配置文件这个它的configure目录下边呢它的
[03:02] 提供的配置我念是这个样子就是路啊simple.cfg就是一个例子对不对那你只需要把这节给他删掉就行了啊这只是一个样例啊你给他删掉改成这个名字哎就ok了里边的配置我念里边的内容你都不用动不用管他啊然后呢去闭目录下啊运行一下他就ok了来我找一找就这个啊他原来不叫这名了他原来是叫这名吗是不是应该改成这个名字就录点cfg就行
[03:33] 然后呢改完之后你直接就去b目录下边这个运行谁啊运行这个ZK server.cmd双击一下它就跑起来你看这个中间有没有报错啊这是ZooKeeper然后呢我们刚才说我们这个业务是不是查询数据吗那我们用哪个数据库哪个表呢大家看一看啊我们用的是跟当初就是很早了啊我们是不是讲过这个mybethes plus有印象吗在讲这个案例的时候呢我们用到一个数据库叫MP大家看这
[04:05] 那么它里边呢有一个表啊叫TB下载线什么U的我们准备用这个表啊来进行什么操作对查询操作那我最终想要干什么呀第一个我要干什么定时查询第二个呢我要进行什么呀分片查询比如说我可以分成两台服务器一台服务器查135一台服务器查246当然你也可以整成什么三台服务器都可以就是分片这我要最重要的这个效果
[04:35] 这是大家知道我们这个查的是哪个库哪个表里面的数据吧这是咱这个入门案例的一些环境上的这个要求我们先跟大家说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Elastic-Job 的环境搭建，包括版本要求、Zookeeper 安装与配置、以及数据库准备。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PPT 第 1 页，标题为“2.1 环境搭建”，内容包括版本要求（JDK 1.7+、Maven 3.0.4+、Zookeeper 3.4.6+）、Zookeeper 安装与运行说明（类比 Eureka）、数据库说明（使用 mybatis-plus 入门案例的数据库 mp，表为 tb_user），并附带一个数据库表结构截图。
画面2: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。
画面3: PPT 第 2 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面4: PPT 第 4 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面5: PPT 第 3 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面6: PPT 第 2 页，标题为“2. Elastic-Job 快速入门”，副标题“在分布式架构下，通过 Elastic-Job 实现分片查询数据的定时任务”，并展示“2.1 环境搭建”部分，其中“版本要求”中“JDK要求1.7以上版本”被高亮。
画面7: 文件资源管理器，显示“ZooKeeper-3.4.9”文件夹内容，其中“conf”文件夹被选中。
画面8: 文件资源管理器，显示“ZooKeeper-3.4.9”文件夹下的“conf”子文件夹内容，其中“zoo.cfg”文件被选中，右侧预览显示“zoo.cfg”文件内容。
画面9: 文件资源管理器，显示“ZooKeeper-3.4.9”文件夹下的“bin”子文件夹内容，其中“zkServer.cmd”文件被选中。
画面10: 文件资源管理器，显示“ZooKeeper-3.4.9”文件夹下的“bin”子文件夹内容，其中“zkServer.cmd”文件被选中，右侧预览显示“zkServer.cmd”文件内容。
画面11: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。
画面12: SQLyog 数据库管理工具界面，显示“p2y_repayment”数据库的表结构，其中“p2y_payment”表被选中。
画面13: PPT 第 6 页，标题为“2.2 入门案例”，内容包括“1.新建maven工程”，并展示“2.1 环境搭建”部分。
画面14: PPT 第 1 页，内容与画面1相同，但页面滚动至“2.1 环境搭建”标题下方。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面8: zoo.cfg 文件内容：
```
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial synchronization phase can take
initLimit=10
# The number of ticks that can pass between sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
dataDir=D:/ZooKeeper-3.4.9/data
# the port at which the clients will connect
clientPort=2181
```
画面10: zkServer.cmd 文件内容：
```
@echo off
setlocal enabledelayedexpansion
set ZK_HOME=%~dp0
set ZK_CONF=%ZK_HOME%conf
set ZK_LOG=%ZK_HOME%logs
set ZK_DATA=%ZK_HOME%data
set ZK_PORT=2181
set ZK_TICK_TIME=2000
set ZK_INIT_LIMIT=10
set ZK_SYNC_LIMIT=5
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%ZK_LOG%
set ZK_CONF_DIR=%ZK_CONF%
set ZK_PORT=%ZK_PORT%
set ZK_TICK_TIME=%ZK_TICK_TIME%
set ZK_INIT_LIMIT=%ZK_INIT_LIMIT%
set ZK_SYNC_LIMIT=%ZK_SYNC_LIMIT%
set ZK_DATA_DIR=%ZK_DATA%
set ZK_LOG_DIR=%Z

