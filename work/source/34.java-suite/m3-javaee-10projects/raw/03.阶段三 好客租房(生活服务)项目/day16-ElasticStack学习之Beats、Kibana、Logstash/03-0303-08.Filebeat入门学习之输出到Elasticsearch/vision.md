# 画面线理解：08.Filebeat入门学习之输出到Elasticsearch

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\08.Filebeat入门学习之输出到Elasticsearch【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:14, 00:18, 00:22, 00:32, 00:37, 01:28, 01:44, 01:56, 02:13, 02:40, 02:46, 03:01, 03:17
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:19:19

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Filebeat 将日志文件输出到 Elasticsearch，并验证数据成功写入。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中 Filebeat 配置文件 `# haoke-log.yml` 的内容，其中包含 `filebeat.inputs`、`paths`、`tags`、`output.elasticsearch.hosts` 等配置项。
画面 2: 在终端中显示 Filebeat 读取日志文件 `a.log` 的内容，输出为 JSON 格式，包含 `@timestamp`、`@metadata`、`input`、`beat`、`source`、`message` 等字段。
画面 3: PDF 文档中 `# haoke-log.yml` 文件的配置内容，光标位于 `from: haoke-im` 行。
画面 4: PDF 文档中 `# haoke-log.yml` 文件的配置内容，下方显示 Filebeat 版本信息 `filebeat-6.5.4-2019.01.12`，并提示“docs: 1 (2)”。
画面 5: 终端中显示 Filebeat 停止时的详细日志，包含 `Stopping filebeat`、`Stopping Crawler`、`Stopping Input`、`Ending Registrar` 等信息。
画面 6: 终端中显示 Filebeat 停止时的详细日志，光标位于命令行提示符 `root@itcast01:filebeat-6.5.4-linux-x86_64#`。
画面 7: 终端中用户执行命令 `cp haoke.yml haoke-es.yml`，将原配置文件复制为新文件。
画面 8: 终端中用户进入 `logs` 目录并打开 `a.log` 文件，准备编辑。
画面 9: 在 Elasticsearch Head 界面中，显示集群状态为绿色，包含节点 `node01`、`node02`、`node03`，并展示多个窗口的截图。
画面 10: 终端中显示 Filebeat 重新启动后连接到 Elasticsearch 的日志，包括 `Connection to backoff(elasticsearch)`、`Connected to Elasticsearch v` 等信息。
画面 11: 在 Elasticsearch Head 界面中，用户点击“数据浏览”按钮，准备查看数据。
画面 12: 在 Elasticsearch Head 界面中，显示 `haoke` 索引的数据，包含 `@timestamp`、`beat`、`host`、`source`、`message`、`tags` 等字段。
画面 13: PDF 文档中 `# haoke-log.yml` 文件的配置内容，`output.elasticsearch.hosts` 行被高亮选中。
画面 14: PDF 文档中显示“查看数据：”字样，右侧弹出窗口展示数据文档，包含编号为 0、1、2 的文档。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
fields_under_root: false
setup.template.settings:
  index.number_of_shards: 3 #指定索引的分片数
output.elasticsearch: #指定ES的配置
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
```

画面 2:
```json
{
  "@timestamp": "2019-01-15T09:38:05.752Z",
  "@metadata": {
    "beat": "filebeat",
    "type": "doc",
    "version": "6.5.4"
  },
  "input": {
    "type": "log"
  },
  "from": "haoke-im",
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 8,
  "message": "111",
  "host": {
    "name": "itcast01"
  },
  "tags": [
    "web",
    "im"
  ]
}
```

画面 3:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
```

画面 4:
```yaml
# haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["haoke-im"]
    fields:
      from: haoke-im
fields_under_root: false
setup.template.settings:
  index.number_of_shards: 3 #指定索引的分片数
output.elasticsearch: #指定ES的配置
  hosts: ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
```

画面 5:
```
INFO beater/filebeat.go:449 Stopping filebeat
INFO crawler/crawler.go:139 Stopping Crawler
INFO input/input.go:149 Stopping Input
INFO input/input.go:167 Stopping ticker
INFO registrar/registrar.go:356 Ending Registrar
INFO [monitoring] log/log.go:152 Total non-zero metrics { "mo
nitoring": { "metrics": { "beat": { "cpu": { "ticks": "60", "time": { "ms": "68"}, "total": { "ticks": "120", "time": { "ms": "132"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "64"}, "total": { "ticks": "120", "time": { "ms": "64"}, "value": "120"}, "user": { "ms": "120"}, "system": { "ticks": "60", "time": { "ms": "6
