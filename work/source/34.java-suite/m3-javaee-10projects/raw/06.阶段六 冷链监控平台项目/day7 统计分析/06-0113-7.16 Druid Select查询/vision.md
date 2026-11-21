# 画面线理解：7.16 Druid Select查询

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.16 Druid Select查询_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 01:24, 01:26, 01:28, 01:32, 01:58, 02:10, 02:11, 02:28, 02:41, 02:42, 02:52, 03:39, 03:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:47:58

1) 这一组画面整体在讲什么（一句话）：
讲解 Druid 查询中的 Select 查询语句结构、参数说明及与 Scan 查询的区别，并通过 Postman 发送请求演示实际效果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节，列出 queryType、dataSource、filter、descending、dimensions、granularity、intervals、metrics、pagingSpec、context 等字段的描述及是否必填。
画面 2: 展示 Select 查询示例 JSON，包含 queryType、dataSource、descending、dimensions、granularity、intervals、pagingSpec 等字段。
画面 3: 展示 Select 查询示例 JSON，补充了 intervals 字段的具体时间范围值。
画面 4: 展示 Select 查询示例 JSON，完整包含 pagingSpec 字段，并在下方添加注意事项，说明 Select 查询在大数据量下可能内存溢出，建议使用 Scan 查询。
画面 5: 展示 Select 查询示例 JSON，光标位于 intervals 字段的时间范围值上。
画面 6: 在 Postman 中构造并发送一个 POST 请求，请求 URL 为 http://172.17.0.143:8888/druid/v2，请求体为 JSON 格式，包含 queryType、dataSource、query、sort、intervals 等字段。
画面 7: 在 Postman 中，光标位于请求体的 intervals 字段上，该字段值为 ["2015-09-12T00:00:00.000Z", "2015-09-12T00:00:00.000Z"]。
画面 8: 在 Postman 中，请求体中添加了 pagingSpec 字段，值为 {"pagingIdentifiers": {}, "threshold": 10}，并发送请求。
画面 9: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的开头部分，介绍 Scan 查询的特点。
画面 10: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的完整内容，说明 Scan 查询与 Select 查询的区别，以及 Scan 查询可以返回分页结果。
画面 11: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节的表格，列出字段名、描述、是否必填。
画面 12: 展示 Druid 官方文档中 1.7.6.3 Scan 查询章节的完整内容，包括 Scan 查询的定义、特点和使用场景。
画面 13: 展示 Druid 官方文档中 1.7.6.2 Select 查询章节的表格，列出字段名、描述、是否必填。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": false,
  "dimensions": [],
  "granularity": "hour",
  "intervals": [],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 2:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 3:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 4:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12/2015-09-13"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

画面 6:
{
  "queryType": "search",
  "dataSource": "wikipedia",
  "query": {
    "type": "inexact",
    "value": "an"
  },
  "sort": {
    "type": "lexicographic"
  },
  "intervals": [
    "2015-09-12T00:00:00.000Z/2015-09-12T00:00:00.000Z"
  ]
}

画面 8:
{
  "pagingSpec": {
    "pagingIdentifiers": {},
    "threshold": 10
  }
}

画面 12:
{
  "queryType": "select",
  "dataSource": "wikipedia",
  "descending": "false",
  "dimensions": [],
  "granularity": "hour",
  "intervals": [
    "2015-09-12T00:00:00.000Z/2015-09-12T00:00:00.000Z"
  ],
  "metrics": [],
  "pagingSpec": {
    "pagingIdentifiers": [],
    "threshold": 10
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
