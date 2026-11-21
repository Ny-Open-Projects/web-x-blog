# 画面线理解：7.12 Druid查询的聚合粒度

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.12 Druid查询的聚合粒度_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:43, 01:55, 02:04, 02:21, 02:25, 02:31, 02:54, 03:00, 03:19, 04:12, 04:19, 04:49, 04:55, 05:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:45:05

1) 这一组画面整体在讲什么（一句话）：
演示 Apache Druid 中聚合粒度（granularity）的概念，通过 Web UI 和 HTTP API 发起 groupBy 查询，并展示不同粒度下查询结果的变化。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容介绍聚合粒度的类型及示例查询。
画面 2: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 3: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 4: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 5: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 6: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容介绍聚合粒度的类型及示例查询。
画面 7: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 8: 显示 Druid 查询结果页面，查询语句为“select * from wikipedia”，结果包含多列数据，当前页为第 1 页，共 500 行。
画面 9: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容介绍聚合粒度的类型及示例查询。
画面 10: 显示 Postman 工具界面，正在构造一个 POST 请求，目标地址为 http://172.17.0.143:8888/druid/v2，Body 中包含一个 JSON 格式的查询请求。
画面 11: 显示 Postman 工具界面，正在构造一个 POST 请求，目标地址为 http://172.17.0.143:8888/druid/v2，Body 中包含一个 JSON 格式的查询请求。
画面 12: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容介绍聚合粒度的类型及示例查询。
画面 13: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容介绍聚合粒度的类型及示例查询。
画面 14: 显示技术文档页面，标题为“1.7.3 聚合粒度(granularity)”，内容展示按“day”粒度聚合后的查询结果示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1、6、9、12、13、14 中的代码：
{
  "queryType": "groupBy",
  "dataSource": "Wikipedia",
  "granularity": "hour",
  "dimensions": [
    "language"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ],
  "intervals": [
    "2018-01-01T00:00Z/2020-01-01T00:00Z"
  ]
}

画面 10、11 中的代码：
{
  "queryType": "groupBy",
  "dataSource": "Wikipedia",
  "granularity": "hour",
  "dimensions": [
    "language"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ],
  "intervals": [
    "2018-01-01T00:00Z/2020-01-01T00:00Z"
  ]
}

画面 14 中的代码：
{
  "version": "v1",
  "timestamp": "2015-09-12T22:00:00.000Z",
  "event": {
    "count": 1570,
    "language": null
  }
}

{
  "version": "v1",
  "timestamp": "2015-09-12T22:00:00.000Z",
  "event": {
    "count": 1,
    "language": "en"
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
