# 画面线理解：09.Filebeat入门学习之工作原理

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\09.Filebeat入门学习之工作原理【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:23, 01:43, 01:50, 03:00, 03:35, 04:06, 04:26, 04:49, 04:56, 05:08, 05:21, 05:27, 05:49, 06:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:20:12

1) 这一组画面整体在讲什么（一句话）：
讲解 Filebeat 的工作原理、配置文件结构、启动命令及日志数据如何被采集并发送到 Elasticsearch。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中“2.6、Filebeat工作原理”章节，说明 Filebeat 由 prospector 和 harvester 两个主要组件组成，分别负责发现文件和读取单个文件内容。
画面2：终端显示文件 a.log 的内容，包含数字 456、789、111、222，用于演示日志数据。
画面3：终端显示文件 a.log 的内容，包含数字 456、789、111、222，用于演示日志数据。
画面4：PDF 文档中“2.6、Filebeat工作原理”章节，详细说明 harvester 和 prospector 的功能，以及 Filebeat 如何保存文件状态。
画面5：终端显示 Filebeat 的安装目录内容，列出多个配置文件，如 fields.yml、filebeat.reference.yml、filebeat.yml、haoke-es.yml、kibana.yml 等。
画面6：PDF 文档中“2.6、Filebeat工作原理”章节，展示 Filebeat 的启动命令和参数说明。
画面7：终端显示进入 data 目录，查看 registry 文件。
画面8：Elasticsearch Head 界面，显示索引 monitoring 中的文档，包含来自 Filebeat 的日志数据。
画面9：终端显示 Filebeat 停止后，日志信息显示“filebeat stopped”。
画面10：终端显示 Filebeat 启动并成功安装，输出配置路径、日志路径、Beat UUID 等信息。
画面11：终端显示 Filebeat 启动后，连接到 Elasticsearch，输出连接成功信息。
画面12：终端显示 Filebeat 发送的 JSON 数据，包含 message、prospector、input、from、host 等字段。
画面13：终端显示 Filebeat 发送的 JSON 数据，包含 timestamp、@metadata、offset 等字段。
画面14：PDF 文档中“2.6、Filebeat工作原理”章节，再次展示 Filebeat 的启动命令和参数说明。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
启动命令：
```
./filebeat -c haoke.yml "publish"
```
参数说明：
```
-c：指定配置文件
-d：输出debug信息
```
画面5：
```
total 35484
drwxr-xr-x 6 root root 4096 Jan 15 17:51 ./
drwxr-xr-x 4 root root 4096 Jan 15 17:51 ../
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .build.hash.txt
drwxr-xr-x 2 root root 4096 Jan 15 17:51 data/
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .cache
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .circleci
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .elastic
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .git
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .idea
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .m2
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .vscode
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarn
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2 root root 4096 Jan 15 17:51 .yarnrc
drwxr-xr-x 2
