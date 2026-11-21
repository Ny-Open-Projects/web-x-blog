# 画面线理解：13.Elasticsearch快速入门之RESTful api（搜索文档数据）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\13.Elasticsearch快速入门之RESTful api（搜索文档数据）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:25, 01:09, 01:51, 02:06, 02:29, 02:57, 03:45, 03:57, 04:04, 04:35, 04:59, 05:27, 05:38
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:32:06

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elasticsearch 的 REST API 进行数据的检索、更新和条件查询操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“根据ID搜索数据”的说明，包含一个 GET 请求示例：GET http://172.16.55.185:9200/haoke/user/B8pB_WcB3cTfOnF3uebrv，以及响应体中的 JSON 数据结构。
画面 2: 在 Advanced REST Client 中准备发送一个 GET 请求，但尚未输入内容。
画面 3: PDF 文档页面显示了多个窗口的截图，其中包含一个 JSON 响应体，内容为：{ "total": 2, "successful": 2, "skipped": 0, "failed": 0 }，以及一个 "hits" 对象。
画面 4: 在 Advanced REST Client 中，显示了 GET 请求的响应，JSON 数据为：{ "_index": "haoke", "_type": "user", "_id": "1001", "_version": 8, "result": "updated", "_source": { } }。
画面 5: 展示了 Elasticsearch 的 Kibana 界面，其中“索引”列表包含“haoke”、“user”、“id”、“name”、“sex”等字段，右侧显示了“haoke”索引下 ID 为 1001 的文档内容。
画面 6: 在 Advanced REST Client 中，显示了 GET 请求的响应，JSON 数据为：{ "_index": "haoke", "_type": "user", "_id": "1001", "_version": 8, "result": "updated", "_source": { } }。
画面 7: 在 Advanced REST Client 中，输入了 PUT 请求体：{ "age": 21, "sex": "男" }，并发送请求，响应状态为 201 Created，响应体为：{ "_index": "haoke", "_type": "user", "_id": "1001", "_version": 9, "result": "created", "_source": { } }。
画面 8: PDF 文档页面显示了“搜索全部数据”的说明，包含一个 GET 请求示例：GET http://172.16.55.185:9200/haoke/user_search，以及响应体中的 JSON 数据结构。
画面 9: 在 Advanced REST Client 中，输入了 GET 请求：http://172.16.55.185:9200/haoke/user_search，请求体为：{ "id": "1001", "name": "李四", "sex": "男" }。
画面 10: 在 Advanced REST Client 中，准备发送一个 GET 请求，但尚未输入内容。
画面 11: PDF 文档页面显示了“关键字搜索数据”的说明，包含一个 GET 请求示例：GET http://172.16.55.185:9200/haoke/user_search?q=age:20，以及响应体中的 JSON 数据结构。
画面 12: 在 Advanced REST Client 中，输入了 GET 请求：http://172.16.55.185:9200/haoke/user_search?q=age:20，请求体为空。
画面 13: 在 Advanced REST Client 中，发送了 GET 请求，响应状态为 200 OK，响应体为：{ "took": 4, "timed_out": false, "_shards": { "total": 1, "successful": 1, "skipped": 0, "failed": 0 }, "hits": { "total": 1, "max_score": 1, "hits": [ ] } }。
画面 14: PDF 文档页面显示了“关键字搜索数据”的说明，包含一个 GET 请求示例：GET http://172.16.55.185:9200/haoke/user_search?q=age:20，以及响应体中的 JSON 数据结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
GET http://172.16.55.185:9200/haoke/user/B8pB_WcB3cTfOnF3uebrv
#返回的数据如下
{
  "_index": "haoke",
  "_type": "user",
  "_id": "B8pB_WcB3cTfOnF3uebrv",
  "_version": 8,
  "found": true,
  "_source": { #原始数据在这里
    "id": 1002
  }
}

画面 3:
{
  "total": 2,
  "successful": 2,
  "skipped": 0,
  "failed": 0
},
"hits": {
  "total": 4,
  "max_score": 1,
  "hits": [
  ]
}

画面 4:
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1001",
  "_version": 8,
  "result": "updated",
  "_source": {
  }
}

画面 6:
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1001",
  "_version": 8,
  "result": "updated",
  "_source": {
  }
}

画面 7:
{
  "age": 21,
  "sex": "男"
}

画面 8:
GET http://172.16.55.185:9200/haoke/user_search
响应：（默认返回10条数据）
{
  "took": 26,
  "timed_out": false,
  "_shards": {
    "total": 2,
    "successful": 2,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 4,
    "max_score": 1,
    "hits": [
    ]
  }
}

画面 11:
GET http://172.16.55.185:9200/haoke/user_search?q=age:20
#查询年龄等于20的用户

画面 13:
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 1,
    "max_score": 1,
    "hits": [
    ]
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“2.4.5. 搜索数据”，下方有小标题“根据ID搜索数据”。
画面 3: PDF 文档页面显示了多个窗口的截图，其中包含一个 JSON 响应体，内容为：{ "total": 2, "successful": 2, "skipped": 0, "failed": 0 }，以及一个 "hits" 对象。
画面 5: Elasticsearch 的 Kibana 界面，左侧“索引”列表包含“haoke”、“user”、“id”、“name”、“sex”等字段，右侧显示了“haoke”索引下 ID 为 1001 的文档内容。
画面 8: PPT 标题为“搜索全部数据”，下方有小标题“响应：（默认返回10条数据）”。
画面 11: PPT 标题为“关键字搜索数据”，下方有小标题“#查询年龄等于20的用户”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
