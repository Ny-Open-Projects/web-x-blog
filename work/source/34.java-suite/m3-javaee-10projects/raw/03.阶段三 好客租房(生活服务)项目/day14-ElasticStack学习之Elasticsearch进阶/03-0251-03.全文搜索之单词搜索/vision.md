# 画面线理解：03.全文搜索之单词搜索

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\03.全文搜索之单词搜索【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:46, 02:22, 02:33, 03:43, 04:07, 04:39, 04:53, 05:05, 05:22, 05:44, 06:34, 07:18, 07:23, 09:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:44:24

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Elasticsearch 创建索引、批量插入数据并执行单字段搜索，重点讲解全文搜索与单词搜索的实现方式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于“全文搜索”的理论内容，包括“相关性”和“分析”两个核心概念，并展示创建索引的 JSON 配置。
画面 2: 在 Postman 中准备发送一个 PUT 请求，用于创建索引，但请求体为空。
画面 3: 在 EditPlus 编辑器中粘贴并格式化了创建索引的 JSON 配置，准备用于后续操作。
画面 4: PDF 文档中展示“批量插入数据”的示例，包含一个 POST 请求和一个 JSON 数组，用于向索引中插入多条文档。
画面 5: 在 Postman 中准备发送一个 POST 请求，用于执行批量插入操作，但请求体为空。
画面 6: PDF 文档中展示批量插入数据的 JSON 数组和执行结果表格，表格显示了插入的文档信息。
画面 7: PDF 文档中展示“hobby”字段的配置，包括类型为 "text" 和使用 "ik_max_word" 分词器。
画面 8: PDF 文档中展示“单词搜索”的 JSON 查询结构，包含 match 查询和 highlight 高亮配置。
画面 9: PDF 文档中展示“hobby”字段的配置，包括类型为 "text" 和使用 "ik_max_word" 分词器。
画面 10: 在 EditPlus 编辑器中粘贴并格式化了单词搜索的 JSON 查询结构。
画面 11: 在 Postman 中发送了单词搜索请求，响应结果中包含匹配的文档和高亮字段。
画面 12: PDF 文档中展示“单词搜索”的 JSON 查询结构。
画面 13: PDF 文档中展示“多词搜索”的理论说明和示例，包括查询过程和相关计算。
画面 14: PDF 文档中展示“单词搜索”的 JSON 查询结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
PUT http://172.16.55.185:9200/itcast
{
  "settings": {
    "number_of_shards": "1",
    "number_of_replicas": "0"
  },
  "mappings": {
    "person": {
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "integer"
        },
        "mail": {
          "type": "keyword"
        }
      }
    }
  }
}

画面 4:
POST http://172.16.55.185:9200/itcast/_bulk
{
  "index": {
    "_index": "itcast",
    "_type": "person"
  },
  "name": "张三",
  "age": 20,
  "mail": "111@qq.com",
  "hobby": "羽毛球,乒乓球,足球"
}
{
  "index": {
    "_index": "itcast",
    "_type": "person"
  },
  "name": "李四",
  "age": 21,
  "mail": "222@qq.com",
  "hobby": "羽毛球,乒乓球,篮球,游泳"
}
{
  "index": {
    "_index": "itcast",
    "_type": "person"
  },
  "name": "王五",
  "age": 22,
  "mail": "333@qq.com",
  "hobby": "篮球,足球,游泳,听音乐"
}
{
  "index": {
    "_index": "itcast",
    "_type": "person"
  },
  "name": "赵六",
  "age": 23,
  "mail": "444@qq.com",
  "hobby": "跑步、游泳、听音乐"
}
{
  "index": {
    "_index": "itcast",
    "_type": "person"
  },
  "name": "孙七",
  "age": 24,
  "mail": "555@qq.com",
  "hobby": "听音乐、看电影、羽毛球"
}

画面 6:
结果：
查询 1 个分片中用时 1 个, 4 秒中, 耗时 0.001 秒
_index      _type    _id              score   name   age   mail           hobby
itcast      person  UPOdWgBR-bsWb-LpdkZ_1  1       张三   20   111@qq.com      羽毛球,乒乓球,足球
itcast      person  UvOdWgBR-bsWb-LpdkZ_1  1       李四   21   222@qq.com      羽毛球,篮球,游泳,足球
itcast      person  VPOdWgBR-bsWb-LpdkZ_1  1       王五   22   333@qq.com      篮球,足球,游泳,听音乐
itcast      person  VPOdWgBR-bsWb-LpdkZ_1  1       孙七   24   555@qq.com      听音乐、看电影、羽毛球

画面 8:
POST http://172.16.55.185:9200/itcast/person/search
{
  "query": {
    "match": {
      "hobby": "音乐"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}

画面 10:
{
  "query": {
    "match": {
      "hobby": "音乐"
    }
  },
  "highlight": {
    "fields": {
      "hobby": {}
    }
  }
}

画面 11:
{
  "_index": "itcast",
  "_type": "person",
  "_id": "UPOdWgBR-bsWb-LpdkZ_1",
  "_score": 0.8122286,
  "_source": {
    "name": "张三",
    "age": 20,
    "mail": "111@qq.com",
    "hobby": "羽毛球,乒乓球,足球"
  },
  "highlight": {
    "hobby": [
      "羽毛球,乒乓球,足球"
    ]
  }
}

画面 13:
POST http://172.16.55.185:9200/itcast/person/_search
{
  "query": {
    "match": {
      "hobby": "音乐"
    }
  }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“1.2、全文搜索”，子标题“全文搜索两个最重要的方面是：”，包含两个要点：“相关性”和“分析”。
画面 4: 标题为“批量插入数据”，包含一个 POST 请求和一个 JSON 数组。
画面 6: 标题为“结果”，包含一个表格，列包括 _index, _type, _id, score, name, age, mail, hobby。
画面 8: 标题为“1.2.2、单词搜索”，包含一个 POST 请求和一个 JSON 查询结构。
画面 13: 标题为“1.2.3、多词搜索”，包含一个 POST 请求和一个 JSON 查询结构。
画面 14: 标题为“1.2.2、单词搜索”，包含一个 POST 请求和一个 JSON 查询结构。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
