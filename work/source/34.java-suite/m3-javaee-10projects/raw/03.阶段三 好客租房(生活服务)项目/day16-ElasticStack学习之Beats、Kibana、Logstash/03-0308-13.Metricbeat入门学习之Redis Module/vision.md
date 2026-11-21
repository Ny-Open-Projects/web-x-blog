# 画面线理解：13.Metricbeat入门学习之Redis Module

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\13.Metricbeat入门学习之Redis Module【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:31, 01:01, 01:26, 02:25, 02:40, 02:59, 03:19, 03:29, 03:42, 04:00, 04:26, 04:43, 05:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:22:44

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Metricbeat 启用和配置 Redis 模块，并查看其采集到的指标数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 讲义中 Metricbeat 的 Module 配置部分，重点是 system 模块的配置示例。
画面2：在终端中执行命令 `./metricbeat modules list`，查看当前已启用的模块，显示 system 模块已启用。
画面3：终端中继续执行 `./metricbeat modules list`，确认 system 模块启用状态。
画面4：在终端中执行 `ls -l` 命令，列出 modules 目录下的所有文件，显示多个 .yaml.disabled 文件。
画面5：展示 PDF 讲义中 Redis Module 部分，介绍如何启用 Redis 模块并编辑配置文件。
画面6：在终端中执行 Metricbeat 启动命令，日志显示成功连接到 Elasticsearch。
画面7：在 Kibana 的 Discover 页面查看 metricbeat 采集到的指标数据，显示 system 模块采集的指标。
画面8：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 filesystem 指标。
画面9：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 process 指标。
画面10：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 network 指标。
画面11：在 Kibana 的 Discover 页面，指标数据中显示了 system 模块采集的 load 指标。
画面12：展示 PDF 讲义中 Redis Module 配置的 hosts 字段，包含三个 Redis 服务地址。
画面13：浏览器打开 Metricbeat 官方文档页面，页面为空白。
画面14：展示 PDF 讲义中 Kibana 部分，介绍如何使用 Elastic Stack 的窗口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
- drop_event.when.regex:
  system.filesystem.mount_point: '/sys/fs/cgroup/proc/devicet/host/lib/{1}/'
- module: system
  period: 15m
  metricssets:
    - uptime
- module: system
  period: 5m
  metricssets:
    - raid
    - raid.mount_point: '/'

画面5：
#启用redis module
./metricbeat modules enable redis
#修改redis module配置
vim modules.d/redis.yml
module: redis
metricssets:
  - info
  # - keyspace
period: 10s

画面12：
# Redis hosts
hosts: ["192.168.1.7:6379","192.168.1.7:6380","192.168.1.7:6381"]
# Network type to be used for redis connection. Default: tcp
#network: tcp
# Max number of concurrent connections. Default: 10
#maxconn: 10
# Redis AUTH password. Empty by default.
#password: foobared

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：标题为“3.4、Redis Module”，内容包括启用模块的命令和配置文件路径。
画面12：标题为“3.4、Redis Module”，内容包括 Redis hosts 配置和网络类型等参数。
画面14：标题为“4、Kibana”，内容包括 Elastic Stack 的窗口介绍。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
