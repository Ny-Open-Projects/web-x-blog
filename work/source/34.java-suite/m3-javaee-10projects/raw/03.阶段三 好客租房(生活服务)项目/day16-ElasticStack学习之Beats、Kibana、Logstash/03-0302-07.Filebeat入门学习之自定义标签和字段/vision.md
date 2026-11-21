# 画面线理解：07.Filebeat入门学习之自定义标签和字段

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\07.Filebeat入门学习之自定义标签和字段【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 01:12, 01:33, 01:57, 02:17, 02:59, 03:22, 03:41, 04:06, 04:40, 04:58, 05:18, 05:30, 06:05
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:18:30

1) 这一组画面整体在讲如何配置 Filebeat 的自定义字段，包括在配置文件中添加 tags 和 fields，并演示其效果。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PDF 文档中关于 Filebeat 配置的说明，包含一个示例配置片段。
画面2: 展示 Filebeat 启动日志，显示其加载配置并开始读取日志。
画面3: 展示一个包含自定义字段的 Filebeat 配置片段，其中 offset 设置为 123。
画面4: 展示 Filebeat 停止的日志，显示其已停止读取日志。
画面5: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields 设置为 "web" 和 "im"。
画面6: 展示在终端中使用 echo 命令向 a.log 文件写入内容。
画面7: 展示在终端中再次使用 echo 命令向 a.log 文件写入内容。
画面8: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields 设置为 "haoke-im" 和 "heima"。
画面9: 展示在终端中编辑名为 haoke.yml 的配置文件。
画面10: 展示 Filebeat 启动日志，显示其加载配置并开始读取日志。
画面11: 展示一个包含自定义字段的 Filebeat 配置片段，其中 fields_under_root 设置为 false。
画面12: 展示一个包含自定义字段的 Filebeat 配置片段，其中 tags 设置为 "web" 和 "im"。
画面13: 展示一个包含自定义字段的 Filebeat 配置片段，其中 tags 设置为 "web" 和 "im"。
画面14: 展示 PDF 文档中关于 Filebeat 配置的说明，包含一个示例配置片段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "version": "6.5.4",
    "name": "itcast01",
    "hostname": "itcast01"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/hanke/beats/logs/a.log",
  "offset": 0,
  "message": "world"
}
```

画面3:
```json
{
  "type": "doc",
  "version": "6.5.4",
  "input": {
    "type": "log"
  },
  "prospector": {
    "type": "Log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": "123",
  "message": "world"
}
```

画面5:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
output.console:
  pretty: true
  enable: true
```

画面6:
```bash
root@itcast01:logs# vim a.log
root@itcast01:logs# echo "123" > a.log
root@itcast01:logs#
```

画面7:
```bash
root@itcast01:logs# vim a.log
root@itcast01:logs# echo "456" > a.log
root@itcast01:logs#
```

画面8:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 4,
  "message": "789",
  "prospector": {
    "type": "log"
  },
  "fields": {
    "from": "haoke-im",
    "itecast": "heima"
  }
}
```

画面9:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
output.console:
  pretty: true
  enable: true
```

画面10:
```json
{
  "input": {
    "type": "log"
  },
  "beat": {
    "name": "itcast01",
    "hostname": "itcast01",
    "version": "6.5.4"
  },
  "host": {
    "name": "itcast01"
  },
  "source": "/haoke/beats/logs/a.log",
  "offset": 0,
  "message": "world"
}
```

画面11:
```yaml
filebeat.inputs:
  type: log
  enabled: true
  paths:
    - /haoke/beats/logs/*.log
  tags: ["web", "im"]
  fields:
    from: haoke-im
    itecast: heima
  fields_under_root: false
output.console:
  pretty: true
  enable: true
```

画面12:
```json
{
  "input": {
    "type": "log",
    "from": "haoke-im"
  },
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
  ],
  "prospector": {
    "type": "log"
  },
  "itcast": "heima"
}
```

画面13:
```json
{
  "input": {
    "type": "log",
    "from": "haoke-im"
  },
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
  ],
  "prospector": {
    "type": "log"
  },
  "itcast": "heima"
}
```

画面14:
```yaml
#配置读取文件 haoke-log.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/beats/logs/*.log
    tags: ["web", "im"]  #添加自定义tag，便于后续的处理
    fields:
      from: haoke-im
      itecast: heima
setup.template.settings:
  index.number_of_shards: 3
output.console:
  pretty: true
  enable: true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
