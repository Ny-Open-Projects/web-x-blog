# 画面线理解：7.14 Druid聚合查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.14 Druid聚合查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:00, 03:02, 04:13, 04:44, 06:11, 06:57, 07:24, 07:37, 08:03, 08:31, 08:42, 09:33, 10:23, 10:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:46:37

1) 这一组画面整体在讲 Apache Druid 的聚合查询（Timeseries）、TopN 查询和 groupBy 查询的语法结构、参数说明及实际请求示例。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Druid 文档中 1.7.5.1 Timeseries 查询的字段说明表，包括 queryType、dataSource、granularity、intervals、filter、aggregations、postAggregations、context 等字段及其是否必需。
画面2：在 Postman 中构造一个 Timeseries 查询请求，JSON 请求体为：
{
  "queryType": "timeseries",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面3：Postman 中 Timeseries 查询的响应结果，包含两个时间戳和对应的 count 值。
画面4：展示 Druid 文档中 1.7.5.2 topN 查询的字段说明表，包括 queryType、dataSource、intervals、filter、aggregations、postAggregations、dimension、threshold、metric、context 等字段及其是否必需。
画面5：在文档页面中，鼠标悬停在 "metric" 字段上，显示其描述为“进行统计并排序的metric”。
画面6：在 Postman 中构造一个 topN 查询请求，JSON 请求体为：
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面7：在 Apache Druid 的 Web UI 中，执行 SQL 查询 "select * from wikipedia"，返回多行数据，包含 _time、channel、cityName、comment、count 等字段。
画面8：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Wikipedia:VandalismCidong'"，返回 3 行数据。
画面9：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Wikipedia:VandalismCidong'"，滚动查看第 2 页数据。
画面10：在 Druid Web UI 中，执行 SQL 查询 "select * from wikipedia where page = 'Anthony Mantial'"，返回 1 行数据。
画面11：在 Postman 中，显示一个查询响应，包含多个 count 和 page 字段，如 "count": 19, "page": "Fanie Pometta"。
画面12：在 Postman 中构造一个 lookup 查询请求，JSON 请求体为：
{
  "queryType": "lookup",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "granularity": "hour",
  "descending": true,
  "metric": "count",
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}
画面13：展示 Druid 文档中 1.7.5.3 groupBy 查询的字段说明表，包括 queryType、dataSource、dimensions、limitSpec、having、granularity、postAggregations、intervals、context 等字段及其是否必需。
画面14：在文档页面中，鼠标悬停在 "dimensions" 字段上，显示其描述为“进行GroupBy查询的维度集合”。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
{
  "queryType": "timeseries",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面3：
{
  "timestamp": "2015-09-12T00:00:00.000Z",
  "result": {
    "count": 266
  },
  "timestamp": "2015-09-12T01:00:00.000Z",
  "result": {
    "count": 133
  }
}

画面6：
{
  "queryType": "topN",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面11：
{
  "count": 19,
  "page": "Fanie Pometta",
  "count": 17,
  "page": "Wikipedia:In the news/Candidates",
  "count": 17,
  "page": "Wikipedia:Benefits for page protection",
  "count": 16,
  "page": "Wikipedia:Administrators intervention against vandalism",
  "count": 15,
  "page": "Anthony Mantial"
}

画面12：
{
  "queryType": "lookup",
  "dataSource": "wikipedia",
  "intervals": [
    "2015-09-12T00:00:00.000Z",
    "2015-09-12T01:00:00.000Z"
  ],
  "granularity": "hour",
  "descending": true,
  "metric": "count",
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1：标题为“1.7.5 聚合查询”，子标题“1.7.5.1 Timeseries”，下方为字段说明表。
画面4：标题为“1.7.5.2 topN”，下方为字段说明表。
画面13：标题为“1.7.5.3 groupBy”，下方为字段说明表。
画面14：标题为“1.7.5.3 groupBy”，下方为字段说明表，同时显示“1.7.6 搜索查询”标题。

5) 无。
