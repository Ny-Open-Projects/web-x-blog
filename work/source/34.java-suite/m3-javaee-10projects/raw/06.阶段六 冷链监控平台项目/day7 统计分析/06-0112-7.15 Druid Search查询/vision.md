# 画面线理解：7.15 Druid Search查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.15 Druid Search查询_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:56, 03:39, 04:04, 04:09, 04:15, 04:35, 05:14, 05:20, 05:36, 06:16, 06:25, 06:37, 06:42, 07:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:47:23

1) 这一组画面整体在讲什么（一句话）：
讲解 Druid 查询语句中 Search 查询的参数结构、查询类型（如 insensitive_contains、fragment、contains、regex）及实际调用示例，并演示通过 Postman 发送请求和查看返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Druid 查询语句中 Search 查询的参数表，包括字段名、描述和是否必填。参数包括：queryType、dataSource、filter、limit、searchDimensions、granularity、query、intervals、sort、context。并说明 queryType 包括 insensitive_contains（非敏感包含）。

画面2：展示 queryType 的三种类型：fragment（片段匹配）、contains（包含）、regex（正则匹配），并给出每种类型的 JSON 语法示例。

画面3：展示一个完整的 Search 查询示例 JSON，包含 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段。

画面4：再次展示 queryType 的三种类型及其 JSON 示例，与画面2内容一致。

画面5：展示 queryType 的三种类型及其 JSON 示例，与画面2、4内容一致。

画面6：展示一个完整的 Search 查询示例 JSON，包含 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段，并在 intervals 字段中设置了时间范围。

画面7：在画面6的基础上，对 JSON 中的 queryType、dataSource、granularity、searchDimensions、query、sort、intervals 字段进行了高亮显示。

画面8：在 Postman 中发送一个 POST 请求，请求地址为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，内容为：
{
  "queryType": "count",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "query": {
    "type": "count"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ],
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面9：展示 Postman 返回的 JSON 响应结果，包含时间戳和结果数组，每个结果包含 dimension、value、count 字段。

画面10：展示文档中 1.7.6.2 Select 查询的标题和说明文字。

画面11：展示多个终端窗口，显示 Druid 服务启动日志，包括 coordinator、broker、historical 等组件的启动和退出信息。

画面12：在 Postman 中发送一个 POST 请求，请求地址为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，内容为：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面13：展示终端窗口中 Druid 服务启动日志，包括 coordinator、broker、historical 等组件的启动和退出信息。

画面14：展示文档中 1.7.6.2 Select 查询的标题和说明文字，与画面10内容一致。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
queryType
dataSource
filter
limit
searchDimensions
granularity
query
intervals
sort
context

参数query的type类型包括：
• insensitive_contains：非敏感包含

画面2：
• fragment：如果维度值的任何部分包含此搜索查询规范中指定的值，则无论默认情况如何，都会满足“匹配”
{
  "query": {
    "type": "fragment",
    "case_sensitive": false,
    "values": ["fragment1", "fragment2"]
  }
}

• contains：如果维度值的任何部分包含搜索查询规范中指定的值，则满足“匹配”。
{
  "query": {
    "type": "contains",
    "case_sensitive": true,
    "value": "some_value"
  }
}

• regex：正则匹配
{
  "query": {
    "type": "regex",
    "pattern": "some_pattern"
  }
}

画面3：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面6：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

画面8：
{
  "queryType": "count",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "query": {
    "type": "count"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ],
  "threshold": 10,
  "aggregations": [
    {
      "type": "count",
      "name": "count"
    }
  ]
}

画面12：
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "granularity": "hour",
  "searchDimensions": [
    "channel",
    "cityName"
  ],
  "query": {
    "type": "insensitive_contains",
    "value": "en"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000/2015-09-13T00:00:00.000"
  ]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“1.7.6.1 Search查询”，下方表格列出了 Search 查询的参数及其描述和必填属性。

画面10：PPT 标题为“1.7.6.2 Select查询”，下方文字说明“Select查询返回原始Druid行并支持分页。”

画面14：PPT 标题为“1.7.6.2 Select查询”，下方文字说明“Select查询返回原始Druid行并支持分页。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
