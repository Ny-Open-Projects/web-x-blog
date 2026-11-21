# 画面线理解：16.Kibana入门学习之数据探索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\16.Kibana入门学习之数据探索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:40, 00:59, 01:17, 01:33, 01:47, 02:22, 02:51, 03:12, 03:25, 03:42, 03:56, 04:03, 04:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:24:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Kibana 中创建索引模式并进行数据探索，包括使用 Dev Tools 执行查询、查看指标数据和可视化图表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 讲义中关于 Kibana 功能说明的章节，右侧是 Kibana 界面截图，标注了主要功能模块：Discover（数据探索）、Visualize（可视化）、Dashboard（仪表盘）、Timelion（时序控件）、Canvas（画布）、Machine Learning（机器学习）。
画面 2: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示需要创建索引模式以可视化数据，页面正在“Checking for Elasticsearch data”。
画面 3: PDF 讲义中关于“4.4、数据探索”的章节，右侧是 Kibana 菜单截图，标注了功能模块：Dashboard（仪表盘）、Timelion（时序控件）、Canvas（画布）、Machine Learning（机器学习）、Infrastructure（基本信息）、Logs（日志数据展现）、APM（性能监控）、Dev Tools（开发者工具）、Monitoring（监控）、Management（管理）。
画面 4: Kibana Dev Tools 控制台，执行了 GET /_search 查询，返回结果中包含索引信息，如 "_index": "kibana_1", "_type": "doc", "space": { "name": "Default", "color": "#000000" }。
画面 5: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示需要创建索引模式以可视化数据，页面正在“Checking for Elasticsearch data”。
画面 6: Kibana 界面，位于“Management”页面，显示了 Elasticsearch 和 Kibana 的管理选项，包括 Index Management、Rollup jobs、License Management、Index Patterns、Saved Objects、Spaces、Reporting。
画面 7: Kibana 界面，位于“Management / Kibana”下的“Create index pattern”页面，提示“Create index pattern”，并显示“Creating index pattern...”。
画面 8: Kibana Discover 页面，选择“metricbeat*”索引，点击“Refresh”按钮，页面显示“Searching”状态。
画面 9: Kibana Discover 页面，显示“metricbeat*”索引的数据，包含时间戳和 source 字段内容。
画面 10: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现柱状图，显示按时间分组的计数。
画面 11: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现列表，包含字段如 network、load、process、info、cpu。
画面 12: Elasticsearch Head 界面，显示集群中各个节点（node01, node02, node03）的索引分布情况，每个节点对应不同的索引。
画面 13: Kibana Discover 页面，显示“metricbeat*”索引的数据，右侧出现柱状图，显示按时间分组的计数。
画面 14: PDF 讲义中关于“4.5、Metricbeat 仪表盘”的章节，右侧是 Kibana Discover 页面截图，显示了数据和图表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```json
{
  "took": 35,
  "timed_out": false,
  "_shards": {
    "total": 12,
    "successful": 13,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 50822,
    "max_score": 2.0,
    "hits": [
      {
        "_index": "kibana_1",
        "_type": "doc",
        "_source": {
          "space": {
            "name": "Default",
            "color": "#000000",
            "reserved": true
          },
          "type": "space",
          "updated_at": "2019-01-15T14:07:25.532Z"
        },
        "_index": "kibana_1",
        "_type": "doc",
        "_id": "config6.5.4"
      }
    ]
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“4.3、功能说明”，右侧截图标注了 Kibana 的功能模块。
画面 3: PPT 标题为“4.4、数据探索”，右侧截图标注了 Kibana 的功能模块。
画面 14: PPT 标题为“4.5、Metricbeat 仪表盘”，右侧截图显示了 Kibana Discover 页面。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
