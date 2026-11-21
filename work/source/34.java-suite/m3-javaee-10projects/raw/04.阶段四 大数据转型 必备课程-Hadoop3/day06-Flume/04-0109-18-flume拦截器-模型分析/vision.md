# 画面线理解：18-flume拦截器-模型分析

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day06-Flume
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day06-Flume\18-flume拦截器-模型分析【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:03, 01:18, 02:04, 02:16, 03:41, 04:00, 04:24, 04:34, 07:03, 07:40, 08:12, 08:33, 08:39, 08:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:30:04

1) 这一组画面整体在讲什么（一句话）：
讲解Flume日志采集系统如何从A、B两台服务器收集access.log、nginx.log、web.log日志，并通过中间服务器C汇总后写入HDFS。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录和Flume案例一的场景描述，要求将A、B服务器的日志采集汇总到服务器C，再写入HDFS，同时列出具体日志路径。
画面2：展示数据流向图，A、B服务器的/data目录下的access.log、nginx.log、web.log通过“数据流入”指向“服务器C”的“汇总”模块。
画面3：在画面2基础上，将“汇总”模块指向“hadoop集群”，并标注“数据存放格式”为“/source/logs/access/20160101/”、“/source/logs/nginx/20160101/”、“/source/logs/web/20160101/”。
画面4：在画面3基础上，将“数据存放格式”中的年份从“20160101”改为“20160101”，并补充“/source/logs/web/20160101/”。
画面5：展示Flume架构图，A、B服务器的access.log、nginx.log、web.log通过“static interceptor”、“memory channel”、“avro sink”发送到服务器C的“avro source”。
画面6：在画面5基础上，对服务器B的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面7：在画面5基础上，将服务器C的“avro source”指向“memory channel”，再由“memory channel”指向“hdfs sink”。
画面8：在画面5基础上，对服务器A的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面9：在画面5基础上，对服务器A的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面10：在画面5基础上，对服务器A的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面11：在画面5基础上，对服务器B的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面12：在画面5基础上，对服务器B的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。
画面13：在画面5基础上，对服务器C的“avro source”指向“memory channel”，再由“memory channel”指向“hdfs sink”。
画面14：在画面5基础上，对服务器A的“access.log”和“nginx.log”添加“hello”和“type”字段，用于区分日志类型。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
1 /source/logs/access/20180101/**
2 /source/logs/nginx/20180101/**
3 /source/logs/web/20180101/**

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
- 服务器A的/data目录下的access.log、nginx.log、web.log → 数据流入 → 服务器C的“汇总”模块
- 服务器B的/data目录下的access.log、nginx.log、web.log → 数据流入 → 服务器C的“汇总”模块
- 服务器C的“汇总”模块 → 指向“hadoop集群”
- “数据存放格式”：
  - /source/logs/access/20160101/
  - /source/logs/nginx/20160101/
  - /source/logs/web/20160101/

画面5：
- 服务器A的access.log、nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source
- 服务器B的access.log、nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source

画面7：
- 服务器C的avro source → memory channel → hdfs sink

画面14：
- 服务器A的access.log、nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source
- 服务器B的access.log、nginx.log、web.log → static interceptor → memory channel → avro sink → 服务器C的avro source
