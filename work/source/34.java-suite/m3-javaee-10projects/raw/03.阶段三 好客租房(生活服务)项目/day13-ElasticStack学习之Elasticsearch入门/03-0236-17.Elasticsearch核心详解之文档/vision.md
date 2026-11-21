# 画面线理解：17.Elasticsearch核心详解之文档

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day13-ElasticStack学习之Elasticsearch入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day13-ElasticStack学习之Elasticsearch入门\17.Elasticsearch核心详解之文档【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:24, 00:51, 01:09, 01:16, 01:32, 02:11, 02:28, 02:30, 02:38, 03:05, 03:15, 05:29, 07:38, 07:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:34:19

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Elasticsearch 中使用 REST API 插入和查询文档，并结合 PDF 讲义解释文档结构、索引和类型的概念。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Elasticsearch Head 界面中，展示索引 "haoke" 下 type 为 "user" 的文档列表，包含字段 id、name、age、sex，状态显示为“集群健康：yellow (5 of 10)”。
画面 2: 在 Postman 中，向 http://172.16.55.185:9200/haoke/user_search 发送 POST 请求，请求体为 JSON 格式，查询条件为 {"query": {"match": {"age": "20"}}}。
画面 3: 在 JSON Viewer 中，显示空的 JSON 结构，用于查看或编辑返回结果。
画面 4: 回到 Elasticsearch Head 界面，显示索引 "haoke" 下 type 为 "user" 的文档列表，与画面 1 相同。
画面 5: 在 Postman 中，切换 Body 格式为 form-data，准备发送数据。
画面 6: 在 Elasticsearch Head 界面，点击“文档”按钮，弹出“文档编辑”窗口，显示一个 JSON 文档，内容为 {"_index": "haoke", "_type": "user", "_id": "1005", "_version": 1, "_score": 1, "_source": {"id": "1005", "name": "张三", "age": "20", "sex": "男", "card": {"card_number": "123456789"}}}。
画面 7: 在 PDF 文档中，显示“3.1、文档”章节，内容为“在Elasticsearch中，文档以JSON格式进行存储，可以是复杂的结构，如：”并展示一个 JSON 示例。
画面 8: 在 PDF 文档中，展示一个更复杂的 JSON 示例，包含字段 "card"，其值为 {"card_number": "123456789"}。
画面 9: 在 Elasticsearch Head 界面，点击“文档”按钮，弹出“文档编辑”窗口，显示一个 JSON 文档，内容为 {"_index": "haoke", "_type": "user", "_id": "1005", "_version": 1, "_score": 1, "_source": {"id": "1005", "name": "张三", "age": "20", "sex": "男", "card": {"card_number": "123456789"}}}。
画面 10: 在 PDF 文档中，展示“元数据 (metadata)”表格，包含节点和说明，如 "_index" 对应“文档存储的地方”，"_type" 对应“文档代表的对象的类”，"_id" 对应“文档的唯一标识”。
画面 11: 在 PDF 文档中，展示“索引(index)”和“类型(type)”的解释，包括索引类似于关系型数据库中的“数据库”，类型类似于“表”。
画面 12: 在 PDF 文档中，继续解释类型(type)的概念，说明每个类型都有自己的映射(mapping)或约束定义，所有类型下的文档存储在同一个索引中。
画面 13: 在 Elasticsearch Head 界面，展示索引 "haoke" 下 type 为 "user" 的文档列表，包含字段 id、name、age、sex，状态显示为“集群健康：yellow (5 of 10)”。
画面 14: 在 PDF 文档中，回到“3.1、文档”章节，展示一个 JSON 示例，内容为 {"_index": "haoke", "_type": "user", "_id": "1005", "_version": 1, "_score": 1}。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2: 
{
  "query": {
    "match": {
      "age": "20"
    }
  }
}

画面 6: 
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1005",
  "_version": 1,
  "_score": 1,
  "_source": {
    "id": "1005",
    "name": "张三",
    "age": "20",
    "sex": "男",
    "card": {
      "card_number": "123456789"
    }
  }
}

画面 7: 
{
  "_index": "haoke",
  "_type": "user",
  "_id": "1005",
  "_version": 1,
  "_score": 1,
  "_source": {
    "id": "1005",
    "name": "张三",
    "age": "20",
    "sex": "男"
  }
}

画面 8: 
{
  "_source": {
    "id": "1005",
    "name": "孙七",
    "age": "37",
    "sex": "女",
    "card": {
      "card_number": "123456789"
    }
  }
}

画面 10: 
| 节点 | 说明 |
| :--- | :--- |
| _index | 文档存储的地方 |
| _type | 文档代表的对象的类 |
| _id | 文档的唯一标识 |

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: 标题为“3.1、文档”，内容为“在Elasticsearch中，文档以JSON格式进行存储，可以是复杂的结构，如：”并展示一个 JSON 示例。
画面 8: 标题为“3.1、文档”，内容为“其中，card 是一个复杂对象，代表的 Card 对象。”并展示一个 JSON 示例。
画面 10: 标题为“元数据 (metadata)”，表格内容为：
| 节点 | 说明 |
| :--- | :--- |
| _index | 文档存储的地方 |
| _type | 文档代表的对象的类 |
| _id | 文档的唯一标识 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
