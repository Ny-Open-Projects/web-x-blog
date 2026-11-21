# 画面线理解：20.Elasticsearch核心详解之批量操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\20.Elasticsearch核心详解之批量操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:56, 01:26, 01:49, 01:59, 02:45, 04:07, 05:27, 05:40, 06:16, 06:25, 06:46, 07:18, 08:24, 08:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:36:01

1) 这一组画面整体在讲如何使用 Elasticsearch 的 Bulk API 批量执行插入、修改和删除操作，并通过 Postman 发送请求验证。

2) 按时间顺序列出每张画面的要点：
画面 1: 使用 Postman 发送 HEAD 请求到 http://172.16.55.185:9200/haoke/user/_mget，状态码 404 Not Found。
画面 2: 在 Elasticsearch Head 插件界面，展示索引 "haoke" 中的用户数据，包含 id、name、age、sex 字段。
画面 3: 使用 Postman 发送 POST 请求到 http://172.16.55.185:9200/haoke/user/_mget，请求体为 {"ids": ["D1Nr2gB85DOPaceWlCd", "D1Nr2gB85DOPaceWlCd"]}，状态码 200 OK。
画面 4: Adobe Reader 中的 PDF 文档，显示 Elasticsearch 的 _mget 操作返回结果，包含两个文档的 _source 信息。
画面 5: Adobe Reader 中的 PDF 文档，展示 _mget 操作的请求示例：POST http://172.16.55.185:9200/haoke/user/_mget，请求体为 {"ids": ["1001", "1008"]}。
画面 6: Adobe Reader 中的 PDF 文档，章节 3.4.2 _bulk操作，说明支持批量插入、修改、删除，并展示请求格式和批量插入数据示例。
画面 7: 使用 Postman 发送 POST 请求到 http://172.16.55.185:9200/haoke/user/_bulk，请求体为批量操作的 JSON 数据。
画面 8: 使用 Postman 发送 POST 请求到 http://172.16.55.185:9200/haoke/user/_bulk，请求体为批量操作的 JSON 数据，包含三个 create 操作。
画面 9: 使用 Postman 发送 POST 请求到 http://172.16.55.185:9200/haoke/user/_bulk，请求体为批量操作的 JSON 数据，包含一个 create 操作和一个 delete 操作。
画面 10: 在 Elasticsearch Head 插件界面，展示索引 "haoke" 中的用户数据，包含 id、name、age、sex 字段。
画面 11: Adobe Reader 中的 PDF 文档，章节 3.4.2 _bulk操作，说明支持批量插入、修改、删除，并展示请求格式和批量插入数据示例。
画面 12: Adobe Reader 中的 PDF 文档，展示 _bulk 操作的响应结果，包含 "result": "Created"、"shards"、"status": 201 等信息。
画面 13: Adobe Reader 中的 PDF 文档，展示批量删除操作的请求格式：{"delete": {"_index": "haoke", "_type": "user", "_id": "2001"}}。
画面 14: Adobe Reader 中的 PDF 文档，章节 3.5 分页，说明 Elasticsearch 支持分页，使用 from 和 size 参数，size 默认为 10。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 3 请求体：
{
  "ids": ["D1Nr2gB85DOPaceWlCd", "D1Nr2gB85DOPaceWlCd"]
}

画面 4 返回结果：
{
  "_index": "haoke",
  "_type": "user",
  "_id": "D1Nr2gB85DOPaceWlCd",
  "_version": 1,
  "_source": {
    "id": "D1Nr2gB85DOPaceWlCd",
    "name": "张三",
    "age": 20,
    "sex": "男"
  }
}

画面 5 请求体：
POST http://172.16.55.185:9200/haoke/user/_mget
{
  "ids": ["1001", "1008"]
}

画面 6 请求格式：
{
  { action: { metadata } }
  { request body }
  { action: { metadata } }
  { request body }
  ...
}

批量插入数据：
{
  "create": {"_index": "haoke", "_type": "user", "_id": "2001"},
  "id": "2001",
  "name": "name1",
  "age": 20,
  "sex": "男"
}
{
  "create": {"_index": "haoke", "_type": "user", "_id": "2002"},
  "id": "2002",
  "name": "name2",
  "age": 20,
  "sex": "男"
}
{
  "create": {"_index": "haoke", "_type": "user", "_id": "2003"},
  "id": "2003",
  "name": "name3",
  "age": 20,
  "sex": "男"
}

画面 7 请求体：
{
  "docs": [
    {
      "_index": "haoke",
      "_type": "user",
      "_id": "D1Nr2gB85DOPaceWlCd",
      "_version": 1,
      "_source": {
        "id": "D1Nr2gB85DOPaceWlCd",
        "name": "张三",
        "age": 20,
        "sex": "男"
      }
    }
  ]
}

画面 8 请求体：
[
  {
    "create": {
      "_index": "haoke",
      "_type": "user",
      "_id": "2001"
    },
    "id": "2001",
    "name": "name1",
    "age": 20,
    "sex": "男"
  },
  {
    "create": {
      "_index": "haoke",
      "_type": "user",
      "_id": "2002"
    },
    "id": "2002",
    "name": "name2",
    "age": 20,
    "sex": "男"
  },
  {
    "create": {
      "_index": "haoke",
      "_type": "user",
      "_id": "2003"
    },
    "id": "2003",
    "name": "name3",
    "age": 20,
    "sex": "男"
  }
]

画面 9 请求体：
{
  "create": {
    "_index": "haoke",
    "_type": "user",
    "_id": "2001"
  },
  "id": "2001",
  "name": "name1",
  "age": 20,
  "sex": "男"
}

画面 12 响应结果：
{
  "result": "Created",
  "shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 0,
  "_primary_term": 1,
  "status": 201
}

画面 13 批量删除操作：
{
  "delete": {"_index": "haoke", "_type": "user", "_id": "2001"}
}

画面 14 分页参数：
size: 结果数，默认 10

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 6 PPT 标题：3.4.2 _bulk操作
画面 6 表格数据：请求格式和批量插入数据示例
画面 11 PPT 标题：3.4.2 _bulk操作
画面 12 PPT 标题：3.4.2 _bulk操作
画面 13 PPT 标题：批量删除
画面 14 PPT 标题：3.5 分页

5) 无。
