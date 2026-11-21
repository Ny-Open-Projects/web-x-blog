# 画面线理解：10.Elasticsearch快速入门之RESTful api（新增文档数据）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\10.Elasticsearch快速入门之RESTful api（新增文档数据）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:57, 01:39, 02:53, 02:59, 03:30, 03:39, 04:11, 04:17, 04:36, 04:53, 05:27, 05:51, 05:58
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:30:03

1) 这一组画面整体在讲如何使用 Elasticsearch 的 REST API 插入数据，包括指定 ID 和不指定 ID 两种情况，并演示了操作失败时的 HTTP 状态码。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 Elasticsearch Head 界面，索引 "haoke" 状态为 green，文档数量为 0。
画面 2: 展示 PDF 文档中关于“插入数据”的部分，包含插入数据的 URI 规则和示例 JSON 数据。
画面 3: 展示 Advanced REST Client 发送 POST 请求后返回 201 Created 状态码。
画面 4: 展示 PDF 文档中关于“插入数据”的部分，包含插入数据的 URI 规则和示例 JSON 数据。
画面 5: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例。
画面 6: 展示 Advanced REST Client 发送 POST 请求后返回 405 Method Not Allowed 状态码。
画面 7: 展示 Advanced REST Client 中的请求体，包含不指定 ID 的 JSON 数据。
画面 8: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例。
画面 9: 展示 Elasticsearch Head 界面，索引 "haoke" 中已存在一条数据。
画面 10: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例。
画面 11: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例，以及成功插入后自动生成的 ID。
画面 12: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例。
画面 13: 展示 PDF 文档中关于“删除索引”的部分，包含删除索引的 DELETE 请求示例。
画面 14: 展示 PDF 文档中关于“不指定id插入数据”的部分，包含不指定 ID 的 POST 请求示例。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
POST http://172.16.55.185:9200/haoke/user/1001
{
  "id": "1001",
  "name": "张三",
  "age": 20,
  "sex": "男"
}
响应
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1",
  "_version": 1,
}

画面 5:
不指定id插入数据：
POST http://172.16.55.185:9200/haoke/user/
{
  "id": "1002",
  "name": "张二",
  "age": 20,
  "sex": "男"
}

画面 11:
不指定id插入数据：
POST http://172.16.55.185:9200/haoke/user/
{
  "id": "1002",
  "name": "张二",
  "age": 20,
  "sex": "男"
}

画面 13:
DELETE http://172.16.55.185:9200/haoke
{
  "acknowledged": true
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“2.4.2. 插入数据”，内容包含“URI 规则”和“#数据”、“#响应”部分。
画面 5: PPT 中表格数据为：
Index type id score id name age sex
haoke user 1001 1 1001 张三 20 男
画面 11: PPT 中表格数据为：
Index type id score id name age sex
haoke user 1001 1 1001 张三 20 男
haoke user 1002 1 1002 张二 20 男
画面 13: PPT 中表格数据为：
Index type id score id name age sex
haoke user 1001 1 1001 张三 20 男

5) 不要评价画面美观，不要输出与课程无关的内容。
