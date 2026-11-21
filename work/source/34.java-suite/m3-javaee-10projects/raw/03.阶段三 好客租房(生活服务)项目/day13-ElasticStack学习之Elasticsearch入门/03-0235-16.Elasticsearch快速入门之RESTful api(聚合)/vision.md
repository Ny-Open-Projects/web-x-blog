# 画面线理解：16.Elasticsearch快速入门之RESTful api（聚合）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\16.Elasticsearch快速入门之RESTful api（聚合）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:36, 00:41, 00:48, 01:03, 01:36, 01:50, 02:02, 02:14, 02:24, 02:44, 02:53, 03:43, 03:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:33:40

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中使用聚合查询（aggs）和更新文档数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PDF 文档中关于 Elasticsearch 聚合功能的说明，包含一个被高亮的 XML 片段 `<em>张</em><em>三</em>`。
画面2：PDF 文档中关于 Elasticsearch 聚合功能的说明，展示了一个被模糊处理的 JSON 请求体。
画面3：Postman 中构建的 POST 请求，目标地址为 `http://172.16.55.185:9200/haoke/user/_search`，请求体为 JSON 格式，包含聚合配置。
画面4：Postman 中的请求体内容，与画面3相同，但高亮了 `“field”: “age”`。
画面5：Postman 中的响应结果，显示了聚合查询的返回数据，包含多个 `key` 和 `doc_count`。
画面6：PDF 文档中关于 Elasticsearch 更新数据的说明，包含一个 PUT 请求示例。
画面7：PDF 文档中关于删除旧文档的说明，包含一个 POST 请求示例。
画面8：JSON Viewer 工具中显示了聚合查询结果的 JSON 数据结构。
画面9：Elasticsearch Head 插件界面，显示了索引 `haoke` 中的文档数据，包含 `id`, `name`, `age`, `sex` 字段。
画面10：Postman 中构建的 POST 请求，目标地址为 `http://172.16.55.185:9200/haoke/user/1001/_update`。
画面11：Postman 中的请求体内容，包含更新文档的 JSON 数据。
画面12：Elasticsearch Head 插件界面，显示了更新后的文档数据。
画面13：PDF 文档中关于更新数据的说明，包含一个 POST 请求示例。
画面14：PDF 文档中关于聚合查询的说明，包含一个完整的聚合配置 JSON。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<em>张</em><em>三</em>
```
画面3：
```json
{
  "aggs": {
    "all_interests": {
      "terms": {
        "field": "age"
      }
    }
  }
}
```
画面5：
```json
{
  "aggregations": {
    "all_interests": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": 20,
          "doc_count": 1
        },
        {
          "key": 21,
          "doc_count": 1
        },
        {
          "key": 22,
          "doc_count": 1
        },
        {
          "key": 23,
          "doc_count": 1
        },
        {
          "key": 24,
          "doc_count": 1
        }
      ]
    }
  }
}
```
画面6：
```json
{
  "id": "1001",
  "name": "张三",
  "age": "21",
  "sex": "女"
}
```
画面7：
```json
POST http://172.16.55.185:9200/haoke/user/1001/_update
{
  "doc": {
    "age": "23"
  }
}
```
画面10：
```json
POST http://172.16.55.185:9200/haoke/user/1001/_update
{
  "doc": {
    "age": "23"
  }
}
```
画面11：
```json
{
  "doc": {
    "age": "23"
  }
}
```
画面14：
```json
{
  "aggs": {
    "all_interests": {
      "terms": {
        "field": "age"
      }
    }
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
