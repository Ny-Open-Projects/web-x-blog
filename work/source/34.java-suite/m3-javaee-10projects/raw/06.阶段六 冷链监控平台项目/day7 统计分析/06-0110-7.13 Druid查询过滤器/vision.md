# 画面线理解：7.13 Druid查询过滤器

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.13 Druid查询过滤器_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 01:03, 01:26, 02:22, 02:31, 02:51, 03:07, 03:29, 03:51, 04:03, 04:44, 05:29, 05:33, 05:36, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:45:54

1) 这一组画面整体在讲 Druid 查询中的过滤器（filter）类型及其 JSON 格式定义，包括 Selector、正则表达式、逻辑表达式、IN、范围、JavaScript 和 Search 过滤器。

2) 按时间顺序列出每张画面的要点：
画面 1:
- 标题：1.7.4.1 Selector 过滤器
- 内容：介绍 Selector 过滤器，等价于 WHERE <dimension_string> = '<dimension_value_string>'，并给出 JSON 格式示例：
  {
  "filter": {
    "type": "selector",
    "dimension": <dimension_string>,
    "value": <dimension_value_string>
  }
  }

画面 2:
- 标题：1.7.4.2 正则表达式过滤器
- 内容：介绍正则表达式过滤器，等价于 Selector 过滤器，但使用正则表达式，给出 JSON 格式示例：
  {
  "filter": {
    "type": "regex",
    "dimension": <dimension_string>,
    "pattern": <pattern_string>
  }
  }

画面 3:
- 标题：1.7.4.3 逻辑表达式过滤器
- 内容：介绍逻辑表达式过滤器，包含 AND、OR、NOT 三种类型，给出 JSON 格式示例：
  AND:
  {
  "filter": {
    "type": "and",
    "fields": [<filter>, <filter>, ...]
  }
  }
  OR:
  {
  "filter": {
    "type": "or",
    "field": <filter>
  }
  }
  NOT:
  {
  "filter": {
    "type": "not",
    "field": <filter>
  }
  }

画面 4:
- 标题：1.7.4.4 IN 过滤器
- 内容：介绍 IN 过滤器，等价于 SQL 中的 IN 语句，给出 JSON 格式示例：
  {
  "type": "in",
  "dimension": "outlaw",
  "values": ["good", "bad", "ugly"]
  }

画面 5:
- 标题：1.7.4.3 逻辑表达式过滤器（AND/OR/NOT）
- 内容：重复展示逻辑表达式过滤器的 JSON 格式示例。

画面 6:
- 标题：1.7.4.3 逻辑表达式过滤器（AND/OR/NOT）
- 内容：重复展示逻辑表达式过滤器的 JSON 格式示例。

画面 7:
- 标题：1.7.4.5 范围过滤器
- 内容：介绍范围过滤器，给出 JSON 格式示例：
  {
  "type": "bound",
  "dimension": "age",
  "lower": "21",
  "upper": "31",
  "ordering": "numeric"
  }

画面 8:
- 标题：1.7.4.5 范围过滤器
- 内容：重复展示范围过滤器的 JSON 格式示例。

画面 9:
- 标题：1.7.4.6 JavaScript 过滤器
- 内容：介绍 JavaScript 过滤器，给出 JSON 格式示例：
  {
  "type": "javascript",
  "dimension": <dimension_string>,
  "function": "function(value) { ... }"
  }

画面 10:
- 标题：1.7.4.7 Search 过滤器
- 内容：介绍 Search 过滤器，给出 JSON 格式示例：
  {
  "filter": {
    "type": "search",
    "dimension": "product",
    "query": {
      "type": "insensitive_contains",
      "value": "foo"
    }
  }
  }

画面 11:
- 标题：1.7.4.7 Search 过滤器
- 内容：重复展示 Search 过滤器的 JSON 格式示例。

画面 12:
- 标题：1.7.4.1 Selector 过滤器
- 内容：重复展示 Selector 过滤器的 JSON 格式示例。

画面 13:
- 标题：1.7.4.5 范围过滤器
- 内容：重复展示范围过滤器的 JSON 格式示例。

画面 14:
- 标题：1.7.5 聚合查询
- 内容：介绍 Timeseries 聚合查询，给出查询参数表：
  | 字段名     | 描述                         | 必须 |
  |------------|------------------------------|------|
  | queryType  | 查询类型，这里填写timeseries查询 | 是   |
  | dataSource | 要查询的数据源               | 是   |
  | descending | 是否降序                     | 否   |
  | granularity | 查询进行聚合的时间粒度       | 是   |
  | intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
{
"filter": {
"type": "selector",
"dimension": <dimension_string>,
"value": <dimension_value_string>
}
}

画面 2:
{
"filter": {
"type": "regex",
"dimension": <dimension_string>,
"pattern": <pattern_string>
}
}

画面 3:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 4:
{
"type": "in",
"dimension": "outlaw",
"values": ["good", "bad", "ugly"]
}

画面 5:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 6:
AND:
{
"filter": {
"type": "and",
"fields": [<filter>, <filter>, ...]
}
}
OR:
{
"filter": {
"type": "or",
"field": <filter>
}
}
NOT:
{
"filter": {
"type": "not",
"field": <filter>
}
}

画面 7:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 8:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 9:
{
"type": "javascript",
"dimension": <dimension_string>,
"function": "function(value) { ... }"
}

画面 10:
{
"filter": {
"type": "search",
"dimension": "product",
"query": {
"type": "insensitive_contains",
"value": "foo"
}
}
}

画面 11:
{
"filter": {
"type": "search",
"dimension": "product",
"query": {
"type": "insensitive_contains",
"value": "foo"
}
}
}

画面 12:
{
"filter": {
"type": "selector",
"dimension": <dimension_string>,
"value": <dimension_value_string>
}
}

画面 13:
{
"type": "bound",
"dimension": "age",
"lower": "21",
"upper": "31",
"ordering": "numeric"
}

画面 14:
| 字段名     | 描述                         | 必须 |
|------------|------------------------------|------|
| queryType  | 查询类型，这里填写timeseries查询 | 是   |
| dataSource | 要查询的数据源               | 是   |
| descending | 是否降序                     | 否   |
| granularity | 查询进行聚合的时间粒度       | 是   |
| intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 14:
- 标题：1.7.5 聚合查询
- 子标题：1.7.5.1 Timeseries
- 表格数据：
  | 字段名     | 描述                         | 必须 |
  |------------|------------------------------|------|
  | queryType  | 查询类型，这里填写timeseries查询 | 是   |
  | dataSource | 要查询的数据源               | 是   |
  | descending | 是否降序                     | 否   |
  | granularity | 查询进行聚合的时间粒度       | 是   |
  | intervals  | 查询的时间范围，默认是ISO-8601格式 | 是   |

5) 无。
