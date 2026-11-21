# 画面线理解：11.Elasticsearch快速入门之RESTful api（更新文档数据）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\11.Elasticsearch快速入门之RESTful api（更新文档数据）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:55, 01:08, 01:18, 01:34, 01:51, 02:10, 02:20, 03:39, 03:49, 04:02, 04:25, 04:46, 04:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:30:42

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中通过覆盖和局部更新两种方式修改文档数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“更新数据”的章节，包含 PUT 请求示例，用于覆盖更新文档，其中 id 为 1001，name 为“张三”，age 为 21，sex 为“女”。
画面 2: 在 Advanced REST Client 中，发送 PUT 请求后，响应状态为 200 OK，但响应体为空。
画面 3: 响应体显示更新成功，包含 _index、_type、_id、_version、_seq_no、_primary_term 等信息，以及 total: 1, successful: 1, failed: 0。
画面 4: 在 Elasticsearch Head 插件中，展示索引为 haoke，类型为 user，id 为 1001 的文档，其 _source 字段显示 name 为“张三”，age 为 21，sex 为“女”。
画面 5: PDF 文档中展示 PUT 请求示例，用于覆盖更新文档，其中 id 为 1001，name 为“张三”，age 为 21，sex 为“女”。
画面 6: 在 Advanced REST Client 中，发送 PUT 请求后，响应状态为 200 OK，但响应体为空。
画面 7: PDF 文档中展示查询结果，显示 id 为 1001 的文档，其 name 为“张三”，age 为 21，sex 为“女”，并指出数据已被覆盖。
画面 8: PDF 文档中指出文档不能直接局部更新，但可以通过“从旧文档中检索 JSON、修改它、删除旧文档、索引新文档”四步实现局部更新。
画面 9: 在 Advanced REST Client 中，尝试使用 PUT 方法更新文档，但返回 405 Method Not Allowed 错误，提示不允许的 HTTP 方法为 PUT。
画面 10: 在 Advanced REST Client 中，尝试使用 POST 方法更新文档，但返回 400 Bad Request 错误，提示“Validation Failed”。
画面 11: 在 Advanced REST Client 中，使用 POST 方法发送请求，请求体为 {"age": 23}，但返回 400 Bad Request 错误。
画面 12: 在 Elasticsearch Head 插件中，展示索引为 haoke，类型为 user，id 为 1001 的文档，其 _source 字段显示 name 为“张三”，age 为 21，sex 为“女”。
画面 13: PDF 文档中展示用于局部更新的 POST 请求示例，URL 为 http://172.16.55.185:9200/haoke/user/1001/_update，请求体为 {"doc": {"age": 23}}。
画面 14: PDF 文档中展示更新成功后的响应，包含 _version: 3，result: "updated"，以及查询结果，显示 id 为 1001 的文档，其 age 已更新为 23，并引出“2.4.4. 删除数据”章节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
PUT http://172.16.55.185:9200/haoke/user/1001
{
  "id":1001,
  "name":"张三",
  "age":21,
  "sex":"女"
}

画面 3:
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1001",
  "_version": 2,
  "result": "updated",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 12,
  "_primary_term": 1
}

画面 5:
PUT http://172.16.55.185:9200/haoke/user/1001
{
  "id":1001,
  "name":"张三",
  "age":21,
  "sex":"女"
}

画面 7:
{
  "_index": "haoke",
  "_type": "user",
  "_id": "BbPe_WcB9cFOnF3uebvr",
  "_version": 2,
  "_source": {
    "id": 1001,
    "name": "张三",
    "age": 21,
    "sex": "女"
  }
}

画面 13:
POST http://172.16.55.185:9200/haoke/user/1001/_update
{
  "doc": {
    "age": 23
  }
}

画面 14:
{
  "_version": 3,
  "result": "updated",
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "_seq_no": 14,
  "_primary_term": 1
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: 表格数据：
_index | _type | _id | _score | id | name | age | sex
---|---|---|---|---|---|---|---
haoke | user | BbPe_WcB9cFOnF3uebvr | 1 | 1002 | 李四 | 40 | 男
haoke | user | 1001 | 1 | 1001 | 张三 | 21 | 女

画面 14: 表格数据：
_index | _type | _id | _score | id | name | age | sex
---|---|---|---|---|---|---|---
haoke | user | BbPe_WcB9cFOnF3uebvr | 1 | 1002 | 李四 | 40 | 男
haoke | user | 1001 | 1 | 1001 | 张三 | 23 | 女

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
