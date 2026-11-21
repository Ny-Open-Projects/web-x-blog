# 画面线理解：day09-18-标的快速检索-logstash测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-18-标的快速检索-logstash测试_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:46, 01:16, 01:49, 02:26, 03:18, 04:24, 05:17, 05:35, 06:14, 07:07, 07:37, 07:56, 08:50, 09:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 07:14:15

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Logstash 将 MySQL 数据库中的项目表数据同步到 Elasticsearch，并展示数据在两个系统中的状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，其中包含“4.4.3 测试”小节，说明启动Logstash并修改jvm.options文件以调整堆内存。
画面2：展示Elasticsearch 7.3.1安装目录结构，包含bin、config、data等文件夹。
画面3：在Elasticsearch的bin目录下，通过命令行启动服务，显示加载了多个插件。
画面4：在Logstash的bin目录下，通过命令行启动服务，显示加载了多个插件。
画面5：在Windows PowerShell中，执行Logstash启动命令：.\logstash.bat -f ..\config\mysql-es.conf。
画面6：再次展示课程PPT内容，强调修改jvm.options文件以调整堆内存。
画面7：在PowerShell中，展示Logstash的SQL查询语句，用于从MySQL中读取数据。
画面8：在PowerShell中，执行SQL查询语句，将数据写入Logstash的管道。
画面9：在Solving Professional 64软件中，展示MySQL数据库中project表的数据。
画面10：在Elasticsearch的Kibana界面中，展示wanxing2p_project索引的状态，显示有11个文档。
画面11：在PowerShell中，展示Logstash的SQL查询语句，用于从MySQL中读取数据。
画面12：在Elasticsearch的Kibana界面中，展示wanxing2p_project索引中的数据。
画面13：展示课程PPT内容，其中包含Logstash的配置文件模板，用于定义数据同步规则。
画面14：在Solving Professional 64软件中，展示MySQL数据库中project表的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
4.4.3 测试
1. 找到案件中的"标的"信息表,测试.sql并执行
2. 启动ES和head插件,然后在Logstash的bin目录中执行如下命令启动Logstash
.\logstash.bat -f ..\config\mysql-es.conf
3. 如果遇到内存溢出的报错,修改config目录下的jvm.options文件,把1g的默认内存改小:
```
画面2：
```
bin
config
data
jdk
logs
modules
plugins
LICENSE.txt
NOTICE.txt
README.txt
```
画面3：
```
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-common]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-geotools]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-geoip]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-user-agent]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-mutate]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T15:54:10,700][INFO ][o.e.p.PluginsService] loaded module [ingest-join]
[2019-08-29T1
