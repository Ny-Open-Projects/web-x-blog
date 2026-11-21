# 画面线理解：06.Filebeat入门学习之读取日志文件

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\06.Filebeat入门学习之读取日志文件【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:50, 01:05, 01:25, 01:39, 01:58, 02:23, 02:38, 02:47, 03:02, 03:16, 03:28, 03:34, 03:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:17:43

1) 这一组画面整体在讲如何配置并运行 Filebeat 来读取日志文件并输出到控制台。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。
画面2: 在终端中列出日志目录内容，进入 Filebeat 安装目录。
画面3: 在终端中编辑配置文件，显示 filebeat.inputs 和 output.console 配置。
画面4: 在终端中编辑配置文件，显示 filebeat.inputs 和 output.console 配置。
画面5: 在终端中列出 Filebeat 目录内容。
画面6: SSH 登录 Ubuntu 服务器，显示系统信息和终端提示符。
画面7: 在终端中切换到日志目录并列出文件。
画面8: 在终端中查看 Filebeat 启动日志，显示加载输入和启动成功。
画面9: 在终端中显示 Filebeat 输出的 JSON 格式日志。
画面10: 在终端中查看 a.log 文件内容，显示 "123"。
画面11: 在终端中列出日志目录内容。
画面12: 在终端中显示 Filebeat 输出的 JSON 格式日志，包含 "message": "456"。
画面13: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。
画面14: 展示 PDF 文档中 Filebeat 的配置文件示例，包含输入和主机信息。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```yaml
#配置读取文件项 haoke-log.yml
filebeat.inputs:
  - type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
  enable: true
```

画面3:
```yaml
filebeat.inputs:
  - type: log
  enabled: true
output.console:
  pretty: true
  enable: true
```

画面4:
```yaml
filebeat.inputs:
  - type: log
  enabled: true
output.console:
  pretty: true
  enable: true
```

画面8:
```
2019-01-15T17:08:58.137+0800 WARN beater/filebeat.go:374 Filebeat is unable to load the Ingest Node pipelines for the configured modules because the Elasticsearch output is not configured/enabled. If you have already loaded the Ingest Node pipelines or are using Logstash pipelines, you can ignore this warning.
2019-01-15T17:08:58.137+0800 INFO crawler/crawler.go:72 Loading Inputs: 1
2019-01-15T17:08:58.137+0800 INFO log/input.go:138 Configured paths: [/haoke/beats/logs]
2019-01-15T17:08:58.137+0800 INFO crawler/crawler.go:106 Loading and starting Inputs complete
2019-01-15T17:08:58.137+0800 INFO log/harvester.go:254 Harvester started for file: /haoke/beats/logs/a.log
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-15T17:08:58.137+0800 INFO log/log.go:144 Non-zero metrics in the last 30s
2019-01-
