# 画面线理解：17即时查询-统计分析-使用hbase注意事项

- 阶段：08.阶段八 智慧学成项目
- 章节：05.第五章 智慧学成-即时查询
- 源文件：08.阶段八 智慧学成项目\05.第五章 智慧学成-即时查询\17即时查询-统计分析-使用hbase注意事项_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 00:50, 01:40, 02:18, 02:37, 03:11, 03:32, 03:54, 04:34, 05:22, 05:33, 05:42, 05:56, 06:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-29 00:04:52

1) 这一组画面整体在讲如何排查和解决 HBase 服务因 ZooKeeper 启动异常导致无法正常访问的问题。

2) 按时间顺序列出每张画面的要点：
画面 1: 在终端中执行 `hbase(main):006> scan 'LearningOnlineDetail'` 命令，显示 HBase 表数据，但提示 `NameError: undefined local variable or method 'a' for #<Object:0x42507640>`，表明 HBase 客户端可能未正确初始化。
画面 2: 执行 `hbase(main):006> exit` 退出 HBase Shell，然后执行 `docker-compose stop xc-online-hbase` 停止 HBase 容器。
画面 3: 执行 `docker-compose start xc-online-zk` 启动 ZooKeeper 容器，但终端提示 `docker-compose: command not found`。
画面 4: 浏览器访问 HBase Web 端口 `http://xc-online:60030`，显示“无法访问此网站”错误。
画面 5: 在 Typora 文档中，显示 HBase 使用注意事项，指出 HBase 严重依赖 ZooKeeper，若 ZooKeeper 未启动，HBase 无法正常工作，并展示“RegionServer is initializing”错误信息。
画面 6: 执行 `docker-compose stop xc-online-hbase` 停止 HBase，然后执行 `docker-compose start xc-online-hbase` 启动 HBase。
画面 7: 在 HBase 容器内执行 `ps aux` 查看进程，显示 HBase 服务未启动，然后执行 `cd $HBASE_HOME/bin` 进入 HBase bin 目录。
画面 8: 在 HBase bin 目录下执行 `ls` 查看脚本，然后执行 `./start-hbase.sh` 启动 HBase。
画面 9: 在 Typora 文档中，再次展示 HBase 使用注意事项，强调 HBase 依赖 ZooKeeper。
画面 10: 在 HBase bin 目录下执行 `./stop-hbase.sh` 停止 HBase，然后执行 `./start-hbase.sh` 启动 HBase。
画面 11: 浏览器访问 HBase Web 端口 `http://xc-online:60030`，显示“无法访问此网站”错误。
画面 12: 浏览器成功访问 HBase Web 端口 `http://xc-online:60030/rs-status`，显示 HBase RegionServer 的软件属性信息。
画面 13: 在 Typora 文档中，展示 HBase Web 端口 `http://xc-online:60030/rs-status` 的成功访问页面。
画面 14: 在 Typora 文档中，再次展示 HBase Web 端口 `http://xc-online:60030/rs-status` 的成功访问页面。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
hbase(main):006> scan 'LearningOnlineDetail'
COLUMN=learning_online_detail.course_id, TIMESTAMP=1576176882366, VALUE=15843a4e69b0d3a7401490.704b3f7e6b0d1d
COLUMN=learning_online_detail.course_id, TIMESTAMP=1576176882366, VALUE=15843a4e69b0d3a7401490.704b3f7e6b0d1d
...
```
画面 2:
```
hbase(main):006> exit
```
画面 3:
```
docker-compose stop xc-online-hbase
```
画面 6:
```
docker-compose stop xc-online-hbase
docker-compose start xc-online-hbase
```
画面 7:
```
ps aux
```
画面 8:
```
ls
./start-hbase.sh
```
画面 10:
```
./stop-hbase.sh
./start-hbase.sh
```
画面 12:
```
Software Attributes
Attribute Name Value Description
HBase Version 1.2.0-cdh14.0 revision=Unknown HBase version and revision
HBase Compiled Sat Jan 6 13:40:03 PST 2018, jenkins When HBase version was compiled and by whom
HBase Source Checksum 8ab06ca3829671d227c0971e565326226 HBase source MD5 checksum
Hadoop Version 2.6.0-cdh14.0 revision=0b1d933383c7980c18ba917ccaa106a17699 Hadoop version and revision
Hadoop Compiled 2018-01-06 21:24 GMT When Hadoop version was compiled and by whom
Hadoop Source Checksum 4adde4598a334aa91db2aa8d731f Hadoop source MD5 checksum
ZooKeeper Client Version 3.4.5-cdh14.0 revision=1 ZooKeeper client version and revision
ZooKeeper Client Compiled 01/06/2018 21:24 GMT When ZooKeeper client version was compiled
ZooKeeper Quorum xc-online-zk:2181 Addresses of all registered ZK servers
Coprocessors []
RS Start Time Thu Dec 12 19:02:56 UTC 2019 Date stamp of when this region server was started
HBase Master xc-online.hbase:60010 Address of HBase Master
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 5、9、13、14:
- 标题：3.2.4 使用hbase注意事项
- 内容：
  1. 访问hbase web端口（hbase web url: http://xc-online:60030）不能正常显示hbase相关信息，如下图所示：
     - The RegionServer is initializing!
  2. 代码操作hbase时抛socket超时异常
     - Exception in thread "main" org.apache.hadoop.hbase.client.RetriesExhaustedException: Failed after attempts=36, ...
  3. 解决方法：
     - ① 登陆hbase容器
       - docker exec -it xc-online-hbase bash
     - ② 切换到hbase bin目录
       - cd $HBASE_HOME/bin
     - ③ 执行运行命令
       - ./start-hbase.sh
     - ④ 访问hbase web http://xc-online:60030，如下图所示，说明hbase启动成功

5) 无
