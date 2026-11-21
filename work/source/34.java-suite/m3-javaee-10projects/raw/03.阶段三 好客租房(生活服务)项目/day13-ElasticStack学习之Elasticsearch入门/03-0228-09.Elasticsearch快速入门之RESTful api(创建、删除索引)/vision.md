# 画面线理解：09.Elasticsearch快速入门之RESTful api（创建、删除索引）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\09.Elasticsearch快速入门之RESTful api（创建、删除索引）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:26, 01:22, 02:28, 02:35, 02:54, 03:34, 04:04, 04:51, 05:02, 05:25, 05:44, 05:50, 06:07, 06:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:29:33

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 RESTful API 在 Elasticsearch 中创建和删除非结构化索引，并通过 ElasticSearch Head 和 Advanced REST Client 工具进行操作和验证。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“2.4.1、创建非结构化索引”的内容，包含创建空索引的 PUT 请求示例，其中包含注释“#分片数”和“#副本数”。
画面 2: 展示 ElasticSearch Head 界面，显示一个名为“test”的索引，状态为“green”，文档数为 0。
画面 3: 展示 ElasticSearch Head 界面，索引名称已变为“haoke”，状态为“green”，文档数为 0。
画面 4: 展示 Advanced REST Client 工具，显示了多个针对“haoke”索引的 HTTP 请求，包括 _search、_mapping、_bulk 等。
画面 5: 展示 Advanced REST Client 工具，准备发送一个 PUT 请求以创建索引，请求体为空。
画面 6: 展示 Advanced REST Client 工具，请求已发送，状态码为 200 OK，响应头显示内容类型为 application/json。
画面 7: 展示 Chrome 网上应用店中 ElasticSearch Head 的页面，显示集群健康状态为黄色。
画面 8: 展示 PDF 文档中关于“删除索引”的内容，包含 DELETE 请求示例，其中包含注释“#删除索引”。
画面 9: 展示 ElasticSearch Head 界面，索引名称为“haoke”，状态为“green”，文档数为 0。
画面 10: 展示 ElasticSearch Head 界面，索引名称为“haoke”，状态为“green”，文档数为 0。
画面 11: 展示 ElasticSearch Head 界面，索引名称为空，状态为“green”，文档数为 0。
画面 12: 展示 PDF 文档中关于“创建索引”的内容，包含 PUT 请求示例，其中包含注释“#分片数”和“#副本数”。
画面 13: 展示 PDF 文档中关于“2.4.1、创建非结构化索引”的内容，包含创建空索引的 PUT 请求示例，其中包含注释“#分片数”和“#副本数”。
画面 14: 展示 PDF 文档中关于“2.4.1、创建非结构化索引”的内容，包含创建空索引的 PUT 请求示例，其中包含注释“#分片数”和“#副本数”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
PUT http://172.16.55.185:9200/haoke
[
  "settings": {
    "index": {
      "number_of_shards": "2", #分片数
      "number_of_replicas": "0" #副本数
    }
  }
]

画面 8:
DELETE http://172.16.55.185:9200/haoke
{
  "acknowledged": true
}

画面 12:
PUT http://172.16.55.185:9200/haoke
[
  "settings": {
    "index": {
      "number_of_shards": "2", #分片数
      "number_of_replicas": "0" #副本数
    }
  }
]

画面 13:
PUT http://172.16.55.185:9200/haoke
[
  "settings": {
    "index": {
      "number_of_shards": "2", #分片数
      "number_of_replicas": "0" #副本数
    }
  }
]

画面 14:
PUT http://172.16.55.185:9200/haoke
[
  "settings": {
    "index": {
      "number_of_shards": "2", #分片数
      "number_of_replicas": "0" #副本数
    }
  }
]

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
