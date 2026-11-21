# 21.cAdvisor

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\21.cAdvisor_【海量资源尽在 ubkz.com】.mp4
- 时长 4分54秒（音频 295s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好,接下来我们来讲解本章的第五个知识点叫C-Advancer那么什么是C-Advancer呢这个C-Advancer其实是谷歌出品的一个用于监控容器的这么一个运维工具它是一个监视工具那么它主要的作用就是用来监视我们容器的一些运营的数据比如说内存CPU的这些占用情况我们主要用来监控
[00:31] 那么这个监控呢这里头他只是负责监控那么他最终他最终要把数据存在哪里呢就是要存到刚才我们所说的这个influencedb那么接下来这个操作呢就是要这个下载他的镜像然后创建容器创建容器之后他就开始运行了他运行时候运行之后这时候他其实就已经开始去采集这些数据
[00:59] 采集了数据之后呢我们一会就可以看到这个数据被插入到influxdb这样的一个效果好咱们现在看一下第一个下载镜像我们这步就不用做了因为我已经提前把这个镜像下好了那么接下来我们直接执行第二句第二句我们先执行看有没有问题好现在已经成功了成功之后呢我们来看一下现在已经有这个已经在运行这个容器了
[01:29] 运行这个容器之后其实这里头这个句话挺长这里头其实大家只要关心哪个部分就行了关心这一部分我们要去这里有一个连接influenceddb这个部分连接influenceddb也就是说我们要将它的存储存储存储到哪存储到influenceddb里存储的名称这里指定为advancer数据库
[01:58] 这两句是大家需要关心的因为以后如果说大家以后用这个东西其实也就是需要改的部分改这个名称改这个名称其他这里有一个杠v这个其实就相当于我们来原来的杠v原来的杠v然后杠publish就相当于杠p就像钻孔运射只不过这里是另外一种写法而已这是我们说的
[02:28] 关于它的创建容器还有就是杠杠link表示是连接连接到另外一个容器这个零件另外一个容器influx svr就是刚才我们所创建的名称创建的influx db的容器的名称这两个这几个关键点大家知道就可以了好我们创建完成之后接下来我们可以通过8080端口去访问一下这个项目
[03:01] 本身它也提供了一个web界面的它也提供了web界面的然后它这里头可以去看到它所监视的一些数据我现在稍等好现在已经打开这个界面了已经打开这个界面了打开这个界面之后大家会看到这上有一些仪表是吧包括什么CPU内存等等这些仪表就是来用来监控的这是一个实时的数据
[03:32] 然后这里有些CPU的一个动态的图表随时在在给你展现出来一些动态图表那么它在运行之后运行之后其实它也在做一件事情就是它会去将运营数据插入到EVLOOKSDB里因为刚才我们所创建的语句其实就是要连接什么其实就在连接我们说的刚才EVLOOKSB这样一个容器并且把数据存到 CAdvancer里
[04:02] 那么咱们接下来看一下influencedb这个数据到底有没有采集进去还是切换到influencedb的页面然后咱们还执行这句话这时候大家会发现这些有这些数据了对吧这些数据就存在了这是我们说的关于数据当然你要去想查看具体的数据也是一样的比如说select from
[04:34] 去查看一些具体的数据也是可以的这是我们说的这个数据就查询出来了这是关于这个cadvance咱们就说到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 cAdvisor 和 InfluxDB 监控 Docker 容器和主机的性能数据，并通过 Grafana 可视化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示文档中“5 cAdvisor”章节，介绍 cAdvisor 是 Google 开源的用于监控 Docker 容器和主机的工具。
画面 2: 展示“5.2 cAdvisor 安装”章节，列出下载镜像和创建容器的 Docker 命令。
画面 3: 展示“5.2 cAdvisor 安装”章节，显示 cAdvisor 容器的 WEB 访问地址和 InfluxDB 的连接信息。
画面 4: 在终端中执行 `Docker run -d` 命令启动 cAdvisor 容器，显示容器 ID。
画面 5: 展示文档中“5.2 cAdvisor 安装”章节，显示创建容器的 Docker 命令。
画面 6: 展示文档中“4.3.2 创建用户并授权”章节，包含创建用户和授权的 SQL 语句。
画面 7: 展示文档中“4.3.1 创建数据库”章节，显示创建数据库的 SQL 语句和 InfluxDB 的访问地址。
画面 8: 浏览器打开 InfluxDB 的 Admin 界面。
画面 9: 在 cAdvisor 界面查看 Docker 容器的 CPU 和内存隔离配置。
画面 10: 在 cAdvisor 界面查看 CPU 使用率图表。
画面 11: 在 cAdvisor 界面查看错误率和文件系统使用情况图表。
画面 12: 展示文档中“6 Grafana”章节，介绍 Grafana 是一个可可视化面板的工具。
画面 13: 在 InfluxDB 的 measurements 页面查看 cAdvisor 采集的指标名称。
画面 14: 在 InfluxDB 的数据页面查看 cAdvisor 采集的容器和系统服务数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
Docker pull google/cadvisor
Docker run --volume=/var/lib/Docker:/var/lib/Docker:ro --volume=/var/run:/var/run --volume=/sys:/sys:ro --volume=/var/lib/Docker:/var/lib/Docker:ro --publish=8080:8080 --detach=true --link influxdb:influxdb --name=cadvisor google/cadvisor storage_driver=host-influxdb storage_driver_db=cadvisor storage_driver_host=influxdb:8086
```
画面 6:
```
CREATE DATABASE "cadvisor"
CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES
grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor
```
画面 7:
```
Docker pull tuturu/influxdb
Docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8086 \
--name influxsrv \
-tuturu/influxdb
```
画面 12:
```
Grafana 是一个可可视化面板（Dashboard），有非常漂亮的图表和下拉显示、功能齐全的度量仪表盘和图形编辑器，支持 Graphite、zabbix、InfluxDB、Prometheus 和 OpenTSDB 作为数据源。
```
画面 13:
```
name
cpu_usage_idle
cpu_usage_system
cpu_usage_total
cpu_usage_user
fs_limit
fs_usage
load_average
memory_usage
memory_working_set
rx_bytes
tx_bytes
tx_errors
rx_errors
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“5 cAdvisor”，子标题“5.1 什么是 cAdvisor”和“5.2 cAdvisor 安装”。
画面 3: PPT 标题为“5.2 cAdvisor 安装”，包含“（1）下载镜像”和“（2）创建容器”两个子项。
画面 6: PPT 标题为“4.3.2 创建用户并授权”，包含“创建用户”和“查看用户”两个子项。
画面 7: PPT 标题为“4.3.1 创建数据库”，包含“CREATE DATABASE "cadvisor"”和“WEB 访问页面地址”两个子项。
画面 12: PPT 标题为“6 Grafana”，子标题“6.1 什么是 Grafana”。
画面 13: InfluxDB 的 measurements 页面显示了 cAdvisor 采集的指标名称列表。
画面 14: InfluxDB 的数据页面显示了 cAdvisor 采集的容器和系统服务数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

