# 画面线理解：23.Logstash入门学习之数据发送到Elasticsearch

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\23.Logstash入门学习之数据发送到Elasticsearch【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:55, 01:15, 01:41, 02:29, 02:57, 03:38, 04:00, 04:25, 05:02, 05:45, 06:20, 07:03, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:28:29

1) 这一组画面整体在讲什么（一句话）：
演示如何配置 Filebeat 将 Nginx 访问日志发送到 Logstash，再由 Logstash 处理后写入 Elasticsearch，并在 Kibana 中进行数据可视化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Filebeat 配置文件 `haoke-pipeline.conf` 的部分内容，用于定义输入源（port 5044）和过滤规则（grok）。
画面 2: 展示终端中 Logstash 启动后因错误（`[ERROR] org.logstash.Logstash`）而终止，提示用户检查配置文件。
画面 3: 展示 Elasticsearch Head 插件的空白页面，表示尚未进行任何操作。
画面 4: 展示 Elasticsearch Head 插件中集群状态为绿色（26 of 26），并列出多个索引及其状态，包括 `metricbeat-6.5.4`、`haoke`、`filebeat-6.5.4` 等。
画面 5: 展示 Elasticsearch Head 插件中索引列表，包含 `logstash-2019.01.15`、`metricbeat-6.5.4`、`haoke` 等索引及其文档数量。
画面 6: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Logstash 配置文件 `logstash.conf` 的部分内容，用于定义输出到 Elasticsearch 的 hosts。
画面 7: 展示 Kibana 的“Create index pattern”页面，正在创建索引模式。
画面 8: 展示 Kibana 的 Discover 页面，显示搜索结果，包含字段如 `@timestamp`、`beat.name`、`host.name`、`metricset.name`。
画面 9: 展示 Kibana 的 Discover 页面，时间范围设置为“Last 4 hours”，并显示数据。
画面 10: 展示 Kibana 的“Select visualization type”页面，提供多种可视化类型选择。
画面 11: 展示 Kibana 的“New Visualization”页面，配置了“Date Histogram”图表，X轴为 `@timestamp`，Y轴为 Count。
画面 12: 展示 Kibana 的“Save visualization”弹窗，标题为“New Visualization”。
画面 13: 展示 Kibana 的“New Visualization”页面，图表显示数据，鼠标悬停在柱状图上显示“Count 35 @timestamp per 5 minutes 00:05”。
画面 14: 展示 PDF 文档中关于“5.3.5、发送到Elasticsearch”的配置说明，其中包含 Filebeat 配置文件 `haoke-pipeline.conf` 的部分内容，用于定义输入源（port 5044）和过滤规则（grok）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
input {
  beats {
    port => "5044"
  }
}

filter {
  grok {
    patterns_dir => "/haoke/logstash-6.5.4/nginx-patterns"
    match => { "message" => "%{NGINX_ACCESS}" }
    remove_tag => ["_grokparsefailure"]
    add_tag => ["nginx_access"]
  }
}
```

画面 6:
```
output {
  elasticsearch {
    hosts => ["192.168.1.7:9200","192.168.1.7:9201","192.168.1.7:9202"]
  }
}
```

画面 14:
```
input {
  beats {
    port => "5044"
  }
}

filter {
  grok {
    patterns_dir => "/haoke/logstash-6.5.4/nginx-patterns"
    match => { "message" => "%{NGINX_ACCESS}" }
    remove_tag => ["_grokparsefailure"]
    add_tag => ["nginx_access"]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 6: PPT 标题为“5.3.5、发送到Elasticsearch”，内容包含 Logstash 配置文件 `logstash.conf` 的输出部分，其中 `hosts` 字段指向 Elasticsearch 的三个节点地址。
画面 7: Kibana 页面标题为“Create index pattern”，提示“Kibana uses index patterns to retrieve data from Elasticsearch indices for things like visualizations.”。
画面 8: Kibana Discover 页面显示搜索结果，包含字段如 `@timestamp`、`beat.name`、`host.name`、`metricset.name`。
画面 9: Kibana Discover 页面显示时间范围为“Last 4 hours”，并显示数据。
画面 10: Kibana 页面标题为“Select visualization type”，提供多种可视化类型选择。
画面 11: Kibana 页面标题为“New Visualization”，配置了“Date Histogram”图表，X轴为 `@timestamp`，Y轴为 Count。
画面 12: Kibana 页面标题为“Save visualization”，弹窗标题为“New Visualization”。
画面 13: Kibana 页面标题为“New Visualization”，图表显示数据，鼠标悬停在柱状图上显示“Count 35 @timestamp per 5 minutes 00:05”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
